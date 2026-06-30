import streamlit as st
from api_client import buscar_ciudades, obtener_clima

st.set_page_config(page_title="Buscador de Clima", layout="centered")

st.title("⛅ Consulta el clima en tu ciudad")
st.write("Obtendras informacion precisa de la zona")

ciudad_buscada = st.text_input("Escribe el nombre de la ciudad:")

if ciudad_buscada:
    resultados = buscar_ciudades(ciudad_buscada)
    
    if resultados:
        
        opciones_ciudades = {}
        for ciudad in resultados:
            nombre_completo = f"{ciudad.get('name')}, {ciudad.get('country', '')}"
            opciones_ciudades[nombre_completo] = (ciudad["latitude"], ciudad["longitude"])
        
        ciudad_seleccionada = st.selectbox("Selecciona la ciudad correcta:", list(opciones_ciudades.keys()))
        
        if st.button("Consultar Clima"):
            lat, lon = opciones_ciudades[ciudad_seleccionada]
            
            clima_data = obtener_clima(lat, lon)
            
            if clima_data and "current" in clima_data:
                current = clima_data["current"]
                temperatura = current.get("temperature_2m", "N/A")
                humedad = current.get("relative_humidity_2m", "N/A")
                viento = current.get("wind_speed_10m", "N/A")
                
                st.subheader(f"Clima actual en {ciudad_seleccionada}")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric(label="Temperatura", value=f"{temperatura} °C")
                with col2:
                    st.metric(label="Humedad", value=f"{humedad} %")
                with col3:
                    st.metric(label="Viento", value=f"{viento} km/h")
            else:
                st.error("Error al obtener los datos del clima.")
    else:
        st.warning("No encontramos ninguna ciudad con ese nombre.")