import __init__
import unittest
import sys, os
import re
# la import seguente verrà risolta dinamicamente tramite import __init__
# la clausola try serve a evitare l'indicazione statica di unresolved
# per il modulo task
try:
    from task import output_console
except ImportError:
    print('file:', __file__,'dir:',os.path.abspath(os.path.dirname(os.path.dirname(__file__))),sep='\n',end='\n\n')
    sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))

def ricerca_commento(self, regex, pos, msg_err):
    passed = False
    print("pattern:", regex)
    lista = str(output_console.__doc__).split('\n')
    for row in lista:
        print("row:", row)
        matches = re.finditer(regex, row)
        for match_num, match in enumerate(matches, start=pos):
            print("Match {match_num} was found at {start}-{end}: {match}"
                  .format(match_num=match_num,
                          start=match.start(),
                          end=match.end(),
                          match=match.group())
                  )
            for group_num in range(0, len(match.groups())):
                group_num = group_num + 1
                self.assertAlmostEqual("#", match.group(group_num), msg_err)
                print("Group {group_num} found at {start}-{end}: {group}"
                      .format(group_num=group_num,
                              start=match.start(group_num),
                              end=match.end(group_num),
                              group=match.group(group_num))
                      )
                passed = True
    return passed


class TestCase(unittest.TestCase):
    def test_10_commento_inizio_riga(self):
        pattern = r"^(#)#*[\S|\s]*$"
        passed = ricerca_commento(self, pattern, 1, "la riga non inizia con #")
        self.assertTrue(passed, "non esiste commento")

    def test_20_commento_dopo_numero(self):
        pattern = r"^\d+\s*(#)#*.*$"
        passed = ricerca_commento(self, pattern, 1, "la riga col commento non inizia con un numero")
        self.assertTrue(passed, "non esiste commento")

    def test_30_commento_dopo_stringa(self):
        pattern1 = r'^".*"\s*(#)#*.*$'
        msg1 = "la riga col commento non inizia con una stringa tra apici doppi"
        pattern2 = r"^'.*'\s*(#)#*.*$"
        msg2 = "la riga col commento non inizia con una stringa tra apici singoli"
        passed1 = ricerca_commento(self, pattern1, 1, msg1)
        passed2 = ricerca_commento(self, pattern2, 1, msg2)
        not_passed = not passed1 and not passed2
        if not_passed:
            self.assertTrue(False, "non esiste riga di commento con stringa")
