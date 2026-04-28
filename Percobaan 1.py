def menu():
    print("1. Tampilkan address array")
    print("2. Tampilkan address dari semua index array")
    print("3. Masukkan nilai kedalam semua index array")
    print("4. Cek isi indeks")
    print("5. Keluar")
          
def main():
    a = [0] * 5
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue
        if choice == 1:
            print(f"Address array: {id(a)}")
        elif choice == 2:
            for i in range(5):
                print(f"Address a[{i}]: {id(a[i])}")
        elif choice == 3:
            print("Masukkan 5 nilai:")
            for i in range(5):
                while True:
                    try:
                        a[i] = int(input(f"a[{i}] = "))
                        break
                    except ValueError:
                        print("Input tidak valid, silakan masukkan angka!")
            print(f"Array sekarang: {a}")

        elif choice == 4:
            try:
                index = int(input("Masukkan index (0-4): "))
                if 0 <= index < len(a):
                    print(f"Isi a[{index}] = {a[index]}")
                else:
                    print("index di luar batas array!")
            except ValueError:
                print("Inddex harus berupa angka!")

        elif choice == 5:
            running = False
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()

            

