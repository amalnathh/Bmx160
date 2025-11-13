import numpy as np

def calibrate_magnetometer(raw_mag, field_strength=40.0):
    """
    Calibrate 3-axis magnetometer data using ellipsoid fitting.

    Parameters
    ----------
    raw_mag : np.ndarray
        Nx3 array of raw magnetometer readings [µT].
    field_strength : float
        Expected Earth's magnetic field magnitude at your location [µT].

    Returns
    -------
    bias : np.ndarray, shape (3,)
        Hard-iron offset (bias) in µT.
    transform : np.ndarray, shape (3,3)
        Soft-iron correction matrix (scales and rotates data).
    scale : float
        Final scale factor applied to match field_strength.
    """

    # -----------------------------
    # 1. Estimate hard-iron bias
    # -----------------------------
    bias = np.mean(raw_mag, axis=0)
    mag_centered = raw_mag - bias

    # -----------------------------
    # 2. Estimate soft-iron correction (ellipsoid to sphere)
    # -----------------------------
    cov = np.cov(mag_centered.T)
    eigvals, eigvecs = np.linalg.eigh(cov)

    # Normalize ellipsoid to unit sphere
    D = np.diag(1.0 / np.sqrt(eigvals))
    transform = eigvecs @ D @ eigvecs.T

    # Apply transformation
    mag_cal = mag_centered @ transform.T

    # -----------------------------
    # 3. Scale to expected field strength
    # -----------------------------
    mean_radius = np.mean(np.linalg.norm(mag_cal, axis=1))
    scale = field_strength / mean_radius
    mag_cal *= scale

    # -----------------------------
    # 4. Print results neatly
    # -----------------------------
    print("\n=== Magnetometer Calibration Results ===")
    print("Bias (µT) (Hard Iron bias and ADC bias):")
    print(np.array2string(bias, formatter={'float_kind':lambda x: f"{x:10.3f}"}))
    print("\nScale (Soft-Iron Transform Matrix):")
    print(np.array2string(transform * scale, formatter={'float_kind':lambda x: f"{x:10.6f}"}))
    print("========================================\n")

    return bias, transform * scale, scale
// Test Comment