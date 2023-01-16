import subprocess
 
# If your shell script has shebang,
# you can omit shell=True argument.
# passing relative path does not work.
output = subprocess.run(["./backend/models/checksum.sh", "/home/vest1/Desktop/multi-01-starting-setup/backend/models/goal.js"], 
                    # shell=True
                    capture_output=True
                    )
print(output.stdout)
output_str = output.stdout.decode('utf-8')
print(output_str.split()[0])

