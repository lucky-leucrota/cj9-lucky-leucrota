import time

from websocket import create_connection

BASE_URL = "ws://127.0.0.1:8000/ws"  # Change this to the address of the server
MESSAGE = "Waaasssup my dudes"


def test_basic():
    """Tests the basic functionality of one connection. (connect, send, receive, disconnect)"""

    ws = create_connection(BASE_URL + "/harshal")

    ws.send(MESSAGE)
    result = ws.recv()

    ws.close()
    assert result[5:] == MESSAGE


def test_multiple_connections():
    """Tests the basic functionality of multiple connections. (connect, send, receive, disconnect)"""

    ws1 = create_connection(BASE_URL + "/sas2k")
    time.sleep(0.1)
    ws2 = create_connection(BASE_URL + "/siamh")

    ws1.send(MESSAGE)
    result = ws2.recv()

    ws1.close()
    time.sleep(0.1)
    ws2.close()
    assert result[:5] == "test:"


def test_send_10_messages():
    """Sends 10 messages to the server and checks if the server received them."""

    ws = create_connection(BASE_URL + "/sarvesh")

    for _ in range(10):
        ws.send(MESSAGE)
        time.sleep(0.1)

    ws.close()