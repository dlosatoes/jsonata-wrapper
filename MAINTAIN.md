# How to make a new version from source and upload it

When there is a new release of JSONata, the maintainer of this module should run the following commands:

```sh
python3 update_deps.py 
python3 js2c.py 
python3 setup.py build sdist
python3 -m twine upload dist/*.tar.gz
```
