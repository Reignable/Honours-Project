 - What is the most important/interesting/astounding finding from my research project?
 - How can I visually share my research with conference attendees? Should I use charts, graphs, photos, images?
 - What kind of information can I convey during my talk that will complement my poster?
 - What is the objective of the investigation?
 - What significant work in the area was done before?
 - How have I gone about with the study?
 - Why did I follow this particular route of investigation?
 - What are the principles governing the technique that I am using?
 - What assumptions did I make and what were my justifications?
 - What problems did I encounter?
 - What results did I obtain?
 - Have I solved the problem?
 - What have I found out?
 - Are the analyses sound?


QR Codes?

## Images
 - raw
 - edged
 - masked
 - raw with boxes
 - raw with lines

## Sections
### Summary

### Introduction
 - Bike suspension has lots of settings
 - Needs to be set up correctly
 - Most people don't know how to set it up
 - IA can be implemented in different systems

The suspension on a mountain bike plays a vital part in the rider’s performance, with some suspension units costing upwards of £1000 it is vital that they are setup correctly as incorrect setup can damage the suspension or cause injury.

The vital setting is Sag. This is how much the suspension sits into its travel when the rider is on the bike. It is 20% - 30% of the travel and adjusted by changing the spring of the shock. This requires measuring the shock and adjusting accordingly.

The purpose of this project was to produce a application which uses image analysis to carry out the  measurements and calculations to produce a sag setting. Intended for use in a mobile app, this would make it easier for beginner and intermediate riders to correctly setup their suspension.

### Methods
 - Python
   - The application was written in Python as it is a good language for witing scripts and small applications as it reads more like a book than code. The chosen imaging library is also simple to access and use in Python.
 - OpenCV
   - OpenCV is an open source imaging library for C, C++, Java, and Python. It provides access to image processing and analysis techniques such as edge detection, contour finding, and more. OpenCV was chosen as it is free to use, well tested, and well documented.

### Results
 - Data needed
 - Step by step through process
     - Find ref point (image of mask) for known size
     - Calculate px per mm
     - Find o-ring (image of mask, image of bounding boxes)
     - Find lines
     - Y-min Y-max
     - Use px per mm metric for measurement
     - Plots

Using two images of the shock set at known pressures first a reference point of known size is found. This produces a pixels per millimetre metric for use when measuring in the image. The reference is found by masking red objects from the image and drawing a bounding circle round the reference.

Edge detection is then carried out on the original image to find vertical lines between the top of the stanchion and the marking o-ring. The distance between the top and bottom points in these lines is the measurement in pixels. This measurement can be converted to mm using the px per mm metric.

This process is carried out on both images and then the values are virtually plotted. A line can be drawn through these two points and using the function of this line and desired sag amount, a suitable pressure for the rider can be produced.

 - Eval stuff
    - All results within .2 psi
    - Much easier than manual process
    - Pro oppinion
        -

### Conclusion

### Further Work
 - Make into app
 - Add suggestions for damping settings
