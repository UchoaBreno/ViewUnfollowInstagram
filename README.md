# Instagram Unfollow Bot

✨ Liberte seu feed do Instagram e recupere o controle da sua lista de seguidores! Este simples, mas poderoso script em Python deixa de seguir automaticamente usuários que não te seguem de volta, economizando tempo e esforço. Perfeito para contas pessoais, gerentes de redes sociais ou qualquer pessoa que queira manter sua lista de seguidos limpa e relevante.

✅ Compatível com Google Chrome e Microsoft Edge  
✅ Configuração fácil com instruções claras  
✅ Totalmente automatizado após iniciar  

---

## 📋 Tutorial em Português e em Inglês

### 📘 Português

### 1️⃣ Pré-requisitos

✅ Python 3.x instalado, disponível em: https://www.python.org/  
✅ Pacotes Python: `selenium` e `webdriver-manager`

Verifique no Prompt de Comando, cntrl + R, digite cmd e digite:
```cmd
python --version
```
Deve aparecer algo como `Python 3.x.x`.

### 2️⃣ Instale as dependências
```cmd
pip install selenium webdriver-manager
```

### 3️⃣ Baixe os dados do Instagram

1. Acesse **Configurações** no Instagram.  
2. Na lupa, digite **informações**.  
3. Clique em *Baixar ou transferir informações*.  
4. Escolha *Algumas de suas informações*.  
5. Marque apenas *Seguidores e seguindo*.  
6. Confirme o e-mail.  
7. Clique em *Criar arquivo*.  
8. Baixe o arquivo ZIP enviado por e-mail e extraia.  
9. Gere o arquivo `nao_me_seguem_de_volta.txt` com os nomes dos usuários que você segue mas não te seguem.

### 4️⃣ Crie o script `.py`

1. Abra o Bloco de Notas.
2. Cole o código para o navegador desejado (Chrome ou Edge).
3. Salve como `instagramUnfollow.py`.
4. No Explorer, vá em *Exibir*, ative *Extensões de nomes de arquivos* e confirme que o arquivo está `.py` e não `.py.txt`.

### 5️⃣ Execute o script

No Prompt de Comando, vá até a pasta:
```cmd
cd caminho\da\pasta
```
E rode:
```cmd
python instagramUnfollowEdge.py ou python instagramUnfollowChrome.py
```

O script abrirá o navegador escolhido, você faz login e o bot começa a deixar de seguir automaticamente.



-------------------



### 📗 English

# Instagram Unfollow Bot

✨ Free up your Instagram feed and take back control of your follower list! This simple yet powerful Python script automatically unfollows users who don't follow you back, saving you time and effort. Perfect for personal accounts, social media managers, or anyone looking to keep their following list clean and relevant.

✅ Supports both Google Chrome and Microsoft Edge  
✅ Beginner-friendly setup with clear instructions  
✅ Fully automated once started  

---

### 1️⃣ Prerequisites

✅ Python 3.x installed: https://www.python.org/  
✅ Python packages: `selenium` and `webdriver-manager`

Check in Command Prompt:
```cmd
python --version
```
It should show `Python 3.x.x`.

### 2️⃣ Install dependencies
```cmd
pip install selenium webdriver-manager
```

### 3️⃣ Download your Instagram data

1. Go to **Settings** in Instagram.  
2. In the search bar, type **information**.  
3. Click *Download or transfer information*.  
4. Select *Some of your information*.  
5. Check only *Followers and following*.  
6. Confirm your email.  
7. Click *Create file*.  
8. Download the ZIP sent to your email and extract it.  
9. Create the `nao_me_seguem_de_volta.txt` file listing the users you follow but who don’t follow you back.

### 4️⃣ Create the `.py` script

1. Open Notepad.
2. Paste the code for your browser of choice (Chrome or Edge).
3. Save as `instagramUnfollow.py`.
4. In Explorer, enable *File name extensions* and confirm the file is `.py`.

### 5️⃣ Run the script

In Command Prompt, navigate to the folder:
```cmd
cd path\to\folder
```
And run:
```cmd
python instagramUnfollowEdge.py or python instagramUnfollowChrome.py
```

The script will open the chosen browser, you log in, and the bot starts unfollowing automatically.


Enjoy! 🚀
