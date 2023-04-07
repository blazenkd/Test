'''
CS50 Python 2023
Week 5: test_twttr.py

Task :

In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2,
restructuring your code per the below, wherein shorten expects a str as input and
returns that same str but with all vowels (A, E, I, O, and U) omitted, whether
inputted in uppercase or lowercase.
'''

from twttr import twttr


def test_assert():
    """
    Test function for the shorten() function.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: if the expected result is not equal to the actual result.
    """

    # Test the function with different inputs and expected outputs using assert statements
    assert twttr("hello world") == "hll wrld"
    assert twttr("HELLO WORLD") == "HLL WRLD"
    assert twttr("h3ll0 w0rld") == "h3ll0 w0rld"
    assert twttr("h@llo w*rld!!!") == "h@ll w*rld!!!"
