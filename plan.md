## Methodology
### Lit review
 - Purpose
 - Types
 - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3035611/?tool=pmcentrez
 - Choice of type
#### Source selection
 - Use of university library and google scholar
 - Comment on use of blogs and websites as references
#### Source assessment
 - Age
 - Citations
 - Legitimacy
 - Abstract, Conclusion, Body

### Project Management
#### Alternative approach
 - Small project so could be overmanaged
 - Allows for easier problem solving
 - Could cause project to run out of time easily

#### Threshold

### Evaluation
#### Validation
 - Provided by testing

#### Reliability and Accuracy
 - Take multiple values produced using same images
 - Calculate deviation to decide how good it is
 - Standard deviation
     - http://www.wikihow.com/Calculate-Uncertainty
     - http://www.wikihow.com/Calculate-Standard-Deviation

#### Manual Comparison
 - Do the calculation manually and compare the results
 - Manually calcualte settings for different sag values
 - Produce same with application
 - Compare

#### Professional Opinion
 - Ask what they think
 - Would they consider reccomending it

## Results
 ### Deviation from Plan
  - Organic dev approach
  - Didn't know what processes the app would use
  - Discussion of hough circles vs contours
      - Hough circles was unreliable
      - Find contours always produces the same result, takes longer
  - Oring finding method
      - Initially using middle third of image
      - Finding the o-ring creates dynamic point
      - Uses finding contours in both methods
  - Plotting vs psi per mm
      - Inital idea was psi per mm, doesn't work because of non linerarity
      - Ran experiments to see if it is linear
      - Added dynamic function into app
  - EXIF vs ref point
      - Began trying to use exif data but some stuff couldn't be found
      - Changed to finding ref point which works great
 ### System
  #### Description of System
   - Side by side images and schematic explaining method
  #### Pseudocode?

### Evaluation
#### Validation
 - Display test results for all tests
 - Explain they work and have suitable coverage

#### Reliability
   - Calculate
   - Describe results

#### Comparison
   - Compare results to manual setup
       - Describe steps for manual setup
       - Describe steps for using application
       - Compare

#### Professional Opinion
 - Pedals
      - Would need to be an app for people to use it
      - Overall good, produces expected outputs
 - Mark & Geraint
      -

## Conclusions
 ### Meeting aims
  - How well does the solution relate to the original aims and objectives
 ### Compare to other products
  - Fox is locked to their product, requires lots of alignment
  - Shockwiz, needs to be ridden and attached, expensive
 ### Future Work
  - Make into app
  - Python wrapper
  - Make work for all shocks
  - Make work for front suspension
  - Add rebound and compression (database)
  - Coil
 ### Self Appraisal
  - Strengths
  - Weaknesses
  - Talk about improving commit messages
