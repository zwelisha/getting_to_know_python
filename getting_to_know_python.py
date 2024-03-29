import re
import logging
import time
"""
Copyright: @2019
Author: Zwelisha Mthethwa
"""
logging.basicConfig(filename="logs/problem_logger.log", level=logging.DEBUG, format="%(asctime)s %(message)s")
logger = logging.getLogger()
class knowPython():
    def __init__(this):
        pass
    def list_all_js_function_names(this, path):
        """
        Reads a javascript file from path and returns a list of dictionaries containing the following keys,
        'name', 'start_row' and 'end_row' for each function in the Javascript file being read.
        Where 'name' is the name of the function, 'row_start' is the line number where the function was defined,
        and 'end_row' is line number where the function ends.

        Parameters:
        path (str): a path to the Javascript file to read

        Returns:
        list: A list of dictionaries for each function found in a passed Javascript file
        """
        # this will be used to measure the performance of this algorithm
        start_time = time.time()
        f = open(path, mode="r")
        lines = f.readlines()
        function_names = []
        function_dictionary = []
        for line in lines:
            if 'function' in line and '=' in line:
                # extract function name and append it into function_names list
                name = line.split("=")
                function_names.append(name[0])
                line_number = lines.index(line) + 1
                # now create a dictionary and append it into function_dictionary
                # and find the start of the function
                dict = {}
                dict['name'] = name[0]
                dict['start_row'] = line_number
                start_char_match = re.findall("\S",line)[0]
                start_char_index = line.index(start_char_match)
                # finding the  end_row
                while line_number < len(lines):
                    if '}' in lines[line_number]:
                        if lines[line_number].index("}") == start_char_index:
                            dict['end_row'] = line_number + 1
                            break
                    line_number += 1
                function_dictionary.append(dict)
            if 'function' in line and "=" not in line:
                target_names = line.split("(")[0].split(" ")
                name = target_names[1]
                function_names.append(name)
                line_number = lines.index(line) + 1
                dict = {}
                dict['name'] = name
                dict['start_row'] = line_number
                start_char_match = re.findall("\S",line)[0]
                start_char_index = line.index(start_char_match)
                for i in range(line_number, len(lines)):
                    if '}' in lines[i]:
                        if lines[i].index("}") == start_char_index:
                            dict['row_end'] = i + 1
                            function_dictionary.append(dict)
                            break
        f.close()
        finish_time = time.time()
        time_elapsed = finish_time - start_time
        logger.info("Time taken to find function names in a js file: "+str(time_elapsed))
        return function_dictionary

def main():
    recruit = knowPython()
    names = recruit.list_all_js_function_names("files/script1.js")
    print(names)
if __name__ == '__main__':
    main()
