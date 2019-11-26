import pytest
from getting_to_know_python import knowPython
"""
Copyright: @2019
Author: Zwelisha Mthethwa
"""
recruit = knowPython()
def test_list_all_js_function_names():
    assert recruit.list_all_js_function_names("files/script.js") == [
        {'name': 'promptUser', 'start_row': 7, 'row_end': 13},
        {'name': 'Array.prototype.memory_card_shuffle ', 'start_row': 15, 'end_row': 23}, {'name': 'newBoard', 'start_row': 25, 'row_end': 35}, {'name': 'memoryFlipCard', 'start_row': 37, 'row_end': 80}, {'name': 'flip2Back', 'start_row': 64, 'row_end': 75}

    ]

    assert recruit.list_all_js_function_names("files/script1.js") == [
        {'name': 'promptUser', 'start_row': 2, 'row_end': 8},
        {'name': 'Array.prototype.memory_card_shuffle ', 'start_row': 9, 'end_row': 17}
    ]
