# Engineering know-how

Transferable software-engineering patterns distilled from a small Python HTTP
service (Flask app, packaged as a container, deployed to a PaaS). Every entry is
written so it can be lifted without knowing what the service computes. Domain
logic is excluded on purpose. Placeholder names (`mypkg`, `Engine`, `Service`,
`AppError`) stand in for the real identifiers, and snippets are trimmed to the
load-bearing lines.

A recurring shape underlies most of these patterns, worth stating once up front:
every single source of truth is defended by a test that fails when a second copy
drifts from it, and every non-obvious decision is documented at the point in the
code where it is made.

## Core

Architecture, module boundaries, naming, documentation, and design restraint.

### Application factory over a module-level singleton

Build the framework object inside a function, never as an import-time global. A
module-level `app = Flask(__name__)` runs side effects on import, forces one
shared error handler, and makes tests import the working tree instead of the
installed package. A factory gives each worker process (and each test) its own
instance with a single deterministic wiring path.

```python
# app.py
def create_app():
    mimetypes.add_type('text/javascript', '.js')      # deterministic MIME, see below
    app = Flask(__name__)
    app.json = StrictJSONProvider(app)                # reject NaN/Infinity
    app.config.from_object(Config())                  # read env once, first
    register_logging(app)                             # cross-cutting hooks
    register_security_headers(app)
    app.register_blueprint(web.bp)                     # unversioned routes
    for version, engine in API_VERSIONS.items():       # one per registry entry
        app.register_blueprint(make_api_blueprint(version, engine))
    app.register_error_handler(Exception, handle_error)  # single boundary
    return app
```

The wiring order is explicit: config is read before anything that consumes it,
hooks are attached before blueprints, the error boundary is last. Both the
production server and the dev CLI reference the factory by import string
(`gunicorn 'mypkg.app:create_app()'`), so there is one construction path, not
two. Pays off the moment you write the second test: `create_app().test_client()`
starts from zero shared state every time.

Rejected: a module-level `app`, because of import-time side effects, a shared
error handler, and harder testing.

### Source layout that forces installed-package imports

Put the package under `src/mypkg/` rather than `mypkg/` at the repo root. A flat
layout lets tests and tooling accidentally import the working directory; the
`src/` layout makes them exercise the installed (or editable-installed) package,
which is what ships. Pair it with `pythonpath = ["src"]` in the test config so
tests resolve the same tree without an install hack.

Rejected: the flat layout, because it allows accidental working-tree imports
instead of the installed package.

### Proportional layering: extract a layer only when it has substance

Apply the dependency rule (imports point inward: presentation depends on
application depends on domain) but do not build empty layers. Extract a `domain/`
subpackage only because it holds real framework-free logic; leave single-file
concerns flat at the package root. An empty persistence or adapter layer is
ceremony without the forces that justify it.

```text
        presentation            (routes, serialization)
             |  depends on
        application             (orchestration service)
             |  depends on
          domain                (pure logic; imports nothing above)
```

Record an escalation trigger instead of pre-building: "if an external resource
(a database, a queue) is ever brought in, add the infrastructure layer then."
That keeps the current structure honest and tells the next reader exactly when to
grow it.

Rejected: the full layered quartet up front (each of two layers would hold one or
two files); a top-level models folder for a hypothetical database; and leaving
the package flat (the layers stay implicit and it reads as a pile).

### Name a module for its role, not its neighborhood

A module that holds the orchestration service must not be named `endpoints`; a
class that is not the transport surface must not be named `...RestApi`. A misnomer
fights the layering it should express and forces the docs to caveat it. Because
internal identifiers are not part of the wire contract, renaming them is invisible
to clients, so do it before a 1.0 freeze while the import surface is small.

Rejected: renaming only the module and keeping the class misnomer; and no rename
at all, which keeps the name fighting the layering.

### Record the rejected alternatives, one file per decision

Keep each architectural decision as `docs/decisions/NNN-slug.md` from a template,
so decisions are individually linkable, diffable, and supersedable, with a single
canonical index elsewhere that gains one row per record. The reusable discipline
is not the folder, it is capturing the alternatives you rejected and why. A
decision with its alternatives is teachable; one that states only the outcome is
folklore. Use frontmatter `supersedes` / `superseded_by` to chain records rather
than editing history in place.

