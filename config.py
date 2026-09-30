EDOs = [
    24, 36,      # extended 12TET
    14, 15, 16,  # xenharmonic
    17, 22, 27,  # superpyth
    19, 31, 43,  # meantone
    29,          # good fifth
    34, 41, 53,  # approximate JI
]

EDTs = [
    26, 39,  # extended Bohlen-Pierce
    27, 54,  # stretched 17EDO, 34EDO
    30, 43   # stretched 19EDO, compressed 27EDO
]

ED6s = [ # splits diff between oct and tritave
    44, 88, # less stretched 17EDO, 34EDO
    49, 70, # optimally stretched 19EDO, 43EDO
    57,     # compressed 22EDO
]

Carlos = [  # wendycarlos.com/resources/pitch.html
    ("Alpha", 15.385),
    ("Beta" , 18.809),
    ("Gamma", 34.188),
]

SHOULD_KEYTRACK_FILTER = True
HALVE_FILTER_KT = True

SHOULD_KEYTRACK_EXTRA = False
