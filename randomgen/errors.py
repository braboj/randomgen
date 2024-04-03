class RandomGeneratorError(Exception):

    def __init__(self, message):
        super().__init__(message)

    @classmethod
    def set_message(cls, message):
        cls.message = message


class RandomGenLengthError(RandomGeneratorError):

    MESSAGE = "The numbers and probabilities lists must have the same length."

    def __init__(self):
        super().__init__(message=self.MESSAGE)


class RandomGenSumError(RandomGeneratorError):

    MESSAGE = "Probabilities must sum to 1."

    def __init__(self):
        super().__init__(message=self.MESSAGE)


class RandomGenNegativeError(RandomGeneratorError):

    MESSAGE = "Probabilities must be non-negative."

    def __init__(self):
        super().__init__(message=self.MESSAGE)


class RandomGeneratorHypothesisError(RandomGeneratorError):

    MESSAGE = ("The hypothesis is not valid, the data doesn't "
               "match the expected distribution.")

    def __init__(self):
        super().__init__(message=self.MESSAGE)
