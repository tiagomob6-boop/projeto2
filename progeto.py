import streamlit as st

# Configuração da página
st.set_page_config(page_title="Desafio Matemático", page_icon="🧮")

# 1. Inicialização do Estado (Session State)
# Isso impede que o quiz recomece do zero a cada clique de botão
if 'index' not in st.session_state:
    st.session_state.index = 0
if 'concluido' not in st.session_state:
    st.session_state.concluido = False

# 2. Lista de perguntas (Corrigida a sintaxe do dicionário)
perguntas = [
    {"pergunta": "Quanto é 15 + 27?", "resposta": "42"},
    {"pergunta": "Quanto é 8 * 9?", "resposta": "72"},
    {"pergunta": "Qual a raiz quadrada de 25?", "resposta": "5"},
    {"pergunta": "Fica comigo?", "resposta": "sim"}
]

# 3. Interface do Usuário
st.title("🎮 Desafio Matemático")

if not st.session_state.concluido:
    index = st.session_state.index
    pergunta_atual = perguntas[index]

    st.subheader(f"Pergunta {index + 1}:")
    st.write(pergunta_atual["pergunta"])

    # Campo de entrada
    usuario_resposta = st.text_input("Sua resposta:", key=f"input_{index}").lower().strip()

    if st.button("Verificar Resposta"):
        respostas_aceitas_final = ["sim", "com certeza", "claro"]
        
        # Lógica para a última pergunta
        if index == len(perguntas) - 1:
            if usuario_resposta in respostas_aceitas_final:
                st.success("Muito bem! ❤️")
                st.session_state.concluido = True
                st.balloons() # Efeito visual de comemoração
                st.rerun()
            else:
                st.error("Tente novamente! 🤔")
        
        # Lógica para as perguntas normais
        else:
            if usuario_resposta == pergunta_atual["resposta"].lower():
                st.toast("Correto!", icon="✅")
                st.session_state.index += 1
                st.rerun() # Recarrega a página para mostrar a próxima pergunta
            else:
                st.error("Resposta errada! Tente de novo.")

else:
    # Tela final
    st.success("Desafio concluído com sucesso!")
    if st.button("Reiniciar Desafio"):
        st.session_state.index = 0
        st.session_state.concluido = False
        st.rerun()

# Rodapé visual
st.divider()
st.caption("Desenvolvido com Streamlit")