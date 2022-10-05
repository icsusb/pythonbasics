

teststring = ' dies ist ein Teststring(); \r\nmit Klammern und <html tags>! \n und Umbrüchen - ‚'
sani1 = teststring.strip(' ')
print('Bereinigter String:\n' + sani1)
sani2 = teststring.rstrip('- ,')
print('Bereinigter Text 2:\n' + sani2)
sani3 = sani1.strip('')
print('Bereinigter Text 3:\n' + sani3)
sani4 = sani3.strip('')
print('Bereinigter Text 4:\n' + sani4)
