from vidstream import ScreenShareClient
import threading
class StreamServer:
    def __init__(self, host, port):
        # host is the host of the CLIENT
        self.server = ScreenShareClient(host, port)

    def start_stream(self):
        self.thread = threading.Thread(target=self.server.start_stream)
        self.thread.start()

    def end_stream(self):
        self.server.stop_stream()

if __name__ == '__main__':
    server = StreamServer('192.168.1.104', 3000)
    server.start_stream()
    while input("") != 'STOP':
        continue 

    server.end_stream()