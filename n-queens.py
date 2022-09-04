import argparse

def init():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n',type=int,default=10,help='Number of queens to place and the edge length of the chess board.')
    args = parser.parse_args()
    print(f'n={args.n}')


if __name__ == "__main__":
    init()