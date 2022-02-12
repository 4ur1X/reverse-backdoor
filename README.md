## Malware - Reverse Backdoor

This is a python program that once executed on victim machine provides a direct backdoor access to it anytime.

Some of its features include:
- access file system
- execute system commands
- download files
- upload files
- maintain access after system restart (persistence)

Note: Before executing this program on the victim machine, make sure your attacker machine is listening on a specific port [via netcat or listener.py (another repository)].

Usage syntax: ````python3 reverse_backdoor.py````
