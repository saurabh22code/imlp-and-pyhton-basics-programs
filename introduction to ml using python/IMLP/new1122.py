#input value
bits=float(input("Enter bits:"))

#conversion to bytes
bytes=bits/8
print(f"{bits}bits ={bytes}Bytes")

#conersion to kilobytes
Kilobytes=bytes/1024
print(f"{bytes} Bytes= {Kilobytes}kB")

#conversion to Megabytes
Megabytes=Kilobytes/1024
print(f"{Kilobytes}Kilobytes = {Megabytes}mB")

#conversion to Gigabytes
Gigabytes=Megabytes/1024
print(f"{Megabytes}Megabytes = {Gigabytes}gB")
