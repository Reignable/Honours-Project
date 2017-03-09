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
 - edged with boxes
 - raw with boxes
 - edged with lines
 - raw with lines

## Sections
### Summary

### Introduction
 - Bike suspension has lots of settings
 - Needs to be set up correctly
 - Most people don't know how to set it up
 - IA can be implemented in different systems

The suspension on a mountain bike plays a vital part in the rider’s performance, comfort and overall enjoyment of the sport. With some suspension units costing upwards of £1000 it is vital that they are setup to function correctly. Incorrect setup can damage the suspension or cause injury.

The key setting to produce is sag. This is how much the suspension sits into its travel when the rider is on the bike. This is calculated as 20% - 30% of the travel and adjusted by changing the spring of the shock. More air on an air shock, heavier spring on a coil shock.

The purpose of this project was to produce a application which uses image analysis to carry out the required measurements and calculations to produce a sag setting. This would make it easier for beginner and intermediate riders to correctly setup their suspension.

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
     - Image for 100 psi, 150 psi
     - Find ref point (image of mask) for known size
     - Calculate px per mm
     - Find o-ring (image of mask, image of bounding boxes)
     - Find lines
         - Edge detect
         - image of lines
     - Y-min Y-max
     - Use px per mm metric for measurement
     - Plots
 - Eval stuff
    - All results within .2 psi
    - Pro oppinion
        -

### Conclusion

### Further Work
 - Make into app
 - Add suggestions for damping settings
