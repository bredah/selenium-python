"""driver_manager.py"""

import logging
from src import driver_factory

logger = logging.getLogger(__name__)


class DriverManager:
    """Gerenciador de driver de contexto para Selenium WebDriver."""

    driver = None

    def __init__(self):
        """
        Inicializa o DriverManager com um navegador específico.
        """

    def __enter__(self):
        """Inicializa o driver ao entrar no contexto."""
        if DriverManager.driver is None:
            try:
                logger.info("iniciando driver")
                DriverManager.driver = driver_factory.get_driver()
                logger.info(
                    "browser: %s - session: %s",
                    DriverManager.driver.name,
                    DriverManager.driver.session_id,
                )
            except RuntimeError as e:
                logger.error("erro ao inicializar o driver: %s", e)
                raise
        return DriverManager.driver

    def __exit__(self, exc_type, exc_value, traceback):
        """Encerra o driver ao sair do contexto."""
        if DriverManager.driver:
            try:
                logger.info("release session")
                DriverManager.driver.quit()
            except RuntimeError as e:
                logger.error("erro ao encerrar o driver: %s", e)
            finally:
                DriverManager.driver = None

    @staticmethod
    def get_driver():
        """Retorna o driver existente, se houver."""
        if DriverManager.driver is None:
            raise RuntimeError("Driver não está inicializado. Use o DriverManager para criá-lo.")
        return DriverManager.driver
