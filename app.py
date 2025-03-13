import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #1e1e2f;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button {
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: black;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1>🚀 Universal Unit Converter </h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight & temperature.")

# Sidebar menu
conversion_type = st.sidebar.selectbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
Value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Milligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def length_converter(Value, from_unit, to_unit):
    length_units = {
        'Meters': 1, 'Kilometers': 0.001, 'Centimeters': 100, 'Millimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feet': 3.28, 'Inches': 39.37
    }
    return (Value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(Value, from_unit, to_unit):
    weight_units = {
        'Kilogram': 1, 'Grams': 1000, 'Milligrams': 1000000, 'Pounds': 2.2046, 'Ounces': 35.27
    }
    return (Value / weight_units[from_unit]) * weight_units[to_unit]

def temp_converter(Value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (Value * 9/5 + 32) if to_unit == "Fahrenheit" else Value + 273.15 if to_unit == "Kelvin" else Value
    elif from_unit == "Fahrenheit":
        return (Value - 32) * 5/9 if to_unit == "Celsius" else (Value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else Value
    elif from_unit == "Kelvin":
        return (Value - 273.15) if to_unit == "Celsius" else (Value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else Value
    return Value

# Button for conversion
if st.button("Convert"):
    result = None  # Default value in case no conversion is performed

    if conversion_type == "Length":
        result = length_converter(Value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = weight_converter(Value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = temp_converter(Value, from_unit, to_unit)

    if result is not None:
        st.markdown(f"<div class='result-box'>{Value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Created with ❤️ by Qarer Shah </div>", unsafe_allow_html=True)
