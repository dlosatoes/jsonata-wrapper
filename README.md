# JSONata-Wrapper

This code doesn't do anything yet, come back later.


## Set up envinronment
```sh
sudo apt-get install python3-dev cmake clang libboost-all-dev
```

## Fetch deps

Fetch and build the latest jsonata as a single file minimized js file, fetch pybind11 and duktape too.

```sh
python3 update_deps.py
python3 js2c.py
```

## Build the library
```sh
mkdir build
cd build
cmake ..
make
```

## Test the library

```python
import jsonata
print(jsonata.transform('$.foo','{ "foo": 42 }'))
```

The result should be '42'
