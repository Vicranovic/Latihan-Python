#KODE KEDUA TANPA FUNGSI whileTrue dan Break
def main():
  # Memilih jenis satuan suhu
  print("Pilih jenis satuan suhu (1-4):")
  print("1. Celsius")
  print("2. Reamur")
  print("3. Kelvin")
  print("4. Fahrenheit")

  pilihan_satuan = int(input("Masukkan pilihan (1-4): "))

  # Meminta input temperatur dan satuan
  satuan_input = ""
  if pilihan_satuan == 1:
    satuan_input = "Celsius"
  elif pilihan_satuan == 2:
    satuan_input = "Reamur"
  elif pilihan_satuan == 3:
    satuan_input = "Kelvin"
  elif pilihan_satuan == 4:
    satuan_input = "Fahrenheit"

  nilai_input = float(input("Masukkan nilai temperatur ({}): ".format(satuan_input)))

  # Menampilkan konversi ke 3 satuan lainnya
  print("\nHasil konversi:")
  if pilihan_satuan == 1:
    # Konversi dari Celsius ke Reamur, Kelvin, dan Fahrenheit
    print("Reamur: {:.2f} R".format(nilai_input * 4 / 5))
    print("Kelvin: {:.2f} K".format(nilai_input + 273.15))
    print("Fahrenheit: {:.2f} F".format(nilai_input * 9 / 5 + 32))
  elif pilihan_satuan == 2:
    # Konversi dari Reamur ke Celsius, Kelvin, dan Fahrenheit
    print("Celsius: {:.2f} C".format(nilai_input * 5 / 4))
    print("Kelvin: {:.2f} K".format(nilai_input * 5 / 4 + 273.15))
    print("Fahrenheit: {:.2f} F".format(nilai_input * 9 / 4 + 32))
  elif pilihan_satuan == 3:
    # Konversi dari Kelvin ke Celsius, Reamur, dan Fahrenheit
    print("Celsius: {:.2f} C".format(nilai_input - 273.15))
    print("Reamur: {:.2f} R".format((nilai_input - 273.15) * 4 / 5))
    print("Fahrenheit: {:.2f} F".format(nilai_input * 9 / 5 - 459.67))
  elif pilihan_satuan == 4:
    # Konversi dari Fahrenheit ke Celsius, Reamur, dan Kelvin
    print("Celsius: {:.2f} C".format((nilai_input - 32) * 5 / 9))
    print("Reamur: {:.2f} R".format((nilai_input - 32) * 4 / 9))
    print("Kelvin: {:.2f} K".format((nilai_input + 459.67) * 5 / 9))

main()