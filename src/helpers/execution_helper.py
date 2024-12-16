"""TBD"""

import json
import logging

logger = logging.getLogger(__name__)
EXECUTION_FILE = ".execution"


def write_execution(data):
    """
    Sobrescreve os dados no arquivo `.execution`.
    :param data: Dicionário com informações de execução.
    """
    try:
        with open(EXECUTION_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
        logger.info("Dados de execução gravados em %s", EXECUTION_FILE)
    except IOError as e:
        logger.error("Erro ao gravar dados de execução: %s", e)
