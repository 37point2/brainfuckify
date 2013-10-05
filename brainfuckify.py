import sys

def main(filename, col_width):
    ascii_input = open(filename, 'r').read()

    if len(filename.split(".")) > 1:
        out_file = ".".join(filename.split(".")[:-1]) + ".bf"
    else:
        out_file = filename + ".bf"
    print out_file

    ascii_output = ""
    prev_char = 0

    for char in ascii_input:
        cur_char = ord(char)
        if cur_char - prev_char < 0:
            ascii_output += "+"*abs(cur_char-prev_char) + "[>-<-]>.<"
        elif cur_char - prev_char > 0:
            ascii_output += "+"*(cur_char-prev_char) + "[>+<-]>.<"
        elif cur_char == prev_char:
            ascii_output += ">.<"
        prev_char = cur_char

    ascii_output = "\n".join([ascii_output[i:i+col_width] for i in xrange(0,len(ascii_output),col_width)])

    open(out_file, "w").write(ascii_output)

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))