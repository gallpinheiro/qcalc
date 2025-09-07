# After generating this file, it is necessary to fix Emptium manually.

_ATOMINFO_ = { 
"Ni":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2010
#
#  Suggested "light" defaults for Ni atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Ni
#     global species definitions
    nucleus             28
    mass                58.6934
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         52 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.4449   50
      division   0.8232  110
      division   1.1299  194
      division   1.4513  302
#      division   1.6613  434
#      division   1.8317  590
#      division   1.9829  770
#      division   2.0231  974
#      division   2.4367 1202
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      3  p   6.
    valence      3  d   8.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      3  p   6.
    ion_occ      3  d   7.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.65 A, 2.00 A, 2.50 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -123.08 meV to -11.61 meV \n"],[" ", "    hydro 3 p 6\n"],[" ", "    hydro 4 f 9\n"],["#", "     hydro 5 g 12.4\n"],[" ", "    hydro 3 d 5.2\n"],[" ", "    ionic 4 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -6.71 meV to -1.07 meV\n"],["#", "     ionic 4 p auto\n"],["#", "     hydro 4 d 6\n"],["#", "     hydro 6 h 18\n"],["#", "     hydro 4 f 9.4\n"],["#", "     hydro 4 f 16.4\n"],["#", "     hydro 1 s 0.75\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.57 meV to -0.07 meV\n"],["#", "     hydro 4 p 18.4\n"],["#", "     hydro 4 d 8\n"],["#", "     hydro 5 g 13.2\n"],["#", "     hydro 5 f 8.4\n"],["#", "     hydro 6 h 16.8\n"],["#", "     hydro 4 s 4.4\n"],],
5:
[[None, "#  Further functions: improvements -0.07 meV and below\n"],["#", "     hydro 5 f 16.8\n"],["#", "     hydro 4 p 10\n"],]},
"Lu":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Lu atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Lu
#     global species definitions
    nucleus        71
    mass           174.967
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    70  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.0940  110
      division   0.8603  194
      division   0.9866  302
#      division   1.1076  434
#      division   1.1732  590
#      division   1.2190  770
#      division   7.7895  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   1.
    valence      4  f  14.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f  14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.20 A, 2.50 A, 3.04 A, 4.0 A, 5.0 A
#
################################################################################
#
""",
1:
[[None, "#  \"First tier\" - improvements: -246.60 meV to -16.76 meV\n"],[" ", "    hydro 2 p 1.3\n"],[" ", "    ionic 6 d auto\n"],[" ", "    hydro 4 f 6.6\n"],["#", "     hydro 5 g 10.4\n"],[" ", "    hydro 4 s 4.4  \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -17.27 meV to - meV\n"],["#", "     hydro 2 p 1.6\n"],["#", "     ionic 6 p auto\n"],["#", "     hydro 4 d 5.6\n"],["#", "     hydro 6 h 14.4\n"],["#", "     hydro 4 f 5.4\n"],["#", "     ionic 5 d auto\n"],["#", "     hydro 5 g 20.8\n"],["#", "     hydro 3 s 1.9 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.77 meV, min. impr. -0.18 meV\n"],["#", "     hydro 3 d 1.9\n"],["#", "     hydro 5 g 9.4\n"],["#", "     hydro 4 f 9.2\n"],["#", "     hydro 6 h 15.6\n"],["#", "     hydro 5 p 7.4\n"],["#", "     hydro 1 s 5.2\n"],],
4:
[[None, "#  \"Fourth tier\" - max. impr. -0.21 meV, min. impr. -0.07 meV\n"],["#", "     hydro 5 g 35.6\n"],["#", "     ionic 6 s auto\n"],["#", "     hydro 4 d 8.6\n"],["#", "     ionic 4 f auto  \n"],["#", "     hydro 5 p 1.2     \n"],]},
"Mo":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Mo atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Mo
#     global species definitions
    nucleus             42
    mass                95.94
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         59 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.4847   50
      division   0.9168  110
      division   1.2280  194
      division   1.6402  302
#      division   1.8849  434
#      division   2.0237  590
#      division   2.0980  974
#      division   2.7405 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   1.
    valence      4  p   6.
    valence      4  d   5.
#     ion occupancy
    ion_occ     5  s   0.
    ion_occ     4  p   6.
    ion_occ     4  d   4.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.675 A, 1.9 A, 2.375 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\"  - max. impr. -711.23  meV, min. impr. -21.07 meV\n"],[" ", "    hydro 4 f 8.4\n"],[" ", "    hydro 3 d 2.8\n"],[" ", "    ionic 5 p auto\n"],["#", "     hydro 5 g 12\n"],[" ", "    ionic 5 s auto\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -39.38  meV, min. impr. -2.68 meV\n"],["#", "     hydro 4 f 12.4\n"],["#", "     hydro 3 d 3.3\n"],["#", "     hydro 6 h 17.2\n"],["#", "     hydro 4 f 7.6    \n"],["#", "     hydro 3 p 3.0    \n"],["#", "     hydro 1 s 0.65   \n"],],
3:
[[None, "#  \"Third tier\"  - max. impr. -5.50 meV, min. impr. -0.47 meV\n"],["#", "     hydro 4 f 29.2\n"],["#", "     hydro 5 g 11.2\n"],["#", "     hydro 3 d 6.8\n"],["#", "     hydro 6 h 14.8\n"],["#", "     hydro 2 p 2.3\n"],["#", "     hydro 4 s 3.8    \n"],],
4:
[[None, "#  \"Fourth tier\"  - max. impr. -0.58 meV, min. impr. -0.19 meV\n"],["#", "     hydro 5 f 6.8    \n"],["#", "     hydro 5 d 14.8\n"],["#", "     hydro 6 s 7.8\n"],["#", "     hydro 5 g 20.8\n"],["#", "     hydro 5 d 10.4\n"],["#", "     hydro 5 p 9.8\n"],],
5:
[[None, "#  Further functions - -0.17 meV and below\n"],["#", "     hydro 5 d 3.2  \n"],]},
"Ga":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ga atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Ga
#     global species definitions
    nucleus             31
    mass                69.723
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         54 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.5103   50
      division   0.8880  110
      division   1.2009  194
      division   1.5000  302
#      division   1.7093  434
#      division   1.8791  590
#      division   1.9525  770
#      division   2.3801 1202
#      outer_grid  1202
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      4  p   1.
    valence      3  d  10.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      3  p   6.
    ion_occ      3  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.85 A, 2.10 A, 2.45 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -222.33 meV to -26.19 meV \n"],[" ", "    hydro 2 p 1.2\n"],[" ", "    hydro 3 d 3.8\n"],["#", "     hydro 4 f 6.8\n"],[" ", "    ionic 4 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -11.68 meV to -1.61 meV\n"],["#", "     hydro 5 g 10\n"],["#", "     hydro 4 p 3.6\n"],["#", "     hydro 4 f 13.2\n"],["#", "     hydro 6 h 14.4\n"],["#", "     hydro 4 d 5.2\n"],["#", "     hydro 1 s 0.45\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.64 meV to -0.15 meV\n"],["#", "     hydro 3 p 3.4\n"],["#", "     hydro 3 s 2.2\n"],["#", "     hydro 5 g 14\n"],["#", "     hydro 4 f 6.2\n"],["#", "     hydro 5 d 7.2\n"],],
4:
[[None, "#  \"Fourth tier\"  -improvements: -0.12 meV and below\n"],["#", "     hydro 3 s 3.8\n"],["#", "     hydro 5 f 27.2\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 5 g 9.2\n"],["#", "     hydro 4 d 8.6\n"],["#", "     hydro 2 p 3.6  \n"],]},
"Eu":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Eu atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Eu
#     global species definitions
    nucleus        63
    mass           151.964
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    68  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.1049  110
      division   0.1343  194
      division   0.6986  302
#      division   0.8085  434
#      division   0.9136  590
#      division   1.0099  770
#      division   3.0016  974
#      outer_grid   974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   0.
    valence      4  f   7.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f   6.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.775, 2.075, 2.5, 3.25, 4.25 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 5 d  auto
""",
1:
[[None, "#  \"First tier\" - improvements: -1273.12 meV to -20.54 meV\n"],[" ", "    hydro 3 d 5.4\n"],[" ", "    hydro 4 f 8.2\n"],[" ", "    hydro 5 g 11.6\n"],[" ", "    hydro 2 p 1.4\n"],[" ", "    hydro 4 s 4.0  \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -71.76 meV to -0.79 meV\n"],["#", "     hydro 4 f 4.4\n"],["#", "     hydro 6 h 16.4\n"],["#", "     hydro 4 d 3.3\n"],["#", "     hydro 5 g 9.6\n"],["#", "     hydro 4 p 9.4\n"],["#", "     hydro 5 s 5.4 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -4.91 meV, min. impr. -0.39 meV\n"],["#", "     hydro 4 d 14.8\n"],["#", "     hydro 5 g 25.6\n"],["#", "     hydro 4 f 8\n"],["#", "     hydro 6 h 14.8\n"],["#", "     hydro 5 p 5.6\n"],["#", "     ionic 6 s auto\n"],],
5:
[[None, "#  Further functions - impr. -0.98 meV and below\n"],["#", "     hydro 4 f 16.8  \n"],["#", "     hydro 4 d 19.6  \n"],["#", "     hydro 4 f 5     \n"],["#", "     hydro 4 d 4.6   \n"],["#", "     hydro 5 f 19.6\n"],["#", "     hydro 5 g 20\n"],["#", "     hydro 5 g 18.8\n"],["#", "     hydro 6 h 14\n"],["#", "     hydro 5 p 16.4\n"],["#", "     hydro 3 d 1.6\n"],["#", "     hydro 6 p 10.4\n"],]},
"Nb":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Nb atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Nb
#     global species definitions
    nucleus             41
    mass                92.90638
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         59 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.5255   50
      division   0.9829  110
      division   1.2922  194
      division   1.6123  302
#      division   1.9879  434
#      division   2.0980  590
#      division   2.1365  770
#      division   2.1759  974
#      division   2.8558 1202
#      outer_grid   974
      outer_grid   302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   1.
    valence      4  p   6.
    valence      4  d   4.
#     ion occupancy
    ion_occ     5  s   0.
    ion_occ     4  p   6.
    ion_occ     4  d   3.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.75 A, 2.05 A, 2.40 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\"  - max. impr. -632.19  meV, min. impr. -22.82 meV\n"],[" ", "    hydro 4 f 7.8\n"],[" ", "    hydro 3 d 2.6\n"],[" ", "    ionic 5 p auto\n"],["#", "     hydro 5 g 11.2\n"],[" ", "    ionic 5 s auto\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -32.41  meV, min. impr. -1.92 meV\n"],["#", "     hydro 4 f 12.4\n"],["#", "     hydro 3 d 3.2\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 4 f 6.8\n"],["#", "     hydro 3 p 2.7\n"],["#", "     hydro 1 s 0.65\n"],],
3:
[[None, "#  \"Third tier\"  - max. impr. -3.96 meV, min. impr. -0.50 meV\n"],["#", "     hydro 4 f 28\n"],["#", "     hydro 5 g 10.8\n"],["#", "     hydro 3 d 6.4\n"],["#", "     hydro 2 p 1.2\n"],["#", "     hydro 6 h 14.4\n"],["#", "     hydro 4 s 3.3\n"],],
4:
[[None, "#  \"Fourth tier\"  - max. impr. -0.36  meV, min. impr. -0.20 meV\n"],["#", "     hydro 5 f 6.6\n"],["#", "     ionic 4 d auto\n"],["#", "     hydro 5 p 6.8\n"],["#", "     hydro 5 g 19.2\n"],["#", "     hydro 6 s 7\n"],],
5:
[[None, "#  Further functions - -0.18 meV and below\n"],["#", "     hydro 5 d 2.7\n"],["#", "     hydro 5 p 7.6\n"],["#", "     hydro 5 d 16.4\n"],]},
"Y":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Y atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Y
#     global species definitions
    nucleus        39
    mass           88.90585
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    58  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.7193   50
      division   1.2925  110
      division   1.6473  194
      division   1.8976  302
#      division   2.1161  434
#      division   2.4151  590
#      division   2.7220  770
#      division   2.7789  974
#      division   3.4772 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   2.
    valence      4  p   6.
    valence      4  d   1.
#     ion occupancy
    ion_occ      5  s   1.
    ion_occ      4  p   6.
    ion_occ      3  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.125, 2.5, 2.875, 3.25, 4.00, 5.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -257.43 meV to -10.18 meV\n"],[" ", "    hydro 4 f 5.4\n"],[" ", "    hydro 2 p 1.3\n"],[" ", "    ionic 4 d auto\n"],["#", "     hydro 5 g 8.4\n"],[" ", "    ionic 5 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -29.28 meV to -1.28 meV\n"],["#", "     hydro 4 f 9.2\n"],["#", "     hydro 4 d 3\n"],["#", "     hydro 6 h 12.4\n"],["#", "     hydro 5 p 5.6\n"],["#", "     hydro 1 s 0.45\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -3.85 meV to -0.14 meV\n"],["#", "     hydro 2 p 1.8\n"],["#", "     hydro 4 f 22\n"],["#", "     hydro 5 g 11.2\n"],["#", "     hydro 4 f 6.2\n"],["#", "     hydro 5 d 10\n"],["#", "     hydro 6 h 13.6\n"],["#", "     hydro 5 s 1.5   \n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.22 meV to -0.11 meV\n"],["#", "     hydro 5 d 7.4\n"],["#", "     ionic 4 p auto\n"],["#", "     hydro 5 g 9.6\n"],["#", "     hydro 4 p 3.3\n"],["#", "     hydro 5 f 2.1   \n"],["#", "     hydro 3 s 1.8   \n"],]},
"Si":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Si atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Si
#     global species definitions
    nucleus             14
    mass                28.0855
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         42 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.5866   50
      division   0.9616  110
      division   1.2249  194
      division   1.3795  302
#      division   1.4810  434
#      division   1.5529  590
#      division   1.6284  770
#      division   1.7077  974
#      division   2.4068 1202
#      outer_grid   974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      3  s   2.
    valence      3  p   2.
#     ion occupancy
    ion_occ      3  s   1.
    ion_occ      3  p   1.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.75 A, 2.0 A, 2.25 A, 2.75 A, 3.75 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -571.96 meV to -37.03 meV\n"],[" ", "    hydro 3 d 4.2\n"],[" ", "    hydro 2 p 1.4\n"],["#", "     hydro 4 f 6.2\n"],[" ", "    ionic 3 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -16.76 meV to -3.03 meV\n"],["#", "     hydro 3 d 9\n"],["#", "     hydro 5 g 9.4\n"],["#", "     hydro 4 p 4\n"],["#", "     hydro 1 s 0.65\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -3.89 meV to -0.60 meV\n"],["#", "     ionic 3 d auto\n"],["#", "     hydro 3 s 2.6\n"],["#", "     hydro 4 f 8.4\n"],["#", "     hydro 3 d 3.4\n"],["#", "     hydro 3 p 7.8\n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.33 meV to -0.11 meV\n"],["#", "     hydro 2 p 1.6\n"],["#", "     hydro 5 g 10.8\n"],["#", "     hydro 5 f 11.2\n"],["#", "     hydro 3 d 1\n"],["#", "     hydro 4 s 4.5\n"],],
5:
[[None, "#  Further basis functions that fell out of the optimization - noise\n"],[None, "#  level... < -0.08 meV\n"],["#", "     hydro 4 d 6.6\n"],["#", "     hydro 5 g 16.4\n"],["#", "     hydro 4 d 9\n"],]},
"Te":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Te atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Te
#     global species definitions
    nucleus             52
    mass                127.60
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         64 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.1259  110
      division   0.8959  194
      division   0.9864  302
#      division   1.1196  434
#      division   1.1922  590
#      division   1.3098  770
#      division   2.9404  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   2.
    valence      5  p   4.
    valence      4  d  10.
#     ion occupancy
    ion_occ     5  s   1.
    ion_occ     5  p   3.
    ion_occ     4  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.15 A, 2.55 A, 3.10 A, 3.60 A, 4.50 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -217.34  meV, min. impr. -22.97 meV\n"],[" ", "    hydro 3 d 3.7\n"],["#", "     hydro 4 f 6\n"],[" ", "    hydro 3 p 2.7\n"],[" ", "    ionic 5 s auto\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -17.80 meV, min. impr. -0.57 meV\n"],["#", "     hydro 5 g 9\n"],["#", "     hydro 4 f 16.4\n"],["#", "     hydro 6 h 12\n"],["#", "     hydro 4 p 6.4\n"],["#", "     hydro 5 f 32.4\n"],["#", "     hydro 4 d 5\n"],["#", "     hydro 3 s 2.8  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.51 meV, min. impr. -0.06 meV\n"],["#", "     hydro 5 f 8.4\n"],["#", "     hydro 5 g 11.6\n"],["#", "     hydro 6 h 15.6\n"],["#", "     hydro 2 p 1.7\n"],["#", "     hydro 4 d 9.6\n"],["#", "     hydro 1 s 6.4  \n"],],
5:
[[None, "#  Further functions that fell out of the optimization: -0.17 meV and below\n"],["#", "     hydro 4 f 33.6\n"],["#", "     hydro 5 d 6.8\n"],["#", "     hydro 5 f 16\n"],]},
"Am":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Am atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Am
#     global species definitions
    nucleus             95
    mass                243
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         77 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.0757  110
      division   0.1049  194
      division   0.1394  302
#      division   0.8765  434
#      division   0.9579  590
#      division   1.1022  770
#      division   7.7698  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   0.
    valence      5  f   7.
#     ion occupancy 
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f    6.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.81, 2.03, 2.5, 3.25, 4.25 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 6 d  auto
""",
1:
[[None, "#  \"First tier\" - max. impr. -1436.48 meV, min. impr. -47.85 meV\n"],[" ", "    hydro 3 d 5.2\n"],[" ", "    hydro 5 g 12.4\n"],[" ", "    hydro 2 p 1.8\n"],[" ", "    hydro 4 f 8.8\n"],[" ", "    hydro 3 s 2.8  \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -126.98 meV, min. impr. -5.11 meV\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 4 f 4.2\n"],["#", "     ionic 6 d auto\n"],["#", "     hydro 5 g 26\n"],["#", "     hydro 2 p 1.5 \n"],["#", "     hydro 5 s 6.4 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -12.67 meV, min. impr. -0.75 meV\n"],["#", "     hydro 5 g 7.6  \n"],["#", "     hydro 6 h 13.2\n"],["#", "     hydro 4 f 7.8\n"],["#", "     hydro 3 d 3.4\n"],["#", "     hydro 5 g 47.6  \n"],["#", "     hydro 5 f 24.4\n"],["#", "     hydro 4 p 6\n"],["#", "     hydro 2 s 1.1   \n"],]},
"Md":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Md atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Md
#     global species definitions
    nucleus             101
    mass                258
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         79 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.0916  110
      division   0.1314  194
      division   0.1740  302
#      division   1.0230  434
#      division   1.0952  590
#      division   1.1723  770
#      division   7.7647  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   0.
    valence      5  f  13.
#     ion occupancy
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f   12.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.08, 2.50, 3.00, 3.43, 4.25 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 6 d  auto
""",
1:
[[None, "#  \"First tier\" - max. impr. -295.40 meV, min. impr. -15.54 meV\n"],[" ", "    hydro 3 d 5.2\n"],[" ", "    hydro 5 g 12\n"],[" ", "    hydro 4 f 7.6\n"],[" ", "    hydro 2 p 1.2\n"],[" ", "    hydro 4 s 4.2\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -15.17 meV, min. impr. -0.91 meV\n"],["#", "     hydro 6 h 15.6\n"],["#", "     hydro 4 f 4.3\n"],["#", "     hydro 4 d 3.1\n"],["#", "     hydro 5 g 29.2\n"],["#", "     hydro 4 p 10.0  \n"],["#", "     hydro 4 s 5.8   \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -1.67 meV, min. impr. -0.32 meV\n"],["#", "     hydro 5 g 7.6   \n"],["#", "     hydro 6 h 12.4\n"],["#", "     hydro 4 p 3.2\n"],["#", "     hydro 5 f 7.8\n"],["#", "     hydro 1 s 9.8\n"],["#", "     hydro 7 d 18.8\n"],],
5:
[[None, "#  Further functions - could be completed to a fourth tier: -0.21 meV and below\n"],["#", "     hydro 5 g 39.6\n"],["#", "     hydro 6 f 21.6\n"],]},
"Pd":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Pd atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Pd
#     global species definitions
    nucleus             46
    mass                106.42
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         62 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.5211   50
      division   0.9161  110
      division   1.2296  194
      division   1.5678  302
#      division   1.9785  434
#      division   2.0474  590
#      division   2.1195  770
#      division   2.1568  974
#      division   2.7392 1202
#       outer_grid  974
       outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   1.
    valence      4  p   6.
    valence      4  d   9.
#     ion occupancy
    ion_occ     5  s   0.
    ion_occ     4  p   6.
    ion_occ     4  d   8.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.0 A, 2.275 A, 2.75 A, 3.75 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -120.76  meV, min. impr. -5.71 meV\n"],[" ", "    ionic 5 p auto\n"],[" ", "    hydro 4 f 8\n"],["#", "     hydro 5 g 10\n"],[" ", "    hydro 3 s 2.6\n"],[" ", "    hydro 3 d 2.5\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -5.00  meV, min. impr. -0.62 meV\n"],["#", "     hydro 5 f 17.2\n"],["#", "     hydro 6 h 14\n"],["#", "     hydro 4 d 4\n"],["#", "     hydro 5 f 7.6\n"],["#", "     hydro 3 p 3.3\n"],["#", "     hydro 4 s 9.4\n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.54  meV, min. impr. -0.14 meV\n"],["#", "     hydro 4 f 20\n"],["#", "     hydro 5 g 12.8\n"],["#", "     hydro 5 d 9.8\n"],["#", "     hydro 6 h 15.2\n"],["#", "     hydro 5 s 10\n"],["#", "     hydro 6 p 9.8\n"],],
4:
[[None, "#  \"Fourth tier\" - max. impr. -0.15  meV, min. impr. -0.05 meV\n"],["#", "     hydro 5 f 9.2\n"],["#", "     hydro 2 s 5.6\n"],["#", "     hydro 5 f 43.2\n"],["#", "     hydro 5 d 13.2\n"],["#", "     hydro 5 g 14\n"],["#", "     hydro 4 p 4.7\n"],]},
"Na":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Na atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Na
#     global species definitions
    nucleus             11
    mass                22.98976928
#
    l_hartree           4
