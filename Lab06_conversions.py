from Lab06_ip_part1 import is_valid_ip

"""PART 2 - RECURSION AND NUMBER CONVERSION"""

def decimal_to_binary(n):
    if n == 0: return "0"
    if n == 1: return "1"
    next, digit = divmod(n, 2)
    return decimal_to_binary(next) + str(digit)
dtb = decimal_to_binary


# Test cases
# print(dtb(168))
# print(dtb(10))  # "1010"
# print(dtb(255))  # "11111111"
# print(dtb(1))# "1")
# print(dtb(1546))



def binary_to_decimal(b:str):
    if b == '': return 0
    place = len(b) - 1
    return 2**place * int(b[0]) + binary_to_decimal(b.removeprefix(b[0]))

# print(binary_to_decimal("1010"))      # 10
# print(binary_to_decimal("11111111"))  # 255
# print(binary_to_decimal("1"))         # 1



"""PART 3 BONUS"""

def ip_to_binary(ip: str):
    if is_valid_ip(ip):
        part = ip.split('.')
        result = (
            dtb(int(part[0])).zfill(8)
            + '.'
            + dtb(int(part[1])).zfill(8)
            + '.'
            + dtb(int(part[2])).zfill(8)
            + '.'
            + dtb(int(part[3])).zfill(8)
        )
        print(result)

ip_to_binary('192.168.0.1')
ip_to_binary('211.174.1.2')


"""saving this for later study"""
"""this was all code that I tried and reworked and such, leaving for posterity lol."""
# print(dtb(int(part[0])) + (dtb(str(part[1]))) + (dtb(str(part[2]))) + (dtb(str(part([3])))))


    # print(dtb(int(part[0])) + dtb(int(part[1])))
    # print(dtb(int(part[2])))
    # print(dtb(int(part[3])))


    # print(
    #     print(dtb(int(part[0]))),
    #     print(dtb(int(part[1]))),
    #     print(dtb(int(part[2]))),
    #     print(dtb(int(part[3])))
    #     )


# def print_right(text, text2, text3, text4):
    #     print(text, sep='\n')  # I couldn't really figure it out  # so i made this specifically for this one phrase
    #     print(text2, sep='\n')  # I looked at yours after...it's amazing lol
    #     print(end="0" * 7)
    #     print(text3, sep="\n")
    #     print(end="0" * 7)
    #     print(text4, sep='\n')
    # print_right(dtb(int(part[0])), dtb(int(part[1])), dtb(int(part[2])), dtb(int(part[3])))