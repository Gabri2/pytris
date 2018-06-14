import sys
import lib

def main(args=None):
    firstPlayer = lib.createPlayer()
    secondPlayer = lib.createPlayer()

    print(firstPlayer)
    print(secondPlayer)

if __name__ == '__main__':
    main(sys.argv[1:])
