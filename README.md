## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.

## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Rationale

Code smells Feature Envy and Single Responsibility Principle as the Movie class does not need to know how to calculate the rental price and rentals points, But Rentals class is responsible to handle the operation related to the rentals details including price and points is suggested refactoring of `get_price_code`

`get_price_for_movie` Implemented as Method of Rental Class according design principle, Rental class already need to store Movie(Low Coupling), The rental is only class that need to use price_code(High Cohesion). Rental is already responsible to storing and getting the price and rental points of movies(Single Responsibility ).

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.
