from pathlib import Path
import matplotlib.pyplot as plt


def savefig(path, dpi=180):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout()
    plt.savefig(path, dpi=dpi, bbox_inches="tight")
    plt.show()
