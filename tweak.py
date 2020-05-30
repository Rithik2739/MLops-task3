import os
for file in os.listdir('/mlops_task'):
 if file.endswith('.py'):
  pyfile=file
  print(file)

print('Making changes in file : '+ pyfile)

f= open("/mlops_task/"+pyfile,"r")


filedata = f.read()
f.close()

newdata = filedata.replace('epochs = ','epochs = 2*')

f= open("/mlops_task/"+pyfile,'w')

f.write(newdata)
f.close()
