# Artifact1

## Usage

A small, standard-library-only Python 3 feature that says "Good evening".

Run it from the command line:

    python greeting.py

This prints:

    Good evening

Or import it in your own code:

    from greeting import good_evening, is_evening

    print(good_evening())        # -> "Good evening"
    is_evening()                 # -> True if the current time is in the evening window (17:00–20:59)

No third-party dependencies are required; the feature uses only the Python 3 standard library.
