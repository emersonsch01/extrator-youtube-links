from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
import time
import pandas as pd

print("\n-------------------------------------")


def busca_youtube():
    pesquisa = input("\nBUSCA: ")
    qtd_videos = int(input("\nQUANTIDADE DE VÍDEOS: "))
    print("\nEXECUTANDO BUSCA...")
    options = ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    driver.get('https://www.youtube.com/')
    time.sleep(5)
    driver.find_element(By.NAME, 'search_query').send_keys(pesquisa)
    driver.find_element(By.ID, 'search-icon-legacy').click()
    time.sleep(5)
    while True:
        videos = driver.find_elements(By.TAG_NAME, 'ytd-video-renderer')
        if len(videos) <= qtd_videos:
            driver.execute_script(f"window.scroll(0, 100000);")
            time.sleep(2)
        else:
            break
    print("\n-------------------------------------\n")
    lista_url = []
    for i, video in enumerate(videos):
        if i <= qtd_videos - 1:
            url = video.find_element(By.TAG_NAME, 'a').get_attribute('href')
            lista_url.append(url)
        else:
            break
    df = pd.DataFrame(lista_url)
    df.to_excel('Lista Links.xlsx', header=False, index=False)
    input("\nBUSCA FINALIZADA!")


busca_youtube()
