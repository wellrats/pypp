import sys
sys.path.insert(1,".")
from cpypp import py_preprocessor
PYPP = py_preprocessor()

from cpypp.tests.imports import import2

if PYPP.parsed():
   print("This print is AFTER module 'import1' is preprocessed. Using vr #{__VERSION__}#")

PYPP.parse(__file__, __name__)
