import pathlib

def main(input):
	with open(input, mode='r') as opened_file:
		data = opened_file.read()

if __name__ == "__main__":
	main(pathlib.Path(__file__).parent.joinpath("input.txt"))