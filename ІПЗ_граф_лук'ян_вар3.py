import matplotlib.pyplot as plt
pot_pr = [0.7, 0.82, 2.04, 40]
cab_pr = [0.36, 0.6, 2.3, 44.6]
oni_pr = [0.63, 0.75, 2, 68]
tomat_pr = [0.68, 0.98, 4.5, 29.6]
cuc_pr = [0.87, 1.22, 4.53, 25]
app_pr = [0.99, 1.31, 5.75, 68.9]
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
