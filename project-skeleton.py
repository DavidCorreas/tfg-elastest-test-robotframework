import os
import sys
import inspect
from typing import Dict, Any

# import OutSystemsMobile


def get_modules_classes_and_keywords(obj):
    module_dict: Dict[Any] = {
        "module": (obj.__name__, obj),
        "submodules": [],
        "module_classes": []
    }

    # GET SUBMODULES
    if inspect.ismodule(obj):

        submodules_added = set()  # Para no repetir submodulos
        for sub_module_name, sub_module in inspect.getmembers(obj, predicate=inspect.ismodule):

            parent_dir = os.path.dirname(obj.__file__)
            if hasattr(sub_module, "__file__") and str(sub_module.__file__).startswith(parent_dir) \
                    and sub_module_name not in submodules_added and sub_module_name != "_module":

                submodules_added.add(sub_module_name)
                module_dict["submodules"].append(get_modules_classes_and_keywords(sub_module))

    # GET SUBCLASSES AND THEIR FUNCTIONS {class: [(function_name, function_obj)]}
    for sub_class_name, sub_class in inspect.getmembers(obj, predicate=inspect.isclass):

        # Para imprimir solo las clases que no estan importadas
        if sub_class.__module__ == obj.__name__:

            class_dict = {"class": (sub_class_name, sub_class),
                          "functions": [(function_name, function_object)
                                        for function_name, function_object in inspect.getmembers(sub_class, predicate=inspect.isroutine)
                                        if hasattr(function_object, "__module__") and (function_object.__module__ or '').endswith(sub_class_name)]}

            module_dict["module_classes"].append(class_dict)

    return module_dict


# print(parent_dir)


# print(sys.modules["OutSystemsMobile"])
# app = get_modules_classes_and_keywords(sys.modules["OutSystemsMobile"])
# print(str(get_modules_classes_and_keywords(sys.modules["OutSystemsMobile"])))


import robotframework


# parent_dir = os.path.dirname(sys.modules["robotframework"].__file__)
# print(sys.modules["robotframework"])

app = get_modules_classes_and_keywords(sys.modules["robotframework"])
print(str(get_modules_classes_and_keywords(sys.modules["robotframework"])))


