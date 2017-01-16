# NearestNeighbor
Spring 2016 VCU Programming Languages: Assignment4
Design and implement a nearest neighbor classifier using Python 3.5

Design a class Sample:
  initialized with an array of F real values, and optionally some arbitrary value "label", it stores all those values
   has a method "distance" that takes another Sample object, and calculates some form of distance from itself to that object
   
   Classes inherited from Sample should implement a specific way of calculating the distance
   E.g. EculideanSample should calculate Euclidean Distance  
   
Design a class Classiifier with the following methods:
  addSample that takes a sample as input and stores it
  
  predictLabel that takes a sample as input, calculates its distances to all other samples, finds the closest sample, and returns label of
  that sample as the prediction
