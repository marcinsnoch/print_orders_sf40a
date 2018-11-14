import serial


def main():
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM5'
    ser.open()

    if ser.is_open:
        print(ser)
    else:
        print("Not open")

    ser.close()


if __name__ == "__main__":
    main()
