********************************************************
*Project No. 3: Secure IP.
*Course: CS425:Computer Networks.
*Date: November 10, 2011
*Members: Nehchal Jindal 	Y9366 nehchal@iitk.ac.in
*		 Kritika Singh 		Y9288 skritika@iitk.ac.in
*		 Pankaj Jindal 		Y9399 pankajj@iitk.ac.in
*		 Suresh Gogulothu 	Y9610 sureshg@iitk.ac.in
********************************************************		 

*Structure of Code*

'client_app.py' : application chat program with GUI for client
'server_app.py': application chat program with GUI for server
'aes_client.py':  network layer(ESP), for encrypting and decrypting the IP packet on client side
'aes_server.py': network layer(ESP), for encrypting and decrypting the IP packet on server side
'md5.py' and 'define.h':  network layer(AH), for  authentication headers(cryptographic hash)
'server.py' and 'client.py':  defines basic functions in link layer

********************************************************
*Instructions to run*

cd to the appropriate folder.
$sudo python server_app.py			//server GUI opens up
$python client_app.py		//client GUI opens up
Click 'Setup Server' on server side. Connect client by clicking 'connect' on client side. 

Input your exponent in the terminal window of the client
Then, input your exponent in the terminal window of the server.
Then, you will see the confirmation of connection being set up on the client GUI
Write in the text box of client or server, and enter "Send", the data will be transmitted to the other side and you can see the encrypted data on the respective terminal windows and the MD5 too.
*********************************************************
*Contribution*

Pankaj Jindal and Suresh Gugulothu: AES encrytion and decryption, Diffie Hellman key exchange
Nehchal Jindal and Kritika Singh: MD5 cryptographic hash, application layer and GUI, link layer
*********************************************************
