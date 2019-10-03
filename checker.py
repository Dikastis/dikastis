import sys
from soldier import soldier
import json
import ipdb
import time
import os
from constants.project_constants import *



verdict = {'TLE': 'TLE', 'RE': 'RE', 'CE': 'CE', 'WA': 'WA', 'AC': 'AC'}
data = {}
def response_msg(status, msg, **kwargs):
    res = {}
    res['status'] = status
    res['msg'] = msg
    for name, value in kwargs.items():
        res[name] = value
    print res['status']
    print res['msg']
    return res


os.system('rm log.json')
f = open('log.json','w')
f.write('{}')
f.close()

# compilation
cmd = "sudo -H -u root bash -c 'g++ -o "+ project_path + "output/" +str(sys.argv[1])+" "+ project_path + "output/" + str(sys.argv[1]) + ".cpp'"
print cmd
a = soldier.run(cmd)
if a.status_code != 0:
	# data = {}
	with open(project_path+'log.json') as data_file:
		data = json.load(data_file)
	data[str(sys.argv[1])] = response_msg('OK', verdict['CE'])
	f = open(project_path+'log.json', 'w')
	f.write(json.dumps(data))
	f.close()
	sys.exit(0)

else:
	# print "timeout 1s ./a.out < problems/" + str(sys.argv[2]) + ".in > " + str(sys.argv[1]) + ".out"
	f = open(project_path+'problems/' + str(sys.argv[2]) + ".in", 'r')
	# f.write(str(a.output))
	a = soldier.run("sudo -H -u root bash -c 'timeout 1s "+ project_path + "output/" +str(sys.argv[1])+"'", stdin=str(f.read()))
	f.close()
	f = open(project_path+'submissions/'+str(sys.argv[1]) + '.out', 'w')
	f.write(str(a.output))
	f.close()
	# time limit check
	if a.status_code == 124:
		# data = {}
		with open(project_path+'log.json') as data_file:
			data = json.load(data_file)
			data[str(sys.argv[1])] = response_msg('OK', verdict['TLE'])
			f = open(project_path+'log.json', 'w')
			f.write(json.dumps(data))
			f.close()
			# sys.exit(0)

	# runtime error
	elif a.status_code != 0:
		# data = {}
		with open(project_path+'log.json') as data_file:
			data = json.load(data_file)
			data[str(sys.argv[1])] = response_msg('OK', verdict['RE'])
			f = open(project_path+'log.json', 'w')
			f.write(json.dumps(data))
			f.close()
			# sys.exit(0)
	# wa check
	else:
		# print "diff problems/" + str(sys.argv[2]) + ".in " + str(sys.argv[1]) + ".out"
		a = soldier.run("diff "+ project_path +"problems/" + str(sys.argv[2]) + ".out " + project_path +"submissions/" + str(sys.argv[1]) + ".out")
		# print a.output
		
		if a.output:
			# data = {}
			with open(project_path+'log.json') as data_file:
				data = json.load(data_file)
				data[str(sys.argv[1])] = response_msg('OK', verdict['WA'])
				f = open(project_path+'log.json', 'w')
				f.write(json.dumps(data))
				f.close()

				# sys.exit(0)

		else:
			# data = {}
			with open(project_path+'log.json') as data_file:
				data = json.load(data_file)
				data[str(sys.argv[1])] = response_msg('OK', verdict['AC'])
				f = open(project_path+'log.json', 'w')
				f.write(json.dumps(data))
				f.close()
				# sys.exit(0)


