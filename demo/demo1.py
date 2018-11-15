path = '/www/webapp/dx-agent/work/dx-agent-3.7.2-SNAPSHOT.war'

paths = path.split('/')

for p in paths:
    print(p)

print('my target file name is ' + paths[len(paths) - 1])
