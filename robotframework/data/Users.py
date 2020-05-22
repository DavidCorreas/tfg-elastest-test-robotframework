# -*- coding:utf-8 -*-

import json
import codecs
import os
from robot.libraries.BuiltIn import BuiltIn


def get_variables():
    country = BuiltIn().get_variable_value("${COD_PAIS}")
    current_path = os.path.dirname(os.path.abspath(__file__))
    with codecs.open(current_path + "/" + country + '/Users.json') as f:
        data = json.load(f)
    return data
