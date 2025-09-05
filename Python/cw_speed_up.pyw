import xmlrpc.client
import argparse
import sys
import re


"""Sends a CAT command to flrig to set the CW keyer speed."""
server_url = "http://127.0.0.1:12345/"
server = xmlrpc.client.ServerProxy(server_url)

#try:
#    with open(input_path, "r") as f:
#        speed_value = f.read().strip()
#        print(speed_value)
#except FileNotFoundError:
#    print("cw_speed.txt not found")
    #exit(1)
try:
    # Ensure the speed is a number and is zero-padded to three digits
    response = server.rig.cat_string("KS;")
    speed_int = int(re.sub("[^0-9]", "", response))
    speed_str = (speed_int + 1)
    formatted_speed = f'{speed_str:03}'

    # Construct the CAT command (KS + speed + terminator)
    cat_command = f'KS{formatted_speed};'
    print(cat_command)
    # Send the CAT command to the radio
    server.rig.cat_priority(cat_command)
    #print(f"Set CW speed to: {speed_int} WPM")
    exit()

except ValueError:
    sys.stderr.write("Error: The speed value must be a valid number.\n")
    exit(1)
except Exception as e:
    sys.stderr.write(f"An XML-RPC error occurred: {e}\n")
    exit(1)
finally:
    exit()  


