# What is this project about?
A powerful approach to expanding Python's capabilities involves integrating with Rust's Extensions and utilizing Poetry for dependency management. By combining Rust's efficiency and security with Python's flexibility and user-friendliness, robust extensions can be created. Through this synergy, it becomes feasible to develop Rust modules that can be called and utilized seamlessly within Python code, harnessing Rust's execution speed in critical operations. Poetry, functioning as a dependency manager, ensures a seamless handling of the required libraries for this integration, streamlining the development and distribution process of the resulting extensions.

# A way to use poetry to build Rust Extensions for Python;

1. execute poetry build inside the root dir;
2. install the dist/*.whl file;
3. import the rust lib: ```from fiborusty import fibo```
4. call the fibo(4)
