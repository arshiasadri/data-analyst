import matplotlib.pylab as plt
months = ["April", "May", "June", "July", "August"]
sales = [120, 150, 170, 130, 160]
# plt.plot(months,sales,color="red",linewidth=5)
plt.bar(months,sales,color="Green")
plt.title("monthly sales volum")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()