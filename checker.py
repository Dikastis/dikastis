import sys
from soldier import soldier
import json
import ipdb

verdict = {'TLE': 'TLE', 'RE': 'RE', 'CE': 'CE', 'WA': 'WA', 'AC': 'AC'}
data = {}
def response_msg(status, msg, **kwargs):
    res = {}
    res['status'] = status
    res['msg'] = msg
    for name, value in kwargs.items():
        res[name] = value
    print res
    return res

# compilation
a = soldier.run("sudo -H -u judge bash -c 'g++ -o /home/judge/"+str(sys.argv[1])+" /home/judge/" + str(sys.argv[1]) + ".cpp'")
if a.status_code != 0:
	# data = {}
	with open('/home/shivangi/Desktop/2/dikastis/log.json') as data_file:
		data = json.load(data_file)
	data[str(sys.argv[1])] = response_msg('OK', verdict['CE'])
	f = open('/home/shivangi/Desktop/2/dikastis/log.json', 'w')
	f.write(json.dumps(data))
	f.close()
	sys.exit(0)

else:
	# print "timeout 1s ./a.out < problems/" + str(sys.argv[2]) + ".in > " + str(sys.argv[1]) + ".out"
	f = open("/home/shivangi/Desktop/2/dikastis/problems/" + str(sys.argv[2]) + ".in", 'r')
	# f.write(str(a.output))
	a = soldier.run("sudo -H -u judge bash -c 'timeout 1s /home/judge/"+str(sys.argv[1])+"'", stdin=str(f.read()))
	f.close()
	f = open("/home/shivangi/Desktop/2/dikastis/submissions/"+str(sys.argv[1]) + '.out', 'w')
	f.write(str(a.output))
	f.close()
	# time limit check
	if a.status_code == 124:
		# data = {}
		with open('/home/shivangi/Desktop/2/dikastis/log.json') as data_file:
			data = json.load(data_file)
			data[str(sys.argv[1])] = response_msg('OK', verdict['TLE'])
			f = open('/home/shivangi/Desktop/2/dikastis/log.json', 'w')
			f.write(json.dumps(data))
			f.close()
			# sys.exit(0)

	# runtime error
	elif a.status_code != 0:
		# data = {}
		with open('/home/shivangi/Desktop/2/dikastis/log.json') as data_file:
			data = json.load(data_file)
			data[str(sys.argv[1])] = response_msg('OK', verdict['RE'])
			f = open('/home/shivangi/Desktop/2/dikastis/log.json', 'w')
			f.write(json.dumps(data))
			f.close()
			# sys.exit(0)
	# wa check
	else:
		# print "diff problems/" + str(sys.argv[2]) + ".in " + str(sys.argv[1]) + ".out"
		a = soldier.run("diff /home/shivangi/Desktop/2/dikastis/problems/" + str(sys.argv[2]) + ".out " + "/home/shivangi/Desktop/2/dikastis/submissions/" + str(sys.argv[1]) + ".out")
		# print a.output
		if a.output:
			# data = {}
			with open('/home/shivangi/Desktop/2/dikastis/log.json') as data_file:
				data = json.load(data_file)
				data[str(sys.argv[1])] = response_msg('OK', verdict['WA'])
				f = open('/home/shivangi/Desktop/2/dikastis/log.json', 'w')
				f.write(json.dumps(data))
				f.close()

				# sys.exit(0)

		else:
			# data = {}
			with open('/home/shivangi/Desktop/2/dikastis/log.json') as data_file:
				data = json.load(data_file)
				data[str(sys.argv[1])] = response_msg('OK', verdict['AC'])
				f = open('/home/shivangi/Desktop/2/dikastis/log.json', 'w')
				f.write(json.dumps(data))
				f.close()
				# sys.exit(0)

print data