#
    cut_pot             4.0          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         40 5.5
    radial_multiplier   1
    angular_grids       specified
      division   0.5925  110
      division   0.7843  194
      division   1.0201  302
#      division   1.1879  434
#      division   1.3799  590
#      division   1.4503  770
#      division   7.0005  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      3  s   1.
    valence      2  p   6.
#     ion occupancy
    ion_occ      2  s   2.
    ion_occ      2  p   6.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.0 A, 2.5 A, 3.0 A, 3.75 A, 4.5 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -60.09 meV to -10.02 meV\n"],[" ", "    hydro 2 p 1.2\n"],[" ", "    hydro 3 s 1.8\n"],[" ", "    hydro 3 d 3.8\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -2.94 meV to -1.27 meV\n"],["#", "     hydro 4 p 3.1\n"],["#", "     hydro 3 s 10\n"],["#", "     hydro 4 f 6.2\n"],["#", "     hydro 4 d 1.3\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.83 meV to -0.07 meV\n"],["#", "     hydro 3 d 7.8\n"],["#", "     hydro 3 p 2.3\n"],["#", "     hydro 5 g 9.6\n"],["#", "     hydro 4 p 0.85\n"],["#", "     hydro 5 f 1.8\n"],["#", "     hydro 2 s 0.6\n"],],
5:
[[None, "#  Further basis functions that fell out of the optimization - noise level...\n"],["#", "     hydro 5 g 0.1\n"],["#", "     hydro 4 d 3.4\n"],["#", "     hydro 4 s 0.1\n"],]},
"K":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for K atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        K
#     global species definitions
    nucleus             19
    mass                39.0983
#
    l_hartree           4
#
    cut_pot             4.0          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         46 5.5
    radial_multiplier   1
    angular_grids       specified
      division   0.5285  110
      division   0.7831  194
      division   0.9986  302
#      division   1.0594  434
#      division   1.1569  590
#      division   1.2994  770
#      division   1.4587  974
#      outer_grid 974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   1.
    valence      3  p   6.
#     ion occupancy
    ion_occ      3  s   2.
    ion_occ      3  p   6.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.5 A, 3.0 A, 3.875 A, 5.0 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -43.02 meV to -8.16 meV\n"],[" ", "    ionic 3 d auto\n"],[" ", "    ionic 4 p auto\n"],[" ", "    hydro 4 s 3.1\n"],["#", "     hydro 4 f 5.6\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -2.10 meV to -0.40 meV\n"],["#", "     hydro 4 d 4.4\n"],["#", "     hydro 3 s 1.5\n"],["#", "     hydro 5 g 8.2\n"],["#", "     hydro 3 p 2.4\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.37 meV to -0.09 meV\n"],["#", "     hydro 1 s 1\n"],["#", "     hydro 2 p 2.4\n"],["#", "     hydro 6 h 11.6\n"],["#", "     hydro 3 d 4.5\n"],["#", "     hydro 5 f 9\n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.09 meV to -0.05 meV\n"],["#", "     hydro 5 s 4\n"],["#", "     hydro 4 d 6.6\n"],["#", "     hydro 5 p 5.8\n"],]},
"Ta":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ta atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Ta
#     global species definitions
    nucleus        73
    mass           180.94788
#
    l_hartree      4
#
    cut_pot        3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    71  5.0
    radial_multiplier  1
    angular_grids specified
      division   0.3792   50
      division   1.0232  110
      division   1.3396  194
      division   1.5892  302
#      division   1.8380  434
#      division   2.1374  590
#      division   2.2049  770
#      division   2.2755  974
#      division   2.8291 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   3.
    valence      4  f  14.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   2.
    ion_occ      4  f  14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.85, 2.12, 2.625, 3.25, 4.50 AA
#
################################################################################
#
""",
1:
[[None, "#  \"First tier\" - improvements: -461.64 meV to -31.84 meV\n"],[" ", "    hydro 4 f 7\n"],[" ", "    hydro 4 d 5.6\n"],[" ", "    ionic 6 p auto\n"],["#", "     hydro 5 g 11.6\n"],[" ", "    ionic 6 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -26.62 meV to -1.73 meV\n"],["#", "     ionic 5 d auto\n"],["#", "     hydro 6 h 15.2\n"],["#", "     hydro 4 f 9.2\n"],["#", "     hydro 5 g 17.6\n"],["#", "     hydro 4 p 4.7\n"],["#", "     hydro 1 s 0.5  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -6.67 meV, min. impr. -0.18 meV\n"],["#", "     hydro 5 d 8  \n"],["#", "     hydro 6 h 20\n"],["#", "     hydro 5 g 38\n"],["#", "     hydro 5 f 8.4\n"],["#", "     hydro 2 p 1.3\n"],["#", "     hydro 5 s 9.4  \n"],],
4:
[[None, "#  \"Fourth tier\" - max. impr. -0.76 meV, min. impr. -0.13 meV\n"],["#", "     hydro 5 g 10.8\n"],["#", "     hydro 6 p 14.8\n"],["#", "     hydro 6 h 20.4\n"],["#", "     hydro 5 f 21.2\n"],["#", "     hydro 4 p 11.6\n"],["#", "     hydro 4 f 3.9\n"],["#", "     hydro 6 d 13.6\n"],["#", "     hydro 4 s 4.6\n"],]},
"Ho":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ho atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Ho
#     global species definitions
    nucleus        67
    mass           164.93032
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    69  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.0971  110
      division   0.1105  194
      division   0.1402  302
#      division   0.8774  434
#      division   0.9690  590
#      division   1.0482  770
#      division   3.1772  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   0.
    valence      4  f  11.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.93, 2.375, 3.0, 4.1, 5.0 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 5 d  auto
""",
1:
[[None, "#  \"First tier\" - improvements: -548.69 meV to -9.98 meV\n"],[" ", "    ionic 5 d auto\n"],[" ", "    hydro 4 f 7.8\n"],[" ", "    hydro 2 p 1.2\n"],[" ", "    hydro 5 g 11.6\n"],[" ", "    hydro 4 s 4.2  \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -21.25 meV to -1.06 meV\n"],["#", "     hydro 4 f 3.7\n"],["#", "     hydro 6 h 15.6\n"],["#", "     hydro 3 d 3\n"],["#", "     hydro 5 g 6.2\n"],["#", "     hydro 5 g 27.2\n"],["#", "     hydro 4 p 5.8\n"],["#", "     hydro 1 s 0.45\n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -1.09 meV, min. impr. -0.21 meV\n"],["#", "     hydro 6 h 10.4\n"],["#", "     hydro 5 f 9.8\n"],["#", "     hydro 3 p 1.9\n"],["#", "     hydro 5 d 18\n"],["#", "     hydro 4 f 20\n"],["#", "     hydro 5 g 13.2\n"],["#", "     hydro 3 s 2.3 \n"],]},
"Cf":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Cf atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Cf
#     global species definitions
    nucleus             98
    mass                251
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         78 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.0703  110
      division   0.1058  194
      division   0.1445  302
#      division   0.2305  434
#      division   0.9565  590
#      division   1.0799  770
#      division   7.7672  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   0.
    valence      5  f  10.
#     ion occupancy
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f    9.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.89, 2.19, 2.625, 3.125, 4.0
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 6 d  auto
""",
1:
[[None, "#  \"First tier\" - max. impr. -821.80 meV, min. impr. -23.25 meV\n"],[" ", "    hydro 3 d 5.2\n"],[" ", "    hydro 5 g 12.4\n"],[" ", "    hydro 2 p 1.6\n"],[" ", "    hydro 4 f 8.4\n"],[" ", "    hydro 4 s 4.3  \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -56.38 meV, min. impr. -2.13 meV\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 4 f 4.3\n"],["#", "     hydro 3 d 3.4\n"],["#", "     hydro 5 g 28\n"],["#", "     hydro 4 p 9.0 \n"],["#", "     hydro 4 s 5.6 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -4.92 meV, min. impr. -0.51 meV\n"],["#", "     hydro 5 g 8\n"],["#", "     hydro 6 h 13.6\n"],["#", "     hydro 4 f 8.2\n"],["#", "     hydro 6 d 20\n"],["#", "     hydro 5 g 52\n"],["#", "     hydro 3 s 2.2 \n"],["#", "     hydro 5 p 18.8\n"],[None, "#  A fourth tier could be added if required.\n"],]},
"Gd":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Gd atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Gd
#     global species definitions
    nucleus        64
    mass           157.25
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    68  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.0917  110
      division   0.1291  194
      division   0.7135  302
#      division   0.8085  434
#      division   0.9322  590
#      division   1.0099  770
#      division   2.9262  974
#      outer_grid   974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   1.
    valence      4  f   7.
#     ion occupancy - 3+ ion, analogous to Ce
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f   6.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.80, 2.11, 2.625, 3.375, 4.1, 5.0 AA
#
################################################################################
#
""",
1:
[[None, "#  \"First tier\" - improvements: -422.89 meV to -6.39 meV\n"],[" ", "    hydro 3 d 5.8\n"],[" ", "    hydro 4 f 9\n"],[" ", "    hydro 5 g 13.2\n"],[" ", "    hydro 2 p 1.9\n"],[" ", "    hydro 3 s 3.0 \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -32.23 meV to -0.42 meV\n"],["#", "     hydro 6 h 17.2\n"],["#", "     hydro 4 f 5.4\n"],["#", "     hydro 3 d 4.3\n"],["#", "     hydro 5 g 27.6\n"],["#", "     hydro 4 p 9.8  \n"],["#", "     ionic 6 s auto \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -2.11 meV, min. impr. -0.16 meV\n"],["#", "     hydro 5 g 9.8\n"],["#", "     hydro 4 d 14.4\n"],["#", "     hydro 6 h 15.6\n"],["#", "     hydro 4 f 13.2\n"],["#", "     hydro 6 p 20.4  \n"],["#", "     hydro 4 s 9.0   \n"],],
5:
[[None, "#  Further functions - impr. -0.49 meV and below\n"],["#", "     hydro 5 f 17.6  \n"],["#", "     hydro 5 d 18.4  \n"],]},
"Ca":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ca atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Ca
#     global species definitions
    nucleus             20
    mass                40.078
#
    l_hartree           4
#
    cut_pot             4.0          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         47 5.5
    radial_multiplier   1
    angular_grids       specified
     division   0.5361  110
     division   0.7866  194
     division   0.9689  302
#     division   1.0269  434
#     division   1.2909  590
#     division   1.3280  770
#     division   1.4872  974
#     outer_grid  974
     outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
#  Note: Ca+ ionic basis functions perform better than Ca2+ ionic
#  basis functions for the neutral Ca dimer. This is why they are used here.
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      3  p   6.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      3  p   6.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.5 A, 3.0 A, 3.5 A, 4.0 A, 5.0 A
#
#  Ca appears to require two d functions in tier 1, because the atomic configuration
#  does not provide a 3d valence function.
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -486.29 meV to -11.73 meV\n"],[" ", "    ionic 3 d auto\n"],[" ", "    ionic 4 p auto\n"],[" ", "    hydro 3 d 2.3\n"],["#", "     hydro 4 f 4.8\n"],[" ", "    ionic 4 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -6.34 meV to -0.27 meV\n"],["#", "     hydro 5 g 6.8\n"],["#", "     hydro 3 p 3.8\n"],["#", "     hydro 6 h 10.4\n"],["#", "     hydro 1 s 0.55\n"],["#", "     hydro 5 f 9.2\n"],["#", "     hydro 5 p 3.3\n"],["#", "     hydro 4 d 5    \n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.18 meV to -0.06 meV\n"],["#", "     hydro 5 p 5.4  \n"],["#", "     hydro 5 f 5\n"],["#", "     hydro 5 s 4.6\n"],["#", "     hydro 2 p 4.2\n"],["#", "     hydro 5 g 9.8\n"],["#", "     hydro 4 d 5.2\n"],[None, "#  Two extra functions (no real \"tier\") - improvements: -0.07 meV, -0.05 meV\n"],["#", "     hydro 4 f 8.8\n"],["#", "     hydro 2 p 1.2\n"],]},
"Ti":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ti atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Ti
#     global species definitions
    nucleus             22
    mass                47.867
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         48 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.5171   50
      division   0.9824  110
      division   1.2917  194
      division   1.4940  302
#      division   1.6934  434
#      division   1.8425  590
#      division   2.1901  770
#      division   2.2896  974
#      division   2.8244 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      3  p   6.
    valence      3  d   2.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      3  p   6.
    ion_occ      3  d   1.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.6 A, 1.85 A, 2.5 A, 3.25 A, 4.25 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -396.25 meV to -19.41 meV\n"],[" ", "    hydro 4 f 8\n"],[" ", "    hydro 3 d 2.7\n"],[" ", "    ionic 4 p auto\n"],["#", "     hydro 5 g 11.6\n"],[" ", "    ionic 4 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -16.30 meV to -2.03 meV\n"],["#", "     hydro 3 d 4.4\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 4 f 9.4\n"],["#", "     hydro 4 p 4.5\n"],["#", "     hydro 1 s 0.5\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -6.28 meV to -0.37 meV\n"],["#", "     hydro 4 d 6.4\n"],["#", "     hydro 4 f 10\n"],["#", "     hydro 5 g 12\n"],["#", "     hydro 2 p 1.7\n"],["#", "     hydro 6 h 16.4\n"],["#", "     hydro 4 s 3.8\n"],],
5:
[[None, "#  Further basis functions: -0.45 meV and smaller improvements\n"],["#", "     hydro 3 d 8.8\n"],["#", "     hydro 5 p 18\n"],["#", "     hydro 4 f 22.4\n"],["#", "     hydro 5 f 7.2  # -0.16 meV\n"],["#", "     hydro 3 d 2.1  # -0.11 meV\n"],["#", "     hydro 5 g 7.4  # -0.09 meV\n"],]},
"Cd":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Cd atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Cd
#     global species definitions
    nucleus             48
    mass                112.411
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         62 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.5937   50
      division   1.0282  110
      division   1.3769  194
      division   1.7301  302
#      division   2.2341  434
#      division   2.2741  590
#      division   2.3152  770
#      division   2.3574  974
#      division   2.9077 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   2.
    valence      4  p   6.
    valence      4  d  10.
#     ion occupancy
    ion_occ     5  s   1.
    ion_occ     4  p   6.
    ion_occ     4  d   9.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.15 A, 2.50 A, 3.10 A, 4.00 A, 5.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -224.92  meV, min. impr. -5.81 meV\n"],[" ", "    hydro 2 p 1.6\n"],[" ", "    hydro 4 f 7\n"],[" ", "    hydro 3 s 2.8\n"],[" ", "    hydro 3 p 5.2\n"],["#", "     hydro 5 g 10.0\n"],[" ", "    hydro 3 d 3.8\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -2.57  meV, min. impr. -0.38 meV\n"],["#", "     hydro 4 f 17.6\n"],["#", "     hydro 6 h 13.6\n"],["#", "     hydro 3 p 7\n"],["#", "     hydro 5 s 17.6\n"],["#", "     hydro 3 d 3.4\n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.37 meV, min. impr. -0.09 meV\n"],["#", "     hydro 3 p 2.4\n"],["#", "     hydro 4 f 6.4\n"],["#", "     hydro 4 s 4\n"],["#", "     hydro 5 f 15.6\n"],["#", "     hydro 5 g 10.8\n"],["#", "     hydro 2 p 6.4\n"],["#", "     hydro 6 h 12.8\n"],["#", "     hydro 5 d 9.0\n"],],
5:
[[None, "#  Further functions: -0.05 meV and below\n"],["#", "     hydro 5 d 5.8  \n"],]},
"Pm":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Pm atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Pm
#     global species definitions
    nucleus        61
    mass           145
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    67  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.0906  110
      division   0.6102  194
      division   0.6960  302
#      division   0.8074  434
#      division   0.9141  590
#      division   1.0120  770
#      division   3.0660  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   0.
    valence      4  f   5.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f   4.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.775, 2.05, 2.5, 3.25, 4.25 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 5 d  auto
