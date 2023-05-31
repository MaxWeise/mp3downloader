"""Definition of a monad.

Monads wrap return values and possible errors in a single datatype.
Typicall usage:

    def some_func() -> Monad:
        ...
        try:
            operation_that_may_fail()
        except Exception as e:
            return Monad(False, e)

        return Monad(True, None)

Created: 31.05.2023
@author: Max Weise
"""


class Monad:
    def __init__(self, return_value: bool, error_value: Exception | None):
        """Initialize a Monad object."""
        self._return_value = return_value
        self._error = error_value

    @property
    def success(self) -> bool:
        return self._return_value

    @property
    def error(self) -> Exception | None:
        return self._error


