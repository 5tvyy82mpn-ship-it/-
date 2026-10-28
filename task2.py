f = open("mailbox.txt")
text = f.readlines()
f.close()

a = len(text)

f = open("output.txt", "w")
f.write(str(a))
f.close()