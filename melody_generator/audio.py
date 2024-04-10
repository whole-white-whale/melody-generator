"""Модуль для работы с аудиофайлами."""

from dataclasses import dataclass

import numpy as np

from numpy.typing import NDArray
from scipy.io import wavfile


@dataclass(frozen=True, slots=True)
class Audio:
    """Аудиофайл."""

    melody: list[str]
    sample_rate: int
    speed: int

    def dump(self, path: str):
        """Записать аудиофайл."""

        wavfile.write(path, self.sample_rate, self.get_wave())

    def get_wave(self) -> NDArray[np.float64]:
        """Получить аудиосигнал."""

        return np.concatenate([self.get_sample(note) for note in self.melody])

    def get_sample(self, note: str) -> NDArray[np.float64]:
        """Получить сэмпл данной ноты."""

        duration = 15.0 / self.speed

        return (
            2.0
            / np.pi
            * np.tan(
                np.sin(
                    2.0
                    * np.pi
                    * self.get_frequency(note)
                    * np.linspace(
                        0.0,
                        duration,
                        int(self.sample_rate * duration),
                        dtype=np.float64,
                    ),
                    dtype=np.float64,
                )
            )
        )

    def get_frequency(self, note: str) -> float:
        """Получить частоту данной ноты."""

        frequencies = {
            "1": 440.00,
            "2": 493.88,
            "3": 523.25,
            "4": 587.33,
            "5": 659.25,
            "6": 698.46,
            "7": 392.00,
        }

        return frequencies[note]
