import re


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\b([u_U][m_M])\b"

    expresion_match = re.findall(pattern, s)
    return len(expresion_match)


if __name__ == "__main__":
    main()