Rejected: keeping decisions inline in a chapter, because they are then neither
individually linkable nor diffable.

### Restraint as an explicit design criterion

Across many decisions the same rejection reason recurs: over-engineering,
premature generalization, ceremony without the forces that justify it. Treat "is
this proportional to the problem in front of me" as a first-class review question,
not an afterthought. Concretely this showed up as: declining a strict
nonce-based security policy for a baseline one, trimming a server config down to
the load-bearing settings, declining structured logging and correlation IDs for a
single replica, and refusing per-version code duplication for an unproven future
divergence. Premature generalization is a negative signal, not a positive one.

## Language and packaging

Per-language structure, typing, dependency, and packaging idioms (Python here,
but most transfer).

### One project descriptor, one lint-format-type toolchain

Consolidate metadata, dependencies, and tool configuration into a single
declarative manifest (`pyproject.toml`) instead of a scattering of
`setup.py` + `requirements.txt` + separate linter configs, which drift out of
sync. Gate quality with one fast tool that both lints and formats plus one type
checker, rather than an older linter with no formatter or typing story.

```toml
# pyproject.toml
[tool.ruff.lint]
select = ["E", "W", "F", "I", "UP", "B", "C4", "SIM"]   # explicit, documented rule sets

[tool.mypy]
ignore_missing_imports = true   # pragmatic, not --strict: a dep ships no stubs
```

Choosing pragmatic type checking (ignore a stubless dependency) over strict mode
is a deliberate, documented trade-off, not laziness. Rejected: keeping the
multi-file toolchain, because of multiple descriptors to sync and a slower,
narrower lint with no formatter or type gate.

### Pin the runtime version identically across every surface

A base-image-only version bump ships an untested runtime: the image runs the new
version while every quality gate still validates the old one, which is the exact
dev/prod skew a version pin exists to prevent. Move the version everywhere in one
coordinated change.

```text
runtime image  ─┐
CI job matrix   ─┼─  all one exact version (e.g. 3.14.6 / >=3.14)
type checker    ─┤
requires-python ─┘
```

What is tested is what is shipped. One deliberate exception is allowed: a
formatter's `target-version` may trail one minor as a style floor when the newer
target introduces a confusing auto-rewrite, and that exception is documented
inline where it is set.

Rejected: merging the base-image bump alone (ships new, tests old); and
advertising a `requires-python` range wider than any gate actually exercises.

### Read configuration at object-creation time, not import time

Read environment variables inside the factory (`Config.__init__`, called once per
`create_app()`), not as module-level constants evaluated at first import.
Import-time reads freeze at first import, so a test cannot override the
environment per case without reimporting the module.

```python
# config.py
class Config:
    def __init__(self):
        self.LOG_LEVEL = os.environ.get('MYAPP_LOG_LEVEL', 'INFO')   # unset means default
```

Keep one `Config` object as the only configuration surface, uppercase attributes
so the framework's `from_object` picks them up, and treat it as read-only startup
state that is never mutated while serving a request. Rejected: module-level
constants read at import (values freeze at first import); and a
framework-provided env reader as the source of truth, which offers no defaults and
would create two competing conventions.

### Derive the version string from installed metadata

Do not hardcode a version in code. Read it from the installed package metadata so
the single source of truth stays the packaging manifest, and fall back gracefully
when running uninstalled.

```python
# __init__.py
try:
    __version__ = version('mypkg')
except PackageNotFoundError:   # pragma: no cover - only when running uninstalled
    __version__ = '0.0.0+unknown'
```

The `pragma: no cover` documents the branch that coverage can never reach.

### Custom exception hierarchy with class-constant messages

Give the domain one base exception and leaf classes that each carry a `MESSAGE`
class attribute and a no-argument constructor. Call sites read `raise
BadInputError()` with no message string, and the boundary keys on the single base
class.

```python
# domain/errors.py
class AppError(Exception):
    def __init__(self, message):
        super().__init__(message)

class ProbabilitySumError(AppError):
    MESSAGE = 'Weights must sum to 1.'
    def __init__(self):
        super().__init__(message=self.MESSAGE)
```

Messages live in one place (a test can assert them), call sites stay clean and
greppable, and `isinstance(e, AppError)` is the one check the error boundary
needs to classify client faults.

### Abstract base with shared behavior and one abstract seam

