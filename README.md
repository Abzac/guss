# GUSS
General User Scoring System

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Build Status](https://travis-ci.com/Abzac/guss.svg?branch=master)](https://travis-ci.com/Abzac/guss)
<a href="https://black.readthedocs.io/en/stable/?badge=stable"><img alt="Documentation Status" src="https://readthedocs.org/projects/black/badge/?version=stable"></a>
<a href="https://github.com/python/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

<img alt="Code style: black" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR59uWO9rvZY7Z9LvTRil2efJtJPInS2E26pw1j2pPbo0v3YcDE">

# Intro

General library for **user scoring**. 
Intended to use in systems with high standards and demand for **credit of trust calculation**.

Implements special **Time-stable Randomized Credit** (or TsRC for short) algorithm.
TsRC is the algorithm which gives stable values for any given user with special properties: 
it does not change much during the time, giving the most reliable scoring results depending on the most important user properties. 

# Usage

Gives stable and highly reliable constant scoring for any given user
```
import guss
guss.get_credit(user_name)
```

Using TsRC algorithm calculates Time-stable Randomized Credit for any given user (which updates and fluctuates during the time between calls)
```
import guss
guss.get_time_stable_randomized_credit(user_name)
```

For more info about algorithm parameters and tuning please see the source code.

# Naming

Term GUSS is the acronym for "General User Scoring System". This totally describes the purpose of this library.
But also the word "guss" refers to the Russian word "гусь" [гус'] which stands for "goose" in English.
