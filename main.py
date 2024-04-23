
import pandas as pd
import matplotlib.pyplot as plt


gia_dong_cua = [100, 105, 102, 110, 107, 113, 108, 111, 115, 112, 109, 116]


df = pd.DataFrame(gia_dong_cua, columns=["Gia Dong Cua"])



df["SMA 10"] = df["Gia Dong Cua"].rolling(window=10, min_periods=1).mean()


print(df)

# tạo biểu đồ
plt.figure(figsize=(10, 6))
plt.plot(df["Gia Dong Cua"], label="Giá Đóng Cửa", linestyle='-', marker='o')  
plt.plot(df["SMA 10"], label="SMA 10", linestyle='-', color='orange')  
plt.title("Biểu đồ Đường với SMA 10")
plt.xlabel("Ngày")
plt.ylabel("Giá trị")
plt.legend()  
plt.grid(True)  
plt.show()  