When implementations differ in exactly one operation, put all shared logic on the
ABC and leave only that operation abstract. A new backend implements one method;
the base guarantees the rest of the contract.

```python
# domain/core.py
class EngineABC(metaclass=ABCMeta):
    def validate(self): ...     # shared
    def run(self): ...          # shared
    @abstractmethod
    def next_value(self): ...   # the only seam that varies
```

Rejected: a single implementation, because it is less instructive and couples
every caller to one strategy.

### Fluent builders return `Self`

Configuration methods that return the instance, typed as `Self`, compose into a
readable pipeline and stay correct under subclassing.

```python
# domain/core.py
def set_items(self, items) -> Self:
    self.items = items
    return self
# usage: Engine().set_items(xs).set_weights(ws).validate()
```

### Optional dependencies as capability tiers

Define optional-dependency groups that map to CI gates and capabilities, not one
flat `dev`. Chain them so the full toolchain composes the lighter tiers instead of
duplicating them.

```toml
# pyproject.toml
[project.optional-dependencies]
test = ["pytest", "pytest-cov", ...]                  # the fast gate
e2e  = ["pytest", "testcontainers", "playwright"]     # heavy: containers + browser, opt-in
dev  = ["mypkg[test]", "ruff", "mypy", "build"]       # composes [test] + static analysis
```

Each CI job installs only the tier it needs, so the heavy container-and-browser
dependencies stay out of the fast gate. Ship non-code assets (templates, a
contract file) as declared package-data, or the installed wheel breaks in the
container.

## Backend

HTTP service, API contract, statelessness, error handling, observability.

### Thin handler, stateless service, framework-free domain

Three layers with a strict dependency direction. The route handler only parses
input and serializes output. A framework-independent service orchestrates. The
domain computes and imports nothing from the web layer.

```text
HTTP request
   │
   ▼
handler ─ parse query, serialize JSON          (knows Flask)
   │  delegates
   ▼
service ─ validate, orchestrate, assemble       (plain object, no Flask)
   │  calls
   ▼
domain  ─ the actual computation                (stdlib + libs only)
```

Business logic never lives in a handler, so it is reachable and testable without
the web framework, and the framework becomes a replaceable detail. The service
holds no mutable state, so a single instance is shared across all requests,
versions, and workers; per-request objects are built fresh where state is needed.

### Path-versioned API as a frozen contract

Expose versions in the path (`/api/v1`, `/api/v2`) and freeze each version's
behavior. A behavior change is a new version, never a change to an existing one.
Parallel versions may differ only in an internal strategy while sharing
parameters, response shape, and status codes.

Rejected: a single unversioned endpoint, because any behavior change would break
existing consumers.

### Registry plus parametric factory over per-version duplication

When several API generations share one contract and differ only by an injected
strategy, do not create a directory tree per version; that duplicates identical
handlers and implies a divergence the model denies. Declare each version once in a
registry and build its blueprint from a factory.

```python
# versions.py: the one place a version is declared
API_VERSIONS: dict[str, type[EngineABC]] = {'v1': EngineV1, 'v2': EngineV2}

# blueprints/api.py: the factory, called once per registry entry
def make_api_blueprint(version: str, engine: type) -> Blueprint:
    bp = Blueprint(f'api_{version}', __name__, url_prefix=f'/api/{version}')

    @bp.get('/compute')
    def compute() -> Response:
        quantity = quantity_from_query()
        items = distribution_from_query()
        return jsonify(service.run(engine=engine, quantity=quantity, items=items))

    return bp
```

```text
API_VERSIONS = { v1: EngineV1, v2: EngineV2 }
        │  factory iterates the registry
        ▼
  /api/v1/compute ─ binds EngineV1 ─┐
  /api/v2/compute ─ binds EngineV2 ─┴─▶ one shared, version-agnostic service
```

Two safeguards make this reliable. The factory captures its dependency as a function
parameter, not a loop variable, which avoids the late-binding closure bug where
every route would end up bound to the last item. And an escalation trigger is
documented: a generation whose contract genuinely diverges graduates to its own
module rather than staying in the registry. Adding a version is then a one-line
registry edit. The registry doubles as machine-readable metadata you can expose at
an info endpoint.

Rejected: a per-version directory tree (duplicate handlers, implied divergence);
and pushing version selection down into the service (it leaks a transport concept
into the framework-independent core).

