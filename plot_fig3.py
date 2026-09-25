# ================= START GABRIEL ADDITION =================
# Custom plotting script for reproducing Figure 3 from the NSphere paper.
# Reads the raw particle output, extracts selected snapshots, bins particle
# radii, and plots the radial particle-number distribution over time.
import numpy as np
import matplotlib.pyplot as plt

filename = "data/all_particle_data_fig3_decay_repeat_1000000_20001_20.dat"


nparticles = 1000000

dtype = np.dtype([
    ("rank", np.int32),
    ("r", np.float32),
    ("vrad", np.float32),
    ("L", np.float32)
])

data = np.memmap(filename, dtype=dtype, mode="r")

nsnapshots = len(data) // nparticles

print("Number of snapshots:", nsnapshots)

data = data.reshape(nsnapshots, nparticles)

timesteps = [0, 4000, 8000, 12000, 16000, 19900]

snapshot_indices = [0, 40, 80, 120, 160, 199]

bins = np.linspace(0, 500, 101)

for timestep, snapshot in zip(timesteps, snapshot_indices):

    radius = data[snapshot]["r"]

    counts, edges = np.histogram(radius, bins=bins)

    centres = (edges[:-1] + edges[1:]) / 2

    plt.plot(
        centres,
        counts,
        label=f"t = {timestep}"
    )

plt.xlabel("Radius (kpc)")
plt.ylabel("Number of Particles")

plt.xlim(0, 500)

plt.legend()

plt.tight_layout()

plt.savefig("results/figure3_reproduction.png", dpi=300)

plt.show()

# ================== END GABRIEL ADDITION ==================