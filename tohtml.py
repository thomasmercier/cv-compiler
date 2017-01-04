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

print('<ul>')
print('\t<li>First name : ' + root.find('info').find('firstname').text + '</li>')
print('\t<li>Last name : ' + root.find('info').find('lastname').text + '</li>')
print('</ul>')

print('<h1>Statement</h1>')

for statement in root.find('statements').findall('statement'):
    print('\t<p>' + statement.text + '</p>')

print('<h1>Work experience</h1>')

for position in root.find('workexperience').findall('position'):
    print('\t<h2>' + position.find('organization').text + '</h2>')
    print('\t<ul>')
    print('\t\t<li>' + position.find('location').find('city').text + ', ' \
         + position.find('location').find('country').text + '</li>')
    print('\t\t<li>From ' + position.find('startdate').text + ' to ' \
         + position.find('enddate').text + '</li>')
    print('\t\t<li>Title: ' + position.find('title').text + '</li>')
    counter = 0
    for project in position.findall('project'):
        print('\t\t<li>Project ' + str(counter) + ': ' \
            + project.text + '</li>')
        counter += 1
    print('\t</ul>')


print('</body>')
print('</html>')
