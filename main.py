import os
from pathlib import Path

if __name__ == '__main__':
    # Change here your path
    mypath: str = r"H:\01_Projekte\Elektroden_Charakterisierung\EIS_Messungen"
    #

    for file in os.listdir(mypath):
        if file.endswith(".DTA"):
            fileExExtension = Path(file).stem
            FilePath = os.path.join(mypath, fileExExtension)

            fOrig = open(FilePath + ".DTA", "r")
            fNew = open(FilePath + ".txt", "w")
            lFound = 0
            for line in fOrig:
                if '	#	s	Hz	ohm	' in line or lFound == 1:
                    line = line.replace(",", ".")
                    fNew.write(line)
                    lFound = 1

            fOrig.close()
            fNew.close()
