import argparse

parser = argparse.ArgumentParser(description='Herramienta Generar informes.')

parser.add_argument('-p', dest='countryname', default="Spain", type=str,
                    help='Pais por defecto España')


args = parser.parse_args()