### Partition routes by audience

Group transport routes by who consumes them, not by file convenience. Unversioned
browser and ops routes (home page, docs, health, info) live in one blueprint;
the versioned machine API lives in the per-version blueprints. Ops and UI concerns
then evolve independently of the versioned contract, and a health probe never
accidentally inherits API versioning.

### Statelessness for horizontal scale

Hold no per-client configuration on the server; make behavior overridable per
request instead. Server-side mutable state complicates horizontal scaling and
forces a persistence and configuration lifecycle the service would not otherwise
need. Config that parameterizes worker startup is fine; config that requests read
or write is not.

Rejected: a server-side config endpoint that stores per-client settings, because
it adds shared mutable state and persistence; replaced by per-request parameters.

### Centralized error boundary returning a uniform JSON envelope

Register one error handler that triages by exception type into a stable
`{"error": ...}` shape. Client-input faults map to 400 with the cause logged;
framework HTTP errors keep their code; everything else is a generic 500 with the
detail logged but never sent to the client.

```python
# app.py
def handle_error(e):
    if isinstance(e, AppError):                    # bad client input
        current_app.logger.warning('Rejected %s %s: %s', request.method, request.path, e)
        return jsonify({'error': str(e)}), 400
    if isinstance(e, HTTPException):               # 404, 405, ...
        return jsonify({'error': e.description}), e.code
    current_app.logger.exception('Unhandled error on %s %s', request.method, request.path)
    return jsonify({'error': 'Internal Server Error'}), 500   # no internal detail leaked
```

Every failure path, including 404 and 405, returns JSON rather than an HTML error
page, so a machine client always gets a parseable body. The 400-versus-500 split
is the client-fault-versus-server-fault classification, and internal detail never
crosses the boundary. Because the handler returns a response rather than
re-raising, the after-request hook still runs, which is what makes "exactly one
log line per request" hold even for errors.

### Design-first contract served as data

Hand-author the API contract as a checked-in file, ship it as package-data, and
serve it verbatim. Do not emit the contract as a side effect of the
implementation, and do not keep a second prose copy; two descriptions of one
contract always drift.

```python
# openapi.py
@lru_cache(maxsize=1)
def load_spec() -> dict[str, Any]:
    text = resources.files('mypkg').joinpath('openapi.yaml').read_text(encoding='utf-8')
    return yaml.safe_load(text)     # importlib.resources works from an installed wheel
```

`importlib.resources` avoids `__file__` path fragility inside a wheel or
container, and caching parses the read-only document once. Changing the API means
editing the contract file first, then implementing to it. The contract is only
kept honest by the drift-guard tests below.

Version the contract document independently of the package version. Tying them
churns the contract version on package patches that do not touch the contract. The
drift test asserts the version field is present, not that it equals the package
version.

Rejected: a code-built spec (the contract should be designed and agreed, not
emitted as a by-product); a hybrid that keeps both with a diff gate (two artifacts
to keep in lockstep for no gain); and a parallel prose contract with nothing
enforcing it.

### Make illegal states unrepresentable in the query API

When two parallel inputs must stay aligned, a caller can submit a misaligned pair.
Add a single combined parameter that binds each value to its partner, give it
precedence, and keep the legacy form for backward compatibility.

```python
# blueprints/api.py: pairs=a:1,b:2 binds each key to its own value
for item in raw.split(','):
    key, sep, value = item.partition(':')
    if not sep:
        raise BadPairFormatError()
    ...
```

The combined form takes precedence when present; the parallel form is consulted
only in its absence. Misalignment becomes impossible to express rather than merely
discouraged.

### Explicit input parsing that refuses silent coercion

Parse query parameters by hand and raise on malformed input, instead of a
framework helper that silently falls back to a default on a bad value. A malformed
explicit value is a client error that must surface as 400, not be masked as a
successful default.

```python
# blueprints/api.py
raw = request.args.get('numbers')
if raw is None:
    return DEFAULT_QUANTITY
try:
    return int(raw)
except (TypeError, ValueError):
    raise BadQuantityError() from None   # explicit bad value -> 400, not silent default
```

`raise ... from None` suppresses the chained traceback so the client-facing error
stays clean.

### Strict serialization at the boundary

