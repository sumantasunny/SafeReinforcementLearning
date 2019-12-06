import numpy as np
import matplotlib.pyplot as plt

ns = np.load("./results/noshield.npy")
bn = np.load("./results/bigneg.npy")
pr = np.load("./results/preemptive.npy")
po = np.load("./results/post.npy")

plt.plot(ns, c="red", linestyle=":", label="No Shield")
# plt.plot(bn, c="green", label="Big Negative")
plt.plot(pr, c="black", linestyle=":", label="Premetive Shield")
plt.plot(po, c="blue", label="Post Shield")
plt.legend()
plt.xlim([-5,155])
plt.grid()
plt.xlabel("Episode")
plt.ylabel("Score")
plt.show()