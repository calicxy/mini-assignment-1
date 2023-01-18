import subprocess
 
# If your shell script has shebang,
# you can omit shell=True argument.
def get_checksum(fp):
# passing relative path does not work.
    output = subprocess.run(["./backend/models/checksum/checksum.sh", fp], 
                        # shell=True
                        capture_output=True
                        )
    output_str = output.stdout.decode('utf-8')
    return output_str.split()[0]

