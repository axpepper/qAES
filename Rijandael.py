import cirq
from sage.all import *

# from sbox_gates import FormulaQubit, SboxCNOT, SboxToffoli
'''
BL+RS Grover AES,  https://arxiv.org/pdf/1512.04965.pdf

'''


class AESVariables():
    def __init__(self):
    	self.KEY = [
    		cirq.NamedQubit("KEY" + str(i)) for i in range(128)
    	]
        self.word1 = [
            cirq.NamedQubit("w1_" + str(i)) for i in range(32)
        ]
        self.word2 = [
        	cirq.NamedQubit("w2_" + str(i)) for i in range(32)
        ]
        self.word3 = [
        	cirq.NamedQubit("w3_" + str(i)) for i in range(32)
        ]
        self.word4 = [
        	cirq.NamedQubit("w4_" + str(i)) for i in range(32)
        ]
        self

def configure_circuit_input(configuration, orig_circuit=None, input_bit_list = []):

    moment_ops = []
    for k in range(len(input_bit_list)):  # initialize Ubox to given ival
        if input_bit_list[k]:
            # X | U[k]
            # circuit.append()
            moment_ops.append(cirq.ops.X.on(configuration.U[k]))

    # TODO: Doubts
    circuit = cirq.Moment(moment_ops) + orig_circuit

    return circuit


def rc(i):
	if i==1:
		RC = initial_word()
		yield RC
	if temp < 256:
		return temp
	else:
		return []
	raise StopIteration
 
def initial_word():
	RC = [cirq.NamedQubit("R" + str(i)) for i in range(8)]
	circuit.append(cirq.X(RC[0]))
	print(RC)
	return RC

def rotword(word):
	word[0:8],word[8:16],word[16:24],word[24:32] = word[8:16],word[16:24],word[24:32],word[0:8]
	return word

def subword(word):
	for offset in range(0,32,8):
		sbox(word[offset:offset+8])


def initial_word():
	pass

def keyExpansion():
	pass

def addRoundKey():
	pass

def subBytes():
	pass

def shiftRows():
	pass

def mixColumns():
	'''
	https://eprint.iacr.org/2019/833.pdf
	92 XOR
	'''
	pass

def subbyte(byte):
	return(byte)

def aes(bits, input):
	circuit = cirq.Circuit()
	print(next(rc(1)))
	print(circuit)

def main():
	print("test")
	aes(0,0)

if __name__ == "__main__":
	main()
