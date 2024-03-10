from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def main():
    # Configuration des options de Chrome
    chrome_options = Options()
    # Décommentez la ligne ci-dessous pour utiliser Chrome en mode sans tête
    # chrome_options.add_argument("--headless")

    # Spécifiez le chemin vers chromedriver
    chromedriver_path = './chromedriver'  # Ajustez le chemin selon votre configuration
    service = Service(executable_path=chromedriver_path)

    # Initialisation du driver Chrome avec les options et le service spécifié
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Naviguez vers une page
    driver.get('https://www.youtube.com')
    
    # Logique supplémentaire ici

    # Fermez le navigateur
    driver.quit()

if __name__ == '__main__':
    main()

