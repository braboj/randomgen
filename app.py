from randomgen.webserver import RandomNumberGeneratorApp
import fire


def main(debug=0):
    rg_app = RandomNumberGeneratorApp(debug=bool(debug))
    rg_app.run()


if __name__ == '__main__':
    fire.Fire(main)
