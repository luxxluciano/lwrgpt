import streamlit as st

# Dictionary of authorized users
authorized_users = {
    "admin": "banana231212..",
    "piti": "pitiaraujo"
}

def authenticate(username, password):
    """Authenticate the user"""
    if username in authorized_users and authorized_users[username] == password:
        return True
    return False

def intro():
    import streamlit as st

    st.write("# Welcome to LwrGPT! 👋")
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Nosso diferencial é trabalhar com inteligência artificial aplicada à solução dos problemas do dia a dia do advogado.
        Por exemplo, ajudamos você a consultar leis, pesquisar jurisprudência, redigir petições, etc.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what LwrGPT can do!

        
    """
    )

def chat_redacao():

    import streamlit as st


    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write(
        """
        
        Um bot de redação jurídica básica. Minuto petições, contratos e outros textos simples.

        **Instruções:**

        - Indique a minuta a ser redigida (dizendo, por exemplo: "escreva um mandado de segurança").
        - Envie todas as informações complementares solicitadas pelo bot em apenas uma mensagem; ou apenas diga "escreva mesmo assim" para que o bot complete seu trabalho sem os dados previstos no roteiro.
        - Aguarde o bot escrever sua minuta.
        - Por ser um bot básico, possivelmente ele não conseguirá responder em apenas uma mensagem. Se travar, basta escrever "continue" e o texto será completado na mensagem seguinte.
        - Copie o texto gerado e cole no editor de texto do seu computador para fazer os ajustes finais no seu trabalho.
        """
    )
    st.markdown(
        """
        <iframe src="https://www.chatbase.co/chatbot-iframe/cpc-txt-85yt5fbsx" width="100%" height="650" frameborder="0"></iframe>
        """,
        unsafe_allow_html=True
    )

def chat_vade():

    import streamlit as st

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    st.write(
        """
       
        Bot de códigos: Constituição, LINDB, Civil, CPC, Comercial, Penal, CPP, Contravenções, CTN, Eleitoral e Consumidor.
        """
    )
    st.markdown(
        """
        <iframe src="https://www.chatbase.co/chatbot-iframe/vade-leis-txt-kycweb1u0" width="100%" height="600" frameborder="0"></iframe>
        """,
        unsafe_allow_html=True
    )

def chat_cpc():
    import streamlit as st

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
    st.write(
        """
         Um bot especialista em legislação e doutrina de processo civil. Qual sua dúvida processual?
        """
    )
    st.markdown(
        """
        <iframe src="https://www.chatbase.co/chatbot-iframe/tOc1_epZLC4b7zWWmx3eP" width="100%" height="650" frameborder="0"></iframe>
        """,
        unsafe_allow_html=True
    )

page_names_to_funcs = {
    "—": intro,
    "chat_redacao": chat_redacao,
    "chat_vade": chat_vade,
    "chat_cpc": chat_cpc
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()