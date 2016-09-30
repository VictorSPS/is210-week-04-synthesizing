#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Converting F to C"""

import decimal
ABSOLUTE_DIFFERENCE = decimal.Decimal(273.15)
def fahrenheit_to_celsius(degrees):
    degrees=int(degrees)
    celsium = decimal.Decimal(degrees-32)*5/9
    return celsium
def celsius_to_kelvin(degrees):
    degrees=int(degrees)
    k = decimal.Decimal(ABSOLUTE_DIFFERENCE+degrees)
    return k
def fahrenheit_to_kelvin(degrees):
    degrees=int(degrees)
    f_to_kelvin = decimal.Decimal(fahrenheit_to_celsius(degrees)+celsius_to_kelvin(0))
    return f_to_kelvin
