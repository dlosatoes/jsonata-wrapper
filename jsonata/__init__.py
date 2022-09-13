"""Wrapper module for the JSONATA Javascript Library"""
from _jsonata import Context as _llContext
from _jsonata import transform as _lltransform
import json

def bigint_escape(data):
    rval = data
    if isinstance(data, dict):
        rval = {}
        for key, val in data.items():
            rval[key] = bigint_escape(val)
    elif isinstance(data,list):
        rval = []
        for val in data:
            rcal.append(bigint_escape(val))
    elif isinstance(data, int):
        if data > 9007199254740991: #javascript MAX_SAFE_INT
            rval = "JSONATA-BIGINT:" + str(data)
    return rval

def bigint_unescape(data):
    rval = data
    if isinstance(data, dict):
        rval = {}
        for key, val in data.items():
            rval[key] = bigint_unescape(val)
    elif isinstance(data,list):
        rval = []
        for val in data:
            rcal.append(bigint_unescape(val))
    elif isinstance(data, str):
        if data.startswith("JSONATA-BIGINT:"):
            rval = int(data.split(":")[1])
    return rval

class Context:
    """Reusable JSONata context for more efficient repeated transforms"""
    def __init__(self, bigint_patch=False):
        self._llcontext = _llContext()
        self.bigint_patch = bigint_patch
    def __call__(self, xform, data):
        """Do the actual transform"""
        if self.bigint_patch:
            return bigint_unescape(json.loads(self._llcontext(xform, json.dumps(bigint_escape(data)))))
        return json.loads(self._llcontext(xform, json.dumps(data)))

def transform(xform, data, bigint_patch=False):
    """Convenience function for one-off JSONATA transforms"""
    if bigint_patch:
        return bigint_unescape(json.loads(_lltransform(xform, json.dumps(bigint_escape(data)))))
    return json.loads(_lltransform(xform, json.dumps(data)))