Subclass the JSON provider to reject non-standard tokens (`NaN`, `Infinity`) that
the default serializer emits as bare words, producing a body that violates the
JSON spec and breaks a strict parser. An undefined value should already be null
before serialization; this is the defense in depth that turns a leaked `NaN` into
a loud 500 instead of a silently invalid 200.

```python
# app.py
class StrictJSONProvider(DefaultJSONProvider):
    def dumps(self, obj, **kwargs):
        kwargs.setdefault('allow_nan', False)
        return super().dumps(obj, **kwargs)
```

### Cross-cutting concerns as `register_x(app)` hooks

Give each cross-cutting concern its own module exposing a `register_x(app)`
function that attaches the request hooks and returns the app for chaining. The
factory then reads as a checklist, and each concern is independently testable.

One access-log line per response is the concrete payoff:

```python
# observability.py
@app.before_request
def _start_timer():
    g.start_time = time.perf_counter()

@app.after_request
def _log_request(response):
    if app.static_url_path and request.path.startswith(f'{app.static_url_path}/'):
        return response                      # skip static-asset noise
    start = getattr(g, 'start_time', time.perf_counter())
    duration_ms = round((time.perf_counter() - start) * 1000, 2)
    app.logger.info('%s %s %s %s %sms', request.remote_addr,
                    request.method, request.path, response.status_code, duration_ms)
    return response
```

Static-asset fetches are skipped as mechanical byproducts, the `getattr` fallback
survives a missing timer, and `%`-formatting stays lazy. For a single replica,
prefer plain text logging to stdout that the runtime collects, and defer
structured or JSON logging until a machine actually consumes it.

Rejected across these concerns: a third-party middleware extension, because the
hooks are a few lines of first-party code with no new runtime dependency.

## Infrastructure

Build, containers, CI/CD mechanics, deployment.

### One gate per job, one fan-in status check

Split CI into one job per quality gate (lint, type-check, test, build, e2e, secret
scan, dependency audit) so each fails fast and reports independently. A single
bundled job hides which gate failed. Then add one fan-in job as the sole required
branch-protection context, so protection requires one check instead of many.

```text
 lint  typecheck  test  build  e2e  secret-scan  sca
   └────────┴───────┴──────┴─────┴────────┴────────┘
                        │  needs: [all], if: always()
                        ▼
                      gate        ← the one required status check
        (fails unless every input is exactly "success")
```

```yaml
# ci.yml
gate:
  needs: [lint, typecheck, test, build, e2e, secret-scan, sca]
  if: always()                     # run even when a gate fails
  steps:
    - run: |
        for r in ${{ needs.lint.result }} ${{ needs.test.result }} ... ; do
          [ "$r" = success ] || { echo "gate got '$r'"; exit 1; }
        done
```

The `if: always()` with an explicit success check is what stops a skipped or
cancelled gate from counting as a pass, which is the subtle failure mode of naive
fan-in. Add a dedicated build gate that packages the distribution and validates
its metadata, since a broken package passes every other gate. Rejected: the single
bundled build job, because it hides which gate failed and violates
one-responsibility-per-job.

### Pin every action to a commit SHA, let a bot update it

Pin third-party CI actions by commit SHA, not by a moving tag, and record the
human-readable version in a trailing comment. A tag can be repointed at malicious
code; a SHA cannot. Let a dependency bot raise the pin updates as reviewable PRs.

```yaml
- uses: actions/checkout@9c091bb21b7c1c1d1991bb908d89e4e9dddfe3e0  # v7
```

### Layer-cache-friendly build order

Copy only the build inputs (the manifest) before the source, so the dependency
install layer stays cached across source-only changes. Run as a non-root user.
Pin the base image by digest with the readable tag in a comment.

```dockerfile
# Dockerfile
FROM python:3.14.6-alpine3.24@sha256:2673...   # digest authoritative, tag readable
WORKDIR /app
COPY pyproject.toml README.md gunicorn.conf.py ./   # build inputs first: cache the install layer
COPY ./src ./src
RUN pip install --no-cache-dir .
RUN adduser -D appuser
USER appuser                                        # least privilege
HEALTHCHECK ... CMD ["python", "-m", "mypkg.healthcheck"]
CMD ["gunicorn", "mypkg.app:create_app()"]          # exec form, production WSGI server
```

