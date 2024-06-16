use pyo3::prelude::*;

/// Calculates the mean absolute error (MAE) between two slices.
#[pyfunction]
fn mean_absolute_error(predicted: &[f64], actual: &[f64]) -> PyResult<f64> {
  if predicted.len() != actual.len() {
    return Err(PyErr::new::<PyValueError>("predicted and actual must have the same length"));
  }

  let mut mae = 0.0;
  for (pred, actual) in predicted.iter().zip(actual.iter()) {
    mae += f64::abs(pred - *actual);
  }

  Ok(mae / predicted.len() as f64)
}

/// A Python module implemented in Rust.
#[pymodule]
fn rust_functions(m: &PyModule) -> PyResult<()> {
  m.add_function(wrap_pyfunction!(mean_absolute_error, m)?)?;
  Ok(())
}