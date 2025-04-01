# Real-time updates
# from fastapi import WebSocket, WebSocketDisconnect, APIRouter
#
# router = APIRouter()
# active_connections = []
#
# @router.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     active_connections.append(websocket)
#     try:
#         while True:
#             message = await websocket.receive_text()
#             for conn in active_connections:
#                 await conn.send_text(message)
#     except WebSocketDisconnect:
#         active_connections.remove(websocket)
