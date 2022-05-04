# Importing the relevant libraries
# import websockets
# import asyncio

# import socketio


import socketio


# standard Python
sio = socketio.Client()


@sio.event()
def connect():
    print("my_event")
    sio.emit(
        'my_event', 'automate')


@sio.on('message')
def on_message(data):

    print('I received a message : ' + str(data))


sio.connect('http://127.0.0.1:5000/')
# The main function that will handle connection and communication
# with the server


# async def listen():
#     url = "https://secrep.herokuapp.com/"
#     # Connect to the server
#     async with websockets.connect(url) as ws:
#         # Send a greeting message
#         await ws.send("Hello Server!")
#         # Stay alive forever, listening to incoming msgs
#         while True:
#             msg = await ws.recv()
#             print(msg)

# # Start the connection
# asyncio.get_event_loop().run_until_complete(listen())