Serve production traffic with a real WSGI/application server, never the framework
dev server, and never with debug on. Use the exec form of `CMD` so signals reach
the process cleanly.

### Testable liveness probe as a module

Write the container health probe as a small importable module invoked with
`python -m mypkg.healthcheck`, not an inline shell one-liner. A slim base image
often ships no `curl`, and a module can be unit-tested by mocking the HTTP call.

```python
# healthcheck.py
def probe() -> int:
    try:
        with urllib.request.urlopen(HEALTH_URL, timeout=REQUEST_TIMEOUT_SECONDS) as r:
            return 0 if r.status == 200 else 1
    except OSError:                 # refused, timeout, or HTTPError (a subclass)
        return 1

if __name__ == '__main__':
    sys.exit(probe())
```

Bound the request timeout below the container's own healthcheck timeout so the
probe can never outlast it. The single broad `except OSError` is justified because
it covers every failure a liveness probe should treat as unhealthy.

### Config-as-code for the runtime server

Keep the runtime server's tuning in a version-controlled config file rather than
implicit CLI defaults, and comment every non-default with its reason. Honor the
platform's environment conventions (a `$PORT`, a `$WEB_CONCURRENCY`) with sane
local fallbacks. Trim it to load-bearing settings only.

```python
# server.conf.py
bind = f'0.0.0.0:{os.environ.get("PORT", "5000")}'         # PaaS injects $PORT
workers = int(os.environ.get('WEB_CONCURRENCY', '2'))      # honor the PaaS convention
timeout = 30                                               # recycle a stuck worker, do not wedge a slot
max_requests, max_requests_jitter = 1000, 50              # recycle to bound slow resource growth; jitter so
                                                          # workers do not all recycle at once
```

### Deploy the built artifact, trigger by release tag

If CI already builds and pushes the image, the deploy target should run that
published artifact, not rebuild from source a second time. Make deploy an explicit
release step gated on publish (artifact promotion), triggered by a version tag
rather than every commit to the main branch, which would redeploy on docs-only
changes.

```text
   push tag v*
        │
   ┌────┴─────┬──────────┬─────────┐
 release   publish     scan      (record, build+push, advisory)
              │  needs: publish
              ▼
           deploy         ← only ever deploys an image that published
```

If the deploy secret is absent (a fork, a contributor without access), skip the
step and still succeed, so the workflow stays green.

```yaml
- run: |
    if [ -n "$DEPLOY_HOOK_URL" ]; then curl -fsS -X POST "$DEPLOY_HOOK_URL";
    else echo "hook unset; skipping"; fi
```

Rejected: rebuilding from the repo on deploy (rebuilds an artifact CI already
produced); and deploying on every green main commit (redeploys on docs-only
changes).

## Security and DevSecOps

Response hardening, SAST, secret scanning, supply chain.

### Baseline response headers via `setdefault`

Stamp a small fixed set of hardening headers on every response with one
`after_request` hook, using `setdefault` so a route may still override any of
them. Choose a baseline policy proportional to the app rather than a strict
lockdown that would thread per-request tokens through pages for little gain.

```python
# security.py
@app.after_request
def _set_security_headers(response):
    for header, value in SECURITY_HEADERS.items():
        response.headers.setdefault(header, value)   # a route may override
    return response
```

Document each policy allowance and each deliberate omission inline (for example,
omitting the transport-security header because the platform terminates TLS and
owns it). Rejected: a strict nonce-based policy as disproportionate, a per-route
policy as over-engineering, and a middleware extension in favor of a few lines of
first-party code.

### Gate on the actionable, inform on the unactionable

Split security scanning by whether you can act on a finding. Dependency-audit your
own dependencies, where a fix is in your control, as a blocking gate. Image and
base-layer scanning, where an upstream CVE may have no available fix, is advisory:
run it after publish, off the deploy path, so it can never block a release for a
problem you cannot patch.

```text
CI (pre-merge)     dependency audit   →  BLOCKS the merge (you can bump the dep)
CD (post-publish)  image / base scan  →  advisory only (continue-on-error, exit 0)
```

A tag-triggered release job cannot be dry-run on a pull request, so a failing scan
step would first surface mid-release. Making it advisory by construction is what
prevents that. Emit a software bill of materials as a durable build artifact, and
track the base image with a dependency bot so drift arrives as a PR rather than a
review finding.

