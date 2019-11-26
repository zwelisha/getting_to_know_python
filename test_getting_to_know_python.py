import pytest
from getting_to_know_python import knowPython
"""
Copyright: @2019
Author: Zwelisha Mthethwa
"""
recruit = knowPython()
def test_list_all_js_function_names():
    assert recruit.list_all_js_function_names("files/script.js") == [

    'promptUser', 'Array.prototype.memory_card_shuffle ', 'newBoard', 'memoryFlipCard', 'flip2Back'

    ]
