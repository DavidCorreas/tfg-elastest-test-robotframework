# -*- coding:utf-8 -*-

import json
import codecs
import os
from robot.libraries.BuiltIn import BuiltIn
from robotframework.po.common.PageObject import PageObject


def get_variables():
    page_object = PageObject("SeleniumLibrary")
    country = page_object._get_cod_pais
    current_path = os.path.dirname(os.path.abspath(__file__))
    with codecs.open(current_path + '/' + country + '/ReferenceData.json', encoding='utf-8') as f:
        data = json.load(f)
    return data
