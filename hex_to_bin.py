#hex_str="0x1234_5678"
#bin_value=bin(int(hex_str,16))[2:]
#print(bin_value)

def hex_bin(hex_str):
    return bin(int(hex_str,16))[2:]

def hex_bin_cut(hex_str,start_bit,end_bit):
    bit_val = bin(int(hex_str,16))[2:]
    return bit_val[1-end_bit:0-start_bit]

def get_dcache_set_index(va):
    #256setx4way
    return hex_bin_cut(va,6,13)
    
def get_mmu_set_index(va):
    #256setx8way
    return hex_bin_cut(va,12,19)


print(hex_bin("000f"))
print(hex_bin_cut("0210",4,12))