Rejected: a blocking image scan, because a minimal base routinely carries CVEs
with no available fix, which would block every release; and manual base bumps
only, which is exactly how a base image goes years stale.

### Secret scanning over full history

A secret scanner needs the whole commit history; the default shallow checkout
(depth 1) sees only the tip commit and misses a secret committed and later
removed. Fetch full history for that job specifically.

```yaml
- uses: actions/checkout@...
  with:
    fetch-depth: 0   # scan all history, not just the tip commit
```

### SAST in its own workflow with a scoped permission

Static analysis needs an elevated permission (to write security findings). Keep it
in a separate workflow so that permission stays scoped away from the main CI, and
add a scheduled re-scan so idle code is re-checked against newly published rules.
Keep the definition in a workflow file (pipeline-as-code, reviewed and SHA-pinned)
rather than a platform default toggle.

### Least-privilege job permissions

Default the whole workflow to read-only and grant a write permission only on the
specific job that needs it (release creation, artifact attach). The blast radius of
a compromised step is then bounded to one job's scope.

```yaml
# ci.yml
permissions:
  contents: read              # workflow default
# ... then, only on the job that needs it:
#   permissions: { contents: write }
```

## Workflow

Quality gates, testing discipline, process hygiene, and records.

### Keep the coverage metric honest

Scope coverage to the package (not the tests) and exclude genuinely non-testable
lines, so the percentage reflects real gaps rather than being inflated by test
code or dragged down by unreachable branches.

```toml
# pyproject.toml
[tool.coverage.run]
source = ["mypkg"]                     # count the package, not the tests
[tool.coverage.report]
exclude_lines = ["pragma: no cover", "if __name__ == .__main__.:", "raise NotImplementedError"]
```

Enforce the threshold in CI (`--cov-fail-under=N`), keeping the config focused on
what to measure and the gate on the number.

### Auto-mark tests by directory tier

Tag every test by the directory it lives in with one collection hook, instead of
hand-marking each file. The tier follows from location, so markers cannot drift.

```python
# tests/conftest.py
def pytest_collection_modifyitems(config, items):
    for item in items:
        parts = Path(str(item.fspath)).parts
        if 'e2e' in parts:            item.add_marker('e2e')
        elif 'integration' in parts:  item.add_marker('integration')
        else:                         item.add_marker('unit')
```

Make the default test run the fast gate and gate the heavy tier behind a flag, so
the common path stays fast and the expensive container-and-browser tests are
opt-in:

```toml
[tool.pytest.ini_options]
addopts = ["-m", "not e2e"]    # default = fast gate; run the rest with `-m e2e`
```

### Drift-guard meta-tests: pin every second copy to its source

The single-source-of-truth patterns above are only honest if a test fails when a
copy drifts. Two such tests recur and generalize widely.

Pin documented constants to the live code constants:

```python
# test_openapi.py
def test_spec_pins_live_limits():
    schema = load_spec()['components']['parameters']['Quantity']['schema']
    assert schema['default'] == DEFAULT_QUANTITY
    assert schema['minimum'] == MIN_ITEMS
    assert schema['maximum'] == MAX_ITEMS
```

Assert every live route is documented by introspecting the router:

```python
# test_openapi.py
def test_spec_documents_every_api_route():
    documented = set(load_spec()['paths'])
    api_rules = {r.rule for r in create_app().url_map.iter_rules() if r.rule.startswith('/api')}
    assert api_rules and api_rules <= documented   # a new/renamed route left undocumented fails here
```

A new or renamed endpoint left out of the contract now fails CI automatically, with
no human diff review. The same shape covers version-string-versus-metadata and any
other fact that exists in two places.

### Anchor regression tests to the incident

Name a regression test after the bug it prevents and assert the exact contract the
fix established, including the deliberate choices (for example, that a degenerate
input returns 200 with a null field rather than an error). The test then documents
the decision, not just the behavior, and ties a future failure back to the
incident it re-opens.

### Inline procedural checklists into the auto-loaded context

A procedure that must be executed reliably by a tool or agent has to be inlined
into the file that is auto-loaded into that tool's context. A soft "follow
other-file.md" reference fails, because referenced files are not auto-loaded and
the procedure gets paraphrased lossily. Inline the full steps, including the
enforcement ("execute sequentially, do not summarize").

