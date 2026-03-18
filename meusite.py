import streamlit as st

# Título do seu site
st.title("🚀 Central de Cálculos do Jorge")

# Menu de escolha
opcao = st.selectbox("O que você quer calcular?", 
                     ["Desconto de 5%", "Média de Aluno", "Conversor de Temperatura" ,"dobro triplo raiz" , "Somar" ,"subtracao" , 'numero multiplos '])

if opcao == "Desconto de 5%":
    preco = st.number_input("Digite o preço do produto (R$):", min_value=0.0)
    if st.button("Calcular"):
        resultado = preco * 0.95
        st.success(f"O valor com desconto é R$ {resultado:.2f}")

elif opcao == "Média de Aluno":
    n1 = st.number_input("Nota 1:")
    n2 = st.number_input("Nota 2:")
    if st.button("Ver Resultado"):
        media = (n1 + n2) / 2
        st.info(f"A média é {media:.1f}")
        if media >= 6.0:
            st.balloons() # Isso faz balões voarem na tela!
            st.success("Aprovado! Você é cuiudo!")
        else:
            st.error("Recuperação... Você é um macio!")

elif opcao == "Conversor de Temperatura":
    c = st.number_input("Temperatura em °C:")
    if st.button("Converter"):
        f = ((9 * c) / 5) + 32
        st.warning(f"{c}°C equivalem a {f:.1f}°F")
elif opcao == "dobro triplo raiz":
    n = st.number_input("Digite um numero:")
    if st.button("calcular agora"):
       d = n * 2 
       t = n * 3
       r =n ** (1/2)
       st.write(f"o dobro de {n} e {d}")
       st.write(f"o triplo de {n} e {t}")  
       st.write(f"a raiz quadrada e {r:.2f}")   
elif opcao == "Somar":
    n1 =st.number_input("digite um numero:")
    n2 = st.number_input("digite o segundo numero:")
    if st.button ("somar agora!"):
        resultado = n1 + n2 
        st.success (f"a soma dos de {n1} + {n2} e igual a {resultado}")
elif opcao == "subtracao":
    n1 = st.number_input('digite um numero:')
    n2 = st.number_input('digite o segundo numero')
    if st.button ('subtracao!'):
        resultado = n1 -n2
        st.success(f'a subtracao de {n1} - {n2} e igual a {resultado}')


