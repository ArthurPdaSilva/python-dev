import streamlit as st
import time
from backend import create_chain_conversa, folder_files

def chat_app():
   st.header("Chat com PDF 🤖", divider=True)
   if not 'chain' in st.session_state:
       st.error("Faça o upload de um arquivo PDF para começar.")
       st.stop()
   
   chain = st.session_state["chain"]
   memory = chain.memory
   messages = memory.load_memory_variables({})['chat_history']

   container = st.container()
   for message in messages:
       chat = container.chat_message(message.type)
       chat.markdown(message.content)
   new_message = st.chat_input("Converse com seus documentos")
   if new_message:
        chat = container.chat_message("human")
        chat.markdown(new_message)
        chat = container.chat_message("ai")
        chat.markdown("Gerando resposta...")
        chain.invoke({"question": new_message})
        st.rerun()

def save_uploaded_file(uploaded_files, folder):
    '''Salva o arquivo enviado na pasta especificada.'''
    for file in folder.glob("*.pdf"):
        file.unlink()
    # Salva o(s) novo(s) arquivo(s) enviado(s)
    for file in uploaded_files:
        (folder / file.name).write_bytes(file.read())

def main():
    with st.sidebar:
        st.header("Upload de PDF's")
        uploaded_files = st.file_uploader("Escolha os arquivos PDF", type="pdf", accept_multiple_files=True)
        if uploaded_files:
            save_uploaded_file(uploaded_files, folder_files)
            st.success(f"{len(uploaded_files)} Arquivo(s) salvo(s) com sucesso!")

        label_button = "Inicializar Chat"
        if "chain" in st.session_state:
            label_button = "Atualizar Chat"
        if st.button(label_button, use_container_width=True):
            if len(list(folder_files.glob("*.pdf"))) == 0:
                st.error("Nenhum arquivo PDF encontrado. Por favor, faça o upload de um arquivo.")
            else:
                create_chain_conversa()
                st.success("Chat inicializado com sucesso!")
                st.rerun()
    chat_app()

if __name__ == "__main__":
    main()