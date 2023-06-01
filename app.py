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

def main():
    # App title and login section
    st.title("LWR-GPT")
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        if authenticate(username, password):
            st.success("Authentication successful!")
            display_content()
        else:
            st.error("Authentication failed!")

def display_content():
  
    
    st.markdown(
        """
        <iframe src="https://www.chatbase.co/chatbot-iframe/cpc-txt-85yt5fbsx" width="100%" height="650" frameborder="0"></iframe>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        ## Como utilizar minhas funções para escrever uma petição judicial.

        1. Para começar, você pode me informar qual é o tipo de petição que deseja redigir. Por exemplo, se é uma petição inicial, uma petição de contestação, uma petição de recurso, entre outras.

        2. Em seguida, você pode me fornecer as informações necessárias para a elaboração da petição, como os dados do cliente, os fatos do caso, os fundamentos jurídicos, entre outros.

        Com base nessas informações, eu posso redigir a petição de acordo com as normas e regras processuais aplicáveis. 
        Por exemplo, se for uma petição inicial, eu posso incluir os requisitos previstos no artigo 319 do Código de Processo Civil, como a indicação das partes, a causa de pedir, o pedido, entre outros.

        Além disso, eu posso utilizar recursos como a inclusão de jurisprudência, doutrina e legislação pertinente ao caso, para fundamentar os argumentos apresentados na petição.

        Por fim, eu posso revisar a petição para garantir que ela esteja clara, objetiva e em conformidade com as normas processuais aplicáveis.
        """
    )


if __name__ == "__main__":
    main()
