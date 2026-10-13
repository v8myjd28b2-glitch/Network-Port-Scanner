from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException

devices = [
    {
        'device_type': 'cisco_ios',
        'host': '192.168.1.1',
        'username': 'admin',
        'password': 'Password123',
    }
]

audit_commands = [
    'show ip interface brief',
    'show running-config | include hostname',
    'show version | include uptime'
]

def run_network_audit():
    print("[*] Starting Automated Network Audit & Configuration Check...\n")
    
    for device in devices:
        print(f"--> Connecting to Device: {device['host']}")
        try:
            net_connect = ConnectHandler(**device)
            print(f"[+] Successfully Connected to {device['host']}")
            
            for cmd in audit_commands:
                output = net_connect.send_command(cmd)
                print(f"\n--- Output for '{cmd}' ---")
                print(output)
            
            net_connect.disconnect()
            print(f"\n[+] Completed Audit for {device['host']}\n" + "="*40)
            
        except NetmikoTimeoutException:
            print(f"[-] Error: Connection Timeout to {device['host']}.")
        except NetmikoAuthenticationException:
            print(f"[-] Error: Authentication Failed for {device['host']}.")
        except Exception as e:
            print(f"[-] Unexpected Error: {str(e)}")

if __name__ == "__main__":
    run_network_audit()
