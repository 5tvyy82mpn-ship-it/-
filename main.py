fin = open("mailbox.txt", 'r')
fout = open("output.txt", 'w')

ls_revisions = []
lines = fin.readlines()

for line in lines:
    if line.startswith("Details:"):
        rev = line.split("rev=")[1].strip()
        if rev not in ls_revisions:
            ls_revisions.append(rev)

ls_revisions.sort(key=int)

for rev in ls_revisions:
    fout.write(rev + "\n")

fin.close()
fout.close()