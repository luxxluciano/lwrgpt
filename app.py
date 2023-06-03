import streamlit as st

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


def intro():
    import streamlit as st

   
    
    st.write("# Welcome to LWYRUP_GPT! 👋")
    st.image("logo.jpg")
    st.sidebar.success("Select a demo above.")
    

    st.markdown(
        """
        Nosso diferencial é trabalhar com inteligência artificial aplicada à solução dos problemas do dia a dia do advogado.
        Por exemplo, ajudamos você a consultar leis, pesquisar jurisprudência, redigir petições, etc.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what LwrGPT can do!\n\n\n\n\n
        

        Built for non-commercial purposes\n
        Contact US
        [contato@bananamachinada.com.br]
    """
    )
   
    st.image("alan.jpg", width=100)

   

def chat_redacao():

    import streamlit as st


    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    st.write(
        """
        
        Um bot de redação jurídica básica. Minuto petições, contratos e outros textos simples.

       
        """
    )
    st.markdown(
        """
        <iframe src="https://www.chatbase.co/chatbot-iframe/cpc-txt-85yt5fbsx" width="100%" height="650" frameborder="0"></iframe>
        """,
        unsafe_allow_html=True
    )

    st.write(
        """
        
        **Instruções:**

        - Indique a minuta a ser redigida (dizendo, por exemplo: "escreva um mandado de segurança").
        - Envie todas as informações complementares solicitadas pelo bot em apenas uma mensagem; ou apenas diga "escreva mesmo assim" para que o bot complete seu trabalho sem os dados previstos no roteiro.
        - Aguarde o bot escrever sua minuta.
        - Por ser um bot básico, possivelmente ele não conseguirá responder em apenas uma mensagem. Se travar, basta escrever "continue" e o texto será completado na mensagem seguinte.
        - Copie o texto gerado e cole no editor de texto do seu computador para fazer os ajustes finais no seu trabalho.
        """
    )

def chat_stf():

    import streamlit as st

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
    st.write(
        """
       
        Sou um bot jurídico especialista em jurisprudência do STF. Vamos conversar?
        """
    )
    st.markdown(
        """
        <iframe src="https://www.chatbase.co/chatbot-iframe/stf-cf-4mm-txt-fekfromuq" width="100%" height="650" frameborder="0"></iframe>
        """,
        unsafe_allow_html=True
    )

def chat_stj():
    import streamlit as st

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
    st.write(
        """
        
        Sou um bot jurídico que conhece a jurisprudência do STJ.
        """
    )
    st.markdown(
        """
        <iframe src="https://lexgpt-flask-front.vercel.app/?model=stj" width="100%" height="600" frameborder="0" id="frame" allowfullscreen="true"></iframe>
        """,
        unsafe_allow_html=True
    )

page_names_to_funcs = {
    "—": intro,
    "chat_redacao": chat_redacao,
    "Chat-STF": chat_stf,
    "Chat-STJ": chat_stj
}

st.sidebar.image("gpt.jpg")
demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
st.sidebar.image("BETTER_CALL_SAUL_R18_1024x1024.png")
st.sidebar.write(
        """
    
        Powered by BananaMachinadaDS®2023\n
            
        """
    )



