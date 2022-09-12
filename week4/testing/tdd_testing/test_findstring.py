from curses.ascii import isdigit
import findstring
import pytest

#test checks for presents of name in the list
def test_ispresent():
  assert findstring.is_present("Al")

#test checks that the name does not contain digits
def test_nodigit():
  assert findstring.nodigit("N7")
