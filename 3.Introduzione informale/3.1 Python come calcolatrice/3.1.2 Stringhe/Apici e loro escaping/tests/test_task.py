import unittest , __init__
from task import outputConsole
import re


def catch_rl_prompt_and_output(pat, src=repr(outputConsole.__doc__.strip("\n").strip()), g2p=1, g2o=2, opts=re.NOFLAG,
                               dbg=False):
    """

    :param pat: pattern registrati su regex101
    :param src: stream in formato repr() escludendo spazi e newline dalla testa e dalla coda
    :param g2p: gruppo del prompt
    :param g2o: gruppo dell'output
    :param opts: NOFLAG per default
    :param dbg: per print di debug
    :return:
    """

    # preleva dalla proprietà __doc__, utilizzando il pat, il prompt e l'output effettuato nella python console
    prompt = None  # comando da eseguire in console
    output = None  # output del comando eseguito
    if dbg: print(
        f"-----\nsrc:\n{src}\n\npattern:\nr\"{pat}\"\n----")  # src deve essere in formato repr() non in formato str(), cioè una sola linea
    matches = re.finditer(pat, src, flags=opts)  # cerca il pat nel src con re options di default
    for matchNum, match in enumerate(matches, start=1):  # matchNum comincia da start
        model2match = r"Match {matchNum} was found at {start}-{end}: {match}"
        if dbg: print(model2match.format(matchNum=matchNum,
                                         start=match.start(),
                                         end=match.end(),
                                         match=match.group()))

        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1  # lo zero è il match
            if matchNum == 1 and groupNum == g2p and prompt is None:
                prompt = match.group(groupNum)
            if matchNum == 1 and groupNum == g2o and output is None:
                output = match.group(groupNum)

            model2group = "Group {groupNum} found at {start}-{end}: {group}"
            if dbg: print(model2group.format(groupNum=groupNum,
                                             start=match.start(groupNum),
                                             end=match.end(groupNum),
                                             group=match.group(groupNum)))

    # test per verificare se la regex ha trovato gli apici alle estrmità con backslsh
    # per riproporre come terminazione l'apice iniziale ( src in formato repr() non str() )
    # es. catch '...\ per ottenere '...' oppure
    #           "...\      ->      "..."
    try:
        if prompt[0] != prompt[-1] and prompt[
            -1] == "\\":  # apici terminale non coincidente: il primo è ' o " ed il terminale è backslash che sostiruisco con quello iniziale
            prompt = prompt.strip("\\")  # tolgo il blackslash
            prompt += prompt[0]  # ed al suo posto inserisco l'apice iniziale
        if output[0] != output[-1] and output[-1] == "\\":  # idem per output
            output = output.strip("\\")
            output += output[0]
    except TypeError:  # se match non effettuato evito la segnlzione
        pass
    if dbg: print(f"prompt: {prompt} \noutput: {output}")
    return (prompt, output)