""",
1:
[[None, "#  \"First tier\" - improvements: -1502.85 meV to -26.63 meV\n"],[" ", "    hydro 3 d 5.2\n"],[" ", "    hydro 5 g 11.6\n"],[" ", "    hydro 4 f 7.8\n"],[" ", "    hydro 2 p 1.4\n"],[" ", "    ionic 6 s auto \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -108.54 meV to -2.30 meV\n"],["#", "     hydro 4 f 4.4\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 4 d 3.4\n"],["#", "     hydro 5 g 8.4\n"],["#", "     hydro 2 p 1.8\n"],["#", "     hydro 5 s 5.4 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -8.02 meV, min. impr. -0.29 meV\n"],["#", "     hydro 4 d 14\n"],["#", "     hydro 6 h 12.4\n"],["#", "     hydro 5 g 27.2\n"],["#", "     hydro 5 f 9.4\n"],["#", "     hydro 5 p 9\n"],["#", "     hydro 6 s 15.6 \n"],],
5:
[[None, "#  Further functions - impr. -1.30 meV and below\n"],["#", "     hydro 4 d 20    \n"],["#", "     hydro 4 f 13.6  \n"],["#", "     hydro 6 d 5.8   \n"],["#", "     hydro 5 g 14.4  \n"],["#", "     hydro 6 h 17.2  \n"],["#", "     hydro 5 g 20\n"],["#", "     hydro 4 f 16.8\n"],["#", "     hydro 5 f 4.1\n"],]},
"Kr":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Kr atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Kr
#     global species definitions
    nucleus             36
    mass                83.798
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         56 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.3980   50
      division   0.7174  110
      division   1.0235  194
      division   1.1824  302
#      division   1.3889  434
#      division   1.8888  590
#      division   1.9972  770
#      division   2.1543  974
#      division   2.4715 1202
#      outer_grid  1202
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      4  p   6.
    valence      3  d  10.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      4  p   5.
    ion_occ      3  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.40 A, 3.00 A, 3.675 A, 4.25 A, 5.00 A
#
#  Noble gas symmetric dimers converge quickly in DFT. If you find that
#  you require a larger basis than tier 2+, please contact us - VB, FHI.
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -60.14 meV to -1.30 meV \n"],[" ", "    hydro 3 d 4.5\n"],[" ", "    hydro 3 p 3.1\n"],["#", "     hydro 4 f 7.4\n"],[" ", "    hydro 3 s 4.2\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -0.97 meV to -0.10 meV\n"],["#", "     hydro 5 g 9.8\n"],["#", "     hydro 3 d 4\n"],["#", "     hydro 5 p 7.6\n"],["#", "     hydro 6 h 13.6\n"],["#", "     hydro 5 f 8.4\n"],["#", "     ionic 5 s auto\n"],],
5:
[[None, "#  Further functions - improvements: -0.11 meV and below\n"],["#", "     hydro 4 d 7.2\n"],["#", "     hydro 4 f 19.6\n"],]},
"Fe":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Fe atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Fe
#     global species definitions
    nucleus             26
    mass                55.845
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         51 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.4337   50
      division   0.8154  110
      division   1.1046  194
      division   1.3713  302
#      division   1.5424  434
#      division   1.7365  590
#      division   1.9587  770
#      division   1.9990  974
#      division   2.4139 1202
#      outer_grid  1202
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      3  p   6.
    valence      3  d   6.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      3  p   6.
    ion_occ      3  d   5.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.45 A, 1.725 A, 2.25 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -300.53 meV to -10.50 meV \n"],[" ", "    hydro 4 f 9.4\n"],[" ", "    hydro 2 p 2.2\n"],["#", "     hydro 5 g 12.4\n"],[" ", "    hydro 3 d 3.1\n"],[" ", "    ionic 4 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -16.31 meV to -0.65 meV\n"],["#", "     hydro 3 d 6.2\n"],["#", "     hydro 6 h 19.2\n"],["#", "     hydro 4 f 15.2\n"],["#", "     hydro 4 f 6.6\n"],["#", "     hydro 3 p 3\n"],["#", "     hydro 5 g 13.2\n"],["#", "     hydro 1 s 0.65  \n"],],
3:
[[None, "#  \"Third tier\" - improvements: -1.60 meV to -0.10 meV\n"],["#", "     hydro 4 d 7.8\n"],["#", "     hydro 4 p 19.6\n"],["#", "     hydro 4 d 10.4\n"],["#", "     ionic 4 p auto\n"],["#", "     hydro 6 h 17.6\n"],["#", "     hydro 5 f 27.2\n"],["#", "     hydro 4 s 4.8\n"],],
4:
[[None, "#  \"Fourth tier\": improvements -0.13 meV and below\n"],["#", "     hydro 5 f 12\n"],["#", "     hydro 5 g 10.4\n"],["#", "     hydro 5 p 8.4\n"],["#", "     hydro 4 d 14.8\n"],["#", "     hydro 2 s 1.9\n"],]},
"Cs":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Cs atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Cs
#     global species definitions
    nucleus        55
    mass           132.9054519
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    65  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.7542  110
      division   1.0056  194
      division   1.2887  302
#      division   1.4138  434
#      division   1.5042  590
#      division   1.6519  770
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   1.
    valence      5  p   6.
    valence      4  d  10.
#     ion occupancy
    ion_occ      6  s   0.
    ion_occ      5  p   6.
    ion_occ      4  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.70, 3.50, 4.50, 5.50 Ang
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -138.41 meV to -7.10 meV\n"],[" ", "    hydro 3 d 3.9\n"],[" ", "    hydro 4 f 6.4\n"],[" ", "    hydro 3 p 2.3\n"],[" ", "    hydro 4 s 2.7\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -6.08 meV to -0.77 meV\n"],["#", "     hydro 4 d 3.9\n"],["#", "     hydro 4 f 20.8\n"],["#", "     hydro 5 g 8.6\n"],["#", "     hydro 5 f 41.6\n"],["#", "     hydro 6 h 11.6\n"],["#", "     hydro 4 p 7.0  \n"],["#", "     hydro 4 s 3.8\n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.54 meV, min. impr. -0.09 meV\n"],["#", "     hydro 5 d 10\n"],["#", "     hydro 5 f 17.6\n"],["#", "     hydro 4 p 3.5\n"],["#", "     hydro 5 f 7.4\n"],["#", "     hydro 1 s 2.3\n"],["#", "     hydro 5 g 11.6\n"],[None, "#  One more function - impr. -0.05 meV\n"],["#", "     hydro 6 d 17.2\n"],]},
"Rn":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Rn atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Rn
#     global species definitions
    nucleus             86
    mass                222
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         75 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.5994  110
      division   0.8610  194
      division   1.0898  302
#      division   1.2801  434
#      division   1.4253  590
#      division   7.7751  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      6  p   6.
    valence      5  d  10.
    valence      4  f  14.
#     ion occupancy
    ion_occ     6  s    1.
    ion_occ     6  p    5.
    ion_occ     5  d   10.
    ion_occ     4  f   14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.80, 3.50, 4.17, 4.75, 5.50 AA
#
#  Noble gas symmetric dimers converge quickly in DFT. If you find that
#  you require a larger basis than tier 2, please contact us - VB, FHI.
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -58.17 meV, min. impr. -1.62 meV\n"],[" ", "    hydro 3 d 3.6\n"],[" ", "    ionic 5 f auto\n"],[" ", "    hydro 2 p 1.5\n"],["#", "     hydro 5 g 8\n"],[" ", "    hydro 3 s 3.6\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -0.82 meV, min. impr. -0.12 meV\n"],["#", "     hydro 5 f 5.6\n"],["#", "     hydro 3 d 3\n"],["#", "     hydro 6 h 10.4\n"],["#", "     hydro 5 f 9.2\n"],["#", "     hydro 4 s 4.2\n"],["#", "     hydro 5 g 8.6\n"],],
5:
[[None, "#  Further functions: max. impr. -0.10 meV, min. impr. -0.05 meV\n"],["#", "     hydro 5 d 13.6\n"],["#", "     hydro 1 s 12\n"],["#", "     hydro 6 h 11.2\n"],]},
"O":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for O atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        O
#     global species definitions
    nucleus             8
    mass                15.9994
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         36 5.0
    radial_multiplier   1
     angular_grids specified
      division   0.2659   50
      division   0.4451  110
      division   0.6052  194
      division   0.7543  302
#      division   0.8014  434
#      division   0.8507  590
#      division   0.8762  770
#      division   0.9023  974
#      division   1.2339 1202
#      outer_grid 974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      2  s   2.
    valence      2  p   4.
#     ion occupancy
    ion_occ      2  s   1.
    ion_occ      2  p   3.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.0 A, 1.208 A, 1.5 A, 2.0 A, 3.0 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -699.05 meV to -159.38 meV\n"],[" ", "    hydro 2 p 1.8\n"],[" ", "    hydro 3 d 7.6\n"],[" ", "    hydro 3 s 6.4\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -49.91 meV to -5.39 meV\n"],["#", "     hydro 4 f 11.6\n"],["#", "     hydro 3 p 6.2\n"],["#", "     hydro 3 d 5.6\n"],["#", "     hydro 5 g 17.6\n"],["#", "     hydro 1 s 0.75\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -2.83 meV to -0.50 meV\n"],["#", "     ionic 2 p auto\n"],["#", "     hydro 4 f 10.8\n"],["#", "     hydro 4 d 4.7\n"],["#", "     hydro 2 s 6.8\n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.40 meV to -0.12 meV\n"],["#", "     hydro 3 p 5\n"],["#", "     hydro 3 s 3.3\n"],["#", "     hydro 5 g 15.6\n"],["#", "     hydro 4 f 17.6\n"],["#", "     hydro 4 d 14\n"],],
5:
[[None, "# Further basis functions - -0.08 meV and below\n"],["#", "     hydro 3 s 2.1\n"],["#", "     hydro 4 d 11.6\n"],["#", "     hydro 3 p 16\n"],["#", "     hydro 2 s 17.2\n"],]},
"Al":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Al atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Al
#     global species definitions
    nucleus             13
    mass                26.9815386
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         41 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.6594  110
      division   0.8170  194
      division   0.9059  302
#      division   1.0363  434
#      division   1.1443  590
#      division   1.2621  770
#      division   2.8177  974
#      outer_grid   974
      outer_grid   302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      3  s   2.
    valence      3  p   1.
#     ion occupancy
    ion_occ      3  s   1.
    ion_occ      2  p   6.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.0 A, 2.5 A, 3.0 A, 3.75 A, 4.5 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -199.47 meV to -10.63 meV\n"],[" ", "    ionic 3 d auto\n"],[" ", "    ionic 3 p auto\n"],["#", "     hydro 4 f 4.7\n"],[" ", "    ionic 3 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -5.35 meV to -1.57 meV\n"],["#", "     hydro 5 g 7\n"],["#", "     hydro 3 d 6\n"],["#", "     hydro 2 s 11.6\n"],["#", "     hydro 2 p 0.9\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.63 meV to -0.20 meV\n"],["#", "     hydro 5 f 7.6\n"],["#", "     hydro 4 p 7.2\n"],["#", "     hydro 4 s 3.7\n"],["#", "     hydro 4 d 7.6\n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.17 meV to -0.08 meV\n"],["#", "     hydro 4 d 13.6\n"],["#", "     hydro 5 g 11.2\n"],["#", "     hydro 4 d 0.9\n"],["#", "     hydro 1 s 0.4\n"],["#", "     hydro 4 p 0.1\n"],["#", "     hydro 5 f 9.8\n"],],
5:
[[None, "#  Further basis functions that fell out of the optimization - noise level...\n"],["#", "     hydro 4 p 5\n"],]},
"Cl":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Cl atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Cl
#     global species definitions
    nucleus             17
    mass                35.453
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         45 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.4412  110
      division   0.5489  194
      division   0.6734  302
#      division   0.7794  434
#      division   0.9402  590
#      division   1.0779  770
#      division   1.1792  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      3  s   2.
    valence      3  p   5.
#     ion occupancy
    ion_occ      3  s   1.
    ion_occ      3  p   4.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.65 A, 2.0 A, 2.5 A, 3.25 A, 4.0 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -429.57 meV to -15.03 meV\n"],[" ", "    ionic 3 d auto\n"],[" ", "    hydro 2 p 1.9\n"],["#", "     hydro 4 f 7.4\n"],[" ", "    ionic 3 s auto\n"],["#", "     hydro 5 g 10.4\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -7.84 meV to -0.48 meV\n"],["#", "     hydro 3 d 3.3\n"],["#", "     hydro 5 f 9.8\n"],["#", "     hydro 1 s 0.75\n"],["#", "     hydro 5 g 11.2\n"],["#", "     hydro 4 p 10.4\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -1.00 meV to -0.12 meV\n"],["#", "     hydro 4 d 12.8\n"],["#", "     hydro 4 f 4.6\n"],["#", "     hydro 4 d 10.8\n"],["#", "     hydro 2 s 1.8\n"],["#", "     hydro 3 p 3\n"],],
5:
[[None, "#  Further functions that fell out - improvements: -0.10 meV and below\n"],["#", "     hydro 5 f 14.4\n"],["#", "     hydro 4 s 12.8\n"],["#", "     hydro 3 d 11.6\n"],["#", "     hydro 4 s 4.1\n"],]},
"H":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for H atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        H
#     global species definitions
    nucleus             1
    mass                1.00794
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#     
    radial_base         24 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.2421   50
      division   0.3822  110
      division   0.4799  194
      division   0.5341  302
#      division   0.5626  434
#      division   0.5922  590
#      division   0.6542  770
#      division   0.6868 1202
#      outer_grid  770
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      1  s   1.
#     ion occupancy
    ion_occ      1  s   0.5
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Basis constructed for dimers: 0.5 A, 0.7 A, 1.0 A, 1.5 A, 2.5 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -1014.90 meV to -62.69 meV\n"],[" ", "    hydro 2 s 2.1\n"],[" ", "    hydro 2 p 3.5\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -12.89 meV to -1.83 meV\n"],["#", "     hydro 1 s 0.85\n"],["#", "     hydro 2 p 3.7\n"],["#", "     hydro 2 s 1.2\n"],["#", "     hydro 3 d 7\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.25 meV to -0.12 meV\n"],["#", "     hydro 4 f 11.2\n"],["#", "     hydro 3 p 4.8\n"],["#", "     hydro 4 d 9\n"],["#", "     hydro 3 s 3.2\n"],]},
"Ra":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ra atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
#  The onset of the cutoff pot'l is set to 6 A by default, because the neutral
#  Ra atom is a large atom. However, this is very expensive. The radius should be
#  much smaller in real-world situations, where Ra will be ionic. Please check 
#  and reduce the cutoff radius explicitly.
#
################################################################################
  species        Ra
#     global species definitions
    nucleus             88
    mass                226
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         75 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.6236  110
      division   0.9264  194
      division   1.1500  302
#      division   1.3507  434
#      division   1.5599  590
#      division   1.6475  770
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      5  d  10.
    valence      4  f  14.
#     ion occupancy
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     5  d   10.
    ion_occ     4  f   14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 3.15, 3.50, 4.25, 5.12, 6.00 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -251.02 meV, min. impr. -8.25 meV\n"],[" ", "    ionic 6 d auto\n"],[" ", "    ionic 5 f auto\n"],[" ", "    hydro 3 p 2.4\n"],["#", "     hydro 5 g 6.8\n"],[" ", "    hydro 4 s 3.3\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -5.03  meV, min. impr. -0.14 meV\n"],["#", "     hydro 4 f 5.2\n"],["#", "     hydro 4 d 4\n"],["#", "     hydro 3 d 1.6\n"],["#", "     hydro 6 h 9.2\n"],["#", "     hydro 2 p 2.6\n"],["#", "     hydro 1 s 12.4  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.36 meV, min. impr. -0.05 meV\n"],["#", "     hydro 5 f 4.3\n"],["#", "     hydro 7 d 1.9\n"],["#", "     hydro 6 f 6.2\n"],["#", "     hydro 5 g 12.4\n"],["#", "     hydro 4 p 2.5\n"],["#", "     hydro 5 p 8\n"],["#", "     hydro 6 s 7.8\n"],],
5:
[[None, "#  Further functions: -0.04 meV and below\n"],["#", "     hydro 6 d 9\n"],]},
"Pb":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Pb atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Pb
#     global species definitions
    nucleus             82
    mass                207.2
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         74 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.1064  110
      division   0.1579  194
      division   0.2150  302
#      division   1.0164  434
#      division   1.1544  590
#      division   1.1970  770
#      division   7.7779  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      6  p   2.
    valence      5  d  10.
    valence      4  f  14.
#     ion occupancy
    ion_occ     6  s    1.
    ion_occ     6  p    1.
    ion_occ     5  d   10.
    ion_occ     4  f   14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.225, 2.50, 2.88, 3.625, 4.50
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -156.54 meV, min. impr. -14.49 meV\n"],[" ", "    hydro 3 p 2.3\n"],[" ", "    hydro 4 f 7.6\n"],[" ", "    hydro 3 d 3.5\n"],["#", "     hydro 5 g 9.8\n"],[" ", "    hydro 3 s 3.2\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -4.38  meV, min. impr. -0.30 meV\n"],["#", "     hydro 6 h 12.8\n"],["#", "     hydro 3 d 2.4\n"],["#", "     hydro 5 f 7.2\n"],["#", "     hydro 5 f 14.8\n"],["#", "     hydro 4 p 5.4\n"],["#", "     ionic 6 s auto \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.86 meV, min. impr. -0.16 meV\n"],["#", "     hydro 5 p 14.4\n"],["#", "     hydro 5 g 8.2\n"],["#", "     hydro 4 d 4.6\n"],["#", "     hydro 6 h 12.4\n"],["#", "     hydro 6 d 12.4\n"],["#", "     hydro 4 s 4\n"],["#", "     hydro 5 g 32.8\n"],["#", "     hydro 5 f 9.4\n"],],
5:
[[None, "#  Further functions: -0.10 meV and below\n"],["#", "     hydro 5 f 17.6\n"],["#", "     hydro 7 p 19.6\n"],]},
"Ar":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ar atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Ar
#     global species definitions
    nucleus             18
    mass                39.948
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         46 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.5855  110
      division   0.8590  194
      division   0.9692  302
#      division   1.1235  590
#      division   1.1911  770
#      division   1.2623  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      3  s   2.
    valence      3  p   6.
#     ion occupancy
    ion_occ      3  s   1.
    ion_occ      3  p   5.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.25 A, 2.625 A, 3.0 A, 3.375 A, 4.0 A
#
#  Noble gas symmetric dimers converge quickly in DFT. If you find that
#  you require a larger basis than tier 3, please contact us - VB, FHI.
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -57.34 meV to -1.14 meV\n"],[" ", "    ionic 3 d auto\n"],[" ", "    ionic 4 p auto\n"],["#", "     hydro 4 f 7.4\n"],[" ", "    hydro 3 s 4.5\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -0.67 meV to -0.10 meV\n"],["#", "     hydro 4 d 7.8\n"],["#", "     hydro 5 g 10.4\n"],["#", "     ionic 3 p auto\n"],["#", "     hydro 1 s 15.2\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.13 meV to -0.02 meV\n"],["#", "     hydro 4 d 5.8\n"],["#", "     hydro 5 f 9.2\n"],["#", "     hydro 4 s 11.2\n"],["#", "     hydro 5 p 10.8\n"],]},
"Dy":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Dy atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Dy
#     global species definitions
    nucleus        66
    mass           162.500
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    69  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.0887  110
      division   0.1200  194
      division   0.7773  302
#      division   0.8774  434
#      division   0.9501  590
#      division   1.0482  770
#      division   3.1772  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   0.
    valence      4  f  10.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f   9.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.85, 2.24, 2.625, 3.375, 4.1, 5.0 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 5 d  auto
""",
1:
[[None, "#  \"First tier\" - improvements: -656.93 meV to -12.11 meV\n"],[" ", "    hydro 3 d 2.2\n"],[" ", "    hydro 4 f 8\n"],[" ", "    hydro 2 p 1.3\n"],[" ", "    hydro 5 g 12\n"],[" ", "    hydro 4 s 4.0   \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -29.85 meV to -0.32 meV\n"],["#", "     hydro 4 f 3.9\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 3 d 2.9\n"],["#", "     hydro 5 g 7\n"],["#", "     hydro 4 p 5.4 \n"],["#", "     hydro 1 s 1.0 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -3.55 meV, min. impr. -0.17 meV\n"],["#", "     hydro 5 g 28\n"],["#", "     hydro 6 d 5\n"],["#", "     hydro 5 f 10\n"],["#", "     hydro 6 h 12.8\n"],["#", "     hydro 5 d 17.2\n"],["#", "     hydro 2 p 1.7\n"],["#", "     hydro 6 s 10.4 \n"],],
5:
[[None, "#  Further functions - impr. -0.47 meV and below\n"],["#", "     hydro 4 f 16.8\n"],["#", "     hydro 5 g 14\n"],["#", "     hydro 6 d 18.4\n"],]},
"Bk":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Bk atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Bk
#     global species definitions
    nucleus             97
    mass                247
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         78 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.0801  110
      division   0.1179  194
      division   0.1540  302
#      division   0.2184  434
#      division   0.9565  590
#      division   1.0799  770
#      division   7.7672  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   0.
    valence      5  f   9.
#     ion occupancy
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f    8.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.86, 2.12, 2.5, 3.0, 4.0 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 6 d  auto
""",
1:
[[None, "#  \"First tier\" - max. impr. -1051.01 meV, min. impr. -27.17 meV\n"],[" ", "    hydro 3 d 5.2\n"],[" ", "    hydro 5 g 12.4\n"],[" ", "    hydro 2 p 1.7\n"],[" ", "    hydro 4 f 8.6\n"],[" ", "    ionic 7 s auto  \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -76.25 meV, min. impr. -3.36 meV\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 3 d 3.6\n"],["#", "     hydro 4 f 5.2\n"],["#", "     hydro 5 g 26.4\n"],["#", "     hydro 4 p 8.8  \n"],["#", "     hydro 4 s 5.6  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -6.71 meV, min. impr. -0.30 meV\n"],["#", "     hydro 5 g 9.6\n"],["#", "     hydro 6 h 16.4\n"],["#", "     hydro 4 f 8.8\n"],["#", "     hydro 6 d 19.2\n"],["#", "     hydro 5 g 48.4  \n"],["#", "     hydro 4 p 6\n"],["#", "     hydro 4 s 6.8  \n"],[None, "#  A fourth tier could be added if required.\n"],]},
"Cm":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Cm atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Cm
#     global species definitions
    nucleus             96
    mass                247
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         77 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.0861  110
      division   0.1215  194
      division   0.1394  302
#      division   0.1793  434
#      division   0.9579  590
#      division   1.0832  770
#      division   7.7698  974
#      outer_grid 974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   1.
    valence      5  f   7.
#     ion occupancy - 3+ ion, analogous to Ce
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f    6.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.83, 2.07, 2.5, 3.25, 4.25 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -869.16 meV, min. impr. -19.23 meV\n"],[" ", "    hydro 3 d 2.7\n"],[" ", "    hydro 5 g 13.2\n"],[" ", "    hydro 4 f 8.8\n"],[" ", "    hydro 2 p 2.1\n"],[" ", "    hydro 1 s 0.7  \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -103.22 meV, min. impr. -2.05 meV\n"],["#", "     hydro 6 h 16.8   \n"],["#", "     ionic 6 d auto\n"],["#", "     hydro 5 f 8.6\n"],["#", "     hydro 5 g 31.6\n"],["#", "     hydro 5 p 17.6\n"],["#", "     hydro 5 s 7.0 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -9.16 meV, min. impr. -0.27 meV\n"],["#", "     hydro 4 d 2.5\n"],["#", "     hydro 5 g 10.8\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 5 f 12\n"],["#", "     hydro 6 p 18.8\n"],["#", "     hydro 1 s 14  \n"],[None, "#  A fourth tier could be added if required.\n"],]},
"Cr":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Cr atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Cr
#     global species definitions
    nucleus             24
    mass                51.9961
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         50 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.4331   50
      division   0.8246  110
      division   1.1008  194
      division   1.3188  302
#      division   1.4867  434
#      division   1.7819  590
#      division   1.9339  770
#      division   1.9742  974
#      division   2.4437 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      3  p   6.
    valence      3  d   4.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      3  p   6.
    ion_occ      3  d   3.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.375 A, 1.55 A, 2.00 A, 2.75 A, 3.75 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -633.53 meV to -21.19 meV \n"],[" ", "    hydro 4 f 9.6\n"],[" ", "    hydro 3 d 3.1\n"],[" ", "    ionic 4 p auto\n"],["#", "     hydro 5 g 13.6\n"],[" ", "    ionic 4 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -23.49 meV to -1.88 meV\n"],["#", "     hydro 4 f 6.8\n"],["#", "     hydro 4 d 14.4\n"],["#", "     hydro 6 h 19.2\n"],["#", "     ionic 3 d auto\n"],["#", "     hydro 4 f 14.8\n"],["#", "     hydro 5 g 10.4\n"],["#", "     hydro 1 s 0.6\n"],["#", "     hydro 3 p 3.5\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -1.02 meV to -0.20 meV\n"],["#", "     hydro 6 h 15.6\n"],["#", "     hydro 3 d 7.4\n"],["#", "     hydro 4 p 18.4\n"],["#", "     hydro 5 g 16.4\n"],["#", "     hydro 4 s 3.9  \n"],["#", "     hydro 4 f 28.8 \n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.42 meV to -0.09 meV\n"],["#", "     hydro 4 d 10.4\n"],["#", "     hydro 5 p 7\n"],["#", "     hydro 4 s 20\n"],["#", "     hydro 5 f 7.2\n"],["#", "     hydro 5 g 20.4\n"],["#", "     hydro 6 h 16.8\n"],],
5:
[[None, "#  Further functions: improvements -0.07 meV and below\n"],["#", "     hydro 5 f 30\n"],["#", "     hydro 5 p 17.2\n"],["#", "     hydro 3 s 2.2\n"],["#", "     hydro 5 s 7.6\n"],]},
"Ce":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ce atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Ce
#     global species definitions
    nucleus        58
    mass           140.116
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    66  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.1028  110
      division   0.1495  194
      division   0.8411  302
#      division   0.9338  434
#      division   0.9935  590
#      division   1.0783  770
#      division   3.5126  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   1.
    valence      4  f   1.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f   0.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.0, 2.375, 2.875, 3.5, 4.5 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -540.10 meV to -12.77 meV\n"],[" ", "    hydro 4 d 4.8\n"],[" ", "    hydro 5 g 11.2\n"],[" ", "    hydro 4 f 7.6\n"],[" ", "    hydro 2 p 1.8\n"],[" ", "    hydro 3 s 2.7  \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -48.86 meV to -0.65 meV\n"],["#", "     hydro 6 h 14.8\n"],["#", "     hydro 4 f 5.2\n"],["#", "     hydro 3 d 3\n"],["#", "     hydro 3 d 2.2\n"],["#", "     hydro 5 g 11.6\n"],["#", "     hydro 3 p 2.8  \n"],["#", "     ionic 6 s auto \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -2.32 meV, min. impr. -0.31 meV\n"],["#", "     hydro 6 h 15.2\n"],["#", "     hydro 4 f 8.2\n"],["#", "     hydro 5 g 30\n"],["#", "     hydro 6 d 16.4\n"],["#", "     hydro 5 f 15.6\n"],["#", "     hydro 5 p 17.6\n"],["#", "     hydro 4 s 7.2  \n"],],
4:
[[None, "#  Fourth tier  - max. impr. -0.36 meV, min. impr. -0.17 meV\n"],["#", "     hydro 5 g 20\n"],["#", "     hydro 4 f 16.4\n"],["#", "     hydro 6 d 20\n"],["#", "     hydro 6 p 9.2\n"],["#", "     hydro 1 s 0.85\n"],["#", "     hydro 6 h 14\n"],]},
"Pr":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Pr atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Pr
#     global species definitions
    nucleus        59
    mass           140.90765
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    66  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.0809  110
      division   0.1276  194
      division   0.7726  302
#      division   0.8590  434
#      division   0.9338  590
#      division   1.0351  770
#      division   3.3134  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   0.
    valence      4  f   3.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f   2.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.90, 2.25, 2.75, 3.5, 4.5 AA
#
################################################################################
#
#  Necessary addition to the minimal basis:
   confined 5 d auto  # fixed addition to minimal basis ...
""",
1:
[[None, "#  \"First tier\" - improvements: -540.10 meV to -22.65 meV\n"],[" ", "    hydro 3 d 4.9\n"],[" ", "    hydro 2 p 1.3\n"],[" ", "    hydro 4 f 8\n"],[" ", "    hydro 5 g 11.2\n"],[" ", "    ionic 6 s auto \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -87.39 meV to -??? meV\n"],["#", "     hydro 4 f 4\n"],["#", "     hydro 6 h 15.2\n"],["#", "     hydro 4 d 3.4\n"],["#", "     hydro 5 g 7.2\n"],["#", "     hydro 2 p 1.6\n"],["#", "     hydro 4 s 3.0  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -9.09 meV, min. impr. -0.40 meV\n"],["#", "     hydro 5 d 12\n"],["#", "     hydro 4 f 6.2\n"],["#", "     hydro 5 g 14.4\n"],["#", "     hydro 6 h 14.4\n"],["#", "     hydro 5 p 8.8\n"],["#", "     hydro 5 s 6.0  \n"],],
5:
[[None, "#  Further functions - impr. -1.09 meV and below\n"],["#", "     hydro 5 f 15.6  \n"],["#", "     hydro 4 d 19.2  \n"],["#", "     hydro 5 g 36    \n"],["#", "     hydro 3 d 1.5   \n"],["#", "     ionic 4 f auto  \n"],["#", "     hydro 5 g 16.4  \n"],["#", "     hydro 5 f 16.4  \n"],["#", "     hydro 6 p 18    \n"],]},
"Ba":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ba atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#  The onset of the cutoff pot'l is set to 8 A by default, because the neutral
#  Ba atom is a large atom. However, this is very expensive. The radius should be
#  much smaller in real-world situations, where Ba will be ionic. Please check 
#  and reduce the cutoff radius explicitly.
#
################################################################################
  species          Ba
