import requests

def post_to_icinga(key, pj, server, metric_value, th, dp, exit_status):
	headers = {'Accept': 'application/json',
			   'Content-Type': 'application/json'}
	params = (('service', 'webserver2!CHECK_DISK_2'),)
	plugin_output = "Disk usage is: " + str(metric_value)
	performance_data = 
	data = { 
            "exit_status": exit_status,
			      "plugin_output": plugin_output,
			      "performance_data": [ "user_space=10"],
			      "check_source": "webserver2" 
          }
	requests.post('https://localhost:5665/v1/actions/process-check-result',
					headers=headers,
					params=params,
					data=data,
					verify=False,
					auth=('director', 'password')
				  )
