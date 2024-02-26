# Ross Compston - Homework 4
# Made with the assistance of ChatGPT


# region Import
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np

# endregion



# region Define Parameters For Normal Dist
mu1, sigma1 = 0, 1
mu2, sigma2 = 1.75, 3

# endregion



# region Calculate probabilities
p_x_less_1 = stats.norm(mu1, sigma1).cdf(1)
p_x_greater_mu2_2sigma = 1 - stats.norm(mu2, sigma2).cdf(mu2 + 2*sigma2)

print(f"Probability x < 1 for N(0,1): {p_x_less_1}")
print(f"Probability x > mu + 2*sigma for N(1.75,3): {p_x_greater_mu2_2sigma}")

# endregion


# region Plotting
# Generate data for plotting
x = np.linspace(-10, 10, 1000)
y_pdf1 = stats.norm(mu1, sigma1).pdf(x)
y_cdf1 = stats.norm(mu1, sigma1).cdf(x)
y_pdf2 = stats.norm(mu2, sigma2).pdf(x)
y_cdf2 = stats.norm(mu2, sigma2).cdf(x)

# Create plots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot PDF for the first distribution
axs[0, 0].plot(x, y_pdf1, 'r-', label=f'N({mu1},{sigma1}) PDF')
axs[0, 0].set_title('Probability Density Function')
axs[0, 0].legend()

# Plot CDF for the first distribution
axs[0, 1].plot(x, y_cdf1, 'b-', label=f'N({mu1},{sigma1}) CDF')
axs[0, 1].set_title('Cumulative Distribution Function')
axs[0, 1].legend()

# Plot PDF for the second distribution
axs[1, 0].plot(x, y_pdf2, 'g-', label=f'N({mu2},{sigma2}) PDF')
axs[1, 0].set_title('Probability Density Function')
axs[1, 0].legend()

# Plot CDF for the second distribution
axs[1, 1].plot(x, y_cdf2, 'm-', label=f'N({mu2},{sigma2}) CDF')
axs[1, 1].set_title('Cumulative Distribution Function')
axs[1, 1].legend()

# Display the plot

# endregion

plt.tight_layout()
plt.show()
