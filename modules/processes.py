from fnmatch import fnmatch
from psutil import Process, process_iter, AccessDenied


class Processes:
    @staticmethod
    def GetProcesses():
        """
        :return: str <processes>
        """
        output = ''
        for process in process_iter():
            try:
                process_name = process.name().lower()
                processes_id = process.pid
                output += f'{process_name} {processes_id}\n'
            except AccessDenied:
                pass

        return output

    def KillProcess(self, target):
        """
        :param target: str
        :return: str (killed)
        """
        killed = ''
        for process in self.GetProcesses().splitlines():
            try:
                process_name = process.split(" ")[0]
                process_id = int(process.split(" ")[1])
                if target.lower() == process_name:
                    Process(process_id).kill()
                    killed += f'{process}\n'
            except Exception as e:
                print(e)

        return killed

    def FindProcess(self, pattern):
        """
        :param pattern:
        :return: str (founded)
        """
        founded = ''
        for process in self.GetProcesses().splitlines():
            try:
                process_name = process.split(" ")[0]
                if fnmatch(process_name, pattern.lower()):
                    founded += f'{process}\n'
            except ValueError and IndexError:
                pass

        return founded

