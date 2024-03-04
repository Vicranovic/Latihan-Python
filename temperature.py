# 1. Ganti celsius ke fahrenheit
def celsius_ke_fahrenheit(celsius):
  return celsius * 9 / 5 + 32

2# 2. Ganti celsius ke reamur
def celsius_ke_reamur(celsius):
   return celsius * 4 / 5

# 3. Ganti celsius ke kelvin
def celsius_ke_kelvin(celsius):
    return celsius + 273.15

# 4. Masukkan input dalam celsius
def main():
    celsius = float(input("masukkan angka dalam celsius: "))
    fahrenheit = celsius_ke_fahrenheit(celsius)
    reamur = celsius_ke_reamur(celsius)
    kelvin = celsius_ke_kelvin(celsius)
    print(f"{celsius} Celsius setara dengan {fahrenheit:.2f} Fahrenheit.")
    print(f"{celsius} Celsius setara dengan {reamur:.2f} Reamur.")
    print(f"{celsius} Celsius setara dengan {kelvin:.2f} Kelvin.")

# 5. Memanggil fungsi main di akhir kode
main()
