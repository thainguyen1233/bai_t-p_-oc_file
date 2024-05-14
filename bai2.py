def nhap_du_lieu_khach(input):
    with open(input, "r") as file:
        so_luong_khach = int(file.readline())
        tong_trong_luong = []
        danh_sach_khach_bi_huy = []

        for i in range(so_luong_khach):
            trong_luong_hanh_ly = list(map(float, file.readline().split()))
            tong_trong_luong_hanh_ly = sum(trong_luong_hanh_ly)
            tong_trong_luong.append(tong_trong_luong_hanh_ly)

            if tong_trong_luong_hanh_ly > 20 or len(trong_luong_hanh_ly) > 5:
                danh_sach_khach_bi_huy.append(i + 1)

    with open("TRONGLUONG.RA", "w") as file:
        for trong_luong in tong_trong_luong:
            file.write(f"{trong_luong:.1f}\n")

    with open("HUYBAY.RA", "w") as file:
        for khach in danh_sach_khach_bi_huy:
            file.write(f"{khach}\n")

if __name__ == "__main__":
    nhap_du_lieu_khach("KHACHBAY.vào")
