#taking input of data in bits
bits=float(input("enter data in bits: "))

#conversion to bytes
byte=bits/8
print(f"{bits} bits = {byte} bytes")

#conversion to kilobytes
kilobyte=byte/1024
print(f"{byte} byte = {kilobyte} KB")

#conversion to megabytes
megabyte=kilobyte/1024
print(f"{kilobyte} KB = {megabyte} MB")

#converion to gigabytes
gigabytes=megabyte/1024
print(f"{megabyte} MB = {gigabytes} GB")