#     global species definitions
    nucleus        56
    mass           137.327
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    65  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.6752  110
      division   0.9746  194
      division   1.2241  302
#      division   1.3850  434
#      division   1.4734  590
#      division   1.6010  770
#      division   4.8366  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      4  d  10.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      4  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.65, 3.00, 3.50, 4.40, 5.50 Ang
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -1277.43 meV to -9.16 meV\n"],[" ", "    ionic 5 d auto\n"],[" ", "    ionic 4 f auto\n"],[" ", "    hydro 3 p 2.7\n"],[" ", "    hydro 4 s 3.3\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -64.04 (!) meV to -0.25 meV\n"],["#", "     hydro 4 f 5.8  \n"],["#", "     hydro 5 g 7.4  \n"],["#", "     hydro 4 d 4.5  \n"],["#", "     hydro 6 h 11.2 \n"],["#", "     hydro 5 p 6.6  \n"],["#", "     hydro 2 s 3.2  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -1.16 meV, min. impr. -0.08 meV\n"],["#", "     hydro 5 f 7.4\n"],["#", "     hydro 5 g 10.8\n"],["#", "     hydro 4 d 2.3\n"],["#", "     hydro 4 p 3.7  \n"],["#", "     hydro 5 s 4.0  \n"],],
5:
[[None, "#  Further functions - impr. -0.35 meV and below\n"],["#", "     hydro 5 d 3.5  \n"],["#", "     hydro 6 d 0.4  \n"],["#", "     hydro 2 p 2.5  \n"],["#", "     hydro 5 f 12   \n"],["#", "     hydro 6 d 8.8  \n"],]},
"Tm":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Tm atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Tm
#     global species definitions
    nucleus        69
    mass           168.93421
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    70  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.1069  110
      division   0.1797  194
      division   1.0059  302
#      division   1.0865  434
#      division   1.1732  590
#      division   1.2665  770
#      division   7.7895  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   0.
    valence      4  f  13.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f  12.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.20, 2.625, 3.25, 4.1, 5.0 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 5 d  auto
""",
1:
[[None, "#  \"First tier\" - improvements: -218.88 meV to -13.75 meV\n"],[" ", "    ionic 5 d auto\n"],[" ", "    hydro 3 p 3.2\n"],[" ", "    hydro 4 f 7\n"],[" ", "    hydro 5 g 10.4\n"],[" ", "    hydro 4 s 4\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -9.82 meV to -0.47 meV\n"],["#", "     hydro 4 d 3.1\n"],["#", "     hydro 6 h 14\n"],["#", "     hydro 5 f 7.8\n"],["#", "     hydro 2 p 1.3\n"],["#", "     hydro 5 g 24.4\n"],["#", "     hydro 2 s 4.5  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.94 meV, min. impr. -0.11 meV\n"],["#", "     hydro 3 p 2.3\n"],["#", "     hydro 5 g 9.4\n"],["#", "     hydro 3 p 7.4\n"],["#", "     hydro 6 h 14.4\n"],["#", "     hydro 3 d 5.2\n"],["#", "     hydro 5 f 4.8\n"],["#", "     hydro 1 s 0.45 \n"],]},
"Sm":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Sm atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Sm
#     global species definitions
    nucleus        62
    mass           150.36
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    67  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.0906  110
      division   0.1284  194
      division   0.6960  302
#      division   0.8074  434
#      division   0.9141  590
#      division   1.0120  770
#      division   3.0660  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   0.
    valence      4  f   6.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f   5.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.775, 2.05, 2.5, 3.25, 4.25 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 5 d  auto
""",
1:
[[None, "#  \"First tier\" - improvements: -1400.30 meV to -23.60 meV\n"],[" ", "    hydro 3 d 5.2\n"],[" ", "    hydro 5 g 11.6\n"],[" ", "    hydro 4 f 7.8\n"],[" ", "    hydro 2 p 1.4\n"],[" ", "    ionic 6 s auto \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -86.29 meV to -2.11 meV\n"],["#", "     hydro 4 f 4.4\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 4 d 3.4\n"],["#", "     hydro 5 g 8.8\n"],["#", "     hydro 4 d 14.8\n"],["#", "     hydro 2 p 2.2\n"],["#", "     hydro 5 s 5.6 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -6.41 meV, min. impr. -??? meV\n"],["#", "     hydro 5 g 25.2\n"],["#", "     hydro 5 f 10.4\n"],["#", "     hydro 6 h 14\n"],["#", "     hydro 5 p 5.6\n"],["#", "     hydro 4 f 15.6\n"],["#", "     hydro 6 d 18.4\n"],["#", "     hydro 5 s 7.6 \n"],],
5:
[[None, "#  Further functions - impr. -0.67 meV and below\n"],["#", "     hydro 4 f 6.2  \n"],["#", "     hydro 3 d 1.8  \n"],["#", "     hydro 5 p 12   \n"],]},
"Se":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Se atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Se
#     global species definitions
    nucleus             34
    mass                78.96
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         55 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.0830  110
      division   0.1357  194
      division   0.7377  302
#      division   0.8610  434
#      division   0.9640  590
#      division   1.0773  770
#      division   2.5539  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      4  p   4.
    valence      3  d  10.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      4  p   3.
    ion_occ      3  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.85 A, 2.15 A, 2.50 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -336.21 meV to -36.85 meV \n"],[" ", "    hydro 3 d 4.3\n"],[" ", "    hydro 2 p 1.6\n"],["#", "     hydro 4 f 7.2\n"],[" ", "    ionic 4 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -14.39 meV to -1.49 meV\n"],["#", "     hydro 5 g 10.4  \n"],["#", "     hydro 4 p 4.5\n"],["#", "     hydro 4 d 6.2\n"],["#", "     hydro 4 f 11.2\n"],["#", "     hydro 1 s 0.65\n"],["#", "     hydro 6 h 15.2\n"],],
3:
[[None, "#  Third tier - improvements: -0.46 meV and below\n"],["#", "     hydro 5 g 14.4\n"],["#", "     ionic 4 d auto\n"],["#", "     hydro 4 f 22.4\n"],["#", "     hydro 5 f 7.4\n"],["#", "     hydro 5 p 8\n"],["#", "     hydro 5 s 9.4    \n"],],
4:
[[None, "#  Fourth tier - improvements: -0.12 meV and below\n"],["#", "     hydro 5 d 11.6\n"],["#", "     hydro 6 h 18\n"],["#", "     hydro 4 p 4\n"],["#", "     hydro 5 f 16\n"],["#", "     hydro 4 s 3.9    \n"],]},
"Be":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Be atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Be
#     global species definitions
    nucleus             4
    mass                9.012182
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#     
    radial_base         31 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.4283  110
      division   0.4792  194
      division   0.5061  302
#      division   0.7227  434
#      division   0.8724  590
#      division   0.9555  770
#      division   2.9770  974
#      outer_grid   974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      2  s   2.
#     ion occupancy
    ion_occ      2  s   1.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.75 A, 2.0 A, 2.375 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -677.26 meV to -34.75 meV\n"],[" ", "    ionic 2 p auto\n"],[" ", "    hydro 3 s 2.9\n"],[" ", "    hydro 3 d 3.5\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -16.34 meV to -1.26 meV\n"],["#", "     hydro 3 p 3.1\n"],["#", "     hydro 4 d 4.7\n"],["#", "     hydro 3 p 2.4\n"],["#", "     hydro 4 f 7.6\n"],["#", "     hydro 2 s 2.9\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.27 meV to -0.05 meV\n"],["#", "     hydro 2 p 8.2\n"],["#", "     hydro 5 g 10.8\n"],["#", "     hydro 4 f 7\n"],["#", "     hydro 3 s 2.3\n"],["#", "     hydro 4 d 3.8\n"],]},
"Li":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Li atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Li
#     global species definitions
    nucleus             3
    mass                6.941
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#     
    radial_base         29 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.4484  110
      division   0.5659  194
      division   0.6315  302
#      division   0.6662  434
#      division   0.8186  590
#      division   0.9037  770
#      division   6.2760  974
#      outer_grid   974
      outer_grid   302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      2  s   1.
#     ion occupancy
    ion_occ      1  s   2.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.80 A, 2.25 A, 2.75 A, 3.50 A, 4.50 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -189.23 meV to -6.35 meV\n"],[" ", "    hydro 2 p 1.6\n"],[" ", "    hydro 2 s 2\n"],[" ", "    hydro 3 d 2.6\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -4.69 meV to -0.41 meV\n"],["#", "     hydro 3 p 4.6\n"],["#", "     hydro 2 p 1.8\n"],["#", "     hydro 3 s 6.2\n"],["#", "     hydro 4 d 4.7\n"],["#", "     hydro 4 f 4.1\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.20 meV to -0.15 meV\n"],["#", "     hydro 4 d 0.95\n"],["#", "     hydro 3 p 6.2\n"],["#", "     hydro 3 s 1.7\n"],],
5:
[[None, "#  Further functions, listed for completeness\n"],[None, "#     VB: The following functions are only listed for completeness; test very\n"],[None, "#         carefully before any kind of production use. From the point of view \n"],[None, "#         of the basis construction, their main role is to fill up space, \n"],[None, "#         and they are solely determined by the location of the cutoff potential.\n"],["#", "     hydro 3 p 0.1  # -0.15 meV\n"],["#", "     hydro 4 d 5    # -0.12 meV\n"],["#", "     hydro 4 f 0.1  # -0.14 meV\n"],["#", "     hydro 5 g 0.1  # -0.06 meV\n"],]},
"U":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for U atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        U
#     global species definitions
    nucleus             92
    mass                238.02891
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         76 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.0850  110
      division   0.1081  194
      division   0.1389  302
#      division   0.1794  434
#      division   0.9255  590
#      division   1.0302  770
#      division   7.7724  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   1.
    valence      5  f   3.
#     ion occupancy - 3+ ion, analogous to Ce
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f    2.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.89, 2.09, 2.75, 3.50, 4.50 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -1205.73 meV, min. impr. -46.18 meV\n"],[" ", "    hydro 3 d 5\n"],[" ", "    hydro 5 g 11.6\n"],[" ", "    hydro 2 p 1.9\n"],["#", "     hydro 6 h 14.8\n"],[" ", "    hydro 4 f 8.2\n"],[" ", "    hydro 3 s 2.8  \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -58.85 meV, min. impr. -2.72 meV\n"],["#", "     hydro 4 f 4.3\n"],["#", "     hydro 3 d 4.1\n"],["#", "     hydro 5 g 18.8\n"],["#", "     hydro 2 p 1.8  \n"],["#", "     hydro 4 s 3.9 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -10.23 meV, min. impr. -0.94 meV\n"],["#", "     hydro 4 f 7\n"],["#", "     hydro 6 d 18\n"],["#", "     hydro 6 h 17.2\n"],["#", "     hydro 5 g 9.6\n"],["#", "     hydro 5 g 41.2\n"],["#", "     hydro 6 p 17.6\n"],["#", "     hydro 6 s 20  \n"],[None, "#  A fourth tier could be added if required.\n"],]},
"V":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for V atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        V
#     global species definitions
    nucleus             23
    mass                50.9415
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         49 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.4553   50
      division   0.8707  110
      division   1.1666  194
      division   1.3737  302
#      division   1.5524  434
#      division   1.8303  590
#      division   2.0330  770
#      division   2.0767  974
#      division   2.5907 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      3  p   6.
    valence      3  d   3.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      3  p   6.
    ion_occ      3  d   2.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.45 A, 1.65 A, 2.25 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -573.19 meV to -17.48 meV \n"],[" ", "    hydro 4 f 9\n"],[" ", "    hydro 3 d 3\n"],[" ", "    ionic 4 p auto\n"],["#", "     hydro 5 g 12.8\n"],[" ", "    ionic 4 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -21.58 meV to -1.18 meV\n"],["#", "     hydro 3 d 5.4\n"],["#", "     hydro 5 f 11.2\n"],["#", "     hydro 6 h 18.4\n"],["#", "     hydro 4 d 7\n"],["#", "     hydro 4 f 11.2\n"],["#", "     hydro 4 p 5.6\n"],["#", "     hydro 5 g 14\n"],["#", "     hydro 1 s 0.6\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.56 meV to -0.32 meV\n"],["#", "     hydro 3 d 8.8\n"],["#", "     hydro 4 p 7.8\n"],["#", "     hydro 6 h 18.8\n"],["#", "     hydro 4 f 24.8  \n"],["#", "     hydro 4 s 4.0   \n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.30 meV to -0.09 meV\n"],["#", "     hydro 5 p 12\n"],["#", "     hydro 5 g 15.2\n"],["#", "     hydro 5 f 8\n"],["#", "     hydro 5 p 6.4\n"],["#", "     hydro 4 d 5.2\n"],["#", "     hydro 5 s 7.8\n"],],
5:
[[None, "#  Further functions - impr. -0.09 meV and below\n"],["#", "     hydro 3 s 12\n"],["#", "     hydro 6 h 20\n"],["#", "     hydro 5 g 7\n"],]},
"At":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for At atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        At
#     global species definitions
    nucleus             85
    mass                210
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         74 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.1106  110
      division   0.1579  194
      division   1.0736  302
#      division   1.1970  434
#      division   1.2869  590
#      division   1.4091  770
#      division   7.7779  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      6  p   5.
    valence      5  d  10.
    valence      4  f  14.
#     ion occupancy
    ion_occ     6  s    1.
    ion_occ     6  p    4.
    ion_occ     5  d   10.
    ion_occ     4  f   14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.375, 2.83, 3.50, 4.50 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -143.60 meV, min. impr. -11.24 meV\n"],[" ", "    hydro 3 d 3.7\n"],[" ", "    hydro 4 f 6.4\n"],[" ", "    hydro 2 p 1.6\n"],["#", "     hydro 5 g 9\n"],[" ", "    ionic 6 s auto\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -7.74 meV, min. impr. -0.45 meV\n"],["#", "     hydro 4 f 14.4\n"],["#", "     hydro 6 h 12.4\n"],["#", "     hydro 4 p 6.6\n"],["#", "     hydro 4 d 5.2\n"],["#", "     hydro 5 s 7.8  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.39 meV, min. impr. -0.07 meV\n"],["#", "     hydro 4 f 5.8\n"],["#", "     hydro 5 g 11.6\n"],["#", "     hydro 5 d 14\n"],["#", "     hydro 6 h 12.8\n"],["#", "     hydro 5 f 25.2\n"],["#", "     hydro 4 p 11.2\n"],["#", "     hydro 1 s 7  \n"],],
5:
[[None, "#  Further functions: -0.07 meV and below\n"],["#", "     hydro 5 f 13.6  \n"],["#", "     hydro 6 d 9.8\n"],["#", "     hydro 5 g 33.2\n"],]},
"W":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for W atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          W
#     global species definitions
    nucleus        74
    mass           183.84
#
    l_hartree      4
#
    cut_pot        3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    71  5.0
    radial_multiplier  1
    angular_grids specified
      division   0.3522   50
      division   0.9662  110
      division   1.2839  194
      division   1.5443  302
#      division   1.7847  434
#      division   2.0413  590
#      division   2.1047  770
#      division   2.1708  974
#      division   2.7309 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   4.
    valence      4  f  14.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   3.
    ion_occ      4  f  14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.775, 1.99, 2.50, 3.25, 4.50 AA
