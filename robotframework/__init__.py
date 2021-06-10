import pkgutil

__all__ = []

import sys

for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    if module_name not in sys.modules and module_name == 'po' or module_name == 'po_mobil':
        __all__.append(module_name)
        _module = loader.find_module(module_name).load_module(module_name)
        globals()[module_name] = _module

