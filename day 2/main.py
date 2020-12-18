import pathlib

def main(input):
	print(input)

if __name__ == "__main__":
	main(pathlib.Path(__file__).parent.joinpath("input.txt"))