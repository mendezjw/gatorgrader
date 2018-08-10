"""Utility functions"""

import os

SLASH = "/"
GATORGRADER_HOME = "GATORGRADER_HOME"


def verify_gatorgrader_home(current_gatorgrader_home):
    """Verifies that the GATORGRADER_HOME variable is set correctly"""
    verified_gatorgrader_home = False
    # pylint: disable=bad-continuation
    if (
        current_gatorgrader_home is not None
        and current_gatorgrader_home.endswith(SLASH) is True
    ):
        verified_gatorgrader_home = True
    return verified_gatorgrader_home


def get_gatorgrader_home():
    """Returns the GATORGRADER_HOME"""
    current_gatorgrader_home = os.environ.get(GATORGRADER_HOME)
    # the current gatorgrader_home is acceptable, so use it
    if verify_gatorgrader_home(current_gatorgrader_home) is not False:
        gatorgrader_home = current_gatorgrader_home
    # the current gatorgrader_home is not okay, so guess at one
    else:
        gatorgrader_home = os.getcwd() + SLASH
    return gatorgrader_home


def get_human_answer(boolean_value):
    """Return a human readable response for the boolean_value"""
    if boolean_value is True:
        return "Yes"
    return "No"