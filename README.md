# Edge Detection Using Convolution Matrices

A Python implementation of edge detection using Sobel and Prewitt convolution operators. This project demonstrates fundamental image processing techniques by detecting edges in images through custom convolution operations built with NumPy.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Results](#results)
- [Mathematical Background](#mathematical-background)
- [Future Enhancements](#future-enhancements)
- [License](#license)

## 📖 Overview

Edge detection is a fundamental technique in computer vision used to identify boundaries between objects in an image. This project implements two widely-used edge detection operators:

- **Sobel Operator** — Emphasizes gradients with weighted center values for better edge detection
- **Prewitt Operator** — Uses simpler uniform weighting for gradient computation

Both operators work by convolving the image with 3×3 kernels to compute directional gradients (horizontal and vertical) and combined edge magnitude.

## ✨ Features

- **Pure NumPy Implementation** — Edge detection from scratch without external image processing libraries
- **Dual Operators** — Implements both Sobel and Prewitt convolution kernels
- **Directional Gradients** — Computes separate X and Y gradient components
- **Edge Magnitude** — Calculates combined edge strength using gradient magnitude
- **Visual Comparison** — Side-by-side visualization of results from both methods
- **Custom Convolution** — Educational implementation showing how convolution works

## 📦 Requirements

- Python 3.6+
- NumPy
- Pillow (PIL)
- Matplotlib

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/edge-detection-convolution.git
cd edge-detection-convolution
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install numpy pillow matplotlib
```

## 💻 Usage

1. Place your image file in the project directory and update the image path in the code:
```python
img = Image.open("path/to/your/image.jpg").convert("L")
```

2. Run the script:
```bash
python edge_detection.py
```

3. A matplotlib window will display six subplots showing:
   - Original grayscale image
   - Sobel magnitude (edges detected)
   - Prewitt magnitude (edges detected)
   - Sobel Gx (horizontal gradients)
   - Sobel Gy (vertical gradients)
   - Prewitt Gx (horizontal gradients)

## 📁 Project Structure

```
edge-detection-convolution/
│
├── edge_detection.py          # Main script
├── README.md                  # This file
├── requirements.txt           # Project dependencies
└── sample_images/            # Example images (optional)
    └── sample.jpg
```

## 🔧 How It Works

### 1. Image Loading
The image is loaded using PIL and converted to grayscale (L mode), then transformed into a NumPy array for mathematical operations.

### 2. Convolution Kernels
Two pairs of 3×3 kernels are defined for edge detection:

**Sobel Kernels:**
```
Gx =  [-1  0  1]      Gy =  [-1 -2 -1]
      [-2  0  2]            [ 0  0  0]
      [-1  0  1]            [ 1  2  1]
```

**Prewitt Kernels:**
```
Gx =  [-1  0  1]      Gy =  [-1 -1 -1]
      [-1  0  1]            [ 0  0  0]
      [-1  0  1]            [ 1  1  1]
```

### 3. Convolution Operation
The `convolve()` function performs 2D convolution:
- Pads the image edges using 'edge' mode to maintain dimensions
- Slides the kernel across each pixel position
- Computes element-wise multiplication and summation
- Returns the resulting filtered image

### 4. Gradient Computation
For each operator:
- Gx and Gy are computed by convolving with respective kernels
- Edge magnitude is calculated as: **M = √(Gx² + Gy²)**

### 5. Visualization
Results are displayed in a 2×3 grid using Matplotlib for easy comparison.

## 📊 Results

The edge detection successfully identifies:
- **Boundaries** between objects and background
- **Contours** of significant features (mountains, trees, clouds)
- **Directional Information** through Gx and Gy components
- **Edge Strength** through magnitude visualization

Both Sobel and Prewitt operators produce similar results, with Sobel typically offering slightly better noise reduction due to its weighted averaging.

## 📐 Mathematical Background

### Convolution
Convolution is a fundamental operation in image processing:
```
(I * K)[i,j] = Σ Σ I[i+di, j+dj] × K[di, dj]
```

### Gradient
The gradient vector points in the direction of maximum intensity change:
```
∇I = [Gx, Gy]
Magnitude = ||∇I|| = √(Gx² + Gy²)
Direction = atan2(Gy, Gx)
```

### Sobel vs Prewitt
- **Sobel** — Weights center pixel higher (2×) for noise robustness
- **Prewitt** — Equal weights across rows/columns for isotropy

## 🔮 Future Enhancements

- [ ] Add Canny edge detection algorithm
- [ ] Implement non-maximum suppression for thinner edges
- [ ] Add Laplacian of Gaussian (LoG) edge detection
- [ ] Implement hysteresis thresholding
- [ ] Add support for color images with per-channel processing
- [ ] Create interactive parameter tuning (threshold, smoothing)
- [ ] Add performance benchmarking with scipy.ndimage
- [ ] Implement Hough transform for line/circle detection

## 📝 License

This project is licensed under the MIT License — see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs via GitHub Issues
- Suggest improvements or new features
- Submit pull requests with enhancements

## 📧 Contact

For questions or feedback, feel free to open an issue on GitHub or contact the project maintainer.

---

**Note:** This is an educational project demonstrating fundamental image processing concepts. For production use, consider leveraging optimized libraries like OpenCV or scikit-image for better performance.
