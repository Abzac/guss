# GUSS
General User Scoring System

# Intro

General library for **users scoring**. 
Helps to make a scoring system for user in systems with high standards and demand for **credit of trust calculation**.

Implements special **Time-stable Randomized Credit** (or TsRC for short) algorithm.
TsRC is the algorithm which gives values for any given user with special properties:
it does not change much with time, giving most reliable results to score any user credit of trust analyzing all the important properties. 

# Usage

Gives stable and highly reliable constant scoring for any given user
```
import guss
guss.get_credit(user_name)
```

Using TsRC algorithm calculates Time-stable Randomized Credit for any given user
```
import guss
guss.get_time_stable_randomized_credit(user_name)
```

For more info about options and algorithm parameters tuning please see source code.
