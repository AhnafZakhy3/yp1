def main():
    with open ("enc") as fd:
        flag = fd.read()

    decoded = []

    for two_bytes in flag:
        # Bytes to integer.
        btoi = ord(two_bytes)
        # First byte.
        decoded.append(chr(btoi >> 8))
        # Second byte.
        decoded.append(chr(btoi & 255))

    print("".join(decoded))


if __name__ == "__main__":
    main()
