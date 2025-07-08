from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# ⚙️ CONFIGURAÇÃO
ARQUIVO_USUARIOS = "nao_me_seguem_de_volta.txt"
TEMPO_LOGIN = 30  # segundos para você logar manualmente
TEMPO_ENTRE_ACOES = 5  # segundos entre cada unfollow
TIMEOUT_CONFIRMAR = 10  # tempo para aguardar a janela flutuante aparecer

# 🚀 LEITURA DOS USUÁRIOS
with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
    usuarios = [line.strip() for line in f if line.strip()]

print(f"Encontrados {len(usuarios)} usuários para deixar de seguir.")

# 🚀 INICIALIZA O NAVEGADOR (Microsoft Edge)
options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)
wait = WebDriverWait(driver, TIMEOUT_CONFIRMAR)

# Abre Instagram e aguarda login manual
print("Abra o navegador e faça login na sua conta.")
driver.get("https://www.instagram.com")
sleep(TEMPO_LOGIN)

# 🚀 PROCESSA CADA USUÁRIO
for idx, usuario in enumerate(usuarios, start=1):
    perfil_url = f"https://www.instagram.com/{usuario}/"
    driver.get(perfil_url)
    print(f"[{idx}/{len(usuarios)}] Visitando {usuario}...")
    sleep(3)
    try:
        btns = driver.find_elements(By.XPATH, "//button")
        for btn in btns:
            if btn.text.lower() in ["seguindo", "following"]:
                btn.click()
                try:
                    # espera o popup aparecer e procura o span com texto "Deixar de seguir"
                    confirmar_span = wait.until(EC.element_to_be_clickable((
                        By.XPATH, "//span[text()='Deixar de seguir'] | //span[text()='Unfollow']"
                    )))
                    confirmar_span.click()
                    print(f"✅ Deixou de seguir: {usuario}")
                except Exception as e:
                    print(f"⚠️ Botão de confirmação não encontrado para {usuario}: {e}")
                break
        else:
            print(f"⚠️ Botão 'Seguindo' não encontrado para {usuario}.")
    except NoSuchElementException as e:
        print(f"⚠️ Erro com {usuario}: {e}")
    sleep(TEMPO_ENTRE_ACOES)

print("🎯 Concluído!")
