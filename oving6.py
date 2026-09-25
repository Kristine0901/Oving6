import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

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

#Del 2: Hent data fra PVGIS
#Bredde og lengdegrader: 58.380494, 6.041657 (Stikkshaug, stapnes)

df = pd.read_csv("Ovinger/Oving6/SolinnstralingStapnes.csv", skiprows = 8)
df = df.iloc[4344:4368]
df["G(i)"] = pd.to_numeric(
    df["G(i)"],
    errors="coerce"
)

df["time"] = np.arange(len(df))
print(df.head())
plt.plot(df["time"], df["G(i)"])
plt.xticks(np.arange(0,25,1))
plt.xlabel("Tid [timer]")
plt.ylabel("Global solinnstråling [W/m²]")
plt.title("Solinnstråling på Stikkshaugen, Stapnes, 1.juli 2025")
plt.grid()
plt.savefig("Ovinger/Oving6/SolinnstrålingStikkshaugen.png")
plt.show()

#Oppgave 6, plott de i samme figur

plt.plot(df["time"], df["G(i)"])
plt.plot(tidsakse,G(tidsakse, A, my, sigma))
plt.xticks(np.arange(0,25,1))
plt.xlabel("Tid [timer]")
plt.ylabel("Global solinnstråling [W/m²]")
plt.title("Solinnstråling på Stikkshaugen, Stapnes, 1.juli 2025, og solinnstråling modell med Gauss-Seidel og maks 800 [W/m^2] kl 13")
plt.grid()
plt.legend()
plt.savefig("Ovinger/Oving6/PlottSolinstralingBegge.png")
plt.show()

#oppgave 7, juster parameterene
A= 987.32
sigma = 2.4

plt.plot(df["time"], df["G(i)"])
plt.plot(tidsakse,G(tidsakse, A, my, sigma))
plt.xticks(np.arange(0,25,1))
plt.xlabel("Tid [timer]")
plt.ylabel("Global solinnstråling [W/m²]")
plt.title("Solinnstråling på Stikkshaugen, Stapnes, 1.juli 2025, og solinnstråling modell med Gauss-Seidel og maks 800 [W/m^2] kl 13")
plt.grid()
plt.legend()
plt.savefig("Ovinger/Oving6/PlottSolinstralingBegge2.png")
plt.show()