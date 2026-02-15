import matplotlib.pylab as plt
plt.figure(figsize=(7,7))
days = ["saturday","sunday","monday","tuesday","wednesday","thursday","friday"]
temps = [22,24,21,26,23,25,20]
plt.plot(days,temps,marker="o")
plt.title("Temperature changes during the week")
plt.grid(True)
plt.xlabel("Days")
plt.ylabel("Celsius")
plt.show()