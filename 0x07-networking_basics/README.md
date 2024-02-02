# OSI Model
- The open system interconnection model is a conceptual model from the international organization of standardization (ISO) that provides a common basis for the coordination of standards development for the purpose of systems interconnection.
- Communication between systems are split into seven different abstraction layers:
![](https://cf-assets.www.cloudflare.com/slt3lc6tev37/6ZH2Etm3LlFHTgmkjLmkxp/59ff240fb3ebdc7794ffaa6e1d69b7c2/osi_model_7_layers.png)
	__Physical Layer (1)__
		![](https://cf-assets.www.cloudflare.com/slt3lc6tev37/1HQ1W5P4XAinIdM37DTu4U/900ccdceda346baf03ce8b9f977d2974/osi_model_physical_layer_1.png)
		- It includes physical equipments involved in data transfer such as cables and switches.
		- It is also the layer where data get converted into bit streams , a string of 1's and 0's
		- The physical layer of both devices must also agree on a signal convertion so that the 1's can be distinguished from the 0's on both devices.
		
__Data link layer (2)__
		![](https://cf-assets.www.cloudflare.com/slt3lc6tev37/3TLHavXiotb9ayyZFKECf3/9456d1c431cd71ceea7f4b407f076f11/data_link_layer_osi_model.png)
		- It is similar to the network layer except it facilitates data transfer between two devices on the same network.
		- allow access of media by upper layers  and control how data is received from thhe media.
	__Network layer (3)__
		![](https://cf-assets.www.cloudflare.com/slt3lc6tev37/3g2Hv0frHsql5SFauJL5EG/d8cede7b6a780e63413bd86de9eee7f9/osi_model_network_layer_3.png)
			- Responsible for facilitating data transfer between two different networks.
			- If two devices are communicating and are the same network, then the network layer is unnecessary.
			- It also find the best physical path for the data to reach its destination (routing).
			- Network layer protocols include Internet control message protocol (IMCP), internet group protocol and IPsec suite
			- Logical addressing, path determination and routing
	__Transport layer (4)__ 
		![](https://cf-assets.www.cloudflare.com/slt3lc6tev37/3OlO75NcADGL3SmEADFDqd/723b8c7639c4e2e6b4febcbe7fd36e0e/osi_model_transport_layer_4.png)
		- Responsible for end to end communication between two devices. This includes taking data from session layer and breaking it into segments before sending it to layer 3
		- It is also responsible for flow control(determine optimal speed of transmission) and error control(ensuring data received is complete and requesting a re-transmission if it is not.).
		- Transmission control protocol (TCP) and user datagram protocol (UDP)
	__Session layer (5)__ 
		![](https://cf-assets.www.cloudflare.com/slt3lc6tev37/29mRrgK22AqJVlg2MMlD86/34d8f4071b6cc0d3b03c93f55e4d89b7/osi_model_session_layer_5.png)
		- responsible for opening and closing communication between the two devices. Also synchronizes data transfer with checkpoints.
		- Helps in session management, authentication and authorization.
	__Presentation layer (6)__
			![](https://cf-assets.www.cloudflare.com/slt3lc6tev37/19L86neKKT8srUkOSe4rf7/ff4c91c94a1790651df7b48433913f59/osi_model_presentation_layer_6.png)
			-  Responsible for preparing data so that it can be used by the application layer. 
			- Responsible for translation, encryption and compression of data.	
	__Application layer (7)__
		- interacts with data from the user 
		-  Application layer protocols include `http` as well as `smtp` and `telnet`
		![](https://cf-assets.www.cloudflare.com/slt3lc6tev37/2rcDKpr4WLqoyAZ7GDKkyJ/7cab96402de7ac5465b86e617da3da4e/osi_model_application_layer_7.png)

- Each intermediate layer serves a class of functionality to the layer above it and is served by the layer below it.
- Each layer in the OSI model has well defined functions, and the methods of each layer communicate and interact with those of the layers immediately above and below as approapriate.
- The OSI provides a standard for different computer systems to e able to communicate with each other. It can be seen as a universal language for computer networking.
- . [DDoS attacks](https://www.cloudflare.com/learning/ddos/what-is-a-ddos-attack/) target specific layers of a network connection; [application layer attacks](https://www.cloudflare.com/learning/ddos/application-layer-ddos-attack/) target [layer 7](https://www.cloudflare.com/learning/ddos/what-is-layer-7/) and protocol layer attacks target layers 3 and 4.

----
#### Local Area Network (LAN)
- It is a computer network that interconnects computers within a limited area as a residence, school, laboratory, university campus or office building.
- It is also typically owned, controlled and managed by a single person or organization.

### Wide Area Network (WAN)
- It is a telecommunication network that extends over a large geographical area.
- The internet is the largest WAN, spanning the earth.
- A network device called a router connect LANs to WAN
- A WAN differs from LAN in several important ways, most arent owned by a single organization. Instead WANS exist under collective or distributed ownership and management.


## Internet
- It is a global system of interconnected computers networks that uses TCP/IP to communicate between networks and devices
- It is a network of networks that consists of public, private, academic, business and government networks of local to global scope, linked by a broad of array of electronic, wireless and optical networking technologies.
- The internet has no single centralized governance in either technological implementation or policies for access and usage; each constituent network sets its own policies.


## MAC Address
- A media access control (MAC) address is a string of characters that identifies a device on a network.
- It is tied to a key connection device called the network interface card (NIC)
- NIC is essentially a computer circuit card that makes it possible for your computer to connect to a network. It turns data into electrical signals that can be transmitted over the network.

__Use__
- All devices on the same network subnet have different MAC addresses, MAC addresses are very useful for diagnosing network issues such as problems with IP addresses.
- This is because they never change as opposed to dynamic IP address which can change from time to time .
- On wireless network, a process called MAC filtering is a seccurity measure to prevent unwanted network access by hackers and intruders. In MAC address filtering, the router is configured to accept traffic only from specific MAC addresses

__Note:__ IP address represent software and a MAC address represents hardware.


## IP address
- It is a unique number assigned to every machine on the internet.
__IPv4 and IPv6__
- Internet protocol version 4 uses 32-bit addresses, which limits the amount of addresses to 4, 294,967,296 possible unique addresses.
- Internet protocol version 6 changes the address size from 32-bit address to 128-bit addresses
- IP address consists of 4 numbers separated by periods, with the number having possible range from 0 through 255. They are 3 special ranged reserved for special purpose
	- 0.0.0 (The default network)
	- 255.255.255.2555 (broadcast address used for routing) - broadcasting messages to the entire network that your computer resides on.
	- 127.0.0.1 (Loop back address refers for your machine), used for testing or debugging your programs on the computer.

__Public IP address__
- It is an IP address that can be accessed over the internet.
- It is globally unique and can only be assigned to a unique device.

__Private Address__
- They are a block of IP addresses that are set aside for internal private use of computers not directly connected to the internet.
- These IP addresses are used for internal use by company or home networks that needs to use TCP/IP but dont want to be directly visible on the internet.


__Internet Protocols__
- It is the technical format of packets and the addressing scheme for computers to communicate over a network.
- __IPv4__ uses a 32-bit addressing scheme allowing a total of 2^32 addresses. written in decimal as four numbers separated by periods.
- __IPv6__  uses a 128-bit address and is written in hexadecimal and separated by colons.


__Local host__
- It is a hostname  that refers to the current computer used to access it.
- It is reserved for loopback and it is used to access the network services that are running on the host via the loopback network interface.
- The local loopback maybe used to run a network service on a host without requiring a physical network interface or without making server accesible from the network services that are running on the host via the loopback network interface.

### TCP / IP
- It is a suite of protocols used by devices to communicate over the internet and most local networks.
- TCP provides apps a way to deliver ( and receive ) an ordered and error checked stream of information packets over a network.
- The user datagram protocol is used by apps to deliver a faster stream of information by doing away with error checking.
- TCP and UDP are protocols used for sending bits of data (packets) over the internet.

### Ping
- It is a computer network administration software utility used to test for reachability of a host on an internet protocol (IP)network.
- It measurres the round trip time for messages sent from the originating host to destination computer that are echoed back to source.
- It operates by means of internet control message protocol. Pinging involves sending an ICMP echo request to target host and waiting for an ICMP echo reply.


### ##  $0 , $1 $2 $3 … bash Parameters
- **$0 : bash Shell argument 0**, It expands into bash script file name or bash shell.
- **$1 $2 $3 …**   : **bash shell argument number** : Used to get the specific argument from the script.

----
# Summary
## OSI Model:
The OSI (Open Systems Interconnection) Model is a conceptual framework that standardizes the functions of a telecommunication or computing system into seven abstraction layers. Each layer serves a specific purpose and interacts with adjacent layers.

### Layers of the OSI Model:
1. **Physical Layer:** Deals with the physical connection between devices. It defines characteristics such as voltage levels, data rates, and physical connectors.

2. **Data Link Layer:** Responsible for creating a reliable link between two directly connected nodes, providing error detection and correction.

3. **Network Layer:** Manages routing, addressing, and forwarding of data packets between devices across different networks.

4. **Transport Layer:** Ensures end-to-end communication, handling issues like flow control, error correction, and data segmentation.

5. **Session Layer:** Establishes, maintains, and terminates sessions between applications.

6. **Presentation Layer:** Handles data format translation, encryption, and compression to ensure that information is properly presented to the application layer.

7. **Application Layer:** Provides network services directly to end-users and application processes.

## LAN (Local Area Network):
A LAN is a network that is limited to a small geographic area, such as a single building or a campus. It connects computers and devices within a close proximity.

- **Typical Usage:** Used for sharing resources like files, printers, and internet access among local users.

- **Typical Geographical Size:** Covers a small area, such as a single building or a campus.

## WAN (Wide Area Network):
A WAN spans a large geographic area, connecting multiple LANs or other types of networks over long distances.

- **Typical Usage:** Enables communication between geographically dispersed offices, organizations, or data centers.

- **Typical Geographical Size:** Covers a wide area, potentially spanning cities, countries, or even continents.

## Internet:
The Internet is a global network that connects millions of private, public, academic, business, and government networks. It uses the TCP/IP protocol suite for communication.

## IP Address:
An IP address is a numerical label assigned to each device participating in a computer network that uses the Internet Protocol for communication.

## Types of IP Addresses:
1. **IPv4 (Internet Protocol version 4):** The most widely used IP version, expressed as four sets of numbers separated by periods (e.g., 192.168.1.1).

2. **IPv6 (Internet Protocol version 6):** Developed to address the exhaustion of IPv4 addresses, expressed as eight groups of hexadecimal digits separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334).

## Localhost:
Localhost refers to the loopback network interface, typically assigned the IP address 127.0.0.1. It allows a device to communicate with itself.

## Subnet:
A subnet is a logical subdivision of an IP network. It enables network administrators to divide an IP address space into sub-networks to improve performance and security.

## IPv6 Creation:
IPv6 was created to address the limitations of IPv4, primarily the exhaustion of available IP addresses due to the rapid growth of the internet and the increasing number of connected devices. IPv6 provides a vastly expanded address space, ensuring a sufficient number of unique addresses for the foreseeable future.
