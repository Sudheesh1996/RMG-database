#!/usr/bin/env python
# encoding: utf-8

name = "Surface_Dissociation/training"
shortDesc = u"Reaction kinetics used to generate rate rules"
longDesc = u"""
Put kinetic parameters for specific reactions in this file to use as a
training set for generating rate rules to populate this kinetics family.
"""

entry(
    index = 1,
    label = "OCX_3 + HOX_5 <=> HOCXO_1 + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(4.02E14, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(11.5, 'kJ/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
    Experimental and microkinetic modeling of steady-state NO reduction by H2 on Pt/BaO/Al2O3 monolith catalysts
    Xu, Clayton, Balakotaiah, Harold et al.
    doi: 10.1016.j.apcatb.2007.08.008
""",
    metal = "Pt",
)

entry(
    index = 4,
    label = "HOCXO_1 + Ni_4 <=> OCX_3 + HOX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.46E20, 'm^2/(mol*s)'),
        n = -0.213,
        Ea=(54300.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R4
""",
    metal = 'Ni',
)

entry(
    index = 10,
    label = "OCX_3 + HOX_5 <=> HOCXO_1 + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.586e16, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(12.9139069, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 10 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
4.667E11 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.586e16 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 9,
    label = "NH2_X + Ni_4 <=> NHX_1 + HX_5",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A = (2.718e22, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (75.74, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""NH2 Surface Dissociation""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R9
    """,
    metal = "Ni",
)

entry(
    index = 11,
    label = "NHX_2 + Ni_4 <=> NX + HX_5",
    kinetics = SurfaceArrhenius(
        A = (6.213e19, 'cm^2/(mol*s)'),
        n = 0,
        Ea = (22.93, 'kJ/mol'),
        Tmin = (200, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""NH Surface Dissociation""",
    longDesc = u"""
    Micro-kinetic modeling of NH3 decomposition on Ni and its application to solid oxide fuel cells
    Deutschmann et al
    doi: 10.1016/j.ces.2011.07.007

    This is R11
    """,
    metal = "Ni",
)

entry(
    index = 16,
    label = "CH2X_3 + HX_5 <=> CH3X_1 + Ni_4",
    degeneracy = 3,
    kinetics = SurfaceArrhenius(
        A=(3.09E19, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(57200.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R16
""",
    metal = "Ni",
)


entry(
    index = 18,
    label = "CHX_3 + HX_5 <=> CH2X_1 + Ni_4",
    degeneracy = 2,
    kinetics = SurfaceArrhenius(
        A=(9.77E20, 'm^2/(mol*s)'),
        n = -0.087,
        Ea=(81000.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R18
""",
    metal = "Ni",
)

#Delgado has this reaction as exothermic. However, our own thermo has this reaction as endothermic. removing and replacing with reverse direction, R20.
#entry(
#    index = 19,
#    label = "CHX_1 + Ni_4 <=> CX_3 + HX_5",
#    degeneracy = 1,
#    kinetics = SurfaceArrhenius(
#        A=(9.88E16, 'm^2/(mol*s)'),
#        n = 0.5,
#        Ea=(21900.0, 'J/mol'),
#        Tmin = (298, 'K'),
#        Tmax = (2000, 'K'),
#    ),
#    rank = 10,
#    shortDesc = u"""Default""",
#    longDesc = u"""
#"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
#Delgado et al
#Catalysts, 2015, 5, 871-904. Reaction R19
#""",
#    metal = "Ni"
#)

entry(
    index = 20,
    label = "CX_3 + HX_5 <=> CHX_1 + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.70E20, 'm^2/(mol*s)'),
        n = -0.5,
        Ea=(157900., 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R20
""",
    metal = "Ni",
)

entry(
    index = 28,
    label = "HCOO* + Ni_4 <=> HCO* + OX_3",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(8.733e16, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(10.8384576, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 28 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
2.570E12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 8.733e16 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 31,
    label = "HCOH* + HX_5 <=> CH2OH* + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.257e17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(54.4228933, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 32 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
3.698E12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.257e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 32,
    label = "HOX_1 + Ni_4 <=> OX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(2.25E16, 'm^2/(mol*s)'),
        n = 0.188,
        Ea=(29600.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R32
""",
    metal = "Ni",
)

entry(
    index = 15,
    label = "HOX_1 + Ni_4 <=> OX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(7.452e17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(38.7417207, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 15 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
2.193E13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 7.452e17 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 36,
    label = "CH3O2* + Ni_4 <=> CH2OH*_2 + OX_3",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(1.864e18, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(46.3517015, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 36 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
5.485E13 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 1.864e18 m^2/(mol*s)
""",
    metal = "Cu",
)

entry(
    index = 48,
    label = "CXHO_1 + Ni_4 <=> OCX_3 + HX_5",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(3.71E17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(0.0, 'J/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
"Surface Reaction Kinetics of Steam- and CO2-Reforming as well as Oxidation of Methane over Nickel-Based Catalysts"
Delgado et al
Catalysts, 2015, 5, 871-904. Reaction R8
""",
    metal = "Ni",
)

entry(
    index = 26,
    label = "OCX_3 + HX_5 <=> CXHO_1 + Ni_4",
    degeneracy = 1,
    kinetics = SurfaceArrhenius(
        A=(3.140e17, 'm^2/(mol*s)'),
        n = 0.0,
        Ea=(22.8299425, 'kcal/mol'),
        Tmin = (298, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank=10,
    shortDesc = u"""Default""",
    longDesc = u"""
Reaction 26 from table 2 in "Mechanism of Methanol Synthesis on Cu through CO2
and CO Hydrogenation", Grabow and Mavrikakis.  doi:10.1021/cs200055d

A factor from paper / surface site density of Cu
9.240E12 m^4/(mol^2 * s) / 2.943e‐5 mol/m^2 = 3.140e17 m^2/(mol*s)
""",
    metal = "Cu",
)
entry(
    index = 49,
    label = "NOX + OX <=> NO2X + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(1.776e+22,'cm^2/(mol*s)'), n=0, Ea=(115788,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ryan_Pt111
Original entry: NO_X + O_X <=> NO2_X + X
"First-principles study of nitric oxide oxidation on Pt(111) versus Pt overlayer on 3d transition metals"
Ryan Lacdao Arevalo, Mary Clare Sison Escaño, and Hideaki Kasai. J. Vac. Sci. Technol. A 33, 021402 (2015)
https://doi.org/10.1116/1.4903225
A (at 300K) = 4.41E13(1/s)/2.483E-9(mol/cm^2) = 1.776E22 cm^2/(mol*s)
Ea = 1.2eV * 96490J/eV mol = 115788J/mol
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 50,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.014e+21,'cm^2/(mol*s)'), n=0, Ea=(110000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: NH2_X + X <=> NH_X + H_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 5.0E12(1/s)/2.483E-9(mol/cm^2) = 2.014E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 51,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.08997e+21,'cm^2/(mol*s)'), n=0, Ea=(118000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Offermans_Pt111
Original entry: NH_X + X <=> N_X + H_X
"Ammonia oxidation on platinum : a density functional theory study of surface reactivity."
Offermans, W. K. (2007). Technische Universiteit Eindhoven. 
https://doi.org/10.6100/IR630067
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 300K) = 7.2E12(1/s)/2.483E-9(mol/cm^2) = 2.8997E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 52,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(4.43e+21,'cm^2/(mol*s)'), n=0, Ea=(101000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Novell_Pt111
Original entry: NH2_X + X <=> NH_X + H_X
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 500K) = 1.1E13(1/s)/2.483E-9(mol/cm^2) = 4.430E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 53,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(5.236e+21,'cm^2/(mol*s)'), n=0, Ea=(116000,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Novell_Pt111
Original entry: NH_X + X <=> N_X + H_X
"Ammonia Dehydrogenation over Platinum-Group Metal Surfaces. Structure, Stability, and Reactivity of Adsorbed NHx Species"
Gerard Novell-Leruth et al. J. Phys. Chem. C 2007, 111, 2, 860–868
https://doi.org/10.1021/jp064742b
This reaction used RMG's surface site density of Pt111 = 2.483E-9(mol/cm^2) to calculate the A factor.
A (at 500K) = 1.3E13(1/s)/2.483E-9(mol/cm^2) = 5.236E21 cm^2/(mol*s)
""",
    metal = "Pt",
    facet = "111",
)

entry(
    index = 54,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.33e+23,'cm^2/(mol*s)'), n=0, Ea=(83946.3,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: NH2_X + X <=> NH_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 0.87eV = 83946.3J/mol

This is reaction (2) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 55,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.33e+23,'cm^2/(mol*s)'), n=0, Ea=(98419.8,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: NH_X + X <=> N_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.02eV = 98419.8J/mol

This is reaction (3) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 56,
    label = "HX_5 + OX <=> HOX_1 + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(61753.6,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Rh111
Original entry: H_X + O_X <=> OH_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Rh111 = 2.656E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 0.64eV = 61753.6J/mol

This is reaction (4) in Table S5
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 57,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.23e+23,'cm^2/(mol*s)'), n=0, Ea=(152454,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: NH2_X + X <=> NH_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.58eV = 152454.2J/mol

This is reaction (2) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 58,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.23e+23,'cm^2/(mol*s)'), n=0, Ea=(118683,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: NH_X + X <=> N_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.23eV = 118682.7J/mol

This is reaction (3) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 59,
    label = "HX_5 + OX <=> HOX_1 + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.44e+21,'cm^2/(mol*s)'), n=0, Ea=(123507,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd211
Original entry: H_X + O_X <=> OH_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd211 = 2.688E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.28eV = 123507.2J/mol

This is reaction (4) in Table S4
""",
    metal = "Pd",
    facet = "211",
)

entry(
    index = 60,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(2.44e+23,'cm^2/(mol*s)'), n=0, Ea=(85876.1,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: NH2_X + X <=> NH_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 0.89eV = 85876.1J/mol

This is reaction (2) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 61,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.44e+23,'cm^2/(mol*s)'), n=0, Ea=(113858,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: NH_X + X <=> N_X + H_X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
Using the method proposed by Campbell et al. to calculate A actor.
Ea = 1.18eV = 113858.2J/mol

This is reaction (3) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 62,
    label = "HX_5 + OX <=> HOX_1 + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(2.47e+21,'cm^2/(mol*s)'), n=0, Ea=(97454.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Schneider_Pd111
Original entry: H_X + O_X <=> OH_X + X
"DFT and microkinetic comparison of Pt, Pd and Rh-catalyzed ammonia oxidation"
Hanyu Ma, and William F.Schneider
Journal of Catalysis 383 (2020) 322–330
https://doi.org/10.1016/j.jcat.2020.01.029

This reaction used RMG's surface site density of Pd111 = 2.534E-9(mol/cm^2) to calculate the A factor.
The A factor is calculated by equation (5) which assumed qTS/qIS = 1
Ea = 1.01eV = 97454.9J/mol

This is reaction (4) in Table S5
""",
    metal = "Pd",
    facet = "111",
)

entry(
    index = 63,
    label = "Ni_4 + NH2_X <=> NHX_1 + HX_5",
    degeneracy = 2.0,
    kinetics = SurfaceArrhenius(A=(6.33e+21,'cm^2/(mol*s)'), n=0, Ea=(92630.4,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Popa_Rh111
Original entry: NH2_X + X <=> NH_X + H_X
Based primarily on "Ab initio density-functional theory study of 
NHx dehydrogenation and reverse reactions on the Rh(111) surface"
C. Popa, W. K. Offermans, R. A. van Santen, and A. P. J. Jansen
American Physical Society Vol. 74, Iss. 15—15, 2006
https://doi.org/10.1103/PhysRevB.74.155428

This is reaction 3 in TABLE VI.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 1.68E13(1/s)/2.656E-9(mol/cm^2) = 6.33E21 cm^2/(mol*s)
Ea = 0.86eV = 92630.4J/mol
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 64,
    label = "Ni_4 + NHX_2 <=> NX + HX_5",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(7.94e+21,'cm^2/(mol*s)'), n=0, Ea=(97454.9,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Popa_Rh111
Original entry: NH_X + X <=> N_X + H_X
Based primarily on "Ab initio density-functional theory study of 
NHx dehydrogenation and reverse reactions on the Rh(111) surface"
C. Popa, W. K. Offermans, R. A. van Santen, and A. P. J. Jansen
American Physical Society Vol. 74, Iss. 15—15, 2006
https://doi.org/10.1103/PhysRevB.74.155428

This is reaction 7 in TABLE VI.

This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
A (at 300K)= 2.11E13(1/s)/2.656E-9(mol/cm^2) = 7.94E21 cm^2/(mol*s)
Ea = 1.91eV = 97454.9J/mol
""",
    metal = "Rh",
    facet = "111",
)

entry(
    index = 65,
    label = "NOX + OX <=> NO2X + Ni_4",
    degeneracy = 1.0,
    kinetics = SurfaceArrhenius(A=(6.52e+19,'cm^2/(mol*s)'), n=1.015, Ea=(155285,'J/mol'), T0=(1,'K'), Tmin=(200,'K'), Tmax=(3000,'K')),
    rank = 3,
    shortDesc = """Surface_Dissociation""",
    longDesc = 
"""
Training reaction from kinetics library: Surface/Ishikawa_Rh111
Original entry: NO_X + O_X <=> NO2_X + X
"First-Principles Microkinetic Analysis of NO + CO Reactions on
Rh(111) Surface toward Understanding NOx Reduction Pathways"
Atsushi Ishikawa and Yoshitaka Tateyama
J. Phys. Chem. C 2018, 122, 30, 17378–17388
https://doi.org/10.1021/acs.jpcc.8b05906
This reaction used RMG's surface site density of Rh111 = 2.656E-09(mol/cm^2) to calculate the A factor.
The modified Arrhenius parameters is calculed from 
Table 2. Activation Energy (Ea) 
and 
Table S3. Reaction rate constant at different temperatures
""",
    metal = "Rh",
    facet = "111",
)

