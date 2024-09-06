#!/usr/bin/python3
""" 0-validate_utf8.py """


def validUTF8(data):
    """ 0-validation_utf8.py """

    # Initialize variables for bits checking (masks)
    continuation_byte = 0

    # Iterate through the data list
    for byte in data:
        # Get the least significant bit (8bits)
        byte = byte & 0xFF

        # Check if the byte is a continuation byte
        if continuation_byte:
            # Check if the byte is a continuation byte
            if byte >> 6 == 0b10:
                continuation_byte -= 1
            else:
                return False
        else:
            # Check how bytes the character has
            if byte >> 7 == 0b0:  # 1-byte character
                continue
            elif byte >> 5 == 0b110:  # 2-byte character
                continuation_byte = 1
            elif byte >> 4 == 0b1110:  # 3-byte character
                continuation_byte = 2
            elif byte >> 3 == 0b11110:  # 4-byte character
                continuation_byte = 3
            else:
                return False
    # Check if there are no continuation bytes, it's a valid UTF-8
    return continuation_byte == 0

    # Setup constants for bits checking (masks)
    # mask1 = 0b10000000
    # mask2 = 0b11000000
    # # Initialize variables for continuation bytes
    # cont_bytes = 0
    # # Iterate through the data
    # for idx in range(len(data)):
    #     # Get the current byte
    #     byte = data[idx]
    #     if cont_bytes == 0:
    #         # Check if the byte is a continuation byte
    #         if byte & mask1 == 0b00000000:
    #             continue
    #         # Check if the byte is a leading byte
    #         elif byte & mask2 == 0b11000000:
    #             cont_bytes = 1
    #         # Check if the byte is a leading byte
    #         elif byte & mask2 == 0b11100000:
    #             cont_bytes = 2
    #         # Check if the byte is a leading byte
    #         elif byte & mask2 == 0b11110000:
    #             cont_bytes = 3
    #         else:
    #             return False
    #     else:
    #         if cont_bytes > 0:
    #             # Check if the byte is a continuation byte
    #             if byte & mask1 == 0b10000000:
    #                 cont_bytes -= 1
    #             else:
    #                 return False
    #     return cont_bytes == 0
    # Check if the byte is a continuation byte
    # check the starting pattern of the byte
    # if byte & 0b10000000 == 0b00000000:
    #     byte1 = 1
    # elif byte & 0b11100000 == 0b11000000:
    #     byte2 = 2
    # elif byte & 0b11110000 == 0b11100000:
    #     byte3 = 3
    # elif byte & 0b11111000 == 0b11110000:
    #     byte4 = 4
    # else:
    #     return False
