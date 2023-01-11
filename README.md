# iris
simple communication tool

The idea is that both computer A and B communicate through a relay server.
The only functionality intended for the relay server is to assign ports to users and to forward the messages from one to other. Clients can also be a server node themselves (in case of storing data and doing remote port forwarding to relay server). Clients read data of another client by local port forwarding from relay server.