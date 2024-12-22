from dataclasses import dataclass
from typing import Optional, Literal
from .physics.friction import local_pressure_drop  # Ensure this import is correct based on your project structure
from .physics.general import calc_velocity

@dataclass
class Connector:
    id: str = None
    shape: Literal["round", "rectangular"] = "round"
    diameter: float = None
    width: float = None
    height: float = None
    flowrate: Optional[float] = None
    area: Optional[float] = None
    velocity: Optional[float] = None
    dzeta: Optional[float] = None
    pressure_drop: Optional[float] = None

    def calculate_velocity(self) -> float:
        print(f"Calculating velocity with flowrate={self.flowrate} and area={self.area}")
        self.velocity = calc_velocity(self.flowrate, self.area)
        print(f"Calculated velocity: {self.velocity}")

    def calculate_pressure_drop(self, area: float, dzeta: float) -> None:
        """
        Calculate the pressure drop at the connector interface.
        """
        print(f"Calculating pressure drop with area={area}, dzeta={dzeta}")
        self.area = area
        self.dzeta = dzeta
        self.calculate_velocity()
        print(f"Velocity calculated: {self.velocity}")  # Check velocity
        self.pressure_drop = local_pressure_drop(self.dzeta, self.velocity)
        print(f"Pressure drop calculated: {self.pressure_drop}")  # Check the pressure drop value
