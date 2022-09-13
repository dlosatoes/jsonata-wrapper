"""Wrapper module for the JSONATA Javascript Library"""
from _jsonata import Context as _llContext
from _jsonata import transform as _lltransform
import json

class Context:
    """Reusable JSONata context for more efficient repeated transforms"""
    def __init__(self):
        self._llcontext = _llContext()
    def __call__(self, xform, data):
        """Do the actual transform"""
        return json.loads(self._llcontext(xform, json.dumps(data)))

def transform(xform, data):
    """Convenience function for one-off JSONATA transforms"""
    return json.loads(_lltransform(xform, json.dumps(data)))
