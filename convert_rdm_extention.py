import logging
import os


logger = logging.getLogger()
wdpath = os.getcwd()


def configure_logging():
    logging.getLogger("matplotlib.font_manager").setLevel(level=logging.WARN)
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('Python.log', 'w', 'utf-8')
    formatter = logging.Formatter('%(asctime)s [%(name)s] %(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

rdm_extention = '.rdm'
new_extention = '.txt'
rdm_filename = 'Frequencies'

def main():
    """Поиск файлов c данными и обработка."""
    for root, dirs, files in os.walk(wdpath):
        for resf in files:
            if resf.endswith(rdm_extention):
                rdm_path = wdpath + '\\' + rdm_filename + rdm_extention
    convert_rdm_extention(rdm_path)


def convert_rdm_extention(rdm_path):
    """Изменение расширения .rdm файла на new_extention"""
    with open(rdm_path, 'r') as f:
        data = f.read()
    with open(wdpath + '\\' + rdm_filename + new_extention, 'w') as f:
        f.write(data)

configure_logging()
main()
logger.info("ALL DONE")