#
################################################################################
#
""",
1:
[[None, "#  \"First tier\" - improvements: -603.77 meV to -28.99 meV\n"],[" ", "    hydro 4 f 7.8\n"],[" ", "    hydro 4 d 5.8\n"],[" ", "    ionic 6 p auto\n"],["#", "     hydro 5 g 12.4\n"],[" ", "    ionic 6 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -28.30 meV to -1.31 meV\n"],["#", "     hydro 6 h 16.8\n"],["#", "     ionic 5 d auto\n"],["#", "     hydro 4 f 8.6\n"],["#", "     hydro 5 g 16.8\n"],["#", "     hydro 5 d 8.4\n"],["#", "     hydro 3 p 3.3\n"],["#", "     hydro 1 s 0.55   \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -1.79 meV, min. impr. -0.26 meV\n"],["#", "     hydro 5 f 10.8\n"],["#", "     hydro 5 g 34.4\n"],["#", "     hydro 6 h 20.8\n"],["#", "     hydro 5 g 12.8\n"],["#", "     hydro 2 p 1.6\n"],["#", "     hydro 4 s 4.7  \n"],["#", "     hydro 6 d 18.4 \n"],],
4:
[[None, "#  \"Fourth tier\" -0.46 max. impr. - meV, min. impr. -0.09 meV\n"],["#", "     hydro 6 h 21.6\n"],["#", "     hydro 5 f 22.4\n"],["#", "     hydro 4 f 4\n"],["#", "     hydro 5 p 9.6\n"],["#", "     hydro 6 d 17.2\n"],["#", "     hydro 3 p 5.2\n"],["#", "     hydro 5 g 4.7\n"],["#", "     hydro 6 s 7.6\n"],]},
"Ru":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ru atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Ru
#     global species definitions
    nucleus             44
    mass                101.07
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         60 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.4743   50
      division   0.8754  110
      division   1.1882  194
      division   1.6059  302
#      division   1.8727  434
#      division   1.9389  590
#      division   2.0082  770
#      division   2.0439  974
#      division   2.6509 1202
#      outer_grid   974
      outer_grid   302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   1.
    valence      4  p   6.
    valence      4  d   7.
#     ion occupancy
    ion_occ     5  s   0.
    ion_occ     4  p   6.
    ion_occ     4  d   6.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.725 A, 1.925 A, 2.375 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\"  - max. impr. -429.72  meV, min. impr. -24.83 meV\n"],[" ", "    hydro 4 f 8.8\n"],[" ", "    ionic 4 d auto\n"],[" ", "    ionic 5 p auto\n"],["#", "     hydro 5 g 12.4\n"],[" ", "    hydro 3 s 2.4\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -18.57  meV, min. impr. -0.96 meV\n"],["#", "     hydro 4 f 20\n"],["#", "     hydro 6 h 16.8\n"],["#", "     hydro 5 f 8.6\n"],["#", "     hydro 5 g 8\n"],["#", "     hydro 4 d 8\n"],["#", "     hydro 4 p 5.4\n"],["#", "     hydro 5 s 8.8  \n"],],
3:
[[None, "#  \"Third tier\"  - max. impr. -1.17  meV, min. impr. -0.22 meV\n"],["#", "     hydro 6 h 12.4 \n"],["#", "     hydro 5 f 38.4\n"],["#", "     hydro 3 d 2.6\n"],["#", "     hydro 5 p 10.4\n"],["#", "     hydro 4 s 3.7  \n"],],
4:
[[None, "#  \"Fourth tier\"  - max. impr. -0.29  meV, min. impr. -0.11 meV\n"],["#", "     hydro 5 d 13.6\n"],["#", "     hydro 5 f 14\n"],["#", "     hydro 5 g 11.2\n"],["#", "     hydro 2 p 1.7\n"],["#", "     hydro 4 s 5.6\n"],]},
"C":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for C atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        C
#     global species definitions
    nucleus             6
    mass                12.0107
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         34 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.3326   50
      division   0.5710  110
      division   0.7727  194
      division   0.8772  302
#      division   0.9334  434
#      division   0.9625  590
#      division   0.9924  770
#      division   1.0230  974
#      division   1.4589 1202
#     outer_grid  974
     outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      2  s   2.
    valence      2  p   2.
#     ion occupancy
    ion_occ      2  s   1.
    ion_occ      2  p   1.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.0 A, 1.25 A, 1.5 A, 2.0 A, 3.0 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -1214.57 meV to -155.61 meV\n"],[" ", "    hydro 2 p 1.7\n"],[" ", "    hydro 3 d 6\n"],[" ", "    hydro 2 s 4.9\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -67.75 meV to -5.23 meV\n"],["#", "     hydro 4 f 9.8\n"],["#", "     hydro 3 p 5.2\n"],["#", "     hydro 3 s 4.3\n"],["#", "     hydro 5 g 14.4\n"],["#", "     hydro 3 d 6.2\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -2.43 meV to -0.60 meV\n"],["#", "     hydro 2 p 5.6\n"],["#", "     hydro 2 s 1.4\n"],["#", "     hydro 3 d 4.9\n"],["#", "     hydro 4 f 11.2\n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.39 meV to -0.18 meV\n"],["#", "     hydro 2 p 2.1\n"],["#", "     hydro 5 g 16.4\n"],["#", "     hydro 4 d 13.2\n"],["#", "     hydro 3 s 13.6\n"],["#", "     hydro 4 f 17.6\n"],],
5:
[[None, "#  Further basis functions - improvements: -0.08 meV and below\n"],["#", "     hydro 3 s 2\n"],["#", "     hydro 3 p 6\n"],["#", "     hydro 4 d 20\n"],]},
"S":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for S atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        S
#     global species definitions
    nucleus             16
    mass                32.065
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         44 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.4665  110
      division   0.5810  194
      division   0.7139  302
#      division   0.8274  434
#      division   0.9105  590
#      division   1.0975  770
#      division   1.2028  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      3  s   2.
    valence      3  p   4.
#     ion occupancy
    ion_occ      3  s   1.
    ion_occ      3  p   3.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.6 A, 1.9 A, 2.5 A, 3.25 A, 4.0 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -652.81 meV to -45.53 meV\n"],[" ", "    ionic 3 d auto\n"],[" ", "    hydro 2 p 1.8\n"],["#", "     hydro 4 f 7\n"],[" ", "    ionic 3 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -30.20 meV to -1.74 meV\n"],["#", "     hydro 4 d 6.2\n"],["#", "     hydro 5 g 10.8\n"],["#", "     hydro 4 p 4.9\n"],["#", "     hydro 5 f 10\n"],["#", "     hydro 1 s 0.8\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -1.04 meV to -0.20 meV\n"],["#", "     hydro 3 d 3.9\n"],["#", "     hydro 3 d 2.7\n"],["#", "     hydro 5 g 12\n"],["#", "     hydro 4 p 10.4\n"],["#", "     hydro 5 f 12.4\n"],["#", "     hydro 2 s 1.9\n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.35 meV to -0.06 meV\n"],["#", "     hydro 4 d 10.4\n"],["#", "     hydro 4 p 7.2\n"],["#", "     hydro 4 d 10\n"],["#", "     hydro 5 g 19.2\n"],["#", "     hydro 4 s 12\n"],]},
"Zr":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Zr atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Zr
#     global species definitions
    nucleus        40
    mass           91.224
#
    l_hartree      4
#
    cut_pot        3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    58  5.0
    radial_multiplier  1
    angular_grids specified
      division   0.5825   50
      division   1.1060  110
      division   1.4586  194
      division   1.7061  302
#      division   1.9320  434
#      division   2.2803  590
#      division   2.4151  770
#      division   2.4626  974
#      division   3.1649 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   2.
    valence      4  p   6.
    valence      4  d   2.
#     ion occupancy
    ion_occ      5  s   1.
    ion_occ      4  p   6.
    ion_occ      4  d   1.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.9, 2.25, 3.00, 4.00 Ang
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -605.96 meV to -18.06 meV\n"],[" ", "    hydro 4 f 7.2\n"],[" ", "    ionic 4 d auto\n"],[" ", "    ionic 5 p auto\n"],["#", "     hydro 5 g 10.4\n"],[" ", "    ionic 5 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -32.47 meV to -1.41 meV\n"],["#", "     hydro 4 f 10.4\n"],["#", "     hydro 6 h 14.8\n"],["#", "     hydro 4 d 6.2\n"],["#", "     hydro 4 p 4.4\n"],["#", "     hydro 4 f 20\n"],["#", "     hydro 5 s 6\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -1.99 meV and lower.\n"],["#", "     hydro 4 f 5.8\n"],["#", "     hydro 5 g 10.8\n"],["#", "     hydro 2 p 1\n"],["#", "     hydro 3 d 8\n"],["#", "     hydro 6 h 14.4\n"],["#", "     hydro 1 s 0.9  \n"],],
5:
[[None, "#  Further functions (approx -0.40 meV and below possible)\n"],]},
"He":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for He atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        He
#     global species definitions
    nucleus             2
    mass                4.002602
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#     
    radial_base         27 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.3349  110
      division   0.4719  194
      division   0.5352  302
#      division   1.8809  770
#      outer_grid    770
      outer_grid    302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      1  s   2.
#     ion occupancy
    ion_occ      1  s   1.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.25 A, 1.75 A, 2.40 A, 3.25 A
#
#  Noble gas symmetric dimers converge quickly in DFT. If you find that
#  you require a larger basis than tier 2, please contact us - VB, FHI.
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -33.45 meV to -13.84 meV\n"],[" ", "    hydro 1 s 0.85\n"],[" ", "    hydro 2 p 3.5\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -0.70 meV to -0.05 meV\n"],["#", "     hydro 3 d 7.2\n"],["#", "     hydro 3 s 3\n"],["#", "     hydro 3 p 4.9\n"],["#", "     hydro 4 f 12\n"],]},
"Po":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Po atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Po
#     global species definitions
    nucleus             84
    mass                209
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         74 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.1022  110
      division   0.1528  194
      division   0.2150  302
#      division   1.0164  434
#      division   1.1133  590
#      division   1.1755  770
#      division   7.7779  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      6  p   4.
    valence      5  d  10.
    valence      4  f  14.
#     ion occupancy
    ion_occ     6  s    1.
    ion_occ     6  p    3.
    ion_occ     5  d   10.
    ion_occ     4  f   14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.30, 2.72, 3.25, 3.875, 4.75 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -135.21 meV, min. impr. -15.99 meV\n"],[" ", "    hydro 3 d 3.5\n"],[" ", "    hydro 4 f 6\n"],[" ", "    hydro 3 p 2.6\n"],[" ", "    ionic 6 s auto\n"],["#", "     hydro 5 g 9\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -8.91 meV, min. impr. -0.69 meV\n"],["#", "     hydro 4 f 12.8\n"],["#", "     hydro 6 h 12\n"],["#", "     hydro 4 p 6\n"],["#", "     hydro 4 d 4.9\n"],["#", "     hydro 5 s 7.2  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.47 meV, min. impr. -0.06 meV\n"],["#", "     hydro 5 g 13.2  \n"],["#", "     hydro 5 f 7.8\n"],["#", "     hydro 6 h 14.8\n"],["#", "     hydro 5 g 9.8\n"],["#", "     hydro 6 p 16.4\n"],["#", "     hydro 6 d 14\n"],["#", "     hydro 1 s 12   \n"],],
4:
[[None, "#  \"Fourth tier\": -0.25 meV and below\n"],["#", "     hydro 5 f 22.8\n"],["#", "     hydro 5 g 34\n"],["#", "     hydro 6 d 9.2\n"],["#", "     hydro 6 p 7.6\n"],["#", "     hydro 4 s 4.7\n"],]},
"Sb":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Sb atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Sb
#     global species definitions
    nucleus             51
    mass                121.760
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         63 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.1144  110
      division   0.1571  194
      division   0.8765  302
#      division   0.9669  434
#      division   1.0315  590
#      division   1.0999  770
#      division   3.0459  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   2.
    valence      5  p   3.
    valence      4  d  10.
#     ion occupancy
    ion_occ     5  s   1.
    ion_occ     5  p   2.
    ion_occ     4  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.10 A, 2.50 A, 3.00 A, 3.50 A, 4.50 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -220.09  meV, min. impr. -43.94 meV\n"],[" ", "    hydro 3 d 3.5\n"],[" ", "    ionic 5 p auto\n"],["#", "     hydro 4 f 6.8\n"],[" ", "    ionic 5 s auto\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -16.60 meV, min. impr. -0.74 meV\n"],["#", "     hydro 5 g 9.8\n"],["#", "     hydro 4 f 19.2\n"],["#", "     hydro 6 h 13.6\n"],["#", "     hydro 4 d 4.5\n"],["#", "     hydro 4 f 4.6\n"],["#", "     hydro 5 p 7.0\n"],["#", "     hydro 3 s 2.7\n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.83 meV, min. impr. -0.11 meV\n"],["#", "     hydro 6 p 7.8\n"],["#", "     hydro 5 g 8.6\n"],["#", "     hydro 6 h 11.6\n"],["#", "     hydro 5 f 16.4\n"],["#", "     hydro 5 d 8.4\n"],["#", "     hydro 1 s 0.7\n"],]},
"Sc":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Sc atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Sc
#     global species definitions
    nucleus             21
    mass                44.955912
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         47 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.6021   50
      division   1.1116  110
      division   1.4663  194
      division   1.6660  302
#      division   1.8551  434
#      division   2.0245  590
#      division   2.2132  770
#      division   2.5421  974
#      division   3.1021 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      3  p   6.
    valence      3  d   1.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      3  p   6.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.75 A, 2.15 A, 2.75 A, 3.5 A, 4.5 A
#
#  Basis set generation could be continued below tier 3.
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -267.88 meV to -17.01 meV\n"],[" ", "    hydro 4 f 6.8\n"],[" ", "    ionic 4 p auto\n"],[" ", "    ionic 4 d auto\n"],["#", "     hydro 5 g 10.4\n"],[" ", "    ionic 4 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -14.68 meV to -1.92 meV\n"],["#", "     hydro 4 f 9.8\n"],["#", "     ionic 3 d auto\n"],["#", "     hydro 3 p 2.4\n"],["#", "     hydro 6 h 14.8\n"],["#", "     hydro 4 d 6.2\n"],["#", "     hydro 1 s 0.45\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -1.14 meV to -0.26 meV\n"],["#", "     hydro 4 f 8\n"],["#", "     hydro 5 g 12\n"],["#", "     hydro 2 p 1.9\n"],["#", "     hydro 3 d 3.2\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 4 s 3.5  \n"],],
5:
[[None, "#  Further basis functions - not yet done.\n"],]},
"Th":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Th atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Th
#     global species definitions
    nucleus             90
    mass                232.03806
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         76 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.0887  110
      division   0.1635  194
      division   0.9942  302
#      division   1.0302  434
#      division   1.1660  590
#      division   1.2294  770
#      division   7.7724  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   2.
    valence      5  f   0.
#     ion occupancy - 3+ ion, analogous to Ce
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f    0.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.25, 2.65, 3.25, 4.00, 5.00 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -3685.84 meV, min. impr. -10.26 meV\n"],[" ", "    ionic 5 f auto\n"],[" ", "    hydro 4 f 5.2\n"],[" ", "    hydro 4 d 4.6\n"],[" ", "    hydro 5 g 10.4\n"],[" ", "    hydro 3 p 3.2\n"],[" ", "    ionic 7 s auto  \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -62.50 meV, min. impr. -1.39 meV\n"],["#", "     hydro 6 h 13.2\n"],["#", "     hydro 5 f 7.2\n"],["#", "     hydro 4 d 3.5\n"],["#", "     hydro 5 g 9.8\n"],["#", "     hydro 6 h 12.8 \n"],["#", "     hydro 4 p 4.4\n"],["#", "     hydro 5 s 5.2  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -2.63 meV, min. impr. -0.56 meV\n"],["#", "     hydro 5 g 32\n"],["#", "     hydro 5 d 10\n"],["#", "     hydro 6 p 17.6\n"],["#", "     hydro 6 f 14\n"],["#", "     hydro 6 s 7.6  \n"],]},
"Br":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Br atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Br
#     global species definitions
    nucleus             35
    mass                79.904
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         56 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.0871  110
      division   0.1400  194
      division   0.7896  302
#      division   0.8837  434
#      division   0.9869  590
#      division   1.0613  770
#      division   2.6835  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      4  p   5.
    valence      3  d  10.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      4  p   4.
    ion_occ      3  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.90 A, 2.25 A, 2.75 A, 3.25 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -247.24 meV to -20.97 meV \n"],[" ", "    hydro 3 d 4.6\n"],[" ", "    hydro 2 p 1.7\n"],["#", "     hydro 4 f 7.6\n"],[" ", "    ionic 4 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -9.01 meV to -0.73 meV\n"],["#", "     hydro 5 g 10.4\n"],["#", "     hydro 3 d 4.1\n"],["#", "     hydro 6 h 14.8\n"],["#", "     hydro 4 p 4.7\n"],["#", "     hydro 1 s 0.7\n"],["#", "     hydro 4 f 12.4\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.26 meV and below\n"],["#", "     hydro 5 f 14.8\n"],["#", "     hydro 5 d 7.8\n"],["#", "     hydro 5 g 14.4\n"],["#", "     ionic 4 p auto\n"],["#", "     hydro 3 s 3.2   \n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.09 meV and below\n"],["#", "     hydro 5 f 25.6\n"],["#", "     hydro 5 d 11.2\n"],["#", "     hydro 3 p 3.9\n"],["#", "     hydro 6 h 16.8\n"],["#", "     hydro 5 g 13.2\n"],["#", "     hydro 5 s 5.4\n"],]},
"Nd":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Nd atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Nd
#     global species definitions
    nucleus        60
    mass           144.242
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    66  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.0851  110
      division   0.1329  194
      division   0.6933  302
#      division   0.8063  434
#      division   0.9338  590
#      division   1.0141  770
#      division   3.0511  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   0.
    valence      4  f   4.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f   3.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.80, 2.125, 2.625, 3.375, 4.5 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 5 d  auto
""",
1:
[[None, "#  \"First tier\" - improvements: -1427.83 meV to -28.23 meV\n"],[" ", "    hydro 3 d 5\n"],[" ", "    hydro 5 g 11.2\n"],[" ", "    hydro 4 f 7.6\n"],[" ", "    hydro 2 p 1.4\n"],[" ", "    hydro 3 s 2.6 \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -101.28 meV to -4.95 meV\n"],["#", "     hydro 4 f 4.3\n"],["#", "     hydro 6 h 15.6\n"],["#", "     hydro 3 d 3\n"],["#", "     hydro 2 p 2\n"],["#", "     hydro 5 g 8.6\n"],["#", "     hydro 4 s 3.6\n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -12.66 meV, min. impr. -0.43 meV\n"],["#", "     hydro 4 d 14\n"],["#", "     hydro 6 h 12.4\n"],["#", "     hydro 4 f 6.6\n"],["#", "     hydro 5 g 24.8\n"],["#", "     ionic 6 p auto\n"],["#", "     hydro 1 s 0.75   \n"],],
4:
[[None, "#  \"Fourth tier\" - max. impr. -1.31 meV, min. impr. -0.39 meV\n"],["#", "     hydro 6 d 18.8\n"],["#", "     hydro 5 f 16\n"],["#", "     hydro 4 p 6\n"],["#", "     hydro 5 g 4.9\n"],["#", "     hydro 3 d 4.2\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 5 g 12\n"],["#", "     hydro 4 s 6.8\n"],]},
"Pt":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Pt atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Pt
#     global species definitions
    nucleus             78
    mass                195.084
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         72 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.4222   50
      division   0.9557  110
      division   1.2477  194
      division   1.5393  302
#      division   1.9382  434
#      division   2.0887  590
#      division   2.1534  770
#      division   2.2208  974
#      division   2.6985 1202
#      outer_grid    974
      outer_grid    302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   1.
    valence      5  p   6.
    valence      5  d   9.
    valence      4  f  14.
#     ion occupancy
    ion_occ     6  s   0.
    ion_occ     5  p   6.
    ion_occ     5  d   8.
    ion_occ     4  f   14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.00, 2.275, 2.75, 3.75 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -193.66  meV, min. impr. -18.25 meV\n"],[" ", "    hydro 4 f 7.4\n"],[" ", "    ionic 6 p auto\n"],["#", "     hydro 5 g 9.8\n"],[" ", "    ionic 6 s auto\n"],[" ", "    hydro 3 d 2.6\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -10.25  meV, min. impr. -0.56 meV\n"],["#", "     hydro 6 h 14\n"],["#", "     hydro 5 f 14\n"],["#", "     hydro 4 d 4\n"],["#", "     hydro 3 p 3.3\n"],["#", "     hydro 5 g 16.4\n"],["#", "     hydro 1 s 0.5 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.72  meV, min. impr. -0.18 meV\n"],["#", "     hydro 5 f 9\n"],["#", "     ionic 5 d auto\n"],["#", "     hydro 6 h 16.4\n"],["#", "     hydro 5 g 12.4\n"],["#", "     hydro 5 g 34\n"],["#", "     hydro 5 s 13.6\n"],["#", "     hydro 5 p 10.4\n"],],
5:
[[None, "#  Further functions: \n"],]},
"Mn":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2010
#
#  Suggested "light" defaults for Mn atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Mn
#     global species definitions
    nucleus             25
    mass                54.938045
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         50 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.4222   50
      division   0.8072  110
      division   1.0787  194
      division   1.2927  302
#      division   1.4573  434
#      division   1.8560  590
#      division   1.8945  770
#      division   1.9339  974
#      division   2.3905 1202
      outer_grid   302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      3  p   6.
    valence      3  d   5.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      3  p   6.
    ion_occ      3  d   4.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.40 A, 1.60 A, 2.10 A, 2.75 A, 3.75 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -466.21 meV to -15.27 meV \n"],[" ", "    hydro 4 f 9.6\n"],[" ", "    hydro 3 d 3.2\n"],[" ", "    hydro 2 p 2\n"],["#", "     hydro 5 g 13.6\n"],[" ", "    hydro 3 s 3.3\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -21.45 meV to -1.55 meV\n"],["#", "     hydro 3 d 6\n"],["#", "     hydro 6 h 19.2\n"],["#", "     hydro 4 f 6.4\n"],["#", "     hydro 4 f 17.2\n"],["#", "     hydro 3 p 3.1\n"],["#", "     hydro 3 d 6.2\n"],["#", "     hydro 5 g 10.8\n"],["#", "     hydro 3 s 3.8\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -1.38 meV to -0.13 meV\n"],["#", "     hydro 5 p 8.6   -1.38 meV\n"],["#", "     hydro 6 h 16    -0.73 meV\n"],["#", "     hydro 3 d 10.8  -0.43 meV\n"],["#", "     hydro 5 f 6.8   # forced: -0.26 meV\n"],["#", "     hydro 5 g 6.4   # forced: -0.21 meV\n"],["#", "     hydro 5 s 9.8   # forced: -0.13 meV\n"],],
5:
[[None, "#  Further functions: improvements -0.32 meV and below\n"],["#", "     hydro 3 p 19.6  # -0.32 meV\n"],["#", "     hydro 5 f 28.4  # -0.20 meV\n"],["#", "     hydro 4 f 26    # -0.08 meV\n"],["#", "     hydro 3 p 3.5\n"],["#", "     hydro 5 g 14.8\n"],["#", "     hydro 5 s 9\n"],["#", "     hydro 4 p 16.8\n"],["#", "     hydro 6 h 18\n"],["#", "     hydro 4 d 13.6\n"],]},
"Fr":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Fr atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Fr
#     global species definitions
    nucleus             87
    mass                223
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         75 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.5994  110
      division   0.8769  194
      division   1.1095  302
#      division   1.2801  434
#      division   1.4253  590
#      division   7.7751  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   1.
    valence      6  p   6.
    valence      5  d  10.
    valence      4  f  14.
#     ion occupancy
    ion_occ     7  s    0.
    ion_occ     6  p    6.
    ion_occ     5  d   10.
    ion_occ     4  f   14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.85, 3.50, 4.43, 5.50 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -109.37 meV, min. impr. -6.38 meV\n"],[" ", "    hydro 3 d 3.6\n"],[" ", "    hydro 4 f 6.4\n"],[" ", "    ionic 7 p auto\n"],[" ", "    hydro 4 s 2.8\n"],["#", "     hydro 5 g 8.2\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -4.96 meV, min. impr. -0.20 meV\n"],["#", "     hydro 4 f 16.4\n"],["#", "     hydro 4 d 3.9\n"],["#", "     hydro 5 f 6.2\n"],["#", "     hydro 6 h 11.2\n"],["#", "     hydro 3 s 2.1\n"],["#", "     hydro 5 g 7\n"],["#", "     hydro 2 p 1.6\n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.23 meV, min. impr. -0.06 meV\n"],["#", "     hydro 5 d 8.2\n"],["#", "     hydro 3 p 2.1\n"],["#", "     hydro 1 s 12\n"],["#", "     hydro 6 h 9\n"],["#", "     hydro 5 g 28.4\n"],["#", "     hydro 6 f 14.4\n"],],
5:
[[None, "#  Further functions - impr. -0.06 meV and below\n"],["#", "     hydro 5 d 12\n"],["#", "     hydro 4 p 4\n"],]},
"Re":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Re atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Re
#     global species definitions
    nucleus        75
    mass           186.207
#
    l_hartree      4
#
    cut_pot        3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    72  5.0
    radial_multiplier  1
    angular_grids specified
      division   0.3533   50
      division   0.9557  110
      division   1.3010  194
      division   1.6061  302
#      division   1.8277  434
#      division   2.0267  590
#      division   2.0887  770
#      division   2.1534  974
#      division   2.6985 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   5.
    valence      4  f  14.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   4.
    ion_occ      4  f  14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.775, 2.01, 2.50, 3.25, 4.25 AA
#
################################################################################
#
""",
1:
[[None, "#  \"First tier\" - improvements: -543.50 meV to -29.94 meV\n"],[" ", "    hydro 4 f 8\n"],[" ", "    hydro 3 d 7\n"],[" ", "    ionic 6 p auto\n"],["#", "     hydro 5 g 12\n"],[" ", "    ionic 6 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -24.32 meV to -1.10 meV\n"],["#", "     hydro 6 h 16.4\n"],["#", "     hydro 3 d 2.6\n"],["#", "     hydro 4 f 9.6\n"],["#", "     hydro 5 g 19.6\n"],["#", "     hydro 3 p 3.4\n"],["#", "     hydro 4 d 7.8\n"],["#", "     hydro 1 s 0.6  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -2.19 meV, min. impr. -0.24 meV\n"],["#", "     hydro 5 f 10\n"],["#", "     hydro 6 h 21.2\n"],["#", "     hydro 5 g 39.6\n"],["#", "     hydro 5 g 11.2\n"],["#", "     hydro 4 d 5.4\n"],["#", "     hydro 2 p 1.6\n"],["#", "     hydro 4 s 4.6  \n"],],
4:
[[None, "#  \"Fourth tier\" - max. impr. -0.49 meV, min. impr. -0.12 meV\n"],["#", "     hydro 6 h 20.8\n"],["#", "     hydro 5 f 22\n"],["#", "     hydro 5 p 9.8\n"],["#", "     hydro 6 d 16\n"],["#", "     hydro 4 f 3.3\n"],["#", "     hydro 5 d 9.8\n"],["#", "     hydro 2 p 5.4\n"],["#", "     hydro 7 s 16\n"],]},
"Ir":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ir atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Ir
#     global species definitions
    nucleus             77
    mass                192.217
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         72 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.3664   50
      division   0.9423  110
      division   1.2652  194
      division   1.6525  302
#      division   1.8819  434
#      division   2.0267  590
#      division   2.0887  770
#      division   2.1534  974
#      division   2.6985 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   7.
    valence      4  f  14.
#     ion occupancy
    ion_occ     6  s   1.
    ion_occ     5  p   6.
    ion_occ     5  d   6.
    ion_occ     4  f   14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.85, 2.125, 2.5, 3.25, 4.25 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -337.32  meV, min. impr. -28.04 meV\n"],[" ", "    hydro 4 f 8.2\n"],[" ", "    ionic 6 p auto\n"],["#", "     hydro 5 g 10.8\n"],[" ", "    hydro 3 d 2.9\n"],[" ", "    ionic 6 s auto\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -17.86  meV, min. impr. -0.56 meV\n"],["#", "     hydro 6 h 15.6\n"],["#", "     hydro 5 f 7.8\n"],["#", "     hydro 5 f 14\n"],["#", "     hydro 5 g 17.2\n"],["#", "     hydro 3 p 3.7\n"],["#", "     hydro 4 d 8.4\n"],["#", "     hydro 1 s 0.6\n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.76 meV, min. impr. -0.18 meV\n"],["#", "     hydro 5 g 34.4\n"],["#", "     hydro 3 d 6\n"],["#", "     hydro 6 h 18.8\n"],["#", "     hydro 5 f 12.4\n"],["#", "     hydro 5 g 15.6\n"],["#", "     hydro 2 p 3.5\n"],["#", "     hydro 5 s 13.6\n"],],
5:
[[None, "#  Further functions - impr.: -0.19 meV and below\n"],["#", "     hydro 6 h 25.6  \n"],]},
"Os":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Os atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Os
#     global species definitions
    nucleus        76
    mass           190.23
#
    l_hartree      4
#
    cut_pot        3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    72  5.0
    radial_multiplier  1
    angular_grids specified
      division   0.3468   50
      division   0.9290  110
      division   1.2652  194
      division   1.5835  302
#      division   1.8546  434
#      division   1.9966  590
#      division   2.0267  770
#      division   2.0887  974
#      division   2.6529 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   6.
    valence      4  f  14.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   5.
    ion_occ      4  f  14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.80, 2.04, 2.50, 3.25, 4.50 AA
#
################################################################################
#
""",
1:
[[None, "#  \"First tier\" - improvements: -453.39 meV to -28.79 meV\n"],[" ", "    hydro 4 f 8.2\n"],[" ", "    ionic 6 p auto\n"],[" ", "    ionic 5 d auto\n"],["#", "     hydro 5 g 12\n"],[" ", "    ionic 6 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -21.76 meV to - meV\n"],["#", "     hydro 6 h 16.4\n"],["#", "     hydro 3 p 3.6\n"],["#", "     hydro 4 f 9.4\n"],["#", "     hydro 5 d 7.6\n"],["#", "     hydro 5 g 20.4\n"],["#", "     hydro 4 s 4.3   \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -1.69 meV, min. impr. -0.23 meV\n"],["#", "     hydro 5 f 10.4\n"],["#", "     hydro 6 h 21.2\n"],["#", "     hydro 5 g 13.2\n"],["#", "     hydro 5 g 38.8\n"],["#", "     hydro 5 d 9.8\n"],["#", "     hydro 2 p 1.9  \n"],["#", "     hydro 1 s 0.75  \n"],],
4:
[[None, "#  \"Fourth tier\" - max. impr. -0.38 meV, min. impr. -0.17 meV\n"],["#", "     hydro 6 h 22\n"],["#", "     hydro 5 f 22.4\n"],["#", "     hydro 5 p 10.4\n"],["#", "     hydro 6 d 16\n"],["#", "     hydro 7 s 11.2  \n"],]},
"La":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for La atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          La
#     global species definitions
    nucleus        57
    mass           138.90547
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    65  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.1164  110
      division   0.8770  194
      division   0.9952  302
