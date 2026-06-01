"""Say "Good evening".

A minimal, standard-library-only feature that produces the salutation
"Good evening", reports whether a given time falls within the evening
window, and prints the greeting when run as a script.

Public interface:
    good_evening()        -> str   Return the exact salutation "Good evening".
    is_evening(now=None)  -> bool  Report whether ``now`` is in the evening window.
    main()                -> None  Print the greeting to standard output.
    EVENING_START, EVENING_END     Module-level constants bounding the window.

Run as a script to emit the greeting::

    $ python greeting.py
    Good evening

Import to use programmatically::

    >>> from greeting import good_evening
    >>> good_evening()
    'Good evening'

The module has no side effects at import time; it only writes to standard
output when executed directly (``__main__``) via :func:`main`.
"""

from datetime import datetime

# Evening window: 17:00 (5 PM) inclusive to 21:00 (9 PM) exclusive,
# i.e. hours 17, 18, 19, and 20. This is the researched convention (a
# defensible midpoint of the "after 5-6 PM until night" usage that stops
# short of late-night "good night" territory). Adjust these two constants
# to change the window in a single place.
EVENING_START = 17
EVENING_END = 21


def good_evening() -> str:
    """Return the evening salutation.

    This is a pure, side-effect-free function. It always returns the exact
    string ``"Good evening"`` (capital ``G``, lowercase ``e``; no surrounding
    whitespace and no punctuation), which callers and tests rely upon.

    Returns:
        str: The literal greeting ``"Good evening"``.
    """
    return "Good evening"


def is_evening(now: datetime | None = None) -> bool:
    """Report whether a time falls within the evening window.

    The window is the half-open interval ``[EVENING_START, EVENING_END)`` on
    the 24-hour clock, i.e. ``EVENING_START`` is inclusive and ``EVENING_END``
    is exclusive. With the default constants this covers hours 17 through 20
    (5:00 PM through 8:59 PM).

    Args:
        now: The :class:`~datetime.datetime` to evaluate. When ``None``
            (the default), the current local time from
            :meth:`datetime.datetime.now` is used.

    Returns:
        bool: ``True`` if ``now`` is within the evening window, else ``False``.
    """
    if now is None:
        now = datetime.now()
    return EVENING_START <= now.hour < EVENING_END


def main() -> None:
    """Print the greeting to standard output.

    This is how the feature "says" good evening: it emits the result of
    :func:`good_evening` to standard output, so that running the module as a
    script produces an observable greeting.
    """
    print(good_evening())


if __name__ == "__main__":
    main()
