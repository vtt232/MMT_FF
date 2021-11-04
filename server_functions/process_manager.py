import os
from subprocess import Popen
import psutil


class ProcessManager:
    def get_running_processes_list(self):
        # Return a list of tuples,each of which contains information about one running process (name , id , thread counts)
        processes_list = []
        for proc in psutil.process_iter():
            try:
                processes_list.append(
                    (proc.name(), proc.pid, proc.num_threads()))
            except:
                pass

        return processes_list

    def kill_process(self, process_id):
        try:
            p = psutil.Process(int(process_id))
            p.kill()
        except:
            raise RuntimeError(f"No process found with id = {process_id}")

    def start_process(self, process_name):
        try:
            Popen(process_name, shell=True)
        except:
            raise RuntimeError(f"Can't start process {process_name}")
