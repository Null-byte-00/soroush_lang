import sys

def byte_to_soroush(in_bytes):
    binary_str = "".join(f"{byte:08b}" for byte in in_bytes)
    soroush_str = "sorooush" * len(in_bytes)
    final_soroush_str = ""
    for i, b in enumerate(binary_str):
        if b == "1":
            final_soroush_str += soroush_str[i].upper()
        elif b == "0":
            final_soroush_str += soroush_str[i].lower()
    return final_soroush_str


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("python decompiler.py <input_file>")
        print("Error: no file specified")
        exit(1)
    in_bytes = open(sys.argv[1], 'rb').read()
    print(byte_to_soroush(in_bytes))
    