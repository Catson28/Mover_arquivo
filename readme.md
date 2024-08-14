### Passo 1: Instalar o Python

Se ainda não tiver o Python instalado, baixe e instale a versão mais recente do Python no site oficial: [python.org](https://www.python.org/downloads/).

### Passo 2: Configurar um Ambiente Virtual

Um ambiente virtual é útil para isolar as dependências do seu projeto. Vamos criar um ambiente virtual e ativá-lo.

1. **Abra o terminal** (CMD no Windows ou Terminal no macOS/Linux).
2. Navegue até a pasta onde você deseja criar seu projeto:

   ```bash
   cd /caminho/para/sua/pasta
   ```

3. **Crie o ambiente virtual**:

   ```bash
   python -m venv env
   ```

   Isso cria uma pasta chamada `env` com uma cópia do Python e as ferramentas necessárias.

4. **Ative o ambiente virtual**:

   - No **Windows**:

     ```bash
     env\Scripts\activate
     ```

   - No **macOS/Linux**:

     ```bash
     source env/bin/activate
     ```

   Após ativar, você verá o nome do ambiente virtual (ex: `(env)`) no início da linha de comando.

### Passo 3: Escrever o Script Python

1. **Crie um arquivo Python**:
   Crie um arquivo chamado `mover_arquivos.py` na pasta do projeto.

2. **Escreva o código no arquivo**:
   Abra o arquivo `mover_arquivos.py` em um editor de texto (ex: VS Code, Sublime Text, Notepad++) e cole o código abaixo:

   ```python
   import os
   import shutil

   def mover_arquivos(diretorio, nomes_arquivos, nova_pasta):
       # Cria a nova pasta, se não existir
       if not os.path.exists(nova_pasta):
           os.makedirs(nova_pasta)

       # Procura e move os arquivos especificados
       for nome_arquivo in nomes_arquivos:
           for raiz, _, arquivos in os.walk(diretorio):
               for arquivo in arquivos:
                   if nome_arquivo in arquivo:
                       caminho_arquivo = os.path.join(raiz, arquivo)
                       destino = os.path.join(nova_pasta, arquivo)

                       # Move o arquivo para a nova pasta
                       shutil.move(caminho_arquivo, destino)
                       print(f"Arquivo {arquivo} movido para {nova_pasta}")

   # Parâmetros
   diretorio_para_pesquisar = "/caminho/para/sua/pasta" #  diretorio_para_pesquisar = "/caminho/para/sua/pasta"
   nomes_dos_arquivos = ["exemplo1.txt", "exemplo2.pdf"]  # Lista de nomes de arquivos
   nova_pasta = "/caminho/para/nova/pasta" #   nova_pasta = "/caminho/para/nova/pasta"

   # Executa o script
   mover_arquivos(diretorio_para_pesquisar, nomes_dos_arquivos, nova_pasta)
   ```

### Passo 4: Executar o Script

1. **Execute o script**:
   No terminal, com o ambiente virtual ativado e na pasta onde o script está salvo, execute:

   ```bash
   python mover_arquivos.py
   ```

2. **Verifique o resultado**:
   O script deve procurar pelos arquivos listados em `nomes_dos_arquivos` na pasta especificada e movê-los para a nova pasta.

### Passo 5: Desativar o Ambiente Virtual

Quando terminar, você pode desativar o ambiente virtual com:

```bash
deactivate
```

### Considerações Finais

Se precisar de mais funcionalidades, como procurar por tipos de arquivos específicos (ex: `.pdf`, `.txt`), o script pode ser facilmente ajustado. Além disso, o ambiente virtual garante que as bibliotecas instaladas (se houver) sejam isoladas e não afetem outros projetos no sistema.
