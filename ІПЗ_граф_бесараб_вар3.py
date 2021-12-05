import matplotlib.pyplot as plt
pot_pr = [0.74, 0.83, 2.08, 70]
cab_pr = [0.38, 0.65, 2.4, 45]
oni_pr = [0.63, 0.79, 2.04, 40]
tomat_pr = [0.69, 0.99, 4.52, 30]
cuc_pr = [0.88, 1.24, 4.56, 25]
app_pr = [1, 1.33, 5.77, 70]
year = [2007, 2008, 2011, 2017]

plt.plot(year, pot_pr, marker = 'o', markersize = 3, linewidth = 2, color = 'red', label = "Картопля")
plt.plot(year, cab_pr, marker = 'o', markersize = 3, linewidth = 2, color = 'green', label = "Капуста")
plt.plot(year, oni_pr, marker = 'o', markersize = 3, linewidth = 2,color = 'blue', label = "Цибуля")
plt.plot(year, tomat_pr, marker = 'o', markersize = 3, linewidth = 2, color = 'orange', label = "Помідори")
plt.plot(year, cuc_pr, marker = 'o', markersize = 3, linewidth = 2, color = 'yellow', label = "Огірки")
plt.plot(year, app_pr, marker = 'o', markersize = 3, linewidth = 2, color = 'lightgreen', label = "Яблука")
plt.xlabel("Рік")
plt.ylabel("Ціна")
plt.legend()
plt.grid()
plt.show()
