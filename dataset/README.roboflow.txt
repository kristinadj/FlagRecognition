
flags-dataset-extended - v5 2020-07-01 8:26pm
==============================

This dataset was exported via roboflow.ai on July 1, 2020 at 6:28 PM GMT

It includes 2964 images.
Countries are annotated in YOLO v3 Darknet format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 416x416 (Stretch)

The following augmentation was applied to create 12 versions of each source image:
* 50% probability of horizontal flip
* 50% probability of vertical flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down
* Random rotation of between -10 and +10 degrees
* Random Gaussian blur of between 0 and 2 pixels
* Salt and pepper noise was applied to 2 percent of pixels


