# Denne funksjonen bruker matplotlib (som er en 2d graf/figur tegner til python), til å tegne en graf basert på våre resultater i "searching.py" filen.
# Den tegner opp en x og y graf for hver av verdiene vi har fått for å sammenligne de grafisk opp imot hverandre.

import matplotlib.pyplot as plt
x = ([2.195, 2.265, 8.753])
y = ([1.572, 1.615, 7.079])

plt.plot(x, linestyle="dashed", marker="o", color="red")
plt.plot(y, linestyle="dashed", marker="o", color="green")
plt.xlim(0.0,3.0)

plt.xlabel("Red= Search_Slow and Green = Search_Fast")

plt.title("Search Algorithm")

plt.show()