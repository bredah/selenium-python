"""test_google_search.py"""

from pages.google.google_page import GooglePage


def test_google_search():

    # Cria uma instância da GooglePage
    google_page = GooglePage()

    # Abre a página inicial do Google
    google_page.open("https://www.google.com")

    # Realiza uma pesquisa e obtém a página de resultados
    google_page.search("Selenium pytest")
    results_page = google_page.get_results()

    # Verifica se há resultados e se o título contém o termo pesquisado
    result_titles = results_page.get_result_titles()
    assert len(result_titles) > 0
    assert any("Selenium" in title for title in result_titles)


def test_google_new_search():

    # Cria uma instância da GooglePage
    google_page = GooglePage()

    # Abre a página inicial do Google
    google_page.open("https://www.google.com")

    # Realiza uma pesquisa e obtém a página de resultados
    google_page.search("Selenium pytest")
