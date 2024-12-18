def compute_crc(data, polynomial, crc_length):
    data = ''.join(format(ord(c), '08b') for c in data)  
    data += '0' * crc_length  
    polynomial = int(polynomial, 2)  
    data = int(data, 2)  
    for i in range(len(bin(data)) - crc_length - 2):
        if data & (1 << (len(bin(data)) - 3 - i)):
            data ^= polynomial << (len(bin(data)) - crc_length - 3 - i)
    return format(data, 'b')[-crc_length:].zfill(crc_length)
def crc12(data):
    return compute_crc(data, '1100000001111', 12)
def crc16(data):
    return compute_crc(data, '11000000000000101', 16)
def crc_ccitt(data):
    return compute_crc(data, '10001000000100001', 16)
if __name__ == "__main__":
    data_set = "Hello CRC!"

    print("Data:", data_set)
    print("CRC-12:", crc12(data_set))
    # print("CRC-16:", crc16(data_set))
    # print("CRC-CCITT:", crc_ccitt(data_set))