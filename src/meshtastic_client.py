import meshtastic
import meshtastic.tcp_interface
import meshtastic.protobuf.portnums_pb2
from meshtastic.protobuf.portnums_pb2 import PortNum

from config import settings


class MeshtasticClient:
    def __init__(self, interface, node):
        self.interface = interface
        self.node = node

    async def send_message_as(self, name: str, msg: str) -> bool:
        try:
            self.node = meshtastic.Node(self.interface, settings.node_id, timeout=10000)
            print(self.interface.getMyUser())
            self.node.setOwner(name, name[:3])

            self.node = meshtastic.Node(self.interface, settings.node_id, timeout=10000)
            print(self.interface.getMyUser())

            pkg = self.interface.sendData(data=msg.encode(), portNum=PortNum.TEXT_MESSAGE_APP, hopLimit=7, wantAck=True)
            print(pkg)

            self.node = meshtastic.Node(self.interface, settings.node_id, timeout=10000)
            self.node.setOwner(settings.default_node_name, settings.node_id[-1:-5:-1][::-1])
            print(self.interface.getMyUser())
        except:
            return False 

        return True
