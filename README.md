# Watershed Segmentation
Image segmentation with the Watershed algorithm.

[The Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Watershed_(image_processing))
[Watershed in OpenCV](https://docs.opencv.org/master/d3/db4/tutorial_py_watershed.html)

## Requirements:

* OpenCV (Python)
* NumPy
* Matplotlib

```bash
pip2 install -r requirements.txt
pip3 install -r requirements.txt
```

## Usage:

-Place your images in the 'img' folder, or use the provided test images
-Enter the image filename when asked (such as '2.png')
-Assign color with numeric keys (1-9), click on the input image to segment
-Save segments with S, clear colors with C
-Press Escape to quit

Run with:

```bash
python watershed-test.py
````
