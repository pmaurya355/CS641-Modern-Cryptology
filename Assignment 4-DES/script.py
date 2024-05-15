import wexpect

child = wexpect.spawn('ssh student@172.27.26.188')
child.expect('student@172.27.26.188\'s password:')
child.sendline("cs641")
child.expect('Enter your group name: ', timeout = 1) 
child.sendline("PriSoN")

child.expect('Enter password: ', timeout = 1)
child.sendline("PriSoN")

child.expect('.*', timeout = 1)
child.sendline("5")

child.expect('.*')
child.sendline("go")

child.expect('.*')
child.sendline("wave")

child.expect('.*')
child.sendline("dive")

child.expect('.*')
child.sendline("go")

child.expect('.*')
child.sendline("read")
print('run')
# child.expect('.*')
# child.sendline("password")


f = open("plain_texts.txt",'r')
g = open("cipher_texts.txt",'w')

for line in f.readlines():
	li = line.split()
	print('reached')
	for l in li:
		print('reached')
		child.sendline(l)
		print(child.before)
		g.writelines(str(child.before)[71: 88]+"\n")
		child.expect("Slowly, a new text starts*")
		child.sendline("c")
		child.expect('The text in the screen vanishes!')

child.close()
f.close()
g.close()