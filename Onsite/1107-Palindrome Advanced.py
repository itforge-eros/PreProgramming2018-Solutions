"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    text = input().replace(' ', '').lower()

    if text == text[::-1]:
        print('Yes')
    else:
        print('No')

main()
