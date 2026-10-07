import numpy as np
import matplotlib.pyplot as plt

T = 5.0
D = 252
E = 100
N = int(T * D * E)
dt = T / N
paths = 1000

mu = 0.05
sigma = 0.20
S0 = 100.0

plt.figure(figsize=(10, 5))
time_axis = np.linspace(0, T, N + 1)

final_prices = []

for i in range(paths):
    Z = np.random.normal(0, 1, N)
    dW = Z * np.sqrt(dt)
    
    W = np.zeros(N + 1)
    W[1:] = np.cumsum(dW)
    
    S = S0 * np.exp((mu - 0.5 * sigma**2) * time_axis + sigma * W)
    
    plt.plot(time_axis, S, linewidth=1.0, alpha=0.6)

    final_prices.append(S[-1])

mc_atlag = np.mean(final_prices)

elmeleti_atlag = S0 * np.exp(mu * T)

mc_variancia = np.var(final_prices, ddof=1)
mc_szoras = np.std(final_prices, ddof=1)

print("-" * 50)
print(f"SZIMULÁCIÓ EREDMÉNYE ({paths} út, {T} év múlva):")
print("-" * 50)
print(f"Szimulált átlagos árfolyam: {mc_atlag:.2f} EUR")
print(f"Elméleti várható érték:     {elmeleti_atlag:.2f} EUR")
print(f"Eltérés (Hiba):             {abs(mc_atlag - elmeleti_atlag):.2f} EUR")
print("-" * 50)
print(f"Végső árak varianciája:     {mc_variancia:.2f}")
print(f"Végső árak szórása:         {mc_szoras:.2f} EUR")
print(f"Legkisebb szimulált ár:     {np.min(final_prices):.2f} EUR")
print(f"Legnagyobb szimulált ár:    {np.max(final_prices):.2f} EUR")

plt.title("Geometriai Brown-mozgás (GBM) - 100 lehetséges részvényút 5 év alatt")
plt.xlabel("Idő, $t$ (Év)")
plt.ylabel("Részvény árfolyama ($S_t$)")
plt.axhline(S0, color='black', linestyle='--', linewidth=1, label="Induló árfolyam ($S_0$)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()