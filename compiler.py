import string
import sys

def soroush_to_bytes(soroush):
    base2_text = ""
    for char in soroush:
        if char in string.ascii_lowercase:
            base2_text += "0"
        elif char in string.ascii_uppercase:
            base2_text += "1"
    return bytes([int(base2_text[i:i+8], 2) for i in range(0, len(base2_text), 8)])


def check_valid_soroush(soroush):
    soroush_lower = soroush.lower()
    if soroush_lower.replace("sorooush", "") != "" or len(soroush) % 8 != 0:
        print("Synthax error")
        exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("python compiler.py <input_file> <output_file>")
        print("Error: no file specified")
        exit(1)
    in_file = sys.argv[1]
    content = open(in_file, 'r').read().replace("\n", "")
    check_valid_soroush(content)
    out_bytes = soroush_to_bytes(content)
    open(sys.argv[2], 'wb').write(out_bytes)