import argparse
import binascii
import urllib


def encode_text(enc_string):
    while True:
        print "Select one of the following:"
        print "1. Base64\n2. URL\n3. Rot13\n4. Ascii\n5. Hex\n6. Binary\n" \
              "7. Uuencode"

        user_sel = input()

        if user_sel == 1:
                print enc_string.encode('base64', 'strict')
                return
        elif user_sel == 2:
                print urllib.quote(enc_string)
                return
        elif user_sel == 3:
                print enc_string.encode('rot13', 'strict')
                return
        elif user_sel == 4:
            print enc_string.encode('ascii', 'strict')
            return
        elif user_sel == 5:
            print enc_string.encode('hex', 'strict')
            return
        elif user_sel == 6:
            print ' '.join(map(bin, bytearray(enc_string)))
            return
        elif user_sel == 7:
            print enc_string.encode('uu', 'strict')
            return
        else:
            print "Please select either 1, 2, 3, 4, 5, 6, or 7."


# Main function.
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()

    # Adding optional arguments.
    parser.add_argument("string", type=str, help="String to decode")

    # Parsing arguments.
    args = parser.parse_args()

    # Checking arguments:
    if args.string:
        encode_text(args.string)
    else:
        print "run '--help' to see flags"