#      division   1.1042  434
#      division   1.1747  590
#      division   1.2496  770
#      division   4.2775  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   1.
    valence      4  f   0.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f   0.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.2, 2.6, 3.25, 4.00, 5.00 Ang
#
################################################################################
#  Necessary addition to minimal basis
     ionic 4 f auto  
""",
1:
[[None, "#  \"First tier\" - improvements: -389.32 meV to -10.38 meV\n"],[" ", "    hydro 4 d 4.6     \n"],[" ", "    hydro 4 f 6.2     \n"],[" ", "    hydro 5 g 10      \n"],[" ", "    hydro 2 p 1.5     \n"],[" ", "    hydro 4 s 4.1     \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -30.19 meV to -0.51 meV\n"],["#", "     hydro 6 h 13.6\n"],["#", "     hydro 4 f 5\n"],["#", "     hydro 5 d 4.6\n"],["#", "     hydro 5 g 9\n"],["#", "     hydro 6 d 11.2\n"],["#", "     hydro 4 p 4.3\n"],["#", "     hydro 5 s 5.4  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -1.72 meV, min. impr. -0.23 meV\n"],["#", "     hydro 6 h 12.4\n"],["#", "     hydro 5 g 6\n"],["#", "     hydro 5 g 28.4\n"],["#", "     hydro 4 f 12.4\n"],["#", "     hydro 4 d 7\n"],["#", "     hydro 5 p 8.4\n"],["#", "     hydro 3 s 2.3\n"],],
5:
[[None, "#  Further functions - impr. -0.22 meV and below\n"],["#", "     hydro 5 f 10.8\n"],["#", "     hydro 5 g 15.6\n"],]},
"As":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for As atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        As
#
    nucleus             33
    mass                74.92160
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         55 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.4982   50
      division   0.9113  110
      division   1.1593  194
      division   1.4959  302
#      division   1.6697  434
#      division   1.8319  590
#      division   1.9752  770
#      division   2.0131  974
#      division   2.4015 1202
#      outer_grid  1202
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      4  p   3.
    valence      3  d  10.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      4  p   2.
    ion_occ      3  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.75 A, 2.10 A, 2.50 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -385.12 meV to -54.94 meV \n"],[" ", "    hydro 3 d 4\n"],[" ", "    hydro 2 p 1.5\n"],["#", "     hydro 4 f 6.8\n"],[" ", "    ionic 4 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -22.14 meV to -3.21 meV\n"],["#", "     hydro 5 g 10\n"],["#", "     hydro 6 h 13.6\n"],["#", "     hydro 4 p 4.3\n"],["#", "     hydro 4 f 15.6\n"],["#", "     hydro 4 d 5.4\n"],["#", "     hydro 1 s 0.6\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.57 meV to -0.13 meV\n"],["#", "     hydro 5 g 16.4\n"],["#", "     hydro 4 f 7.4\n"],["#", "     hydro 5 d 7.4\n"],["#", "     ionic 4 p auto\n"],["#", "     hydro 3 s 2.6     \n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.30 meV and below\n"],["#", "     hydro 3 p 3\n"],["#", "     hydro 6 h 18.4\n"],["#", "     hydro 5 d 11.2\n"],["#", "     hydro 5 f 15.2\n"],["#", "     hydro 5 g 13.6\n"],["#", "     hydro 5 s 6.2   \n"],]},
"Hf":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Hf atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Hf
#     global species definitions
    nucleus        72
    mass           178.49
#
    l_hartree      4
#
    cut_pot        3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    71  5.0
    radial_multiplier  1
    angular_grids specified
      division   0.4447   50
      division   1.1303  110
      division   1.4795  194
      division   1.7333  302
#      division   1.9508  434
#      division   2.2755  590
#      division   2.4268  770
#      division   2.5081  974
#      division   3.0443 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   2.
    valence      4  f  14.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   1.
    ion_occ      4  f  14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.975, 2.49, 3.25, 4.50 AA
#
################################################################################
#
""",
1:
[[None, "#  \"First tier\" - improvements: -322.32 meV to -24.16 meV\n"],[" ", "    hydro 4 f 6\n"],[" ", "    hydro 3 d 6\n"],[" ", "    ionic 6 p auto\n"],["#", "     hydro 5 g 10.8\n"],[" ", "    hydro 4 s 4.7  \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -29.31 meV to -1.14 meV\n"],["#", "     hydro 5 f 9.6\n"],["#", "     ionic 5 d auto\n"],["#", "     hydro 6 h 15.2\n"],["#", "     hydro 3 p 2.3\n"],["#", "     hydro 4 d 6.6\n"],["#", "     hydro 3 s 2.1 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -1.11 meV, min. impr. - meV\n"],["#", "     hydro 5 f 6.6\n"],["#", "     hydro 5 g 11.2\n"],["#", "     hydro 6 h 17.6\n"],["#", "     hydro 3 p 3\n"],["#", "     hydro 5 g 38.8\n"],["#", "     hydro 4 d 4.9\n"],["#", "     hydro 1 s 0.5 \n"],],
4:
[[None, "#  \"Fourth tier\" - max. impr. -0.31 meV, min. impr. -0.11 meV\n"],["#", "     hydro 5 p 12\n"],["#", "     hydro 5 f 14\n"],["#", "     hydro 5 f 20.8\n"],["#", "     hydro 4 s 12.4\n"],["#", "     hydro 5 d 19.2\n"],["#", "     hydro 6 h 22\n"],],
5:
[[None, "#  Further functions: -0.14 meV and below.\n"],["#", "     hydro 5 p 8.6\n"],["#", "     hydro 4 s 6\n"],["#", "     hydro 6 d 9.8\n"],["#", "     hydro 5 f 19.6\n"],]},
"Bi":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Bi atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Bi
#     global species definitions
    nucleus             83
    mass                208.98040
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         74 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.1064  110
      division   0.1579  194
      division   0.2150  302
#      division   1.0164  434
#      division   1.1133  590
#      division   1.1970  770
#      division   7.7779  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      6  p   3.
    valence      5  d  10.
    valence      4  f  14.
#     ion occupancy
    ion_occ     6  s    1.
    ion_occ     6  p    2.
    ion_occ     5  d   10.
    ion_occ     4  f   14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.225, 2.61, 3.125, 3.75, 4.75 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -158.89 meV, min. impr. -15.41 meV\n"],[" ", "    hydro 2 p 1.4\n"],[" ", "    ionic 5 d auto\n"],[" ", "    hydro 4 f 7.6\n"],[" ", "    hydro 3 s 3.3\n"],["#", "     hydro 5 g 10.4\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -8.24  meV, min. impr. -0.46 meV\n"],["#", "     ionic 6 d auto\n"],["#", "     hydro 3 p 3.1\n"],["#", "     hydro 6 h 14\n"],["#", "     hydro 5 f 15.6\n"],["#", "     hydro 4 f 5.6\n"],["#", "     hydro 6 s 19.6 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.99 meV, min. impr. -0.11 meV\n"],["#", "     hydro 4 d 4.4\n"],["#", "     hydro 5 g 8.8\n"],["#", "     hydro 3 p 2.4\n"],["#", "     hydro 6 h 12\n"],["#", "     hydro 4 d 5.2\n"],["#", "     hydro 4 f 16.4\n"],["#", "     hydro 4 s 4.2  \n"],]},
"Ne":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ne atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Ne
#     global species definitions
    nucleus             10
    mass                20.1797
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         38 5.0
    radial_multiplier   1
    angular_grids specified 
      division   0.4737  110
      division   0.6363  194
      division   0.7448  302
#      division   0.8348  590
#      division   1.0034  770
#      division   1.7611  974
#      outer_grid   974
      outer_grid   302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      2  s   2.
    valence      2  p   6.
#     ion occupancy
    ion_occ      2  s   1.
    ion_occ      2  p   5.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.5 A, 1.75 A, 2.25 A, 2.625 A, 3.0 A, 3.5 A
#
#  Noble gas symmetric dimers converge quickly in DFT. If you find that
#  you require a larger basis than tier 3, please contact us - VB, FHI.
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -20.90 meV to -4.46 meV\n"],[" ", "    hydro 3 d 6\n"],[" ", "    hydro 2 p 1.5\n"],[" ", "    hydro 3 s 7.6\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -2.26 meV to -0.22 meV\n"],["#", "     hydro 4 f 9.4\n"],["#", "     ionic 3 d auto\n"],["#", "     ionic 3 s auto\n"],["#", "     hydro 5 g 13.6\n"],["#", "     hydro 3 p 6\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.21 meV and below\n"],["#", "     hydro 2 s 8.6\n"],["#", "     hydro 4 d 12\n"],["#", "     hydro 4 d 7.6\n"],["#", "     hydro 3 p 2.3\n"],]},
"Pu":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Pu atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Pu
#     global species definitions
    nucleus             94
    mass                244
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         77 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.0660  110
      division   0.0897  194
      division   0.1215  302
#      division   0.8157  434
#      division   0.9246  590
#      division   1.0644  770
#      division   7.7698  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   0.
    valence      5  f   6.
#     ion occupancy 
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f    5.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.81, 2.02, 2.5, 3.25, 4.25 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 6 d  auto
""",
1:
[[None, "#  \"First tier\" - max. impr. -1573.49 meV, min. impr. -39.69 meV\n"],[" ", "    hydro 3 d 5\n"],[" ", "    hydro 5 g 12\n"],[" ", "    hydro 2 p 1.8\n"],[" ", "    hydro 5 f 7.2\n"],[" ", "    hydro 4 s 4.0 \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -138.69 meV, min. impr. -1.71 meV\n"],["#", "     hydro 6 h 16.4\n"],["#", "     hydro 4 f 7\n"],["#", "     hydro 3 d 3.5\n"],["#", "     hydro 5 g 17.6\n"],["#", "     hydro 2 p 1.5\n"],["#", "     ionic 7 s auto  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -10.48 meV, min. impr. -0.84 meV\n"],["#", "     hydro 6 f 16.8\n"],["#", "     hydro 7 d 17.6\n"],["#", "     hydro 5 g 36.8\n"],["#", "     hydro 6 h 18   \n"],["#", "     hydro 5 g 9.2\n"],["#", "     hydro 5 p 17.2  \n"],["#", "     hydro 1 s 0.35  \n"],[None, "#  A fourth tier could be added if required.\n"],]},
"I":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for I atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          I
#     global species definitions
    nucleus        53
    mass           126.90447
#
    l_hartree      4
#
    cut_pot        3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    64  5.0
    radial_multiplier  1
    angular_grids specified
      division   0.1103  110
      division   0.1515  194
      division   0.9554  302
#      division   1.1196  590
#      division   1.1922  770
#      division   6.1948  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   2.
    valence      5  p   5.
    valence      4  d  10.
#     ion occupancy
    ion_occ      5  s   1.
    ion_occ      5  p   4.
    ion_occ      4  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.22, 2.65, 3.25, 4.25 Ang
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -270.74 meV to -21.24 meV\n"],[" ", "    hydro 3 d 4\n"],["#", "     hydro 4 f 6.4\n"],[" ", "    hydro 2 p 1.6\n"],[" ", "    ionic 5 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -16.39 meV to -0.39 meV\n"],["#", "     hydro 5 g 9.4\n"],["#", "     hydro 4 f 18.4\n"],["#", "     hydro 6 h 12.4\n"],["#", "     hydro 4 p 4.5\n"],["#", "     hydro 3 d 4.2\n"],["#", "     hydro 3 s 3.0  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.76 meV, min. impr. -0.06 meV\n"],["#", "     hydro 5 f 15.6\n"],["#", "     hydro 5 g 12\n"],["#", "     hydro 5 d 16\n"],["#", "     hydro 4 f 42   \n"],["#", "     hydro 6 h 15.2\n"],["#", "     ionic 5 p auto\n"],["#", "     hydro 1 s 6.2   \n"],],
5:
[[None, "#  Further functions that fell out of the optimization: -0.10 meV and below\n"],["#", "     hydro 4 f 7    \n"],["#", "     hydro 6 p 9    \n"],["#", "     hydro 2 s 6.4  \n"],]},
"B":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for B atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        B
#     global species definitions
    nucleus             5
    mass                10.811
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         32 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.3742  110
      division   0.5197  194
      division   0.5753  302
#      division   0.7664  434
#      division   0.8392  770
#      division   1.6522  974
#      outer_grid   974
      outer_grid   302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      2  s   2.
    valence      2  p   1.
#     ion occupancy
    ion_occ      2  s   1.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.25 A, 1.625 A, 2.5 A, 3.5 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -710.52 meV to -92.39 meV\n"],[" ", "    hydro 2 p 1.4\n"],[" ", "    hydro 3 d 4.8\n"],[" ", "    hydro 2 s 4\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -33.88 meV to -2.20 meV\n"],["#", "     hydro 4 f 7.8\n"],["#", "     hydro 3 p 4.2\n"],["#", "     hydro 3 s 3.3\n"],["#", "     hydro 5 g 11.2\n"],["#", "     hydro 3 d 5.4\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -1.28 meV to -0.36 meV\n"],["#", "     hydro 2 p 4.7\n"],["#", "     hydro 2 s 8.4\n"],["#", "     hydro 4 d 5.8\n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.25 meV to -0.12 meV\n"],["#", "     hydro 3 p 2.2\n"],["#", "     hydro 3 s 3\n"],["#", "     hydro 4 f 9.8\n"],["#", "     hydro 5 g 12.8\n"],["#", "     hydro 4 d 10\n"],],
5:
[[None, "#  Further functions\n"],["#", "     hydro 4 f 14\n"],["#", "     hydro 3 p 12.4\n"],]},
"Zn":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2010
#
#  Suggested "light" defaults for Zn atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Zn
#     global species definitions
    nucleus             30
    mass                65.409
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         53 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.5114   50
      division   0.8989  110
      division   1.2692  194
      division   1.6226  302
#      division   1.7854  434
#      division   2.0877  590
#      division   2.1298  770
#      division   2.1730  974
#      division   2.5659 1202
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      3  p   6.
    valence      3  d  10.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      3  p   6.
    ion_occ      3  d   9.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.00 A, 2.30 A, 2.85 A, 3.50 A, 4.25 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -270.82 meV to -12.81 meV \n"],[" ", "    hydro 2 p 1.7\n"],[" ", "    hydro 3 s 2.9\n"],[" ", "    hydro 4 p 5.4\n"],[" ", "    hydro 4 f 7.8\n"],[" ", "    hydro 3 d 4.5\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -3.35 meV to -0.82 meV\n"],["#", "     hydro 5 g 10.8\n"],["#", "     hydro 2 p 2.4\n"],["#", "     hydro 3 s 6.2\n"],["#", "     hydro 3 d 3\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.61 meV to -0.12 meV\n"],["#", "     hydro 6 h 15.2\n"],["#", "     ionic 4 p auto\n"],["#", "     hydro 5 s 12.8\n"],["#", "     hydro 4 f 5.4    \n"],["#", "     hydro 4 d 7      \n"],],
5:
[[None, "#  Further functions - improvements: -0.16 meV and below\n"],["#", "     hydro 4 f 20   \n"],["#", "     hydro 3 p 2.2  \n"],["#", "     hydro 5 f 6.4  \n"],["#", "     hydro 5 g 8    \n"],]},
"N":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for N atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        N
#     global species definitions
    nucleus             7
    mass                14.0067
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         35 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.2599   50
      division   0.4601  110
      division   0.5885  194
      division   0.6503  302
#      division   0.6939  434
#      division   0.7396  590
#      division   0.7632  770
#      division   0.8122  974
#      division   1.1604 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      2  s   2.
    valence      2  p   3.
#     ion occupancy
    ion_occ      2  s   1.
    ion_occ      2  p   2.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.0 A, 1.1 A, 1.5 A, 2.0 A, 3.0 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -1193.42 meV to -220.60 meV\n"],[" ", "    hydro 2 p 1.8\n"],[" ", "    hydro 3 d 6.8\n"],[" ", "    hydro 3 s 5.8\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -80.21 meV to -6.86 meV\n"],["#", "     hydro 4 f 10.8\n"],["#", "     hydro 3 p 5.8\n"],["#", "     hydro 1 s 0.8\n"],["#", "     hydro 5 g 16\n"],["#", "     hydro 3 d 4.9\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -4.29 meV to -0.53 meV\n"],["#", "     hydro 3 s 16\n"],["#", "     ionic 2 p auto\n"],["#", "     hydro 3 d 6.6\n"],["#", "     hydro 4 f 11.6\n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.75 meV to -0.25 meV\n"],["#", "     hydro 2 p 4.5\n"],["#", "     hydro 2 s 2.4\n"],["#", "     hydro 5 g 14.4\n"],["#", "     hydro 4 d 14.4\n"],["#", "     hydro 4 f 16.8\n"],],
5:
[[None, "# Further basis functions - -0.21 meV and below\n"],["#", "     hydro 3 p 14.8\n"],["#", "     hydro 3 s 4.4\n"],["#", "     hydro 3 d 19.6\n"],["#", "     hydro 5 g 12.8\n"],]},
"Yb":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Yb atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Yb
#     global species definitions
    nucleus        70
    mass           173.04
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    70  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.1305  110
      division   0.8949  194
      division   1.1509  302
#      division   1.2665  434
#      division   1.3413  590
#      division   1.4207  770
#      division   7.7895  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   0.
    valence      4  f  14.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f  13.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.5, 3.0, 3.5, 4.1, 5.0 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 5 d  auto
""",
1:
[[None, "#  \"First tier\" - improvements: -11.877 meV to -8.92 meV\n"],[" ", "    hydro 2 p 1\n"],[" ", "    hydro 3 d 1.6\n"],[" ", "    hydro 4 f 5.6\n"],[" ", "    hydro 5 g 8.4\n"],[" ", "    hydro 4 s 4.2 \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -11.70 meV to -0.33 meV\n"],["#", "     hydro 3 p 3.2\n"],["#", "     hydro 6 h 11.2\n"],["#", "     ionic 5 d auto\n"],["#", "     hydro 4 f 3.4\n"],["#", "     hydro 5 g 19.2\n"],["#", "     hydro 1 s 0.35  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.41 meV, min. impr. -0.11 meV\n"],["#", "     hydro 5 f 10\n"],["#", "     hydro 5 g 5.6\n"],["#", "     hydro 5 p 4.7\n"],["#", "     hydro 6 h 9.2\n"],["#", "     hydro 6 d 6.6  \n"],["#", "     hydro 1 s 4.4  \n"],],
5:
[[None, "#  Further functions: -0.28 meV and below\n"],["#", "     hydro 4 p 9.2  \n"],["#", "     hydro 6 s 6.6  \n"],]},
"No":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for No atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        No
#     global species definitions
    nucleus             102
    mass                259
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         79 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.1145  110
      division   0.1640  194
      division   1.0952  302
#      division   1.2546  590
#      division   1.4376  770
#      division   7.7647  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   0.
    valence      5  f  14.
