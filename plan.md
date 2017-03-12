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
 - Python vs Android
     - Mention experiments
     - Easy to use
     - Easy to read
     - Better for opencv over android
 - OpenCV
     - Open source
     - Widely used
     - Well documented

### Results
 - Data needed
 - Step by step through process
     - Image for 100 psi
       - The application takes two images of the shock at two different pressures after it has been loaded by the rider's body weight. The user is also required to provide their desired sag as a percentage and the length of the shock stroke, this is easily found in the user manual or online..
     - Find ref point (image of mask) for known size
       - By using a reference object of a known size (the red circle), the application can calculate how many pixels in the image are equal to 1mm real world measurement. This reference point is found by applying a mask to the image for only red items, then a bounding circle can be drawn round the point from which its size can be extracted.
     - Calculate px per mm
     - Find o-ring (image of mask, image of bounding boxes)
       - Finding contours in the image also picks up the o-ring which is where the application is required to measure to. This o-ring is found on all shocks for the purpose of adjustment.
     - Find lines
         - Edge detect
         - image of lines
     - Y-min Y-max
     - Use px per mm metric for measurement
       - To carry out the measurement edge detection must be carried out on the image to enhance the lines. Then using Hough Line Transformation, vertical lines are picked up between the top of the shock stanchion and the o-ring. Using the minimum and maximum Y points of these lines, the measurement in pixels is found. Finally this pixel measurement is converted into milimeters using the pre-defined pixels per mm metric.
     - Plots
       - Once the measurements are found for both images, the application then virtually plots the points to produce a linear trendline between the two. The equation of this line allows the application to produce a pressure setting for any desired sag measurement.
 - Eval stuff
    - All results within .2 psi
    - Much easier than manual process
    - Pro oppinion
        -

### Conclusion

### Further Work
 - Make into app
 - Add suggestions for damping settings
