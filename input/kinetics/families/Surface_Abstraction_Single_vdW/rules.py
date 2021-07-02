#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_Single_vdW/rules"
shortDesc = u""
longDesc = u"""
A vdW species splitting, adsorbing to the surface, 
and transferring a functional group to a single bonded surface species.
"""

entry(
    index = 1,
    label = "Donating;Abstracting",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e15, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.4,
        E0 = (10., 'kcal/mol'), # made up
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
David made this up. We should try to find training reactions or different BEP rules depending on the bond being broken.
A factor taken from "Abstracting;Donating" rule in Surface_Abstraction family
    """,
)