#!/usr/bin/python3
"""
utf-8 validation
"""


def validUTF8(data):
    """
    Check if a string is valid UTF-8 encoded.
    """
    def check(num):
        """
        bitmask function
        """
        Mask = 1 << 7
        i = 0
        while Mask & num:
            Mask >>= 1
            i += 1
        return i
    index = 0
    while(index < len(data)):
        num = data[index] % 256
        i = check(num)
        if i == 0:
            index += 1
            continue
        elif i == 1:
            return False
        for j in range(1, i):
            if(index + j > len(data) - 1):
                return False
            num = data[index + j] % 256
            if not (check(num) == 1):
                return False
        index += i
    return True


data = [197,130,1]
print(validUTF8(data))