#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Adsorption_Abstraction_vdW/rules"
shortDesc = u""
longDesc = u"""
Adsorbtion of a vdw species to the surface with a surface species."""

entry(
    index = 43,
    label = "AdsorbateVdW;Adsorbate1",
    kinetics = SurfaceArrheniusBEP(
        A = (1.845e16, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.4,
        E0 = (0.6, 'eV/molecule'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""
Estimated from training reactions 43 and 44:

rxn  Ea    E0rxn
43   0.42  -0.68
44   0     -1.81

Ea = 0.37 * E0rxn + 0.67 eV

E0 ~ 0.6 eV
alpha ~ 0.4
"""
)