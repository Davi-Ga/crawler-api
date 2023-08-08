import unittest
from core import get_page
from fastapi import HTTPException, status

class TestGetPage(unittest.TestCase):
    def test_successful_request(self):
        url = "https://www.jusbrasil.com.br/jurisprudenca/busca?q=Roberto+Naves"
        soup = get_page(url)
        self.assertIsNotNone(soup)
        self.assertEqual(soup.title.string, "Jusbrasil")  # Verifique se o título da página está correto.

    def test_page_not_found(self):
        url = "https://www.jusbrasil.com.br/jurisprudencia/Roberto+Naves"
        with self.assertRaises(HTTPException) as context:
            get_page(url)
        self.assertEqual(context.exception.status_code, status.HTTP_404_NOT_FOUND)

    def test_internal_server_error(self):
        # Simule uma URL que cause um erro interno no servidor (por exemplo, um site em manutenção ou indisponível)
        url = "https://server-error-page.com"
        with self.assertRaises(HTTPException) as context:
            get_page(url)
        self.assertEqual(context.exception.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # def test_connection_timeout(self):
    #     # Simule uma URL que cause um erro interno no servidor (por exemplo, um site em manutenção ou indisponível)
    #     url = "https://www.jusbrasil.com.br/jurisprudencia/busca?q=Roberto+Naves"
    #     with self.assertRaises(HTTPException) as context:
    #         get_page(url)
    #     self.assertEqual(context.exception.status_code, status.HTTP_408_REQUEST_TIMEOUT)
        
if __name__ == '__main__':
    unittest.main()
