import matplotlib

from constants import TYPE_A

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import Patch
import os


class WorldRenderer:
    def __init__(self, world, out_dir="frames"):
        os.makedirs(out_dir, exist_ok=True)
        self.out_dir = out_dir
        cmap = ListedColormap(["beige", "blue", "green", "orange"])
        self.fig, ax = plt.subplots(figsize=(8, 8))
        self.img = ax.imshow(world, cmap=cmap, vmin=0, vmax=3, interpolation="nearest")
        self.title = ax.set_title("")
        ax.axis("off")
        ax.legend(
            handles=[
                Patch(color=c, label=l)
                for c, l in [
                    ("beige", "Empty"),
                    ("blue", "Water"),
                    ("green", "Grass"),
                    ("orange", "Type A"),
                ]
            ],
            loc="upper right",
            bbox_to_anchor=(1.25, 1),
        )
        self.fig.tight_layout()

    def save(self, world, organisms, day, year):
        frame = world.copy()  # keep terrain untouched
        for o in organisms:
            frame[o["coordinates"]] = TYPE_A
        self.img.set_data(frame)  # just swap the data
        self.title.set_text(f"Year {year}, day {day}")
        self.fig.savefig(f"{self.out_dir}/world_{year:04d}_{day:03d}.png", dpi=100)

    def close(self):
        plt.close(self.fig)
