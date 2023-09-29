import argparse
import sys



parser = argparse.ArgumentParser()
parser.add_argument("--nombre", "-n", type=str, help="El nombre que deseas pasar", required=True)

args = parser.parse_args()
print(f"Hola {args.nombre}")
print(sys.argv)

