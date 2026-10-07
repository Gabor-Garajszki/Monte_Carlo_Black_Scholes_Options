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

mean_price = np.mean(final_prices)
theoretical_mean = K * np.exp(r * T)
variance = np.var(final_prices, ddof=1)
std_dev = np.std(final_prices, ddof=1)

payoffs = np.maximum(final_prices - K, 0)
expected_payoff = np.mean(payoffs)
standard_error = np.std(payoffs, ddof=1) / np.sqrt(paths)
fair_value = expected_payoff * np.exp(-r * T)

print("-" * 50)
print(f"SIMULATION RESULT ({paths} paths, in {T} years):")
print("-" * 50)
print(f"Simulated average price:    {mean_price:.2f} EUR")
print(f"Theoretical expected value: {theoretical_mean:.2f} EUR")
print(f"Deviation (Error):          {abs(mean_price - theoretical_mean):.2f} EUR")
print("-" * 50)
print(f"Variance of final prices:   {variance:.2f}")
print(f"Std dev of final prices:    {std_dev:.2f} EUR")
print(f"Lowest simulated price:     {np.min(final_prices):.2f} EUR")
print(f"Highest simulated price:    {np.max(final_prices):.2f} EUR\n\n")

print("-" * 50)
print(f"OPTION PRICING (FAIR VALUE):")
print("-" * 50)
print(f"Strike price (Strike):      {K:.2f} EUR")
print(f"Expected payoff (T={T}):    {expected_payoff:.2f} EUR")
print(f"Option Fair Value (Present): {fair_value:.4f} EUR")
print(f"Estimation error (SE):      +/- {standard_error:.4f} EUR")

#plt.title("Geometric Brownian Motion (GBM) - 100 possible stock paths over 5 years")
#plt.xlabel("Time, $t$ (Years)")
#plt.ylabel("Stock price ($S_t$)")
#plt.axhline(K, color='black', linestyle='--', linewidth=1, label="Initial price ($S_0$)")
#plt.grid(True, alpha=0.3)
#plt.legend()
#plt.show()