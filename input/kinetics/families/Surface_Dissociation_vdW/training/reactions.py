#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation_vdW/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 7,
    label = "NH3_X + X_4 <=> NH2_X + H*",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A = (5.723e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (78.99, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R7
""",
    metal = "Ni",
)

entry(
    index = 12,
    label = "CH4* + X_4 <=> CH3* + H*",
    degeneracy = 4,
    kinetics = SurfaceArrhenius(
        A = (1.54E17,'m^2/(mol*s)'),
        n = 0.087,
        Ea = (55800, 'J/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""R13
    test surface mechanism: based upon Olaf Deutschmann's work:
    "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
    Delgado et al
    Catalysts, 2015, 5, 871-904""",
	metal = "Ni",
)

entry(
    index = 13,
    label = "COOH* + H* <=> HCOOH* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.308e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (16.8342, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 13 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
6.793e13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 2.308e18 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 14,
    label = "H2O* + X_4 <=> OH* + H*",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (4.879e15, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (4.84271508, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 14 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.436e11 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 4.879e15 m^2/(mol*s)
""",
    metal = "Cu",
)

#duplicate of 14
# entry(
#     index = 29,
#     label = "H2O* + X_4 <=> OH* + H*",
#     kinetics = SurfaceArrhenius(
#         A = (3.67E17, 'm^2/(mol*s)'),
#         n = -0.086,
#         Ea = (92.9, 'kJ/mol'),
#         Tmin = (200, 'K'),
#         Tmax = (3000, 'K'),
#     ),
#     rank = 10,
#     shortDesc = u"""Default""",
#     longDesc = u"""R29
#     test surface mechanism: based upon Olaf Deutschmann's work:
#     "Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#     Delgado et al
#     Catalysts, 2015, 5, 871-904""",
# 	metal = "Ni",
# )

entry(
    index = 19,
    label = "HCOO* + H* <=> HCOOH_1* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (4.424e18, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (20.9850987, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 19 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.302e14 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 4.424e18 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 25,
    label = "CH3O* + H* <=> CH3OH_2* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (4.349e22, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (10.8384576, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 25 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
1.28e18 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 4.349e22 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 30,
    label = "HCO* + H* <=> CH2O* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (1.932e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (10.8384576, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 30 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
5.685e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.932e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 33,
    label = "CH2OH* + H* <=> CH3OH_1* + X_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (2.783e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (37.5886933, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 33 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
8.189e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 2.783e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 34,
    label = "HCOOH_2* + X_4 <=> HCO* + OH_2*",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A = (1.781e17, 'm^2/(mol*s)'),
        n = 0.,
        Ea = (37.5886933, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 34 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
5.242e12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.781e17 m^2/(mol*s)
""",
    metal = "Cu",
)
entry(
    index = 35,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.255e+20,'cm^2/(mol*s)'), n=0, Ea=(93000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: NH3_X + X <=> NH2_X + H_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K)= 5.6E11(1/s)/2.483E-9(mol/cm^2) = 2.255E20 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 36,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.859e+20,'cm^2/(mol*s)'), n=0, Ea=(91000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Novell_Pt111
Original entry: NH3_X + X <=> NH2_X + H_X
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 500K) = 7.1E11(1/s)/2.483E-9(mol/cm^2) = 2.859E20 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 37,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.08e+23,'cm^2/(mol*s)'), n=0, Ea=(100350,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: NH3_X + X <=> NH2_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.04eV = 100349.6J/mol
This is reaction (1) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 38,
    label = "H* + OH* <=> H2O* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(63683.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: H_X + OH_X <=> H2O_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.66eV = 63683.4J/mol

This is reaction (5) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 39,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.06e+23,'cm^2/(mol*s)'), n=0, Ea=(97454.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: NH3_X + X <=> NH2_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.01eV = 97454.9/mol
This is reaction (1) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 40,
    label = "H* + OH* <=> H2O* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.44e+21,'cm^2/(mol*s)'), n=0, Ea=(91665.5,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: H_X + OH_X <=> H2O_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.95eV = 91665.5J/mol

This is reaction (5) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 41,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(2.18e+23,'cm^2/(mol*s)'), n=0, Ea=(104209,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: NH3_X + X <=> NH2_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.08eV = 104209.2J/mol
This is reaction (1) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 42,
    label = "H* + OH* <=> H2O* + X_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(64648.3,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: H_X + OH_X <=> H2O_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.67eV = 64648.3J/mol

This is reaction (5) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 43,
    label = "X_4 + NH3_X <=> NH2_X + H*",
    degeneracy = 3.0,
    kinetics = SurfaceArrhenius(A=(8.21e+21,'cm^2/(mol*s)'), n=0, Ea=(109034,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation_vdW""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Popa_Rh111
Original entry: NH3_X + X <=> NH2_X + H_X
Based primarily on "Ab initio density-functional theory study of 
NHx dehydrogenation and reverse reactions on the Rh(111) surface"
C. Popa, W. K. Offermans, R. A. van Santen, and A. P. J. Jansen
American Physical Society Vol. 74, Iss. 15—15, 2006
https://doi.org/10.1103/PhysRevB.74.155428

This is reaction 1 in TABLE VI.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 2.18E13(1/s)/2.656E-9(mol/cm^2) = 8.21E21 cm^2/(mol*s)
Ea = 1.13eV = 109033.7J/mol
""",
    metal = "Rh",
    facet = "111",
)

