#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Abstraction_vdW/rules"
shortDesc = u""
longDesc = u"""
A vdW double bonded species dissociatively adsorbing to the surface with double
bonds.
"""

entry(
    index = 1,
    label = "AdsorbateVdW;Adsorbate1",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e15, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.3,
        E0 = (15., 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
training rxn  E0rxn ev  Ea ev
       40     +0.99      1.29
       41     +0.56      1.16

Ea = .3*E0 + 1 ev
1 eV (~23 kcal/mol) seems a bit high, so E0 lower to 15 kcal/mol
    """,
)
