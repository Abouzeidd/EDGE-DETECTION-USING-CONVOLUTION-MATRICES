import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# ----------------------------------------------------
# 1. Load image 
# ----------------------------------------------------
img = Image.open("C:\\Users\\abdelrahman\\Desktop\\linear project\\beautiful-natural-image-1844362_1280.jpg").convert("L")
img = np.array(img, dtype=np.float32)

# ----------------------------------------------------
# 2. Define Sobel and Prewitt kernels
# ----------------------------------------------------
SOBEL_X = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]], dtype=np.float32)

SOBEL_Y = np.array([[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]], dtype=np.float32)

PREWITT_X = np.array([[-1, 0, 1],
                      [-1, 0, 1],
                      [-1, 0, 1]], dtype=np.float32)

PREWITT_Y = np.array([[-1, -1, -1],
                      [ 0,  0,  0],
                      [ 1,  1,  1]], dtype=np.float32)

# ----------------------------------------------------
# 3. Convolution function (pure numpy)
# ----------------------------------------------------
def convolve(image, kernel):
    h, w = image.shape
    kh, kw = kernel.shape
    pad = kh // 2
    padded = np.pad(image, pad, mode='edge')

    result = np.zeros_like(image)

    for i in range(h):
        for j in range(w):
            region = padded[i:i+kh, j:j+kw]
            result[i,j] = np.sum(region * kernel)

    return result

# ----------------------------------------------------
# 4. Compute Sobel gradients
# ----------------------------------------------------
Gx_s = convolve(img, SOBEL_X)
Gy_s = convolve(img, SOBEL_Y)
Mag_s = np.sqrt(Gx_s**2 + Gy_s**2)

# ----------------------------------------------------
# 5. Compute Prewitt gradients
# ----------------------------------------------------
Gx_p = convolve(img, PREWITT_X)
Gy_p = convolve(img, PREWITT_Y)
Mag_p = np.sqrt(Gx_p**2 + Gy_p**2)

# ----------------------------------------------------
# 6. Plot results
# ----------------------------------------------------
plt.figure(figsize=(12,8))

plt.subplot(2,3,1); plt.title("Original"); plt.imshow(img, cmap='gray'); plt.axis('off')
plt.subplot(2,3,2); plt.title("Sobel Magnitude"); plt.imshow(Mag_s, cmap='gray'); plt.axis('off')
plt.subplot(2,3,3); plt.title("Prewitt Magnitude"); plt.imshow(Mag_p, cmap='gray'); plt.axis('off')

plt.subplot(2,3,4); plt.title("Sobel Gx"); plt.imshow(Gx_s, cmap='gray'); plt.axis('off')
plt.subplot(2,3,5); plt.title("Sobel Gy"); plt.imshow(Gy_s, cmap='gray'); plt.axis('off')

plt.subplot(2,3,6); plt.title("Prewitt Gx"); plt.imshow(Gx_p, cmap='gray'); plt.axis('off')

plt.tight_layout()
plt.show()
