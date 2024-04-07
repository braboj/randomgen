# encoding: utf-8
import pytest

from randomgen.core import (
    RandomGenV1,
    RandomGenV2
)

from randomgen.endpoints import (
    RandomGenRestApi,
    DEFAULT_NUMBERS,
    DEFAULT_PROBABILITIES,
    MAX_NUMBERS
)

from randomgen.errors import (
    RandomGenMinError,
    RandomGenMaxError,
    RandomGenTypeError,
    RandomGenEmptyError,
    RandomGenMismatchError,
    RandomGenProbabilitySumError,
    RandomGenProbabilityNegativeError,
)


class TestRandomGenRestApi(object):
    """Test the REST API endpoints."""

    @classmethod
    def setup_class(cls):
        cls.api = RandomGenRestApi()

    def test_endpoint_api_v1_randomgen_pos(self):
        """Test the randomgen v1 endpoint with positive scenarios. """

        for num in (1, 1000, 10000):
            self.api.randomgen_endpoint(RandomGenV1, num)

    def test_endpoint_api_v1_randomgen_neg(self):
        """Test the randomgen v1 endpoint with negative scenarios."""

        # Test the RandomGenMinError exception
        with pytest.raises(RandomGenMinError):
            for num in (-1, 0):
                self.api.randomgen_endpoint(RandomGenV1, num)

        # Test the RandomGenMaxError exception
        with pytest.raises(RandomGenMaxError):
            for num in (10001,):
                self.api.randomgen_endpoint(RandomGenV1, num)

    def test_endpoint_v2_randomgen_pos(self):
        """Test the randomgen v2 endpoint with positive scenarios. """

        for num in (1, 1000, 10000):
            self.api.randomgen_endpoint(RandomGenV2, num)

    def test_endpoint_api_v2_randomgen_neg(self):
        """Test the randomgen v2 endpoint with negative scenarios."""

        # Test the RandomGenMinError exception
        with pytest.raises(RandomGenMinError):
            for num in (-1, 0):
                self.api.randomgen_endpoint(RandomGenV2, num)

        # Test the RandomGenMaxError exception
        with pytest.raises(RandomGenMaxError):
            for num in (10001,):
                self.api.randomgen_endpoint(RandomGenV2, num)

    def test_endpoint_api_config_pos(self):
        """Test the configuration endpoin in positive scenarios."""

        # Configuration endpoint
        self.api.config_endpoint(numbers=[1, 2, 3],
                                 probabilities=[0.2, 0.2, 0.6])

        assert self.api.config['NUMBERS'] == [1, 2, 3]
        assert self.api.config['PROBABILITIES'] == [0.2, 0.2, 0.6]

    def test_endpoint_api_config_neg(self):
        """Test the configuration endpoint with negative scenarios."""

        with pytest.raises(RandomGenMismatchError):
            self.api.config_endpoint(numbers=[1, 2, 3],
                                     probabilities=[0.2, 0.2, 0.6, 0.1])

        with pytest.raises(RandomGenMismatchError):
            self.api.config_endpoint(numbers=[1, 2, 3],
                                     probabilities=[0.2, 0.2])

        with pytest.raises(RandomGenEmptyError):
            self.api.config_endpoint(numbers=[], probabilities=[])

        with pytest.raises(RandomGenProbabilityNegativeError):
            self.api.config_endpoint(numbers=[1, 2, 3],
                                     probabilities=[0.2, 0.2, -0.6])

        with pytest.raises(RandomGenProbabilitySumError):
            self.api.config_endpoint(numbers=[1, 2, 3],
                                     probabilities=[0.2, 0.2, 0.5])

        with pytest.raises(RandomGenTypeError):
            self.api.config_endpoint(numbers=1, probabilities=0.2)

        with pytest.raises(RandomGenTypeError):
            self.api.config_endpoint(numbers=[1, 2, 3], probabilities=0.2)

        with pytest.raises(RandomGenTypeError):
            self.api.config_endpoint(numbers=1, probabilities=[0.2, 0.2, 0.6])

    def test_endpoint_api_reset(self):
        """Test the reset endpoint."""

        self.api.config_endpoint(
            numbers=[1, 2, 3],
            probabilities=[0.2, 0.2, 0.6]
        )

        assert self.api.config['NUMBERS'] == [1, 2, 3]
        assert self.api.config['PROBABILITIES'] == [0.2, 0.2, 0.6]

        self.api.reset_endpoint()

        assert self.api.config['NUMBERS'] == DEFAULT_NUMBERS
        assert self.api.config['PROBABILITIES'] == DEFAULT_PROBABILITIES


if __name__ == "__main__":
    pytest.main()
