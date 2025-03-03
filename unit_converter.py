# import streamlit as st

# # Define conversion functions
# def convert_length(value, from_unit, to_unit):
#     length_conversions = {
#         'meter': 1.0,
#         'kilometer': 1000.0,
#         'centimeter': 0.01,
#         'millimeter': 0.001,
#         'mile': 1609.34,
#         'yard': 0.9144,
#         'foot': 0.3048,
#         'inch': 0.0254
#     }
#     return value * length_conversions[from_unit] / length_conversions[to_unit]

# def convert_weight(value, from_unit, to_unit):
#     weight_conversions = {
#         'kilogram': 1.0,
#         'gram': 0.001,
#         'milligram': 0.000001,
#         'tonne': 1000.0,
#         'pound': 0.453592,
#         'ounce': 0.0283495
#     }
#     return value * weight_conversions[from_unit] / weight_conversions[to_unit]

# def convert_temperature(value, from_unit, to_unit):
#     if from_unit == 'celsius':
#         if to_unit == 'fahrenheit':
#             return (value * 9/5) + 32
#         elif to_unit == 'kelvin':
#             return value + 273.15
#         else:
#             return value
#     elif from_unit == 'fahrenheit':
#         if to_unit == 'celsius':
#             return (value - 32) * 5/9
#         elif to_unit == 'kelvin':
#             return (value - 32) * 5/9 + 273.15
#         else:
#             return value
#     elif from_unit == 'kelvin':
#         if to_unit == 'celsius':
#             return value - 273.15
#         elif to_unit == 'fahrenheit':
#             return (value - 273.15) * 9/5 + 32
#         else:
#             return value
#     else:
#         return value

# # Streamlit app
# st.set_page_config(page_title="Professional Unit Converter", page_icon="📏", layout="centered")

# # Custom CSS for styling
# st.markdown("""
#     <style>
#     .stApp {
#         background-color: #f0f2f6;
#     }
#     h1 {
#         color: #4a90e2;
#         text-align: center;
#     }
#     .stSelectbox, .stNumberInput {
#         background-color: #ffffff;
#         border-radius: 10px;
#         padding: 10px;
#     }
#     .stButton button {
#         background-color: #4a90e2;
#         color: white;
#         border-radius: 10px;
#         padding: 10px 20px;
#         font-size: 16px;
#     }
#     .stMarkdown {
#         font-size: 18px;
#         color: #333333;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Title with emoji
# st.title("📏 Professional Unit Converter")

# # Select the type of conversion
# conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# # Define units based on conversion type
# if conversion_type == "Length":
#     units = ['meter', 'kilometer', 'centimeter', 'millimeter', 'mile', 'yard', 'foot', 'inch']
# elif conversion_type == "Weight":
#     units = ['kilogram', 'gram', 'milligram', 'tonne', 'pound', 'ounce']
# elif conversion_type == "Temperature":
#     units = ['celsius', 'fahrenheit', 'kelvin']

# # Input value and units
# col1, col2, col3 = st.columns(3)
# with col1:
#     value = st.number_input("Enter the value to convert", value=1.0, step=0.1)
# with col2:
#     from_unit = st.selectbox("From unit", units)
# with col3:
#     to_unit = st.selectbox("To unit", units)

# # Perform conversion
# if conversion_type == "Length":
#     result = convert_length(value, from_unit, to_unit)
# elif conversion_type == "Weight":
#     result = convert_weight(value, from_unit, to_unit)
# elif conversion_type == "Temperature":
#     result = convert_temperature(value, from_unit, to_unit)

# # Display the result with a colorful box
# st.markdown(f"""
#     <div style="background-color: #4a90e2; padding: 20px; border-radius: 10px; text-align: center;">
#         <h2 style="color: white;">Converted Value</h2>
#         <p style="font-size: 24px; color: white;">{result:.2f} {to_unit}</p>
#     </div>
#     """, unsafe_allow_html=True)

# # Footer
# st.markdown("---")
# st.markdown("Made with ❤️ using Streamlit")


# import streamlit as st

# # Define conversion functions
# def convert_length(value, from_unit, to_unit):
#     length_conversions = {
#         'meter': 1.0,
#         'kilometer': 1000.0,
#         'centimeter': 0.01,
#         'millimeter': 0.001,
#         'mile': 1609.34,
#         'yard': 0.9144,
#         'foot': 0.3048,
#         'inch': 0.0254
#     }
#     return value * length_conversions[from_unit] / length_conversions[to_unit]

# def convert_weight(value, from_unit, to_unit):
#     weight_conversions = {
#         'kilogram': 1.0,
#         'gram': 0.001,
#         'milligram': 0.000001,
#         'tonne': 1000.0,
#         'pound': 0.453592,
#         'ounce': 0.0283495
#     }
#     return value * weight_conversions[from_unit] / weight_conversions[to_unit]

# def convert_temperature(value, from_unit, to_unit):
#     if from_unit == 'celsius':
#         if to_unit == 'fahrenheit':
#             return (value * 9/5) + 32
#         elif to_unit == 'kelvin':
#             return value + 273.15
#         else:
#             return value
#     elif from_unit == 'fahrenheit':
#         if to_unit == 'celsius':
#             return (value - 32) * 5/9
#         elif to_unit == 'kelvin':
#             return (value - 32) * 5/9 + 273.15
#         else:
#             return value
#     elif from_unit == 'kelvin':
#         if to_unit == 'celsius':
#             return value - 273.15
#         elif to_unit == 'fahrenheit':
#             return (value - 273.15) * 9/5 + 32
#         else:
#             return value
#     else:
#         return value

# # Streamlit app
# st.set_page_config(page_title="Professional Unit Converter", page_icon="📏", layout="centered")