#     ion occupancy
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f   13.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.60, 3.125, 3.75, 4.27, 5.00
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 6 d  auto
""",
1:
[[None, "#  \"First tier\" - max. impr. -74.62 meV, min. impr. -9.09 meV\n"],[" ", "    hydro 2 p 1\n"],[" ", "    hydro 3 d 4.7\n"],[" ", "    hydro 4 f 5.8\n"],[" ", "    hydro 4 s 4.4\n"],[" ", "    hydro 5 g 9.8\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -2.00  meV, min. impr. -0.38 meV\n"],["#", "     hydro 6 h 12.8\n"],["#", "     hydro 5 p 5.6\n"],["#", "     hydro 3 d 1.6\n"],["#", "     hydro 4 d 3\n"],["#", "     hydro 4 f 2.8\n"],["#", "     hydro 5 g 25.6\n"],["#", "     hydro 1 s 10\n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.35 meV, min. impr. -0.07 meV\n"],["#", "     hydro 4 p 3.9\n"],["#", "     hydro 5 f 7.4\n"],["#", "     hydro 5 g 7\n"],["#", "     hydro 6 p 5.4\n"],["#", "     hydro 3 s 1.8\n"],["#", "     hydro 6 h 11.2\n"],["#", "     hydro 5 d 4.1   \n"],]},
"Au":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Au atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Au
#     global species definitions
    nucleus             79
    mass                196.966569
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         73 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.5066   50
      division   0.9861  110
      division   1.2821  194
      division   1.5344  302
#      division   2.0427  434
#      division   2.1690  590
#      division   2.2710  770
#      division   2.3066  974
#      division   2.7597 1202
#      outer_grid 974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   1.
    valence      5  p   6.
    valence      5  d  10.
    valence      4  f  14.
#     ion occupancy
    ion_occ     6  s   0.
    ion_occ     5  p   6.
    ion_occ     5  d   9.
    ion_occ     4  f   14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.10, 2.45, 3.00, 4.00 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -161.60  meV, min. impr. -4.53 meV\n"],[" ", "    ionic 6 p auto\n"],[" ", "    hydro 4 f 7.4\n"],[" ", "    ionic 6 s auto\n"],["#", "     hydro 5 g 10\n"],["#", "     hydro 6 h 12.8\n"],[" ", "    hydro 3 d 2.5\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -2.46  meV, min. impr. -0.28 meV\n"],["#", "     hydro 5 f 14.8\n"],["#", "     hydro 4 d 3.9\n"],["#", "     hydro 3 p 3.3\n"],["#", "     hydro 1 s 0.45\n"],["#", "     hydro 5 g 16.4\n"],["#", "     hydro 6 h 13.6\n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.49  meV, min. impr. -0.09 meV\n"],["#", "     hydro 4 f 5.2\n"],["#", "     hydro 4 d 5\n"],["#", "     hydro 5 g 8\n"],["#", "     hydro 5 p 8.2\n"],["#", "     hydro 6 d 12.4\n"],["#", "     hydro 6 s 14.8\n"],],
5:
[[None, "#  Further basis functions: -0.08 meV and below\n"],["#", "     hydro 5 f 18.8\n"],["#", "     hydro 5 g 20\n"],["#", "    hydro 5 g 15.2\n"],]},
"Tl":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Tl atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Tl
#     global species definitions
    nucleus             81
    mass                204.3833
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         73 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.1054  110
      division   0.1577  194
      division   0.2156  302
#      division   1.0186  434
#      division   1.1590  590
#      division   1.2472  770
#      division   7.7807  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      6  p   1.
    valence      5  d  10.
    valence      4  f  14.
#     ion occupancy
    ion_occ     6  s    1.
    ion_occ     6  p    0.
    ion_occ     5  d   10.
    ion_occ     4  f   14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.21, 2.60, 3.11, 3.75, 4.75 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -121.13 meV, min. impr. -15.24 meV\n"],[" ", "    hydro 3 p 2.1\n"],[" ", "    hydro 4 f 7.6\n"],[" ", "    hydro 3 d 3.4\n"],[" ", "    hydro 3 s 3\n"],["#", "     hydro 5 g 10\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -4.10 meV, min. impr. -0.85 meV\n"],["#", "     hydro 3 p 2.5\n"],["#", "     hydro 6 h 13.6\n"],["#", "     hydro 5 f 15.6\n"],["#", "     hydro 4 d 4.1\n"],["#", "     hydro 4 s 3.0  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.88 meV, min. impr. -0.21 meV\n"],["#", "     hydro 4 f 5.2\n"],["#", "     hydro 5 p 8.6\n"],["#", "     hydro 5 g 11.6\n"],["#", "     hydro 5 s 19.2\n"],["#", "     hydro 5 d 4.6\n"],],
4:
[[None, "#  \"Fourth tier\" - max. impr. -0.20 meV, min. impr. -0.21 meV\n"],["#", "     hydro 5 g 33.2\n"],["#", "     hydro 6 d 11.2\n"],["#", "     hydro 6 h 13.2\n"],["#", "     hydro 5 g 7.8\n"],["#", "     hydro 5 f 6.8\n"],["#", "     hydro 4 d 8.4\n"],["#", "     hydro 2 s 3.2\n"],],
5:
[[None, "#  Further functions: -0.05 meV and below\n"],["#", "     hydro 1 s 9.8\n"],]},
"Hg":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Hg atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Hg
#     global species definitions
    nucleus             80
    mass                200.59
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         73 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.5485   50
      division   1.0425  110
      division   1.3361  194
      division   1.5779  302
#      division   2.1690  434
#      division   2.2710  590
#      division   2.3801  770
#      division   2.4181  974
#      division   2.8573 1202
#      outer_grid  974
      outer_grid 302
 ################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d  10.
    valence      4  f  14.
#     ion occupancy
    ion_occ     6  s   1.
    ion_occ     5  p   6.
    ion_occ     5  d   9.
    ion_occ     4  f   14.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.225, 2.50, 3.04, 4.00, 5.00 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -228.38  meV, min. impr. -2.59 meV\n"],[" ", "    hydro 2 p 1.7\n"],[" ", "    hydro 4 f 7\n"],[" ", "    ionic 6 s auto\n"],["#", "     hydro 5 g 9.6\n"],[" ", "    hydro 4 p 4.7\n"],[" ", "    hydro 4 d 7.8   \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -2.80  meV, min. impr. -0.17 meV\n"],["#", "     hydro 6 h 13.2\n"],["#", "     hydro 5 f 12.8\n"],["#", "     hydro 5 p 8\n"],["#", "     hydro 5 s 6.8\n"],["#", "     hydro 4 d 5\n"],["#", "     hydro 5 g 16\n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.15 meV, min. impr. -0.04 meV\n"],["#", "     hydro 2 p 2.3\n"],["#", "     hydro 4 f 6\n"],["#", "     hydro 6 p 16.4\n"],["#", "     hydro 4 f 13.2\n"],["#", "     hydro 6 h 13.6\n"],["#", "     hydro 5 g 9.8\n"],["#", "     hydro 6 d 8\n"],["#", "     hydro 1 s 10.8  \n"],]},
"Cu":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2010
#
#  Suggested "light" defaults for Cu atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Cu
#
    nucleus      29
    mass         63.546
#
    l_hartree    4
#
    cut_pot      3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base        53 5.0
    radial_multiplier  1
    angular_grids       specified
      division   0.5231   50
      division   0.8642  110
      division   1.1767  194
      division   1.5041  302
#      division   1.9293  434
#      division   2.0065  590
#      division   2.0466  770
#      division   2.0877  974
#      division   2.4589 1202
      outer_grid   302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   1.
    valence      3  p   6.
    valence      3  d  10.
#     ion occupancy
    ion_occ      4  s   0.
    ion_occ      3  p   6.
    ion_occ      3  d   9.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.8, 2.2, 3.0, 4.0 Ang
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -211.42 meV to -9.17 meV\n"],[" ", "    ionic 4 p auto\n"],[" ", "    hydro 4 f 7.4\n"],[" ", "    hydro 3 s 2.6\n"],[" ", "    hydro 3 d 5\n"],["#", "     hydro 5 g 10.4\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -2.49 meV to -1.08 meV \n"],["#", "     hydro 4 p 5.8\n"],["#", "     hydro 3 d 2.7\n"],["#", "     hydro 6 h 15.2\n"],["#", "     hydro 5 s 10.8\n"],["#", "     hydro 4 f 16\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.50 meV to -0.21 meV\n"],["#", "     hydro 4 d 6\n"],["#", "     hydro 3 p 2.4\n"],["#", "     hydro 4 f 6.4\n"],["#", "     hydro 3 s 6.8\n"],["#", "     hydro 5 g 11.2\n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.13 meV to -0.05 meV\n"],["#", "     hydro 4 p 7\n"],["#", "     hydro 4 s 4\n"],["#", "     hydro 6 h 14\n"],["#", "     hydro 4 d 8.6\n"],["#", "     hydro 5 f 15.2\n"],]},
"Mg":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Mg atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Mg
#     global species definitions
    nucleus             12
    mass                24.3050
#
    l_hartree           4
#
    cut_pot             4.0          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         40 5.5
    radial_multiplier   1
    angular_grids       specified
      division   0.7029   50
      division   0.9689  110
      division   1.1879  194
      division   1.3129  302
#      division   1.4867  434
#      division   1.6018  590
#      division   1.8611  770
#      division   1.9576  974
#      division   2.2261 1202
#      outer_grid   974
      outer_grid   302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      3  s   2.
    valence      2  p   6.
#     ion occupancy
    ion_occ      2  s   2.
    ion_occ      2  p   6.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.125 A, 2.375 A, 2.875 A, 3.375 A, 4.5 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -230.76 meV to -21.94 meV\n"],[" ", "    hydro 2 p 1.5\n"],[" ", "    ionic 3 d auto\n"],[" ", "    hydro 3 s 2.4\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -5.43 meV to -1.64 meV\n"],["#", "     hydro 4 f 4.3\n"],["#", "     hydro 2 p 3.4\n"],["#", "     hydro 4 s 11.2\n"],["#", "     hydro 3 d 6.2\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.92 meV to -0.22 meV\n"],["#", "     hydro 2 s 0.6\n"],["#", "     hydro 3 p 4.8\n"],["#", "     hydro 4 f 7.4\n"],["#", "     hydro 5 g 6.6\n"],["#", "     hydro 2 p 1.6\n"],["#", "     hydro 3 d 1.8\n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.09 meV to -0.05 meV\n"],["#", "     hydro 4 p 0.45\n"],["#", "     hydro 5 g 10.4\n"],["#", "     hydro 2 s 12.4\n"],["#", "     hydro 4 d 1.7\n"],]},
"Np":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Np atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Np
#     global species definitions
    nucleus             93
    mass                237
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         77 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.0861  110
      division   0.1172  194
      division   0.1637  302
#      division   0.1740  434
#      division   0.9579  590
#      division   1.0832  770
#      division   7.7698  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   1.
    valence      5  f   4.
#     ion occupancy - 3+ ion, analogous to Ce
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f    3.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.84, 2.05, 2.625, 3.375, 4.50 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -1201.52 meV, min. impr. -41.92 meV\n"],[" ", "    hydro 3 d 5.2\n"],[" ", "    hydro 5 g 12.4\n"],[" ", "    hydro 2 p 2\n"],["#", "     hydro 6 h 15.6\n"],[" ", "    hydro 4 f 8.6\n"],[" ", "    hydro 3 s 2.9  \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -49.98 meV, min. impr. -3.69 meV\n"],["#", "     hydro 4 f 4.5\n"],["#", "     hydro 3 d 4.4\n"],["#", "     hydro 5 g 27.2\n"],["#", "     hydro 4 p 4.7 \n"],["#", "     hydro 4 s 3.9 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -11.76 meV, min. impr. -0.91 meV\n"],["#", "     hydro 5 g 8.6\n"],["#", "     hydro 6 h 14\n"],["#", "     ionic 6 d auto\n"],["#", "     hydro 4 f 7.8\n"],["#", "     hydro 6 f 24\n"],["#", "     hydro 5 g 47.6\n"],["#", "     hydro 4 p 7.0 \n"],["#", "     hydro 4 s 7.4\n"],[None, "#  More basis functions could be added if needed.\n"],]},
"Ac":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ac atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Ac
#     global species definitions
    nucleus             89
    mass                227
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         76 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.1040  110
      division   0.1635  194
      division   1.0865  302
#      division   1.2735  434
#      division   1.3667  590
#      division   1.4413  770
#      division   7.7724  974
#      outer_grid 974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   1.
    valence      5  f   0.
#     ion occupancy
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f    0.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.48, 3.10, 3.72, 4.25, 5.00
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -692.46 meV, min. impr. -12.07 meV\n"],[" ", "    ionic 5 f auto\n"],[" ", "    hydro 4 d 4\n"],[" ", "    ionic 7 p auto\n"],[" ", "    hydro 5 g 9.8\n"],[" ", "    hydro 4 f 5.4\n"],[" ", "    hydro 4 s 3.8  \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -18.06 meV, min. impr. -0.74 meV\n"],["#", "     hydro 6 h 12.4\n"],["#", "     hydro 5 d 4.6\n"],["#", "     hydro 5 f 7\n"],["#", "     hydro 3 p 2\n"],["#", "     hydro 6 d 9.2\n"],["#", "     hydro 5 g 8.6\n"],["#", "     hydro 1 s 0.35  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.79 meV, min. impr. -0.18 meV\n"],["#", "     hydro 5 g 28.4\n"],["#", "     hydro 6 h 12.8\n"],["#", "     hydro 2 p 1\n"],["#", "     hydro 6 f 20\n"],["#", "     hydro 7 d 9.6\n"],["#", "     hydro 3 s 1.8  \n"],]},
"Co":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Co atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Co
#     global species definitions
    nucleus      27
    mass         58.933195
#
    l_hartree    4
#
    cut_pot      3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base        52 5.0
    radial_multiplier  1
    angular_grids       specified       
      division   0.4668   50
      division   0.8401  110
      division   1.1973  194
      division   1.4237  302
#      division   1.5981  434
#      division   1.7961  590
#      division   1.9829  770
#      division   2.0231  974
#      division   2.4367 1202
#      outer_grid   974
      outer_grid   302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      3  p   6.
    valence      3  d   7.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      3  p   6.
    ion_occ      3  d   6.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.8, 2.0, 2.5, 3.5 Ang
#
################################################################################
""",
1:
[[None, "#  \"First tier\" (improvements: -167.79 meV ...  -15.31 meV)\n"],[" ", "    hydro 3 p 5.8\n"],[" ", "    hydro 4 f 8.2\n"],[" ", "    hydro 3 d 5.4\n"],["#", "     hydro 5 g 12\n"],[" ", "    ionic 4 s auto\n"],],
2:
[[None, "#  \"Second tier\" (improvements: -8.83 meV ... -0.89 meV)\n"],["#", "     ionic 4 p auto\n"],["#", "     hydro 6 h 16.4\n"],["#", "     hydro 4 d 5.6\n"],["#", "     hydro 4 f 17.2\n"],["#", "     hydro 1 s 0.75\n"],],
3:
[[None, "#  \"Third tier\" (improvements: -1.03 meV ... -0.06 meV)\n"],["#", "     hydro 4 d 7.8\n"],["#", "     hydro 2 p 5.8\n"],["#", "     hydro 4 f 8\n"],["#", "     hydro 5 g 11.6\n"],["#", "     hydro 4 s 4.3\n"],["#", "     hydro 6 h 14.4\n"],],
4:
[[None, "#  \"Fourth tier\" (minor improvements)\n"],["#", "     hydro 5 f 16\n"],["#", "     hydro 5 d 8\n"],["#", "     hydro 4 p 10\n"],["#", "     hydro 5 s 7.4\n"],]},
"In":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for In atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        In
#     global species definitions
    nucleus             49
    mass                114.818
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         62 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.1831  110
      division   0.9161  194
      division   1.0115  302
#      division   1.1156  434
#      division   1.1524  590
#      division   1.2296  770
#      division   7.0005  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   2.
    valence      5  p   1.
    valence      4  d  10.
#     ion occupancy
    ion_occ     5  s   1.
    ion_occ     5  p   0.
    ion_occ     4  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.15 A, 2.50 A, 3.00 A, 3.75 A, 4.75 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -128.95  meV, min. impr. -24.61 meV\n"],[" ", "    hydro 3 p 2.1\n"],["#", "     hydro 4 f 7.6\n"],[" ", "    hydro 3 d 3.3\n"],[" ", "    hydro 3 s 2.9\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -11.49 meV, min. impr. -0.63 meV\n"],["#", "     hydro 5 g 10\n"],["#", "     hydro 5 p 5.2\n"],["#", "     hydro 4 f 20.8\n"],["#", "     hydro 6 h 13.6\n"],["#", "     hydro 5 f 7.8\n"],["#", "     hydro 4 d 4.3\n"],["#", "     hydro 4 s 3.7   \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.88 meV, min. impr. -0.10 meV\n"],["#", "     hydro 2 p 1.4\n"],["#", "     hydro 5 s 6\n"],["#", "     hydro 5 g 9.2\n"],["#", "     hydro 3 d 2.5\n"],["#", "     hydro 6 h 12.4\n"],["#", "     hydro 5 d 8.2\n"],["#", "     hydro 4 f 40.8\n"],],
5:
[[None, "#  Further functions that fell out of the optimization: -0.08 meV and below\n"],["#", "     hydro 6 p 0.45\n"],["#", "     hydro 4 f 0.1\n"],]},
"P":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2010
#
#  Suggested "light" defaults for P atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        P
#     global species definitions
    nucleus             15
    mass                30.973762
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         43 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.5527   50
      division   0.8801  110
      division   1.1447  194
      division   1.3165  302
#      division   1.4113  434
#      division   1.4781  590
#      division   1.5482  770
#      division   1.5845  974
#      division   2.2606 1202
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      3  s   2.
    valence      3  p   3.
#     ion occupancy
    ion_occ      3  s   1.
    ion_occ      3  p   2.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.625 A, 1.875 A, 2.5 A, 3.25 A, 4.0 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -726.20 meV to -35.91 meV\n"],[" ", "    ionic 3 d auto\n"],[" ", "    ionic 3 p auto\n"],["#", "     hydro 4 f 6.2\n"],["#", "     hydro 5 g 8.6\n"],[" ", "    ionic 3 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -16.02 meV to -1.71 meV\n"],["#", "     hydro 4 d 6.2\n"],["#", "     hydro 4 p 9.2\n"],["#", "     hydro 5 f 9.8\n"],["#", "     hydro 1 s 0.7\n"],["#", "     hydro 5 g 13.2\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -1.82 meV to -0.20 meV\n"],["#", "     hydro 3 p 2.5\n"],["#", "     hydro 4 d 6.4\n"],["#", "     hydro 5 f 11.2\n"],["#", "     hydro 2 s 1.5\n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.91 meV to -0.17 meV\n"],["#", "     hydro 3 d 16.8\n"],["#", "     hydro 5 g 18\n"],["#", "     hydro 4 p 4.5\n"],["#", "     hydro 3 s 2.1\n"],],
5:
[[None, "#  Further basis functions that fell out of the optimization - < -0.09 meV\n"],["#", "     hydro 4 p 10.4\n"],["#", "     hydro 4 d 17.6\n"],["#", "     hydro 4 s 11.2\n"],]},
"Tc":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "tight" defaults for Tc atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Tc
#     global species definitions
    nucleus             43
    mass                98
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         60 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.4840   50
      division   0.9061  110
      division   1.2286  194
      division   1.6333  302
#      division   1.9054  434
#      division   1.9732  590
#      division   2.0439  770
#      division   2.0806  974
#      division   2.7039 1202
#      outer_grid   974
      outer_grid   302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   1.
    valence      4  p   6.
    valence      4  d   6.
#     ion occupancy
    ion_occ     5  s   0.
    ion_occ     4  p   6.
    ion_occ     4  d   5.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.70 A, 1.915 A, 2.375 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\"  - max. impr. -556.71  meV, min. impr. -22.50 meV\n"],[" ", "    hydro 4 f 8.6\n"],[" ", "    ionic 4 d auto\n"],[" ", "    ionic 5 p auto\n"],["#", "     hydro 5 g 12.4\n"],[" ", "    ionic 5 s auto    \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -27.10  meV, min. impr. -0.98 meV\n"],["#", "     hydro 4 f 16\n"],["#", "     hydro 6 h 17.2\n"],["#", "     hydro 4 f 5.8\n"],["#", "     hydro 4 d 4.5\n"],["#", "     hydro 4 p 5.2\n"],["#", "     hydro 5 g 10.8\n"],["#", "     hydro 5 s 6.2    \n"],],
3:
[[None, "#  \"Third tier\"  - max. impr. -2.65 meV, min. impr. -0.20 meV\n"],["#", "     hydro 4 f 32.4\n"],["#", "     hydro 6 h 14.4\n"],["#", "     hydro 4 d 13.2\n"],["#", "     hydro 5 p 11.2\n"],["#", "     hydro 1 s 1.5  \n"],],
4:
[[None, "#  \"Fourth tier\"  - max. impr. -0.28 meV, min. impr. -0.14 meV\n"],["#", "     hydro 5 f 16.4\n"],["#", "     hydro 4 d 12\n"],["#", "     hydro 4 p 6.8\n"],["#", "     hydro 3 d 2.4\n"],["#", "     hydro 5 g 19.6\n"],["#", "     hydro 2 s 2.8\n"],],
5:
[[None, "#  Further functions - -0.13 meV and below\n"],["#", "     hydro 5 f 32\n"],]},
"Sn":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Sn atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Sn
#     global species definitions
    nucleus             50
    mass                118.710
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         63 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.1666  110
      division   0.9058  302
#      division   0.9669  434
#      division   1.0315  590
#      division   1.0999  770
#      division   3.0459  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   2.
    valence      5  p   2.
    valence      4  d  10.
#     ion occupancy
    ion_occ     5  s   1.
    ion_occ     5  p   1.
    ion_occ     4  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.10 A, 2.40 A, 3.75 A, 3.50 A, 4.50 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -189.53  meV, min. impr. -22.71 meV\n"],[" ", "    hydro 2 p 1.3\n"],[" ", "    hydro 3 d 3.7\n"],["#", "     hydro 4 f 7.4\n"],[" ", "    ionic 5 s auto\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -15.73 meV, min. impr. -0.95 meV\n"],["#", "     hydro 5 g 10.4\n"],["#", "     hydro 4 p 6\n"],["#", "     hydro 4 f 20\n"],["#", "     hydro 3 d 4.3\n"],["#", "     hydro 6 h 14.4\n"],["#", "     hydro 4 f 5.6\n"],["#", "     hydro 3 s 2.4\n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.66 meV, min. impr. -0.09 meV\n"],["#", "     hydro 5 g 9.2\n"],["#", "     hydro 3 p 2.6\n"],["#", "     hydro 3 d 7.2\n"],["#", "     hydro 6 h 12.4\n"],["#", "     hydro 5 f 38\n"],["#", "     hydro 1 s 0.55  \n"],],
4:
[[None, "#  \"Fourth tier\" - max. impr. -0.13 meV, min. impr. -0.04 meV\n"],["#", "     hydro 4 p 8.4\n"],["#", "     hydro 4 d 8\n"],["#", "     hydro 6 p 2.1   \n"],["#", "     hydro 5 f 8.6\n"],["#", "     hydro 1 s 4.2   \n"],]},
"Es":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "safe" defaults for Es atom (to be pasted into control.in file)
#
#  Constructed for dimers: 1.93, 2.29, 2.625, 3.125, 4.0 AA
#
################################################################################
  species        Es
#     global species definitions
    nucleus             99
    mass                252
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         78 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.0871  110
      division   0.1221  194
      division   0.1398  302
#      division   0.1793  434
#      division   0.9565  590
#      division   1.0799  770
#      division   7.7672  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   0.
    valence      5  f  11.
