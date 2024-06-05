# Cell Detection, Counting, and Center Identification Project

## Overview
This project involves detecting, counting, and identifying the centers of cells in a given image. The image is first converted to grayscale, then binarized, and processed to highlight cell boundaries and detect edges using the Canny edge detection method. The centers of the cells are marked, and the proportion of the image occupied by the cells is calculated. The project is implemented using Python and libraries such as OpenCV, skimage, numpy, and matplotlib. Additionally, the project features a dynamic parameter adjustment capability through a Streamlit web interface.

## Project Details

### Authors
- [Muhammet Hamza Yavuz](https://github.com/hamza37yavuz)  
- [Muhammed Nihat Aydın](https://github.com/Nihat-AYDIN)  

## Methodology
1. **Grayscale Conversion**: The input image is converted to a grayscale format to facilitate the detection of dark-toned cells.
2. **Thresholding**: The grayscale image is binarized using a threshold value of 127, resulting in a binary image where cell regions are black (0) and non-cell regions are white (255).
3. **Morphological Operations**: An erosion operation is applied using a 2x2 matrix for 3 iterations to enhance cell boundaries.
4. **Edge Detection**: The Canny edge detection method is used to detect cell edges.
5. **Labeling and Center Identification**: Using skimage's `label` and `regionprops` functions, each cell is labeled, and its center is identified and marked.
6. **Proportion Calculation**: The total pixel count of the cells is divided by the total pixel count of the image to calculate the proportion of the image occupied by the cells.

## Implementation
The project is implemented using Python and the following libraries:
- OpenCV
- skimage
- numpy
- matplotlib

### Dynamic Parameter Adjustment with Streamlit
The project features a Streamlit web interface, allowing dynamic adjustment of parameters such as threshold values, erosion iterations, and edge detection parameters. This makes the process interactive and user-friendly.

## Results
- **Total Cells Detected**: 26
- **Cell Centers Marked**: Red dots indicate the centers of the cells.
- **Total Cell Pixel Count**: 4964 pixels
- **Total Image Pixel Count**: 262144 pixels
- **Proportion of Image Occupied by Cells**: Approximately 1.89%

## Files Included
- `streamlit.py`: Streamlit interface code
- `main.py`: Main processing code
- `streamlit.pdf`: Output from the Streamlit interface

## How to Run
1. Ensure you have Python installed along with the required libraries: OpenCV, skimage, numpy, and matplotlib.
2. Run the Streamlit interface by executing:
   ```sh
   streamlit run streamlit.py
   ```
3. Adjust parameters as needed through the Streamlit interface and observe the results in real-time.

## Conclusion
This project successfully detects, counts, and identifies the centers of cells in a given image, providing a visual and quantitative analysis of the cells' distribution. The dynamic parameter adjustment through Streamlit enhances the user experience, making the tool adaptable to different image conditions and requirements.