class TestCase(unittest.TestCase):
    def test_rl_1_1_apici_singoli_e_doppi(self):
        pattern = r"[\'\"].*rl1\.1>{3}\\(.*\\)\'\\nrl1\.1\\(.*\\)\'[\\n]{1,}rl1.2>{3}"  # registrato PBST31211 https://regex101.com/r/rGOtpT/4
        (prompt, output) = catch_rl_prompt_and_output(pattern)
        if prompt is not None and output is not None:
            output_atteso = eval(repr(prompt))
            self.assertEqual(output_atteso, output,
                             msg="prompt:{}\noutput atteso:{}\noutput fornito:{}".format(prompt, output_atteso, output))
        else:
            self.assertTrue(False, "Non rilevato prompt nè output")

    def test_rl_1_2_apici_singoli_e_doppi_invertiti(self):
        pattern = r"[\'\"].*rl1\.2>{3}([\'\"].*[\'\"])[\\n]{1,}rl1\.2\\(.*)\'[\\n]{4,}rl1\.3>{3}"  # registrato PBST31212 https://regex101.com/r/MiytQq/3
        (prompt, output) = catch_rl_prompt_and_output(pattern)
        if prompt is not None and output is not None:
            output_atteso = eval(repr(prompt))
            # gli apici estremi possono essere diversi, quindi li escludo dal controllo
            self.assertEqual(output_atteso[1:-1], output[1:-1],
                             msg="prompt:{}\noutput atteso:{}\noutput fornito:{}".format(prompt, output_atteso, output))
        else:
            self.assertTrue(False, "Non rilevato prompt nè output")

    def test_rl_1_3_apici_singoli_e_doppi_vers2(self):
        pattern = r"[\'\"].*rl1\.3>{3}([\'\"].*[\'\"])\\nrl1\.3\\([\'\"].*).*[\'\"][\\n]*rl1\.4>>>.*[\'\"]"  # registrato PBST31213 https://regex101.com/r/Ryk17f/2
        (prompt, output) = catch_rl_prompt_and_output(pattern)
        if prompt is not None and output is not None:
            output_atteso = eval(repr(prompt))
            # gli apici estremi possono essere diversi, quindi li escludo dal controllo
            self.assertEqual(output_atteso[1:-1], output[1:-1],
                             msg="prompt:{}\noutput atteso:{}\noutput fornito:{}".format(prompt, output_atteso, output))
        else:
            self.assertTrue(False, "Non rilevato prompt nè output")

    def test_rl_1_4_apici_singoli_e_doppi_vers3(self):
        pattern = r"[\'\"].*rl1\.4>{3}[\'\"]*(.*)[\'\"]*\\n+rl1\.4[\'\"]*(.*)[\'\"][\\n]{4,}rl2\.1>{3}.*[\'\"]"  # registrato PBST31214 https://regex101.com/r/2mE9S3/2
        (prompt, output) = catch_rl_prompt_and_output(pattern)
        if prompt is not None and output is not None:
            try:
                output_atteso = eval(repr(prompt))
                self.assertEqual(output_atteso[1:-1], output[1:-1],
                                 msg="prompt:{}\noutput atteso:{}\noutput fornito:{}".format(prompt, output_atteso,
                                                                                             output))
            except AssertionError:
                # ammenocchè siano triple nel prompt e quindi singole nell' output nel caso strippo
                output_atteso2 = output_atteso.strip("\\'")
                output2 = output.strip("\\'")
                self.assertEqual(output_atteso2, output2,
                                 msg="prompt:{}\noutput atteso:{}\noutput fornito:{}".format(prompt, output_atteso,
                                                                                             output))
                pass
        else:
            self.assertTrue(False, "Non rilevato prompt nè output")

    def test_rl_2_1_assegna_stringa_a_variabile_con_stampa(self):
        pattern = r"[\'\"].*rl2\.1>{3}[\'\"]*(.*)[\'\"]*\\n+rl2\.1[\'\"]*(.*)[\'\"]*\\n+rl2\.2>{3}[\'\"]*.*[\'\"]"  # registrato PBST31221 https://regex101.com/r/Cv9avs/2
        (prompt, output) = catch_rl_prompt_and_output(pattern, dbg=True)
        if prompt is not None and output is not None:
            # verifico se viene eseguita perchè sostituisco il newline con il comando multistruzione su stessa linea
            prompt2 = str(prompt).replace("\\'", "\'").replace("\\n", ";").replace(";", "\\n", 1)
            self.assertGreater(prompt2.find("\\n"), 0, "output non multilinea")
            print("exec(prompt) 2.1:")
            exec(prompt2)
        else:
            self.assertTrue(False, "Non rilevato prompt nè output")

    def test_rl_2_2_assegna_stringa_a_variabile_con_richiamo(self):
        pattern = r"[\'\"].*rl2\.2>{3}[\'\"]*(.*)[\'\"]*\\n+rl2\.2[\'\"]*(.*)[\'\"]*.*[\'\"]"  # registrato PBST31222 https://regex101.com/r/emSrz0/1
        (prompt, output) = catch_rl_prompt_and_output(pattern)
        if prompt is not None and output is not None:
            self.assertRaises(NameError, exec, prompt)
            self.assertEqual(1, list(output.splitlines()).__len__(), "output multilinea")
        else:
            self.assertTrue(False, "Non rilevato prompt nè output")

    def test_rl_2_3_print_path_windows(self):
        pattern = r"[\'\"].*rl2\.3>{3}[\'\"]*(.*)[\'\"]*\\n+rl2\.3(.*)[\\n]{2,}rl2\.4>{3}.*[\'\"]*.*[\'\"]"  # registrato PBST31223 https://regex101.com/r/emSrz0/1https://regex101.com/r/zPtA9Z/1
        (prompt, output) = catch_rl_prompt_and_output(pattern)
        if prompt is not None and output is not None:
            try:
                exec(prompt)
                self.assertTrue(False,"prompt non in errore")
            except SyntaxError:
                pass
                self.assertRaises(SyntaxError, exec, prompt)
                self.assertEqual(0, str(output).find("SyntaxError"), "Non trovato SyntaxError in output")
        else:
            self.assertTrue(False, "Non rilevato prompt nè output")

    def test_rl_2_4_print_path_windows(self):
        pattern = r"[\'\"].*rl2\.4>{3}(.*)[\\n]{2,}rl2\.4(.*)[\\n]{4,}rl2\.5>{3}.*[\'\"]*.*[\'\"]"  # registrato PBST31224 https://regex101.com/r/2mE9S3/4
        (prompt, output) = catch_rl_prompt_and_output(pattern)
        if prompt is not None and output is not None:
            prompt = str(prompt).replace(r"\'","'") # adjust to avoid continuation line with char after
            exec(prompt)
            self.assertNotEqual(-1, str(prompt).find(output), f"Non trovato output <{output}> in prompt <{str(prompt)}>")
        else:
            self.assertTrue(False, "Non rilevato prompt nè output")

    def test_rl_2_5_print_path_windows(self):
        pattern = r"[\'\"].*rl2\.5>{3}[\'\"]*(.*)[\'\"]*\\n+rl2\.5(.*)[\\n]{4,}rl2\.6>{3}.*[\'\"]*.*[\'\"]"  # registrato PBST31225 https://regex101.com/r/dItzAU/1
        (prompt, output) = catch_rl_prompt_and_output(pattern,dbg=True)
        if prompt is not None and output is not None:
            prompt = str(prompt).replace(r"\'","'") # adjust to avoid continuation line with char after
            exec(prompt)
            prompt = str(prompt).replace(r"\\","@") # adjust to catch \\
            output = str(output).replace(r"\\","@@") # adjust to catch \\
            self.assertNotEqual(-1, str(prompt).find(output), f"Non trovato output <{output}> in prompt <{str(prompt)}>")
        else:
            self.assertTrue(False, "Non rilevato prompt nè output")

    def test_rl_2_6_print_path_windows(self):
        pattern = r"[\'\"].*rl2\.6>{3}[\'\"]*(.*)[\'\"]*\\n+rl2\.6(.*)\\n\\nrl2\.7>{3}.*"  # registrato PBST31226 https://regex101.com/r/dItzAU/3
        (prompt, output) = catch_rl_prompt_and_output(pattern, dbg=True)
        if prompt is not None and output is not None:
            prompt = str(prompt).replace(r"\'","'") # adjust to avoid continuation line with char after
            exec(prompt)
            prompt = str(prompt).replace(r"\\","@@") # adjust to catch \\\\ in \\
            prompt = str(prompt).replace(r"@@","@")  # adjust to catch \\ in \
            output = str(output).replace(r"\\","@@") # adjust to catch \\ in @@
            output = str(output).replace(r"\n","@n") # adjust to catch \n in @n
            self.assertNotEqual(-1, str(prompt).find(output), f"Non trovato output <{output}> in prompt <{str(prompt)}>")
        else:
            self.assertTrue(False, "Non rilevato prompt nè output")
