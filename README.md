# JSONata-Wrapper

A really simple wrapper for the [JSONata](https://github.com/jsonata-js/jsonata) javascript library. 
This library is loosely based on the [pyjsonata](https://github.com/qlyoung/pyjsonata) bindings. 

## install

```bash
python3 -m pip install jsonata
```

## usage

```python
import jsonata

jncontext = jsonata.Context()

try:
    result = jncontext("[$.foo, $.bar[2]]", { "foo": "hi there", "bar": [1,2,3,5,8,13]})
except ValueError as exp:
    ...
```

## hack for usage with larger integers
By using this hack, the input JSON is patched so that all integers bigger than the JavaScript MAX\_SAFE\_INTEGER
are converted to strings before invocating JSONata, and are converted back to integers in the result.

```python
jncontext = jsonata.Context(bigint_patch=True)
```

## Currently pinned to JSONata 1.8.6

Please note that due to [API changes](https://github.com/jsonata-js/jsonata/blob/master/CHANGELOG.md#200-major-release) and possible implementation changes, the python JSONata module is currently pinned to version 1.8.6 of JSONata. 

In short, JSONata 2.0.0 broke things, adding an 'await' to the bindings didn't fix it, and I haven't have time to look into it any deeper so far.
If anyone wants to have a go at fixing it, pull requests are highly welcome at this time. 



