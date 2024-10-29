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
            Mask <<= 1
            i += 1
        return i
    for i in range(len(data)):
        num = data[i] % 255
        i = check(num)
        if i == 0:
            continue
        if i == 1:
            j = check(data[i + 1])
            if j == 1:
                continue
            else:
                return False
        elif i == 2:
            j = check(data[i + 1])
            if j == 1:
                k = check(data[i + 2])
                if k == 1:
                    i = i + 1
                else:
                    return False
            else:
                return False
        elif i == 3:
            j = check(data[i + 1])
            if j == 1:
                k = check(data[i + 2])
                if k == 1:
                    last = check(data[i + 3])
                    if last == 1:
                        i = i + 2
                    else:
                        return False
                else:
                    return False
            else:
                return False
        elif i == 4:
            j = check(data[i + 1])
            if j == 1:
                k = check(data[i + 2])
                if k == 1:
                    last = check(data[i + 3])
                    if last == 1:
                        m = check(data[i + 4])
                        if m == 1:
                            i = i + 3
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False

    return True
