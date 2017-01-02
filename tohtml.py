import xml.etree.ElementTree as ET

xmlFileName = 'master-resume.xml'

resumeTree = ET.ElementTree(file=xmlFileName)
root = resumeTree.getroot()

print('<!DOCTYPE html>')
print('<html>')
print('<head>')
print('<title>' + root.find('info').find('firstname').text + ' ' + root.find('info').find('lastname').text + ' -- Master Resume</title>')
print('</head>')
print('<body>')

print('<h1>Info</h1>')

print('</body>')
print('</html>')