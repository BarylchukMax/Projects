import matplotlib.pyplot as plt
pot_pr = [0.66, 0.75, 2.03, 39.8]
cab_pr = [0.59, 0.75, 2.03, 69.5]
oni_pr = [0.36, 0.6, 2.35, 44.8]
tomat_pr = [0.69, 0.95, 4.45, 29.6]
cuc_pr = [0.85, 1.24, 4.55, 25]
app_pr = [0.99, 1.33, 5.75, 69]
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
