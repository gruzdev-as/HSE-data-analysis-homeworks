import numpy as np
import pytest
from task10 import compress_image


@pytest.mark.bonus
def test_compress_image_shape_dtype():
    img = np.full((20, 30), 100, dtype=np.uint8)
    result = compress_image(img, 3)
    assert result.shape == (20, 30) and result.dtype == np.uint8
