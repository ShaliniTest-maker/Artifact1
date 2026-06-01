"""Unit tests for the :mod:`greeting` module.

Standard-library-only (:mod:`unittest`, :mod:`datetime`) tests that verify the
public contract of ``greeting.py``:

* :func:`greeting.good_evening` returns the exact salutation ``"Good evening"``.
* :func:`greeting.is_evening` reports membership in the half-open evening
  window ``[EVENING_START, EVENING_END)`` on the 24-hour clock.

The boundary tests construct fixed :class:`~datetime.datetime` values rather
than reading the wall clock, so every assertion is deterministic and
independent of when the suite is executed. The window constants
``EVENING_START`` / ``EVENING_END`` are imported (instead of hard-coded) so the
tests track a future change to the window made in a single place in
``greeting.py``.

Run the suite with either of::

    $ python -m unittest -v
    $ python test_greeting.py
"""

import unittest
from datetime import datetime

from greeting import good_evening, is_evening, EVENING_START, EVENING_END


class GoodEveningTests(unittest.TestCase):
    """Verify the greeting string contract and ``is_evening`` boundaries."""

    def test_returns_good_evening(self):
        """``good_evening()`` returns the exact, drift-free salutation."""
        self.assertEqual(good_evening(), "Good evening")

    def test_is_evening_true_at_start_boundary(self):
        """The inclusive lower bound (17:00) is inside the evening window."""
        self.assertTrue(is_evening(datetime(2024, 1, 1, EVENING_START, 0)))  # 17:00

    def test_is_evening_true_at_last_evening_hour(self):
        """The last evening minute (20:59) is inside the evening window."""
        self.assertTrue(is_evening(datetime(2024, 1, 1, EVENING_END - 1, 59)))  # 20:59

    def test_is_evening_false_before_window(self):
        """The minute before the window (16:59) is outside the evening window."""
        self.assertFalse(is_evening(datetime(2024, 1, 1, EVENING_START - 1, 59)))  # 16:59

    def test_is_evening_false_at_end_boundary(self):
        """The exclusive upper bound (21:00) is outside the evening window."""
        self.assertFalse(is_evening(datetime(2024, 1, 1, EVENING_END, 0)))  # 21:00

    def test_is_evening_false_midday(self):
        """Midday (12:00) is well outside the evening window."""
        self.assertFalse(is_evening(datetime(2024, 1, 1, 12, 0)))  # 12:00

    def test_is_evening_default_returns_bool(self):
        """Calling with no argument (current time) returns a boolean."""
        self.assertIsInstance(is_evening(), bool)


if __name__ == "__main__":
    unittest.main()
