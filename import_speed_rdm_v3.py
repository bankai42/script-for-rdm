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


values_filename = 'values'
values_extention = '.csv'
rdm_filename = 'Frequencies'
rdm_extention = '.rdm'
new_rdm_extention = '.txt' # костыль, чтобы не было двух .rdm файлов
new_rdm_filename = 'new_rdm'

value_name = 'Speed'

k1 = 11250/7470
k2 = 1


def main():
    """Поиск файлов c данными и обработка."""
    for root, dirs, files in os.walk(wdpath):
        for resf in files:
            # ищем values.csv и читаем скорость
            if resf.startswith(values_filename) and resf.endswith(values_extention):
                values_path = root + '\\' + os.path.basename(resf)
                speed = read_speed(values_path)

            # ищем Frequencies.txt   
            if resf.startswith(rdm_filename) and resf.endswith(new_rdm_extention):
                rdm_path = wdpath + '\\' + rdm_filename + new_rdm_extention
    write_rdm(rdm_path, speed)


def read_speed(file_path):
    """Чтение значения скорости из файла .csv"""
    with open(file_path,'r') as f:
        for index, line in enumerate(f):
            data = line.split(',')
            if data[0] == value_name:
                return float(data[1])
    

def write_rdm(rdm_path, speed):
    """Запись нового *.rdm файла."""
    line_speed_arg = '						<argument><value>' + str(int(speed)) + '</value></argument>\n'
    line_speed_fun = '						<function><value>' + str(int(speed)) + '</value></function>\n'
    line_speed_k1_arg = '						<argument><value>' + str(int(speed*k1)) + '</value></argument>\n'
    line_speed_k1_fun = '						<function><value>' + str(int(speed*k1)) + '</value></function>\n'
    line_speed_k1_stoptime = '						<stop_time_proprotion unit="unitTimeProportion"><value>' + str(int(speed*k1)) + '</value></stop_time_proprotion>\n'
    line_speed_k2 = '						<max_regime unit="unitTimeProportion"><value>' + str(int(speed*k2)) + '</value></max_regime>\n'
    with open(rdm_path, 'r') as f:
        lines = f.readlines()
    # заменяем строчки на новые
    lines[6937-1] = line_speed_arg
    lines[6938-1] = line_speed_fun
    lines[6941-1] = line_speed_k1_arg
    lines[6942-1] = line_speed_k1_fun
    lines[7028-1] = line_speed_k1_stoptime
    lines[7030-1] = line_speed_k2

    with open(wdpath + '\\' + new_rdm_filename+rdm_extention, 'w') as f:
        f.writelines(lines)


configure_logging()
main()
logger.info("ALL DONE")