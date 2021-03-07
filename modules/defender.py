"""
Trying to find any defenders
"""


from os import path


class Defenders:
    def __init__(self):
        """
        Popular Defenders
        """
        self.defenders = {
            'C:\\Program Files\\Windows Defender': 'Windows Defender',
            'C:\\Program Files\\AVAST Software\\Avast': 'Avast',
            'C:\\Program Files\\AVG\\Antivirus': 'AVG',
            'C:\\Program Files (x86)\\Avira\\Launcher': 'Avira',
            'C:\\Program Files (x86)\\IObit\\Advanced SystemCare': 'Advanced SystemCare',
            'C:\\Program Files\\Bitdefender Antivirus Free': 'Bitdefender',
            'C:\\Program Files\\DrWeb': 'Dr.Web',
            'C:\\Program Files\\ESET\\ESET Security': 'ESET',
            'C:\\Program Files (x86)\\Kaspersky Lab': 'Kaspersky Lab',
            'C:\\Program Files (x86)\\360\\Total Security': '360 Total Security'
        }

    def GetDefenders(self):
        """
        :return: string: (founded defenders)
        """
        founded = [self.defenders[defender] for defender in self.defenders.keys() if path.exists(defender)]
        if founded:
            output_string = "\n".join(founded)
            return output_string
        else:
            return "Defenders was not founded"
