import streamlit as st

def unit_conversion(value,from_unit, to_unit, category):
  if category == "Length":
    conversion_factors = {
      "Meter":1,"Kilometer":0.001, "Centimeter":100, "Millimeter":1000, "Mile":0.000621371, "Yard":1.09361, "Foot":3.28084, 
      "Inch":39.3701
    }
  elif category == "Weight":
    conversion_factors = {
      "Kilogram":1, "Gram":1000, "Pound":2.20462, "Ounce":35.0274
    }
  elif category == "Temperature":
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
      return(value * 9/5) +32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
      return (value -32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
      return (value + 273.15)
    elif from_unit == "Kelvin" and to_unit == "Celsius":
      return (value - 273.15)
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
      return (value -32)*5/9 +273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
      return (value -273.15) *9/5 +32 
  return value * conversion_factors[to_unit] / conversion_factors[from_unit]

st.title("Unit Converter")

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

unit_options = {
 "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
 "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
 "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

from_unit = st.selectbox("From", unit_options[category])

to_unit = st.selectbox("To", unit_options[category])

value = st.number_input("Enter value", min_value=0.0, format="%.4f")

if st.button("Conversion"):
  result = unit_conversion(value, from_unit, to_unit, category)
  st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")




