accuracy = model.history['accuracy'][-1:][0]


import os

if int(accuracy) > .80:

print('accuracy is: ',accuracy)

os.system('curl --user admin:redhat https://c48610e2.ngrok.io/job/job3/build?token=success')

else:

print('accuracy is: ',accuracy)


os.system('curl --user admin:redhat https://c48610e2.ngrok.io/job/job4/build?token=failure')