#     ion occupancy
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f   10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 6 d  auto
""",
1:
[[None, "#  \"First tier\" - max. impr. -637.91 meV, min. impr. -18.41 meV\n"],[" ", "    hydro 3 d 5.2\n"],[" ", "    hydro 5 g 12.4\n"],[" ", "    hydro 4 f 8\n"],[" ", "    hydro 2 p 1.5\n"],[" ", "    hydro 4 s 4.4  \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -40.33 meV, min. impr. -1.59 meV\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 3 d 3.5\n"],["#", "     hydro 4 f 5.2\n"],["#", "     hydro 5 g 28.4\n"],["#", "     hydro 4 p 9.2 \n"],["#", "     hydro 5 s 6.0 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -3.50 meV, min. impr. -0.39 meV\n"],["#", "     hydro 5 g 9.2 \n"],["#", "     hydro 6 h 15.2\n"],["#", "     hydro 7 d 18.8\n"],["#", "     hydro 4 p 6\n"],["#", "     hydro 5 f 10.8\n"],["#", "     hydro 5 g 52.4\n"],["#", "     ionic 7 s auto\n"],[None, "#  A fourth tier could be added if required.\n"],]},
"Er":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Er atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Er
#     global species definitions
    nucleus        68
    mass           167.259
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    69  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.1015  110
      division   0.1349  194
      division   0.8600  302
#      division   0.9314  434
#      division   1.0079  590
#      division   1.1114  770
#      division   3.2637  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   0.
    valence      4  f  12.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f  11.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.025, 2.5, 3.125, 4.1, 5.0 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 5 d  auto
""",
1:
[[None, "#  \"First tier\" - improvements: -386.89 meV to -12.16 meV\n"],[" ", "    ionic 5 d auto\n"],[" ", "    hydro 4 f 7.4\n"],[" ", "    hydro 2 p 1.2\n"],[" ", "    hydro 5 g 11.2\n"],[" ", "    hydro 4 s 4.0   \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -12.67 meV to -0.39 meV\n"],["#", "     hydro 3 d 2.9\n"],["#", "     hydro 6 h 15.2\n"],["#", "     hydro 4 f 4.6\n"],["#", "     hydro 5 p 5.4\n"],["#", "     hydro 5 g 24\n"],["#", "     hydro 2 s 4.5  \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -1.71 meV, min. impr. -0.18 meV\n"],["#", "     hydro 5 g 7.6\n"],["#", "     hydro 2 p 1.6\n"],["#", "     hydro 6 h 12\n"],["#", "     hydro 3 d 5.2\n"],["#", "     hydro 5 p 6.6\n"],["#", "     ionic 4 f auto\n"],["#", "     hydro 1 s 0.30 \n"],]},
"Tb":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Tb atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Tb
#     global species definitions
    nucleus        65
    mass           158.92535
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    68  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.0876  110
      division   0.1343  194
      division   0.7135  302
#      division   0.8085  434
#      division   0.9322  590
#      division   1.0509  770
#      division   3.0016  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      6  s   2.
    valence      5  p   6.
    valence      5  d   0.
    valence      4  f   9.
#     ion occupancy
    ion_occ      6  s   1.
    ion_occ      5  p   6.
    ion_occ      5  d   0.
    ion_occ      4  f   8.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.825, 2.16, 2.625, 3.375, 4.1, 5.0
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 5 d  auto
""",
1:
[[None, "#  \"First tier\" - improvements: -782.75 meV to -15.06 meV\n"],[" ", "    hydro 3 d 5.4\n"],[" ", "    hydro 4 f 8.2\n"],[" ", "    hydro 2 p 1.4\n"],[" ", "    hydro 5 g 12.4\n"],[" ", "    hydro 4 s 4.0   \n"],],
2:
[[None, "#  \"Second tier\" - improvements: -36.08 meV to -0.43 meV\n"],["#", "     hydro 4 d 3.3\n"],["#", "     hydro 6 h 16.4\n"],["#", "     hydro 4 f 5\n"],["#", "     hydro 5 g 9\n"],["#", "     hydro 5 d 14.4\n"],["#", "     ionic 5 p auto\n"],["#", "     hydro 1 s 0.35 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -3.40 meV, min. impr. -0.23 meV\n"],["#", "     hydro 5 g 28.4\n"],["#", "     hydro 6 h 14.8\n"],["#", "     hydro 4 p 3.7\n"],["#", "     hydro 4 f 6.2\n"],["#", "     hydro 4 f 18.8\n"],["#", "     hydro 4 d 10.4\n"],["#", "     ionic 6 s auto \n"],],
4:
[[None, "#  \"Fourth tier\" - impr. -0.25 meV and below\n"],["#", "     hydro 6 p 14\n"],["#", "     hydro 5 f 15.2\n"],["#", "     hydro 5 g 20\n"],["#", "     hydro 3 d 1.4\n"],["#", "     hydro 1 s 3.6  \n"],]},
"F":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for F atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        F
#     global species definitions
    nucleus             9
    mass                18.9984032
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         37 5.0
    radial_multiplier   1
    angular_grids specified 
      division   0.4014  110
      division   0.5291  194
      division   0.6019  302
#      division   0.6814  434
#      division   0.7989  590
#      division   0.8965  770
#      division   1.3427  974
#      outer_grid   974
      outer_grid   302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      2  s   2.
    valence      2  p   5.
#     ion occupancy
    ion_occ      2  s   1.
    ion_occ      2  p   4.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.2 A, 1.418 A, 1.75 A, 2.25 A, 3.25 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -149.44 meV to -45.88 meV\n"],[" ", "    hydro 2 p 1.7\n"],[" ", "    hydro 3 d 7.4\n"],[" ", "    hydro 3 s 6.8\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -12.96 meV to -1.56 meV\n"],["#", "     hydro 4 f 11.2\n"],["#", "     ionic 2 p auto\n"],["#", "     hydro 1 s 0.75\n"],["#", "     hydro 4 d 8.8\n"],["#", "     hydro 5 g 16.8\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.58 meV to -0.05 meV\n"],["#", "     hydro 3 p 6.2\n"],["#", "     hydro 3 s 3.2\n"],["#", "     hydro 4 f 9.6\n"],["#", "     hydro 3 s 19.6\n"],["#", "     hydro 4 d 8.6\n"],["#", "     hydro 5 g 14.4\n"],],
5:
[[None, "# Further basis functions: -0.05 meV and below\n"],["#", "     hydro 3 p 4.2\n"],]},
"Xe":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Xe atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Xe
#     global species definitions
    nucleus        54
    mass           131.293
#
    l_hartree      4
#
    cut_pot        3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    64  5.0
    radial_multiplier  1
    angular_grids specified
      division   0.7862  110
      division   1.1196  194
      division   1.4850  302
#      division   1.6329  434
#      division   1.6858  590
#      division   1.7978  770
#      division   1.9188  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   2.
    valence      5  p   6.
    valence      4  d  10.
#     ion occupancy
    ion_occ      5  s   1.
    ion_occ      5  p   5.
    ion_occ      4  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 3.0, 3.5, 4.06, 4.50, 5.25 Ang
#
#  Noble gas symmetric dimers converge quickly in DFT. If you find that
#  you require a larger basis than tier 2, please contact us - VB, FHI.
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -33.50 meV to -0.77 meV\n"],[" ", "    hydro 3 d 3.8\n"],["#", "     hydro 4 f 6.2\n"],[" ", "    ionic 6 p auto\n"],[" ", "    ionic 6 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -0.75 meV to -0.05 meV\n"],["#", "     hydro 5 g 8.4\n"],["#", "     ionic 4 f auto\n"],["#", "     hydro 3 d 3.1\n"],["#", "     hydro 5 f 6.8\n"],["#", "     hydro 6 h 10.8\n"],["#", "     hydro 5 p 6.2\n"],["#", "     hydro 1 s 12.8\n"],],
3:
[[None, "#  \"Third tier\" - no more improvements > 0.05 meV\n"],[None, " \n"],]},
"Fm":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Fm atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Fm
#     global species definitions
    nucleus             100
    mass                257
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         78 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.0735  110
      division   0.1138  194
      division   0.1445  302
#      division   0.2429  434
#      division   1.0077  590
#      division   1.0799  770
#      division   7.7672  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   0.
    valence      5  f  12.
#     ion occupancy
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f   11.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.98, 2.375, 2.75, 3.25, 4.25 AA
#
################################################################################
#
#  Necessary addition to the minimal basis
   confined 6 d  auto
""",
1:
[[None, "#  \"First tier\" - max. impr. -424.25 meV, min. impr. -12.95 meV\n"],[" ", "    hydro 3 d 5.2\n"],[" ", "    hydro 5 g 12\n"],[" ", "    hydro 4 f 8\n"],[" ", "    hydro 2 p 1.5\n"],[" ", "    hydro 4 s 4.6  \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -27.52  meV, min. impr. -0.98 meV\n"],["#", "     hydro 6 h 15.6 # -27.52 meV; switched with s above\n"],["#", "     hydro 3 d 3.6\n"],["#", "     hydro 4 f 5.4\n"],["#", "     hydro 5 g 27.2\n"],["#", "     hydro 2 p 2.3 \n"],["#", "     hydro 5 s 5.8 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -2.07 meV, min. impr. -0.30 meV\n"],["#", "     hydro 5 g 10\n"],["#", "     hydro 6 h 15.2\n"],["#", "     hydro 5 d 12.8\n"],["#", "     hydro 4 p 6.4\n"],["#", "     hydro 5 g 52.4\n"],["#", "     hydro 4 f 9.4\n"],["#", "     hydro 1 s 14.8\n"],[None, "#  Could add further functions if required.\n"],]},
"Emptium":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2012
#
#  This species defaults file defines an empty site with no basis functions
#  or nuclear potential, just integration grids.
#
#  We specify the default grids of Hydrogen, but this assumption should be checked
#  by any user. 
#
#  We do need a cut_pot definition, as this is tied into the construction
#  of our integration weights.
#
################################################################################
  species        Emptium
#     global species definitions
    nucleus             0
    mass                0
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#     
    radial_base         24 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.2421   50
      division   0.3822  110
      division   0.4799  194
      division   0.5341  302
#      division   0.5626  434
#      division   0.5922  590
#      division   0.6542  770
#      division   0.6868 1202
#      outer_grid  770
      outer_grid  302
#
    include_min_basis .false.
"""},
"Rh":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Rh atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Rh
#     global species definitions
    nucleus             45
    mass                102.90550
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         61 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.4929   50
      division   0.8959  110
      division   1.2091  194
      division   1.6265  302
#      division   1.8928  434
#      division   1.9931  590
#      division   2.0637  770
#      division   2.6689 1202
#      outer_grid   974
      outer_grid   302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   1.
    valence      4  p   6.
    valence      4  d   8.
#     ion occupancy
    ion_occ     5  s   0.
    ion_occ     4  p   6.
    ion_occ     4  d   7.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.80 A, 2.10 A, 2.50 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\"  - max. impr. -246.65  meV, min. impr. -25.24 meV\n"],[" ", "    hydro 4 f 8.6\n"],[" ", "    ionic 5 p auto\n"],[" ", "    ionic 4 d auto\n"],["#", "     hydro 5 g 11.6\n"],[" ", "    hydro 3 s 2.5\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -10.97 meV, min. impr. -0.96 meV\n"],["#", "     hydro 4 f 21.2\n"],["#", "     hydro 6 h 16\n"],["#", "     hydro 5 f 8.2\n"],["#", "     hydro 4 d 4.1\n"],["#", "     hydro 3 p 3.3\n"],["#", "     hydro 5 g 10.4\n"],["#", "     hydro 5 s 9\n"],],
3:
[[None, "#  \"Third tier\"  - max. impr. -0.62 meV, min. impr. -0.16 meV\n"],["#", "     hydro 5 f 20\n"],["#", "     hydro 3 d 2.4\n"],["#", "     hydro 6 h 14.8\n"],["#", "     hydro 3 s 3.2\n"],["#", "     hydro 4 f 45.2\n"],["#", "     hydro 5 p 10.81\n"],],
4:
[[None, "#  \"Fourth tier\"  - max. impr. -0.15 meV, min. impr. -0.06 meV\n"],["#", "     hydro 5 d 14.8\n"],["#", "     hydro 4 s 7.2\n"],["#", "     hydro 4 p 5\n"],["#", "     hydro 2 p 0.1\n"],["#", "     hydro 5 g 7.4\n"],]},
"Rb":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Rb atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#  The onset of the cutoff pot'l is set to 6 A by default, because the neutral
#  Rb atom is a large atom. However, this is very expensive. The radius should be
#  much smaller in real-world situations, where Rb will be ionic. Please check 
#  and reduce the cutoff radius explicitly.
#
################################################################################
  species          Rb
#     global species definitions
    nucleus        37
    mass           85.4678
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    57  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.1250  110
      division   0.9394  194
      division   1.1230  302
#      division   1.2051  434
#      division   1.2929  590
#      division   1.3869  770
#      division   7.0005  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   1.
    valence      4  p   6.
    valence      3  d  10.
#     ion occupancy
    ion_occ      5  s   0.
    ion_occ      4  p   6.
    ion_occ      3  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.45, 3.00, 4.00, 5.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -104.04 meV to -9.25 meV\n"],[" ", "    hydro 3 d 4.5\n"],[" ", "    hydro 3 p 2.5\n"],["#", "     hydro 4 f 6.6\n"],[" ", "    hydro 4 s 2.9\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -4.35 meV to -0.89 meV\n"],["#", "     ionic 4 d auto\n"],["#", "     hydro 5 g 9.2\n"],["#", "     hydro 2 s 2.4\n"],["#", "     hydro 5 p 8\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.76 meV to -0.13 meV\n"],["#", "     hydro 4 d 7.6\n"],["#", "     hydro 4 f 4.2\n"],["#", "     hydro 4 f 18\n"],["#", "     hydro 6 h 12.8\n"],["#", "     hydro 4 p 2.9\n"],["#", "     hydro 1 s 0.4\n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.07 meV and lower.\n"],["#", "     hydro 5 g 6.2\n"],["#", "     hydro 2 s 1.1\n"],["#", "     hydro 5 d 9.2\n"],]},
"Sr":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Sr atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species          Sr
#     global species definitions
    nucleus        38
    mass           87.62
#
    l_hartree      4
#
    cut_pot        4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base    57  5.5
    radial_multiplier  1
    angular_grids specified
      division   0.6981  110
      division   0.9394  194
      division   1.1230  302
#      division   1.2482  434
#      division   1.3391  590
#      division   1.4365  770
#      division   7.0005  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   2.
    valence      4  p   6.
    valence      3  d  10.
#     ion occupancy
    ion_occ      5  s   1.
    ion_occ      4  p   6.
    ion_occ      3  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.75, 3.50, 4.40, 5.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -289.57 meV to -14.02 meV\n"],[" ", "    ionic 4 d auto\n"],[" ", "    ionic 5 p auto\n"],["#", "     hydro 4 f 5.6\n"],[" ", "    ionic 5 s auto\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -4.95 meV to -0.45 meV\n"],["#", "     hydro 5 g 7.4\n"],["#", "     hydro 4 d 4.4\n"],["#", "     hydro 3 p 3.3\n"],["#", "     hydro 6 h 10.4\n"],["#", "     hydro 5 s 4.9\n"],["#", "     hydro 5 f 13.2\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -0.38 meV to -0.11 meV\n"],["#", "     hydro 6 p 4.8\n"],["#", "     hydro 5 f 6\n"],["#", "     hydro 2 p 1.2\n"],["#", "     hydro 1 s 0.55\n"],["#", "     hydro 5 d 3.6   \n"],],
4:
[[None, "#  \"Fourth tier\" - improvements: -0.12 meV and lower.\n"],["#", "     hydro 5 p 5.2\n"],["#", "     hydro 4 f 14.8\n"],["#", "     hydro 5 g 7.6\n"],["#", "     hydro 4 p 4.5\n"],["#", "     hydro 5 d 5.4\n"],["#", "     hydro 6 s 6.8   \n"],]},
"Ag":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ag atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Ag
#     global species definitions
    nucleus             47
    mass                107.8682
#
    l_hartree           4
#
    cut_pot             3.5  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         62 5.0
    radial_multiplier   1
    angular_grids specified
      division   0.5617   50
      division   0.9788  110
      division   1.2700  194
      division   1.5678  302
#      division   2.1195  434
#      division   2.1949  590
#      division   2.2741  770
#      division   2.8497 1202
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      5  s   1.
    valence      4  p   6.
    valence      4  d  10.
#     ion occupancy
    ion_occ     5  s   0.
    ion_occ     4  p   6.
    ion_occ     4  d   9.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.1 A, 2.45 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -144.99  meV, min. impr. -3.42 meV\n"],[" ", "    ionic 5 p auto\n"],[" ", "    hydro 4 f 7.6\n"],[" ", "    hydro 3 s 2.6\n"],["#", "     hydro 5 g 9.8\n"],[" ", "    hydro 4 d 8.4\n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -3.10  meV, min. impr. -0.64 meV\n"],["#", "     hydro 5 f 16.8\n"],["#", "     hydro 6 h 13.2\n"],["#", "     hydro 4 p 5\n"],["#", "     hydro 4 d 4.3\n"],["#", "     hydro 5 s 17.2\n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -0.48  meV, min. impr. -0.12 meV\n"],["#", "     hydro 4 f 19.2\n"],["#", "     hydro 5 f 8.4\n"],["#", "     hydro 6 p 12\n"],["#", "     hydro 5 g 12.8\n"],["#", "     hydro 5 d 8.4\n"],["#", "     hydro 5 s 5.8\n"],["#", "     hydro 6 h 15.2\n"],]},
"Ge":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Ge atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
################################################################################
  species        Ge
#     global species definitions
    nucleus             32
    mass                72.64
#
    l_hartree           4
#
    cut_pot             3.5          1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         54 5.0
    radial_multiplier   1
    angular_grids       specified
      division   0.0947  110
      division   0.1314  194
      division   0.7746  302
#      division   0.8710  434
#      division   0.9770  590
#      division   1.1356  770
#      division   2.6430  974
#      outer_grid  974
      outer_grid  302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      4  s   2.
    valence      4  p   2.
    valence      3  d  10.
#     ion occupancy
    ion_occ      4  s   1.
    ion_occ      4  p   1.
    ion_occ      3  d  10.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 1.80 A, 2.00 A, 2.35 A, 3.00 A, 4.00 A
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - improvements: -329.04 meV to -37.61 meV \n"],[" ", "    hydro 2 p 1.4\n"],[" ", "    hydro 3 d 4.3\n"],["#", "     hydro 4 f 7.4\n"],[" ", "    hydro 3 s 3.4\n"],],
2:
[[None, "#  \"Second tier\" - improvements: -13.91 meV to -1.23 meV\n"],["#", "     hydro 5 g 10.8\n"],["#", "     hydro 3 d 2.5\n"],["#", "     hydro 3 p 3.3\n"],["#", "     hydro 4 f 12\n"],["#", "     hydro 6 h 15.6\n"],["#", "     hydro 3 s 7.2\n"],],
3:
[[None, "#  \"Third tier\" - improvements: -1.47 meV to -0.40 meV\n"],["#", "     hydro 3 d 5.8\n"],["#", "     hydro 4 f 4.3\n"],["#", "     hydro 5 g 11.6\n"],["#", "     hydro 5 s 14.8\n"],["#", "     hydro 4 p 3.9\n"],],
4:
[[None, "#  \"Fourth tier\"  -improvements: -0.39 meV to -0.11 meV\n"],["#", "     hydro 4 f 23.2\n"],["#", "     hydro 2 s 6.2\n"],["#", "     hydro 5 d 9.8\n"],["#", "     hydro 5 p 6\n"],["#", "     hydro 6 h 14.8\n"],],
5:
[[None, "#  Further functions - -0.13 meV and below\n"],["#", "     hydro 5 f 9.6\n"],]},
"Pa":
{"head":
"""################################################################################
#
#  FHI-aims code project
#  VB, Fritz-Haber Institut, 2009
#
#  Suggested "light" defaults for Pa atom (to be pasted into control.in file)
#  Be sure to double-check any results obtained with these settings for post-processing,
#  e.g., with the "tight" defaults and larger basis sets.
#
#
################################################################################
  species        Pa
#     global species definitions
    nucleus             91
    mass                231.03588
#
    l_hartree           4
#
    cut_pot             4.0  1.5  1.0
    basis_dep_cutoff    1e-4
#
    radial_base         76 5.5
    radial_multiplier   1
    angular_grids specified
      division   0.0746  110
      division   0.1252  194
      division   0.1687  302
#      division   0.1905  434
#      division   0.9942  590
#      division   1.0865  770
#      division   7.7724  974
#      outer_grid  974
      outer_grid 302
################################################################################
#
#  Definition of "minimal" basis
#
################################################################################
#     valence basis states
    valence      7  s   2.
    valence      6  p   6.
    valence      6  d   1.
    valence      5  f   2.
#     ion occupancy - 3+ ion, analogous to Ce
    ion_occ     7  s    1.
    ion_occ     6  p    6.
    ion_occ     6  d    0.
    ion_occ     5  f    1.
################################################################################
#
#  Suggested additional basis functions. For production calculations, 
#  uncomment them one after another (the most important basis functions are
#  listed first).
#
#  Constructed for dimers: 2.04, 2.30, 3.00, 3.75, 4.75 AA
#
################################################################################
""",
1:
[[None, "#  \"First tier\" - max. impr. -950.25 meV, min. impr. -33.92 meV\n"],[" ", "    hydro 3 d 2.5\n"],[" ", "    hydro 5 g 10.8\n"],[" ", "    hydro 2 p 1.5\n"],[" ", "    hydro 4 f 8\n"],[" ", "    hydro 4 s 4.6  \n"],],
2:
[[None, "#  \"Second tier\" - max. impr. -105.23 meV, min. impr. -2.37 meV\n"],["#", "     hydro 6 h 14\n"],["#", "     hydro 4 f 4\n"],["#", "     hydro 3 d 3.2\n"],["#", "     hydro 5 g 11.2\n"],["#", "     hydro 3 p 2.5\n"],["#", "     hydro 5 s 5.4 \n"],],
3:
[[None, "#  \"Third tier\" - max. impr. -8.25 meV, min. impr. -0.57 meV\n"],["#", "     hydro 4 f 7\n"],["#", "     hydro 6 h 14.4\n"],["#", "     hydro 5 g 33.2\n"],["#", "     hydro 3 d 1.9\n"],["#", "     hydro 5 g 5.6\n"],["#", "     hydro 6 p 17.2\n"],["#", "     hydro 6 s 19.2\n"],[None, "#  A fourth tier could be added if needed.\n"],]},
}
