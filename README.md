# networking_fundamentals
Repository to understand networking fundaments with python, C++ and linux tools

## Linux networking command line tools
1. `nc`
2. `telnet`
3. 
4. `ssh`
5. `lsof`
   - Check the network sockets in memory
   ```
   lsof -i :PORT
   ```

## Sockets
- These are software components - linux implements different protocols with sockets
- can be a bluetooth socket, Infrared socket, network socket (TCP, UDP) etc.
- Can be used for IPC (Inter Process Communication) on the same machine.
- Eg: TCP Socket is a socket that uses TCP protocol
- Python has a socket library with which you can create a server and a client. 
- When creating a server, the main socket object and the communication socket object are different. 
- In the client side it is the same socket object used for message passing. 

## TCP
- sends data as a byte stream
- sequential
- reliable

## Datagram
- datagram based
- we can handle packet loss by writing custom checks


## Single threaded vs Multithreaded socket applications

## Testing servers and clients with linux tools