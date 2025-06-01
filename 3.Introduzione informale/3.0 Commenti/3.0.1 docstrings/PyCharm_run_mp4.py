import sys
import subprocess

def play_video(file_path):
    if sys.platform.startswith('darwin'):  # macOS
        subprocess.call(('open', file_path))
    elif os.name == 'nt':  # Windows
        os.startfile(file_path)
    elif os.name == 'posix':  # Linux
        subprocess.call(('xdg-open', file_path))

import zipfile
import os

def decompress_zip(zip_file_path, extract_to_dir):
    """
    Decomprime un file ZIP in una directory specificata.

    :param zip_file_path: Percorso del file ZIP da decomprimere.
    :param extract_to_dir: Directory in cui estrarre i file.
    """
    # Verifica se il file ZIP esiste
    if not os.path.isfile(zip_file_path):
        print(f"Il file {zip_file_path} non esiste.")
        return

    # Apri il file ZIP
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Estrai tutti i file nella directory di destinazione
        zip_ref.extractall(extract_to_dir)
        print(f"File estratti in {extract_to_dir}")

from pathlib import Path

def get_file_name_without_extension(file_path):
    # Crea un oggetto Path dal percorso del file
    path = Path(file_path)
    # Ottieni il nome del file senza l'estensione
    file_name = path.stem
    return file_name

def estrae_mp4(zip_file):
    # Percorso del file ZIP da decomprimere
    # zip_file = "PyCharm-runInstruction2PythonConsole.zip"

    # Directory in cui estrarre i file
    extract_directory = "./"

    # Decomprimi il file ZIP
    decompress_zip(zip_file, extract_directory)

    # video_file = "PyCharm-runInstruction2PythonConsole.mp4"  #
    video_file = get_file_name_without_extension(zip_file)


if __name__ == "__main__":
    estrae_mp4(sys.argv[1])