Rejected: the soft reference, because referenced files are not auto-loaded and the
procedure was paraphrased away.

### Track work as issues; make docs an index of live status

Inline descriptions of trackable work drift: when the work is done, the prose and
the tracker disagree and the doc goes stale. Track each actionable item as a
labeled issue and make the doc section an index (a short name plus a live status
badge that links to the issue), with the tracker as the source of truth. Keep
genuinely-accepted boundaries inline, since they are not work to track. Adopt an
existing label standard rather than inventing one, so the scheme stays consistent
with the wider system.

Rejected: inline descriptions (go stale as work is resolved); and a bare link to
the tracker with no per-item summary (loses the at-a-glance view).

### Normalize line endings for a cross-platform repo

Commit a line-ending policy so a mixed Windows-and-Linux team does not churn files
or break shell scripts. Normalize text to LF in the repository, force
platform-native scripts to their required ending, and mark binaries so they are
never touched.

```gitattributes
* text=auto eol=lf
*.sh  text eol=lf
*.ps1 text eol=crlf
*.png binary
```

## Free-form

Patterns that map to no standard category cleanly. These are the ones most worth
examining for upstreaming.

### In-process ephemeral server on port 0 for drivers and UI tests

Drive the real application in-process by starting it on an OS-assigned port
(bind to port 0) in a daemon thread, deriving the base URL from the assigned port,
and tearing it down in a `finally`. The same recipe powers a screenshot/driver
script and the browser-test fixture, so UI tests need no container.

```python
# a shared test/script helper
server = make_server('127.0.0.1', 0, create_app(), threaded=True)   # port 0 = OS assigns, no collisions
base_url = f'http://127.0.0.1:{server.server_port}'
thread = Thread(target=server.serve_forever, daemon=True)
```

Port 0 avoids fixed-port collisions and races, and the browser exercises the same
app object the unit tests do.

### Container-runtime-agnostic end-to-end tests

Build the image from the repo and run it through a container-test library that
speaks a Docker-compatible API, so the same test runs against either Docker or a
rootless daemon on any developer's machine and in CI. Gate readiness with a
poll-until-healthy loop rather than a fixed sleep, and skip cleanly (an import
guard) when the optional dependency is absent so every job can still collect the
module.

### Deterministic MIME registration to defeat OS-registry drift

Two individually-correct features can combine into a bug. A no-sniff response
header plus an OS MIME lookup breaks static scripts on a platform whose registry
maps the script extension to plain text, so the browser refuses to execute it.
Pin the content types explicitly in the app factory for deterministic serving
everywhere.

```python
# app.py
mimetypes.add_type('text/javascript', '.js')
mimetypes.add_type('text/css', '.css')
```

### Structural response-signature snapshot testing

Assert a response's shape independent of the contract document by reducing a JSON
body to a recursive signature of keys and leaf types (collapsing int and float to
one "number" type, checking `bool` before `int` since it is a subclass), then
asserting parallel API versions produce the identical signature. It catches
accidental shape changes and version divergence without coupling to the spec.

### Concurrency-isolation test to prove statelessness

Turn the "the service is stateless and thread-safe" claim into an executable proof:
fire many parallel requests, each with a disjoint input space, and assert every
response stays within its own expected outcome set. Any shared-state bleed shows up
as a value that could only have come from another request.

Candidates worth flagging for an upstream engineering-template library are noted
in the summary below.

## Shortlist: the highest-leverage patterns

1. Single source of truth defended by a drift-guard test. The pin-constants and
   documented-every-route tests generalize to any fact that lives in two places.
2. Application factory plus registry plus parametric blueprint factory. Adding a
   variant becomes a one-line registry edit with no duplicated code, and every
   test starts from zero shared state.
3. One gate per CI job with a single fan-in status check that treats skipped or
   cancelled as failure. Clear failure attribution and one required context.
4. Proportional layering with a documented escalation trigger. Extract a boundary
   only when it has substance; write down exactly when to grow the next one.
5. Pin the runtime version identically across image, CI, type checker, and
   packaging metadata, so what is tested is what ships.
6. Gate on the actionable, inform on the unactionable. Block on findings you can
   fix (your own dependencies); keep advisory the ones you cannot (upstream base
   CVEs), off the release path.
