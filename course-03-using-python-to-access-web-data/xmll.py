import xml.etree.ElementTree as ET
data = ''' <person>
<name>Fahad </name>
<phone type="int1">9832564719</phone>
<email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))
