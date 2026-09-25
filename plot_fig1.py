import numpy as np
import matplotlib.pyplot as plt

filename = "init/fig1_initial_200m.bin"

with open(filename, "rb") as f:
    nparticles = np.fromfile(f, dtype=np.int32, count=1)[0]

print("Number of particles:", nparticles)

data = np.memmap(
    filename,
    dtype=np.float64,
    mode="r",
    offset=4,
    shape=(nparticles, 7)
)

r = data[:, 0]
v = data[:, 1]

plt.hist2d(
    r,
    v,
    bins=300,
    range=[[0, 250], [0, 300]]
)

plt.xlabel("Radius (kpc)")
plt.ylabel("Velocity (km/s)")

plt.xlim(0, 250)
plt.ylim(0, 300)

plt.colorbar(label="Number of Particles")

plt.tight_layout()
plt.savefig("results/figure1_reproduction_200m.png", dpi=300)

plt.show()