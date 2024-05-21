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
##

def tinh_tan_suat_tu(nhap_vao):
    # Tách chuỗi nhập vào thành các từ
    cac_tu = nhap_vao.split()

    # Tạo một từ điển rỗng để lưu tần suất của từ
    tan_suat_tu = {}

    # Lặp qua từng từ và cập nhật số lần xuất hiện trong từ điển
    for tu in cac_tu:
        if tu in tan_suat_tu:
            tan_suat_tu[tu] += 1
        else:
            tan_suat_tu[tu] = 1

    # Sắp xếp danh sách các từ duy nhất theo thứ tự bảng chữ cái
    cac_tu_sap_xep = sorted(tan_suat_tu.keys())

    # In ra tần suất của từ
    for tu in cac_tu_sap_xep:
        print(f"{tu}: {tan_suat_tu[tu]}")

# Hàm chính để chạy chương trình
def chuong_trinh_chinh():
    while True:
        try:
            cau_nhap = input("Nhập một câu: ")
            if any(ky_tu in cau_nhap for ky_tu in "!@#$%^&*()_+"):
                raise ValueError("Dữ liệu không được chứa kí tự đặc biệt!")
            break
        except ValueError as ve:
            print(ve)

    tinh_tan_suat_tu(cau_nhap)

# Điểm bắt đầu của chương trình
if __name__ == "__main__":
    chuong_trinh_chinh()

