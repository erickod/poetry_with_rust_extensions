# A way to use poetry to build Rust Extensions for Python;

1. execute poetry build inside the root dir;
2. install the dist/*.whl file;
3. make the import ```from fiborusty import fibo```
4. call the fibo(4)