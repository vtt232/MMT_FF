import subprocess
from .process_manager import ProcessManager
import psutil


class AppManager(ProcessManager):
    def get_win_ids(self):
        win_ids = []
        cmd = 'powershell "Get-Process | where {$_.MainWindowTitle } | select ProcessName,Id"'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if line.rstrip():
                tmp = line.decode().rstrip()
                if tmp.endswith("Id") or tmp.endswith("-"):
                    continue
                win_id = tmp.rpartition(" ")[2]
                win_ids.append(int(win_id))

        return win_ids

    def get_running_app_list(self):
        try:
            # Return a list of tuples , each of which contains information about running apps (name , id , thread count)
            apps = []
            for win_id in self.get_win_ids():
                app = psutil.Process(win_id)
                apps.append((app.name(), app.pid, app.num_threads()))

            return apps
        except Exception as e:
            print(str(e))

    def kill_app(self, app_id):
        try:
            if int(app_id) in self.get_win_ids():
                self.kill_process(app_id)
            else:
                raise Exception
        except:
            raise RuntimeError(f"No app was found with id = {app_id}")

    def start_app(self, app_name):
        try:
            self.start_process(app_name)
        except:
            raise RuntimeError(f"Cannot start app {app_name}")
