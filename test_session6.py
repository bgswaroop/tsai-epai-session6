import inspect
import os
import re

import pytest

import session6
from session6 import *

vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']


def test_readme_exists():
    """
    Check if the README file exists
    :return: None
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test the length of the README file
    :return: None
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add at least 500 words"


def test_readme_file_for_formatting():
    """
    Tests the formatting for the README file
    :return: None
    """
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_function_name_had_cap_letter():
    """
    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
    :return: None
    """
    functions = inspect.getmembers(session6, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_doc_string_generate_deck_single_expression():
    """
    Test the presence of docstring
    :return: None
    """
    assert generate_deck_single_expression.__doc__ is not None, "missing docstring"


def test_doc_string_generate_deck_function():
    """
    Test the presence of docstring
    :return: None
    """
    assert generate_deck_function.__doc__ is not None, "missing docstring"


def test_annotations_generate_deck_single_expression():
    """
    Test the presence of annotations
    :return: None
    """
    assert generate_deck_single_expression.__annotations__ is not None, "missing annotations"


def test_annotations_generate_deck_function():
    """
    Test the presence of annotations
    :return: None
    """
    assert generate_deck_function.__annotations__ is not None, "missing annotations"


def test_invalid_input1_generate_deck_function():
    """
    Test invalid input type for vals
    :return: None
    """
    with pytest.raises(ValueError):
        generate_deck_function(['12', 12], suits)


def test_invalid_input2_generate_deck_function():
    """
    Test invalid input type for suits
    :return: None
    """
    with pytest.raises(ValueError):
        generate_deck_function(vals, ['12', 12])


def test_invalid_input1_generate_deck_single_expression():
    """
    Test invalid input type for vals
    :return: None
    """
    with pytest.raises(ValueError):
        generate_deck_single_expression(['12', 12], suits)


def test_invalid_input2_generate_deck_single_expression():
    """
    Test invalid input type for suits
    :return: None
    """
    with pytest.raises(ValueError):
        generate_deck_single_expression(vals, ['12', 12])


def test_generate_deck_single_expression():
    """
    test the result of single expression
    :return: None
    """
    deck = generate_deck_single_expression(vals, suits)
    assert deck == [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds'), ('3', 'spades'),
                    ('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('4', 'spades'), ('4', 'clubs'),
                    ('4', 'hearts'), ('4', 'diamonds'), ('5', 'spades'), ('5', 'clubs'), ('5', 'hearts'),
                    ('5', 'diamonds'), ('6', 'spades'), ('6', 'clubs'), ('6', 'hearts'), ('6', 'diamonds'),
                    ('7', 'spades'), ('7', 'clubs'), ('7', 'hearts'), ('7', 'diamonds'), ('8', 'spades'),
                    ('8', 'clubs'), ('8', 'hearts'), ('8', 'diamonds'), ('9', 'spades'), ('9', 'clubs'),
                    ('9', 'hearts'), ('9', 'diamonds'), ('10', 'spades'), ('10', 'clubs'), ('10', 'hearts'),
                    ('10', 'diamonds'), ('jack', 'spades'), ('jack', 'clubs'), ('jack', 'hearts'), ('jack', 'diamonds'),
                    ('queen', 'spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'),
                    ('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds'), ('ace', 'spades'),
                    ('ace', 'clubs'), ('ace', 'hearts'), ('ace', 'diamonds')]


def test_generate_deck_function():
    """
    test the result of generating deck without single expression
    :return: None
    """
    deck = generate_deck_function(vals, suits)
    assert deck == [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds'), ('3', 'spades'),
                    ('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('4', 'spades'), ('4', 'clubs'),
                    ('4', 'hearts'), ('4', 'diamonds'), ('5', 'spades'), ('5', 'clubs'), ('5', 'hearts'),
                    ('5', 'diamonds'), ('6', 'spades'), ('6', 'clubs'), ('6', 'hearts'), ('6', 'diamonds'),
                    ('7', 'spades'), ('7', 'clubs'), ('7', 'hearts'), ('7', 'diamonds'), ('8', 'spades'),
                    ('8', 'clubs'), ('8', 'hearts'), ('8', 'diamonds'), ('9', 'spades'), ('9', 'clubs'),
                    ('9', 'hearts'), ('9', 'diamonds'), ('10', 'spades'), ('10', 'clubs'), ('10', 'hearts'),
                    ('10', 'diamonds'), ('jack', 'spades'), ('jack', 'clubs'), ('jack', 'hearts'), ('jack', 'diamonds'),
                    ('queen', 'spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'),
                    ('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds'), ('ace', 'spades'),
                    ('ace', 'clubs'), ('ace', 'hearts'), ('ace', 'diamonds')]


def test_determine_test_rank1():
    """
    test five of a kind
    :return: None
    """
    a1 = determine_set_rank([('queen', 'hearts'), ('king', 'hearts'), ('ace', 'hearts')])
    assert a1 == 1

def test_determine_test_rank2():
    """
    straight flush
    :return: None
    """
    a2 = determine_set_rank([('jack', 'hearts'), ('queen', 'hearts'), ('king', 'hearts')])
    assert a2 == 2

def test_determine_test_rank3():
    """
    test four of a kind
    :return: None
    """
    a3 = determine_set_rank([('6', 'hearts'), ('6', 'diamonds'), ('6', 'clubs'), ('6', 'spades')])
    assert a3 == 3

def test_determine_test_rank4():
    """
    test flush
    :return: None
    """

    a4 = determine_set_rank([('2', 'hearts'), ('2', 'diamonds'), ('2', 'clubs'), ('ace', 'diamonds'), ('ace', 'clubs')])
    assert a4 == 4

def test_determine_test_rank5():
    """
    test straight
    :return: None
    """
    a5 = determine_set_rank([('7', 'hearts'), ('2', 'hearts'), ('3', 'hearts'), ('ace', 'hearts'), ('5', 'hearts')])
    assert a5 == 5

def test_determine_test_rank6():
    """
    test three of a kind
    :return: None
    """

    a6 = determine_set_rank([('jack', 'spades'), ('queen', 'hearts'), ('king', 'hearts')])
    assert a6 == 6

def test_determine_test_rank7():
    """
    test two pair
    :return: None
    """
    a7 = determine_set_rank([('jack', 'spades'), ('jack', 'hearts'), ('jack', 'clubs'), ('2', 'clubs'), ('5', 'clubs')])
    assert a7 == 7

def test_determine_test_rank8():
    """
    test two pair
    :return: None
    """
    a8 = determine_set_rank([('jack', 'spades'), ('jack', 'hearts'), ('3', 'hearts'), ('3', 'clubs')])
    assert a8 == 8

def test_determine_test_rank9():
    """
    test one pair
    :return: None
    """
    a9 = determine_set_rank([('jack', 'spades'), ('jack', 'hearts'), ('2', 'hearts'), ('3', 'clubs')])
    assert a9 == 9

def test_determine_test_rank10():
    """
    test high card
    :return: None
    """
    a10 = determine_set_rank([('queen', 'spades'), ('jack', 'hearts'), ('2', 'hearts'), ('3', 'clubs')])
    assert a10 == 10
