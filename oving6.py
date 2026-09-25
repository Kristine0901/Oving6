import numpy as np 
import matplotlib.pyplot as plt 

def G(t,A, my, sigma):
    solinnstraling = A * np.exp(-(t-my)**2 / (2*sigma**2))
    return solinnstraling



tidsakse = np.linspace(0, 23, 23)

A = 800
my = 13

sigma = 3

plt.plot(tidsakse,G(tidsakse, A, my, sigma))
plt.xlabel("Tid [timer]")
plt.ylabel("Innstråling [W/m²]")
plt.grid()
plt.savefig("Ovinger/Oving6/SolinnstralingEnSigma.png")

plt.show()

#Hvordan påvirker sigma modellen? 

plt.plot(tidsakse,G(tidsakse, A, my, 3))
plt.plot(tidsakse,G(tidsakse, A, my, 5))
plt.plot(tidsakse,G(tidsakse, A, my, 1))
plt.xlabel("Tid [timer]")
plt.ylabel("Innstråling [W/m²]")
plt.grid()
plt.savefig("Ovinger/Oving6/SolinnstralingTreSigmaer.png")
plt.show()
