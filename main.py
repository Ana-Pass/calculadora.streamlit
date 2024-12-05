
import streamlit as st

#Criar bassa lateral
with st.sidebar:
    st.title("Calculadora IMC")

    st.header("Oque é IMC?")
    st.markdown("""O IMC é determinado pela divisão da massa do indivíduo pelo quadrado de sua altura, em que a massa está em quilogramas e a altura em metros.""")
    #Alinha o texto
    st.write("""
    - **Abaixo do peso**: IMC menor que 18.5
    - **Peso ideal**: IMC entre 18.5 e 24.9
    - **Sobrepeso**: IMC entre 25 e 29.9
    - **Obesidade**: IMC entre 30 e 39.9
    - **Obesidade mórbida**: IMC acima de 40    
""")





st.title("Calculadora IMC")

#Entrada de dados
peso = st.number_input(label="Digite seu peso (Em kg)", min_value= 0.0, step=0.10, format="%.1f") #min_value o minimo de valor que ele recebe, step de quanto em quanto ele aumenta,

altura = st.number_input(label="Digite sua altura (Em metros)", min_value= 0.0, step=0.10, format="%.1f")

if st.button("Calcular"):
    if peso > 0 and altura > 0:
        imc = peso / (altura ** 2 )
        imc_ideal = 21.7
        imc_delta = imc - imc_ideal

        if imc < 18.5:
            classe = "Abaixo do peso"
        elif imc < 24.9:
            classe = "Peso ideal"
        elif imc < 29.9:
            classe = "Sobrepeso"
        elif imc < 40:
            classe = "Obesidade"
        else:
            classe = "Obesidade morbida"

        st.success("Calculo realizado com sucesso!")

        #Escrever o valores 
        st.write(f"Seu *IMC* é {imc:.2f}")
        st.write(f"classificação: {classe}")
        st.write(f"comparação com o IMC ideal (21.7): **{imc_delta: .2f}")

        #Dividir a linha em duas colunas
        col1, col2 = st.columns(2)

        col1.metric("Classificação", classe, f"{imc_delta:.2f}",delta_color="inverse")

        col2.metric("IMC",f"{imc:.2f}", f"{imc_delta:.2f}", delta_color="off")

        #Criar uma linha 
        st.divider()

        st.image("./imc2.png")
        


    else:
        #Mostrar mensagem de erro
        st.error("Por favor, insira os valores validos para peso e altura.")


    

