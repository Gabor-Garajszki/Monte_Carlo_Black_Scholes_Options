import numpy as np
import matplotlib.pyplot as plt

T = 5.0
D = 252
E = 100
N = int(T * D * E)
dt = T / N
paths = 5000

r = 0.04
sigma = 0.20
K = 100.0

plt.figure(figsize=(10, 5))
time_axis = np.linspace(0, T, N + 1)
final_prices = np.zeros(paths)

for i in range(paths):
    Z = np.random.normal(0, 1, N)
    dW = Z * np.sqrt(dt)
    
    W = np.zeros(N + 1)
    W[1:] = np.cumsum(dW)
    
    S = K * np.exp((r - 0.5 * sigma**2) * time_axis + sigma * W)
    
    #plt.plot(time_axis, S, linewidth=1.0, alpha=0.6)

    final_prices[i] = S[-1]

atlag = np.mean(final_prices)
elmeleti_atlag = K * np.exp(r * T)
variancia = np.var(final_prices, ddof=1)
szoras = np.std(final_prices, ddof=1)

payoffs = np.maximum(final_prices - K, 0)
expected_payoff = np.mean(payoffs)
standard_error = np.std(payoffs, ddof=1) / np.sqrt(paths)
fair_value = expected_payoff * np.exp(-r * T)

print("-" * 50)
print(f"SZIMULÁCIÓ EREDMÉNYE ({paths} út, {T} év múlva):")
print("-" * 50)
print(f"Szimulált átlagos árfolyam: {atlag:.2f} EUR")
print(f"Elméleti várható érték:     {elmeleti_atlag:.2f} EUR")
print(f"Eltérés (Hiba):             {abs(atlag - elmeleti_atlag):.2f} EUR")
print("-" * 50)
print(f"Végső árak varianciája:     {variancia:.2f}")
print(f"Végső árak szórása:         {szoras:.2f} EUR")
print(f"Legkisebb szimulált ár:     {np.min(final_prices):.2f} EUR")
print(f"Legnagyobb szimulált ár:    {np.max(final_prices):.2f} EUR\n\n")

print("-" * 50)
print(f"OPCIÓ ÁRAZÁS (FAIR VALUE):")
print("-" * 50)
print(f"Kötési árfolyam (Strike):   {K:.2f} EUR")
print(f"Várható kifizetés (T={T}):  {expected_payoff:.2f} EUR")
print(f"Opció Fair Value (Jelen):   {fair_value:.4f} EUR")
print(f"Becslés hibája (SE):        +/- {standard_error:.4f} EUR")

#plt.title("Geometriai Brown-mozgás (GBM) - 100 lehetséges részvényút 5 év alatt")
#plt.xlabel("Idő, $t$ (Év)")
#plt.ylabel("Részvény árfolyama ($S_t$)")
#plt.axhline(K, color='black', linestyle='--', linewidth=1, label="Induló árfolyam ($S_0$)")
#plt.grid(True, alpha=0.3)
#plt.legend()
#plt.show()