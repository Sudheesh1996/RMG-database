#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_Double_vdW/rules"
shortDesc = u""
longDesc = u"""
A vdW double bonded species dissociatively adsorbing to the surface with double
bonds.
"""

entry(
    index = 1,
    label = "AdsorbateVdW;VacantSite",
    kinetics = SurfaceArrheniusBEP(
        A = (1.0e16, 'm^2/(mol*s)'),
        n = 0,
        alpha = 0.4,
        E0 = (1., 'eV/molecule'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
    longDesc = u"""Made up"""
)
