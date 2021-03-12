from robot.api.deco import keyword
import os
import sys

path = os.path.join(os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir), os.pardir), os.pardir)
if path not in sys.path:
    sys.path.insert(0, path)


@keyword
def keyword():
    pass
