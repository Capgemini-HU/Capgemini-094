import socketserver
from threading import Thread, Event
import time
import sys
from server import TCPHandler

stop_event = Event()

def timeout():
    timer = 0
    while True:
        timer += 1
        time.sleep(1)
        if stop_event.is_set():
            handle_shutdown()
            break


def handle_shutdown():
    print("Shutting down server")
    server.server_close()
    server.shutdown()

if __name__ == '__main__':
    try:
        TCPHandler.set_debug(TCPHandler, debug=sys.argv[1])
    except IndexError:
        TCPHandler.set_debug(TCPHandler, debug=0)
    server = socketserver.TCPServer(("", 9999), TCPHandler)
    # run server
    print("starting server, timeout after 30 seconds.")
    main_thread = Thread(target=server.serve_forever)
    main_thread.start()

    second_thread = Thread(target=timeout)
    second_thread.start()
    second_thread.join(timeout=30)
    stop_event.set()


