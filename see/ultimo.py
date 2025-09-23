import streamlit as st


st.set_page_config(page_title="Analizador Café Rubio", layout="centered")

st.title("Analizador de Sentimientos - Cafetería Café Rubio")
st.markdown("---")

def analizar_caracteristicas(rapido, lento, amable, grosero, caro, barato, limpio, sucio, sabroso, ruido):
    puntos_positivos = rapido + amable + barato + limpio + sabroso
    puntos_negativos = lento + grosero + caro + sucio + ruido
    
    if puntos_positivos > puntos_negativos:
        return "Positivo", puntos_positivos, puntos_negativos
    elif puntos_negativos > puntos_positivos:
        return "Negativo", puntos_positivos, puntos_negativos
    else:
        return "Neutral", puntos_positivos, puntos_negativos

st.header("🔍 Analizador de Características")
st.write("Selecciona las características que describen tu experiencia:")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Características Positivas")
    rapido = st.checkbox("Rápido")
    amable = st.checkbox("Amable")
    barato = st.checkbox("Barato")
    limpio = st.checkbox("Limpio")
    sabroso = st.checkbox("Sabroso")

with col2:
    st.subheader("Características Negativas")
    lento = st.checkbox("Lento")
    grosero = st.checkbox("Grosero")
    caro = st.checkbox("Caro")
    sucio = st.checkbox("Sucio")
    ruido = st.checkbox("Ruido")


if st.button("Analizar Experiencia", type="primary"):
    rapido_val = 1 if rapido else 0
    lento_val = 1 if lento else 0
    amable_val = 1 if amable else 0
    grosero_val = 1 if grosero else 0
    caro_val = 1 if caro else 0
    barato_val = 1 if barato else 0
    limpio_val = 1 if limpio else 0
    sucio_val = 1 if sucio else 0
    sabroso_val = 1 if sabroso else 0
    ruido_val = 1 if ruido else 0
    
    sentimiento, positivos, negativos = analizar_caracteristicas(
        rapido_val, lento_val, amable_val, grosero_val, caro_val, 
        barato_val, limpio_val, sucio_val, sabroso_val, ruido_val
    )
    
    st.markdown("---")
    st.subheader(" Resultados del Análisis")
    
    col_res1, col_res2, col_res3 = st.columns(3)
    
    with col_res1:
        st.metric("Puntos Positivos", positivos)
    
    with col_res2:
        st.metric("Puntos Negativos", negativos)
    
    with col_res3:
        if sentimiento == "Positivo":
            st.success(sentimiento)
        elif sentimiento == "Negativo":
            st.error(sentimiento)
        else:
            st.info(sentimiento)
    
    st.write("**Características seleccionadas:**")
    
    caracteristicas_positivas = []
    if rapido: caracteristicas_positivas.append("Rápido")
    if amable: caracteristicas_positivas.append("Amable")
    if barato: caracteristicas_positivas.append("Barato")
    if limpio: caracteristicas_positivas.append("Limpio")
    if sabroso: caracteristicas_positivas.append("Sabroso")
    
    caracteristicas_negativas = []
    if lento: caracteristicas_negativas.append("Lento")
    if grosero: caracteristicas_negativas.append("Grosero")
    if caro: caracteristicas_negativas.append("Caro")
    if sucio: caracteristicas_negativas.append("Sucio")
    if ruido: caracteristicas_negativas.append("Ruido")
    
    if caracteristicas_positivas:
        st.write("**Positivas:**", ", ".join(caracteristicas_positivas))
    if caracteristicas_negativas:
        st.write("**Negativas:**", ", ".join(caracteristicas_negativas))

st.markdown("---")
st.markdown("**Cafetería Café Rubio** • Análisis de Sentimientos • 2025")

