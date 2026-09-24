Transmission Line Calculations
Power Systems-II
Medium Transmission Line - Nominal Pi Model

import math
import cmath

def calculate_line_parameters(length, resistance_per_km, inductance_per_km,
capacitance_per_km, frequency):
"""Calculate total R, X, and B of the transmission line."""

R = resistance_per_km * length

L = inductance_per_km * 1e-3 * length       # mH/km to H
C = capacitance_per_km * 1e-6 * length     # uF/km to F

omega = 2 * math.pi * frequency

X = omega * L
B = omega * C

return R, X, B


def calculate_abcd(R, X, B):
"""
Calculate ABCD parameters for the nominal-pi model.

Series impedance:
    Z = R + jX

Shunt admittance:
    Y = jB

For nominal-pi:
    A = D = 1 + YZ/2
    B = Z(1 + YZ/4)
    C = Y(1 + YZ/4)
"""

Z = complex(R, X)
Y = complex(0, B)

A = 1 + (Y * Z) / 2
B_parameter = Z * (1 + (Y * Z) / 4)
C = Y * (1 + (Y * Z) / 4)
D = A

return A, B_parameter, C, D


print("=" * 55)
print(" TRANSMISSION LINE CALCULATOR")
print(" POWER SYSTEMS - II")
print("=" * 55)

try:
length = float(input("Enter transmission line length (km): "))
resistance_per_km = float(input("Enter resistance (ohm/km): "))
inductance_per_km = float(input("Enter inductance (mH/km): "))
capacitance_per_km = float(input("Enter capacitance (uF/km): "))
frequency = float(input("Enter frequency (Hz): "))

if length <= 0:
    raise ValueError("Line length must be positive.")

if resistance_per_km < 0:
    raise ValueError("Resistance cannot be negative.")

if inductance_per_km < 0:
    raise ValueError("Inductance cannot be negative.")

if capacitance_per_km < 0:
    raise ValueError("Capacitance cannot be negative.")

if frequency <= 0:
    raise ValueError("Frequency must be positive.")

# Calculate line parameters
R, X, B = calculate_line_parameters(
    length,
    resistance_per_km,
    inductance_per_km,
    capacitance_per_km,
    frequency
)

# Calculate ABCD parameters
A, B_parameter, C, D = calculate_abcd(R, X, B)

print("\n" + "=" * 55)
print("                 RESULTS")
print("=" * 55)

print(f"Total Resistance (R)       : {R:.4f} ohm")
print(f"Total Inductive Reactance   : {X:.4f} ohm")
print(f"Total Shunt Susceptance (B) : {B:.8f} S")

print("\nABCD PARAMETERS")
print("-" * 55)

print(f"A = {A.real:.6f} + j{A.imag:.6f}")
print(f"B = {B_parameter.real:.6f} + j{B_parameter.imag:.6f} ohm")
print(f"C = {C.real:.8f} + j{C.imag:.8f} S")
print(f"D = {D.real:.6f} + j{D.imag:.6f}")

print("=" * 55)


except ValueError as error:
print(f"\nError: {error}")
