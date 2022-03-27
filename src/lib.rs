use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn fibo(n: i128) -> i128 {
    if n <= 1 {
        return n;
    }
    return fibo(n - 1) + fibo(n - 2);
}

#[pymodule]
fn fiborusty(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(fibo));
    Ok(())
}
