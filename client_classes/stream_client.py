from vidstream import StreamingServer 
import threading

class StreamClient:
    def __init__(self, client):
        # host is the host of the CLIENT (which is the IP address of current computer)
        self.client = client


    def watch_stream(self):
        self.client.Command({"state": "StartStream"})

        data = self.client.bytes2dict(self.client.Recv())
        host, port = data["ip"], data["port"]
        self.stream = StreamingServer(host, port, 1)

        self.thread = threading.Thread(target=self.stream.start_server)
        self.thread.start()

    def stop_watching_stream(self):
        self.client.Command({"state": "StopStream"})
        self.stream.stop_server()

if __name__ == '__main__':
    host = '192.168.1.104'
    port = 3000
    client = StreamClient(host, port)
    client.watch_stream()
    while input("") != 'STOP':
        continue 

    client.stop_watching_stream()