# Program Biodata Kelompok
#Ingel_F5212510015
def tampilkan_biodata():
    print("=" * 40)
    print("         BIODATA ANGGOTA KELOMPOK       ")
    print("=" * 40)
    
    anggota_kelompok = [
        {
            "nama": "sintondo",
            "nim": "12345",
            "peran": "Ketua Kelompok"
        },
        {
            "nama": "ribelv",
            "nim": "678910",
            "peran": "Anggota 1"
        },
        {
            "nama": "sepertiga",
            "nim": "012345",
            "peran": "Anggota 2"
        }
    ]

    for index, anggota in enumerate(anggota_kelompok, start=1):
        print(f"Anggota Ke-{index}:")
        print(f"  Nama  : {anggota['nama']}")
        print(f"  NIM   : {anggota['nim']}")
        print(f"  Peran : {anggota['peran']}")
        print("-" * 40)

if __name__ == "__main__":
    tampilkan_biodata()