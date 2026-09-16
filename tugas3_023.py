# Kalkulator BMI (Body Mass Index)

def hitung_bmi(berat, tinggi_cm):
    """Menghitung nilai BMI dari berat (kg) dan tinggi (cm)"""
    tinggi_m = tinggi_cm / 100  # konversi cm ke meter
    bmi = berat / (tinggi_m ** 2)
    return bmi

def kategori_bmi(bmi):
    """Menentukan kategori BMI"""
    if bmi < 18.5:
        return "Kurus"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesitas"

def main():
    print("======KALKULATOR BMI======")
    berat = float(input("Berat (kg) : "))
    tinggi = float(input("Tinggi (cm) : "))

    bmi = hitung_bmi(berat, tinggi)
    kategori = kategori_bmi(bmi)

    print("====== HASIL======")
    print(f"Berat     : {berat} kg")
    print(f"Tinggi    : {tinggi} cm")
    print(f"BMI       : {bmi}")
    print(f"Kategori  : {kategori}")
    print("=" * 40)

if __name__ == "__main__":
    main()
