# 7- MACHINE-LEVEL REPRESENTATION OF PYTHON TYPES

Computers store everything as binary (0s and 1s). Even high-level types like int, float, or str are converted to binary internally.

Example binary sequence:
0 0 0 1 1 0 1 1 0 1 1 1 0 0 0 1 0 1 1 0 ...

Memory is divided into chunks with fixed sizes (powers of 2):

```abap
 ______________________                 _______________________
|  Byte - smallest unit |              |  Word - fundamental   |
|   of addressable mem  |              |  unit (32 or 64 bits) |
|_______________________|              |_______________________|
        |                                           |
  8 bits (1 byte)                         4 or 8 bytes (32/64-bit)

```

### ADDRESSING:

Each byte in memory has a unique address.
Example: machine with 8-bit bytes and 32-bit words:

```abap
Memory view:
Address     Value (Bits)
736424      00111011
736425      00011011
736426      01110001
736427      01100100
```

That’s 4 bytes → 1 full word (if system is 32-bit).

In Python, you don’t work directly with memory addresses, but under the hood, types are stored in memory as binary, just like in C/C++.

Example: inspecting binary representations in Python

```python
x = 25
print("Decimal:", x)
print("Binary:", bin(x))  # Output: 0b11001

# If stored in 32-bit memory, padding is added:
binary_32bit = format(x, '032b')
print("32-bit binary representation:", binary_32bit)

```

Type affects memory interpretation: The same bits can mean different things depending on the type

```python
import struct

# Let's treat same 4 bytes differently
raw_bytes = struct.pack('f', 3.14)  # float packed into 4 bytes
int_version = struct.unpack('I', raw_bytes)[0]
print("Float 3.14 as int (bit-wise):", int_version)
print("Float 3.14 as binary:", format(int_version, '032b'))

```
