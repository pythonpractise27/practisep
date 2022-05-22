sw=['Python','Perl','C','Java','C++']
print (f'This the software list : {sw}')
sw.append('php')
print (f'This the software list after append: {sw}')
sw.insert(2,'COBOL')
print (f'This the software list after insert: {sw}')
tools=['Rally','Jira','Accurev','Git']
print (f'This the tools list : {tools}')
#Rally is a project management tool like Jira
sw.extend(tools)
print (f'This the tools list  after extend : {tools}')

developer=[]
developer.insert(1,'Python')
developer.insert(1,'Git')
developer.insert(1,'Jira')
developer.insert(2,'Git')
developer.insert(3,'Jira')
print (f'This the developer list : {developer}')