# # Custom CSS for light and dark mode
# st.markdown("""
#     <style>
#     :root {
#         --background-color: #f0f2f6;
#         --text-color: #333333;
#         --input-bg-color: #ffffff;
#         --button-bg-color: #4a90e2;
#         --button-text-color: white;
#     }
#     .dark-mode {
#         --background-color: #1e1e1e;
#         --text-color: #ffffff;
#         --input-bg-color: #2d2d2d;
#         --button-bg-color: #6fa8dc;
#         --button-text-color: white;
#     }
#     .stApp {
#         background-color: var(--background-color);
#         color: var(--text-color);
#     }
#     h1 {
#         color: var(--button-bg-color);
#         text-align: center;
#     }
#     .stSelectbox, .stNumberInput {
#         background-color: var(--input-bg-color);
#         color: var(--text-color);
#         border-radius: 10px;
#         padding: 10px;
#     }
#     .stButton button {
#         background-color: var(--button-bg-color);
#         color: var(--button-text-color);
#         border-radius: 10px;
#         padding: 10px 20px;
#         font-size: 16px;
#     }
#     .stMarkdown {
#         font-size: 18px;
#         color: var(--text-color);
#     }
#     </style>
#     """, unsafe_allow_html=True)

# # Toggle button for dark mode
# if 'dark_mode' not in st.session_state:
#     st.session_state.dark_mode = False

# dark_mode = st.sidebar.checkbox("Dark Mode", value=st.session_state.dark_mode)

# # Apply dark mode
# if dark_mode:
#     st.session_state.dark_mode = True
#     st.markdown('<div class="dark-mode">', unsafe_allow_html=True)
# else:
#     st.session_state.dark_mode = False
#     st.markdown('<div class="">', unsafe_allow_html=True)

# # Title with emoji
# st.title("📏 Professional Unit Converter")

# # Select the type of conversion
# conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# # Define units based on conversion type
# if conversion_type == "Length":
#     units = ['meter', 'kilometer', 'centimeter', 'millimeter', 'mile', 'yard', 'foot', 'inch']
# elif conversion_type == "Weight":
#     units = ['kilogram', 'gram', 'milligram', 'tonne', 'pound', 'ounce']
# elif conversion_type == "Temperature":
#     units = ['celsius', 'fahrenheit', 'kelvin']

# # Input value and units
# col1, col2, col3 = st.columns(3)
# with col1:
#     value = st.number_input("Enter the value to convert", value=1.0, step=0.1)
# with col2:
#     from_unit = st.selectbox("From unit", units)
# with col3:
#     to_unit = st.selectbox("To unit", units)

# # Perform conversion
# if conversion_type == "Length":
#     result = convert_length(value, from_unit, to_unit)
# elif conversion_type == "Weight":
#     result = convert_weight(value, from_unit, to_unit)
# elif conversion_type == "Temperature":
#     result = convert_temperature(value, from_unit, to_unit)

# # Display the result with a colorful box
# st.markdown(f"""
#     <div style="background-color: var(--button-bg-color); padding: 20px; border-radius: 10px; text-align: center;">
#         <h2 style="color: white;">Converted Value</h2>
#         <p style="font-size: 24px; color: white;">{result:.2f} {to_unit}</p>
#     </div>
#     """, unsafe_allow_html=True)

# # Footer
# st.markdown("---")
# st.markdown("Made with ❤️ using Streamlit")




import streamlit as st

# Define conversion functions
def convert_length(value, from_unit, to_unit):
    length_conversions = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    }
    return value * length_conversions[from_unit] / length_conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_conversions = {
        'kilogram': 1.0,
        'gram': 0.001,
        'milligram': 0.000001,
        'tonne': 1000.0,
        'pound': 0.453592,
        'ounce': 0.0283495
    }
    return value * weight_conversions[from_unit] / weight_conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        else:
            return value
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value

# Streamlit app
st.set_page_config(
    page_title="Professional Unit Converter",
    page_icon="📏",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for additional styling
st.markdown("""
    <style>
    h1 {
        color: #4a90e2;
        text-align: center;
    }
    .stSelectbox, .stNumberInput {
        background-color: var(--background-color);
        color: var(--text-color);
        border-radius: 10px;
        padding: 10px;
    }
    .stButton button {
        background-color: #4a90e2;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-size: 16px;
    }
    .stMarkdown {
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title with emoji
st.title("📏 Professional Unit Converter")

# Select the type of conversion
conversion_type = st.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])

# Define units based on conversion type
if conversion_type == "Length":
    units = ['meter', 'kilometer', 'centimeter', 'millimeter', 'mile', 'yard', 'foot', 'inch']
elif conversion_type == "Weight":
    units = ['kilogram', 'gram', 'milligram', 'tonne', 'pound', 'ounce']
elif conversion_type == "Temperature":
    units = ['celsius', 'fahrenheit', 'kelvin']

# Input value and units
col1, col2, col3 = st.columns(3)
with col1:
    value = st.number_input("Enter the value to convert", value=1.0, step=0.1)
with col2:
    from_unit = st.selectbox("From unit", units)
with col3:
    to_unit = st.selectbox("To unit", units)

# Perform conversion
if conversion_type == "Length":
    result = convert_length(value, from_unit, to_unit)
elif conversion_type == "Weight":
    result = convert_weight(value, from_unit, to_unit)
elif conversion_type == "Temperature":
    result = convert_temperature(value, from_unit, to_unit)

# Display the result with a colorful box
st.markdown(f"""
    <div style="background-color: #4a90e2; padding: 20px; border-radius: 10px; text-align: center;">
        <h2 style="color: white;">Converted Value</h2>
        <p style="font-size: 24px; color: white;">{result:.2f} {to_unit}</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Made by [ALISHBA REHMAN]")