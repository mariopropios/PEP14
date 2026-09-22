# EN SISTEMA DECIMAL
bytes_totales = int(input("Introduce el numero de bytes: "))

# 1 KB = 1000 bytes, 1 MB = 1000 KB, 1 GB = 1000 MB
resto = bytes_totales
gb = resto // 1000000000
resto = resto % 1000000000
mb = resto // 1000000
resto = resto % 1000000
kb = resto // 1000
resto = resto % 1000
bytes_dec = resto

print(
    bytes_totales,
    "bytes en sistema decimal (SI):",
    gb,
    "GB,",
    mb,
    "MB,",
    kb,
    "KB,",
    bytes_dec,
    "bytes",
)
# EN SISTEMA BINARIO

# 1 KiB = 1024 bytes, 1 MiB = 1024 KiB, 1 GiB = 1024 MiB
resto2 = bytes_totales
gib = resto2 // 1073741824
resto2 = resto2 % 1073741824
mib = resto2 // 1048576
resto2 = resto2 % 1048576
kib = resto2 // 1024
resto2 = resto2 % 1024
bytes_bin = resto2

print(
    bytes_totales,
    "bytes en sistema binario (IEC):",
    gib,
    "GiB,",
    mib,
    "MiB,",
    kib,
    "KiB,",
    bytes_bin,
    "bytes",
)
