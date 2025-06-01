import PyCharm_run_mp4 as rmp4
import os

if __name__ == "__main__":
    # Percorso del file ZIP da decomprimere
    zip_file = "PyCharm-runInstruction2PythonConsole.zip"
    mp4_file = "PyCharm-runInstruction2PythonConsole.mp4"

    # Verifica se il file MP4 esiste lo invoco
    if os.path.isfile(mp4_file):
        rmp4.play_video(mp4_file)
    elif os.path.isfile(zip_file):
        rmp4.estrae_mp4(zip_file)
        rmp4.play_video(mp4_file)

