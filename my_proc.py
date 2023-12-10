import subprocess

server_ip = '192.168.157.4'

def client(server_ip):
    try:
        result_bytes = subprocess.check_output(['iperf', '-c', server_ip], stderr=subprocess.STDOUT)
        result = result_bytes.decode('utf-8')
        return result, None
    except subprocess.CalledProcessError as e:
        return None, f"Error: {e.output.decode('utf-8')}"

def parser(result):
    intervals = [] 
    lines = result.split('\n')
    for line in lines:
        if 'Interval' in line and 'Transfer' in line and 'Bitrate' in line:
            parts = line.split()
            interval = {
                'Interval': parts[1],
                'Transfer': float(parts[3]),
                'Bitrate': float(parts[6])
            }
            intervals.append(interval)
    return intervals

result, error = client(server_ip)

if error:
    print(error)
else:
    print("Results:")
    for value in parser(result):
        print(value)
