import numpy as np

from dataclasses import dataclass
from scipy.io import wavfile


@dataclass(frozen=True, slots=True)
class Audio:
    melody: str
    sample_rate: int

    def dump(self, path: str):
        samples, t = [], np.linspace(0.0, 1.0, self.sample_rate)

        for note in self.melody:
            sample = np.sin(2 * np.pi * get_frequency(note) * t)
            samples.append(sample[: int(len(sample) / 3)])

        wavfile.write(path, self.sample_rate, np.concatenate(samples))


def get_frequency(note: str) -> float:
    frequency = 0.0

    match note:
        case "1":
            frequency = 440.00

        case "2":
            frequency = 493.88

        case "3":
            frequency = 523.25

        case "4":
            frequency = 587.33

        case "5":
            frequency = 659.25

        case "6":
            frequency = 698.46

        case "7":
            frequency = 392.00

    return frequency
