import xml.etree.ElementTree as ET

data = '''
<person>
    <name>David</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide = "yes"/>
</person>'''

data2 = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>David</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Joe</name>
        </user>
    </users>
</stuff>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

stuff = ET.fromstring(data2)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get("x"))