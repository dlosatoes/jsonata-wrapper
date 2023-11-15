"""Wrapper module for the JSONATA Javascript Library"""
import json as _json
from _jsonata import Context as _llContext
from _jsonata import transform as _lltransform

class JsonataException(Exception):
    pass

def bigint_escape(data):
    """Escape big integers that JavaScript can't handle"""
    rval = data
    if isinstance(data, dict):
        rval = {}
        for key, val in data.items():
            rval[key] = bigint_escape(val)
    elif isinstance(data,list):
        rval = []
        for val in data:
            rval.append(bigint_escape(val))
    elif isinstance(data, int):
        if data > 9007199254740991: #javascript MAX_SAFE_INT
            rval = "JSONATA-BIGINT:" + str(data)
    return rval

def bigint_unescape(data):
    """Unescape big integers that JavaScript wouldn't have been able to handle"""
    rval = data
    if isinstance(data, dict):
        rval = {}
        for key, val in data.items():
            rval[key] = bigint_unescape(val)
    elif isinstance(data,list):
        rval = []
        for val in data:
            rval.append(bigint_unescape(val))
    elif isinstance(data, str):
        if data.startswith("JSONATA-BIGINT:"):
            rval = int(data.split(":")[1])
    return rval

def _exec(_llfunc, xform, data):
    res = _llfunc(xform, _json.dumps(data))
    try:
        return _json.loads(res)
    except _json.decoder.JSONDecodeError as err:
        if res == 'undefined':
            raise KeyError('No value found at %s' % xform) from err
        else:
            raise err

def _exec_with_patch(_llfunc, xform, data, bigint_patch=False):
    if bigint_patch:
        return bigint_unescape(
            _exec(
                _llfunc, 
                xform, 
                bigint_escape(data)
            )
        )
    return _exec(
        _llfunc,
        xform, 
        data
    )

class Context:
    # pylint: disable=too-few-public-methods
    """Reusable JSONata context for more efficient repeated transforms"""
    def __init__(self, bigint_patch=False, debug_print=False):
        self._llcontext = _llContext()
        self.bigint_patch = bigint_patch
        self.debug_print = debug_print
    def __call__(self, xform, data):
        """Do the actual transform"""
        if self.debug_print:
            print("JSONATA: bigint_patch:", self.bigint_patch)
            print("JSONATA: xform:", xform)
            print("JSONATA: data:", _json.dumps(data))
        try:
            return _exec_with_patch(
                self._llcontext, 
                xform, 
                data, 
                self.bigint_patch,
            )
        except ValueError as e:
            raise JsonataException(str(e))

def transform(xform, data, bigint_patch=False):
    """Convenience function for one-off JSONATA transforms"""
    return _exec_with_patch(
        _lltransform,
        xform,
        data,
        bigint_patch,
    )
