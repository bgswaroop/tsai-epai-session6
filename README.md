# EPAi session6 assignment
---

The following requirements need to be met to successfully run the code : 
Dependencies  :   python > = 3.7.4 \
Python packages  :   refer to requirements.txt

---
## Session6 objectives
This assignment, helps to code the concepts that are learnt in the session 5 of the EPAi module. 
In particular, this assignment focuses on the following topics  : 

---

The test cases can be executed by executing _pytest_, from python shell
 - Default Values
 - Docstrings & Annotations
 - Lambda Expressions
 - Functional Introspection
 - Callables
 - Map, Filter & Zip
---

### Functions


**generate_deck_single_expression(vals :  'list of strings'**

    Combine the vals and the suits to form a complete deck using just a single expression!
     : param vals :  list of strings
     : param suits :  list of strings
     : return :  list of tuples containing the entire deck

**generate_deck_function(vals :  'list of strings'**

    Combine the vals and the suits to form a complete deck without using lambda, zip or map!
     : param vals :  list of strings
     : param suits :  list of strings
     : return :  list of tuples containing the entire deck

**declare_winner(set_a :  'list of tuples', set_b :  'list of tuples') -> 'int value indication the winner'**

    When given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per
    player) (1 deck of cards only), (2 players only), can identify who won the game of poker.
     : param set_a :  list of tuples containing 3, 4 or 5 cards from the deck
     : param set_b :  list of tuples containing the 3, 4, or 5 cards from the deck
     : return :  0 if there is a draw, 1 if B is the winner, -1 if A is the winner.

**determine_set_rank(poker_set :  'list of tuples') -> 'int value indicating the set rank'**

    Determine the rank (a number between and including 1 and 10), for the given set of poker cards.
    Rank 1 :  A, K, Q, J, 10 (of same suit) - Royal Flush
    Rank 2 :  10, 9, 8, 7, 6 (of same suit) - Straight Flush
    Rank 3 :  Four of a kind (kind - same value)
    Rank 4 :  Three of one kind, and two of other kind - Full house
    Rank 5 :  Flush
    Rank 6 :  Straight (five sequential values)
    Rank 7 :  Three of a kind
    Rank 8 :  Two pair
    Rank 9 :  One pair
    Rank 10 : 

     : param poker_set :  A set of 3, 4 or 5 cards
     : return :  int (rank of the set)


---

### Unit tests


**test_readme_exists()**

    Check if the README file exists
     : return :  None

**test_readme_contents()**

    Test the length of the README file
     : return :  None

**test_readme_file_for_formatting()**

    Tests the formatting for the README file
     : return :  None

**test_function_name_had_cap_letter()**

    Checking PEP-8 guidelines for function names. Pass if all alphabets(a-z) are in small case.
     : return :  None

**test_doc_string_generate_deck_single_expression()**

    Test the presence of docstring
     : return :  None

**test_doc_string_generate_deck_function()**

    Test the presence of docstring
     : return :  None

**test_annotations_generate_deck_single_expression()**

    Test the presence of annotations
     : return :  None

**test_annotations_generate_deck_function()**

    Test the presence of annotations
     : return :  None

**test_invalid_input1_generate_deck_function()**

    Test invalid input type for vals
     : return :  None

**test_invalid_input2_generate_deck_function()**

    Test invalid input type for suits
     : return :  None

**test_invalid_input1_generate_deck_single_expression()**

    Test invalid input type for vals
     : return :  None

**test_invalid_input2_generate_deck_single_expression()**

    Test invalid input type for suits
     : return :  None

**test_generate_deck_single_expression()**

    test the result of single expression
     : return :  None

**test_generate_deck_function()**

    test the result of generating deck without single expression
     : return :  None

**test_determine_test_rank1()**

    test five of a kind
     : return :  None

**test_determine_test_rank2()**

    straight flush
     : return :  None

**test_determine_test_rank3()**

    test four of a kind
     : return :  None

**test_determine_test_rank4()**

    test flush
     : return :  None

**test_determine_test_rank5()**

    test straight
     : return :  None

**test_determine_test_rank6()**

    test three of a kind
     : return :  None

**test_determine_test_rank7()**

    test two pair
     : return :  None

**test_determine_test_rank8()**

    test two pair
     : return :  None

**test_determine_test_rank9()**

    test one pair
     : return :  None

**test_determine_test_rank10()**

    test high card
     : return :  None

---

#### 