#3 thuộc tính của file 
# thuộc tính trong css 
#kiểm tra giá trị của thuộc tính 
# Đọc dữ liệu từ tệp
# Mở tệp foo.txt để đọc dữ liệu
# Đọc dữ liệu từ foo.txt và thêm dữ liệu mới
# Mở tệp foo.txt và thêm dữ liệu mới
with open("foo.txt", "r+") as fo:
    data = fo.read()
    data += "4\n 241 164 180 2\n 162 81 102 96\n 169 197 80 153\n"
    fo.write(data)

# Đọc lại dữ liệu sau khi đã thêm
with open("foo.txt", "r") as fo:
    rep = fo.readlines()

# In ra thông báo kết quả
print("Kết quả hiển thị")
print("Dòng 1:", rep[0].strip())
print("Dòng 2:", rep[2].strip())

# Tìm các số lẻ trong file và ghi chúng vào tệp sole.txt dưới dạng ma trận 4x4
with open("foo.txt", "r") as fo:
    data = fo.read()

# Chuyển dữ liệu thành danh sách các số nguyên
numbers = [int(num) for num in data.split() if num.isdigit()]

# Lọc ra các số lẻ
odd_numbers = [num for num in numbers if num % 2 != 0]

# Kiểm tra xem có đủ số lẻ để tạo ma trận 4x4 không
if len(odd_numbers) >= 16:
    # Ghi các số lẻ vào sole.txt dưới dạng ma trận 4x4
    with open("sole.txt", "w") as fo:
        for i in range(0, 16, 4):
            fo.write(' '.join(str(num) for num in odd_numbers[i:i+4]) + '\n')
else:
    print("Không đủ số lẻ để tạo ma trận 4x4.")

# Mở tệp sole.txt và đọc nội dung
with open("sole.txt", "r") as file:
    lines = file.readlines()

# Kiểm tra nếu tệp không trống
if lines:
    # In ra dòng cuối cùng
    print("Nội dung cuối cùng của tệp 'sole.txt':")
    print(lines[-1].strip())
