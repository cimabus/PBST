#-------------------------------------------------------------------------------
# espressioni regolari per espressioni aritmetiche
#
# sono comprese anche le rappresentazioni dei falsi negativi
# qualora vengano rifiutate dall'interprete
#-------------------------------------------------------------------------------
# https://regex101.com/r/oR1nl1/1
EXP_CON_PARENTESI = r"^.*([{}\[\]()]).*$"
# { 3 - 2 } + [ ( 5 + 2 ) * 4 ] / { 8 + [ 5+4 } * -1 }
# { 3 - 2 } + [ ( 5 + 2 ) * 4 ] / { 8 + [ 5+4 } * -1
# { 3 - 2 } + [ ( 5 + 2 ) * 4 ] / { 8 + [ 5+4  * -1
# { 3 - 2 } + [ ( 5 + 2 ) * 4 ] / { 8 +  5+4  * -1
#  3 - 2 } +   5 + 2  * 4  /  8 +  5+4  * -1
#  3 - 2  +   5 + 2  * 4  /  8 +  5+4  * -1
#-------------------------------------------------------------------------------
# https://regex101.com/r/jfCXDu/2
EXP_SOLO_NATURALI = r"^(\x20*\d+\x20*([\-+*]\x20*\d+\x20*)+[\-+*]*)*$"
# 3*1+2
# 33
# 44+2
#-------------------------------------------------------------------------------
# https://regex101.com/r/YHIUFU/1
EXP_SENZA_DIV = r"^(([+\-\s]*\d+\s*)+|[*+\-]*)*$"
# +  +  - + -232332  - 3 - - 4 *  - 1 +2     + 3
# Out[9999] = 232330
#-------------------------------------------------------------------------------
# https://regex101.com/r/OpaecZ/1
EXP_CON_DIV = r"^(([+\-\s]*\d+\s*)+|[*+\-/]*)*$"
# +  +  - + -232332  - 3 / 3 * 3 - - 4 *  - 1 +2     + 3
# Out[9999] = 232330.0
#-------------------------------------------------------------------------------
# https://regex101.com/r/nck8eh/2
EXP_RIS_INT = r"^Out\[\d+\]:\s*(-?\d+)\s*$"
# Out[9999] = 232330
#-------------------------------------------------------------------------------
# https://regex101.com/r/z2qbAc/2
EXP_RIS_FLOAT = r"^Out\[\d+\]:\s*(-?\d+\.\d+)\s*$"
# Out[9999] = 232330.0
#-------------------------------------------------------------------------------
# https://regex101.com/r/TdZ1Mk/3
#
EXP_CON_DIV_TRONCATA = r"^(([+\-\x20]*\d+\x20*)+|//|\*|)*$"
# 7 // 3 + 4*3-4// -7
# 1 + 4 - 5 # falso positivo
# #-------------------------------------------------------------------------------
# https://regex101.com/r/cL3WlR/1
EXP_UND_CON_DIV_IN_MOD = r"^_(([+\-\s]*\d+\s*)+|\s*%\s*|([*+\-])*)*$"
# _ + 17 % 5
# #-------------------------------------------------------------------------------
# https://regex101.com/r/i6ML5Y/2
EXP_ASS_INT = r"^([a-zA-Z].*\x20*=\x20*([0-9]+)\x20*)$"
# base = 16
#---------------------------------------------------------------------------------
# https://regex101.com/r/DGY4nb/3
EXP_ASS_EXP_INT = r"^(?:[a-zA-Z].*\x20*=)([\x20*0-9\-+*/]*)$"
# altezza = 3 + 1
#---------------------------------------------------------------------------------
# https://regex101.com/r/lNjAs6/3
EXP_CON_VARIABILI = r"^([+\-\x20]*[a-zA-Z_]+[0-9a-zA-Z_]*\x20*[\-*+/]*\x20*)*$"
# base * altezza
# - + +aew3_   * / + err3
# 1 + 2*3 * -4 -2
#----------------------------------------------------------------------------------
# https://regex101.com/r/v0ySMV/4
EXP_SOM_SOT_MOL_DIV_TRONC_MOD = r"^(([\-+\x20]*\d+\x20*)*|[*]|//|%|/|\-*\+*\x20*\d+\x20*|//\-*\+*\x20*\d+\x20*|/\-*\+*\x20*\d+\x20*|%\-*\+*\x20*\d+\x20*|([\-+\x20]*\d+\x20*))*$"
# - 22 + - 33 * 2 / - 4 // - 5 % 6
# -4 + 3 % 4 / 3 * 66 / 3 + 4  % + 5 - 3 / 3
# - 3 / * 3   # invalido il secondo operatore
#----------------------------------------------------------------------------------
# https://regex101.com/r/XQ7yWq/2
EXP_TRACEBACK_NAME_ERROR = r".*Traceback.*\nNameError:.*"
# 1 + 2* -3 * -4 -2
# Out[2]: 23
# base = 16
# altezza = 1 + 2
# base * altezza
# Out[3]: 48
# 1 + 4 *2  -5 -4
# Out[4]: 0
# -3 * -5 / 15
# Out[5]: 1
# -7 * -5 // - + 4
# Out[6]: -9
# _ + 7 % 4
# Out[7]: -6
# 34 / 6 + 1
# Out[8]: 6.666666666666667
# literal_non_ancora_utilizzato
# Traceback (most recent call last):
# NameError: name 'literal_non_ancora_utilizzato' is not defined
#----------------------------------------------------------------------------------
# https://regex101.com/r/YodzAm/3
EXP_LIST_IVA_MSG_ERR = ["calcola iva : iva non presente"
                       ,"calcola iva : prezzo non presente"
                        ,"calcola iva : espressione tassa, cioè 'prezzo * iva' non presente"
                        ,"calcola iva : valore calcolato tassa non presente"
                        ,"calcola iva : espressione costo, cioè 'prezzo + _' non presente"
                        ,"calcola iva : valore costo non presente"
                        ]
EXP_LIST_IVA_PATTERN = [r"iva\x20*=\x20*.*\n"
                        ,r"prezzo\x20*=\x20*.*\n"
                        ,r"prezzo\x20*\*\x20*iva\n|\x20*iva\x20*\*\x20*prezzo\n"
                        ,r"Out\[\d+\]:\x20\d{1,2}\.\d{1,3}\n"
                        ,r"prezzo\x20*\+\x20*_\n|\x20*_\x20*\+\x20*prezzo\n"
                        ,r"Out\[\d+\]:\x20\d{3}\.\d{1,3}\n"
                        ]
# 1 + 2* -3 * -4 -2
# Out[2]: 23
# base = 16
# altezza = 1 + 2
# base * altezza
# Out[3]: 48
# 1 + 4 *2  -5 -4
# Out[4]: 0
# -3 * -5 / 15
# Out[5]: 1
# -7 * -5 // - + 4
# Out[6]: -9
# _ + 7 % 4
# Out[7]: -6
# 34 / 6 + 1
# Out[8]: 6.666666666666667
# literal_non_ancora_utilizzato
# Traceback (most recent call last):
# NameError: name 'literal_non_ancora_utilizzato' is not defined
# iva = 8.5/100
# prezzo = 100
# prezzo * iva
# Out[10]: 8.5
# prezzo + _
# Out[11]: 108.5
#
#----------------------------------------------------------------------------------
