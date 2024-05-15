def nhap_du_lieu_khach(input):
    with open(input, "r") as file:
        so_luong_khach = int(file.readline())
        print(f"Số lượng khách: {so_luong_khach}")
        print("Dữ liệu từng khách:")

        for i in range(so_luong_khach):
            trong_luong_hanh_ly = list(map(float, file.readline().split()))
            print(f"Khách {i + 1}: {trong_luong_hanh_ly}")

            tong_trong_luong_hanh_ly = sum(trong_luong_hanh_ly)
            if tong_trong_luong_hanh_ly > 20 or len(trong_luong_hanh_ly) > 5:
                print(f"Khách {i + 1} bị hủy chuyến bay")

if __name__ == "__main__":
    nhap_du_lieu_khach("KHACHBAY.vào")
