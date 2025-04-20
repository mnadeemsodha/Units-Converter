import streamlit as st
from pint import UnitRegistry

# Set up the unit registry
ureg = UnitRegistry()

# Define available categories and units
unit_categories = {
    "Length": ["meter", "kilometer", "mile", "yard", "foot", "inch"],
    "Weight": ["gram", "kilogram", "pound", "ounce"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Volume": ["liter", "milliliter", "gallon", "fluid_ounce"]
}

st.title("🔄 Google Style Unit Converter")

# Select category
category = st.selectbox("Select Unit Type", list(unit_categories.keys()))

# Select units
units = unit_categories[category]
from_unit = st.selectbox("Convert from", units)
to_unit = st.selectbox("Convert to", units)

# Input value
value = st.number_input(f"Enter value in {from_unit}", value=0.0, step=1.0)

# Convert and show result
if st.button("Convert"):
    try:
        input_quantity = value * ureg(from_unit)
        output_quantity = input_quantity.to(to_unit)
        st.success(f"{value} {from_unit} = {output_quantity:.3f}")
    except Exception as e:
        st.error(f"Conversion error: {e}")
