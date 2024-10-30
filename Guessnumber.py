import random

def main():
    print("Selamat datang di Permainan Tebak Angka!")
    print("Saya sedang memikirkan sebuah angka antara 1 dan 100.")
    
    # Menghasilkan angka acak antara 1 dan 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Masukkan tebakan Anda: "))
            attempts += 1

            if guess < number_to_guess:
                print("Terlalu rendah! Coba lagi.")
            elif guess > number_to_guess:
                print("Terlalu tinggi! Coba lagi.")
            else:
                print(f"Selamat! Anda telah menebak angka {number_to_guess} dalam {attempts} percobaan.")
                break
        except ValueError:
            print("Harap masukkan angka yang valid.")

if __name__ == "__main__":
    main()
