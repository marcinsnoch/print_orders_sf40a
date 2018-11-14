import config
import serial
import requests
import time
import datetime


def main():
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM5'
    ser.timeout = 5
    ser.bytesize = serial.EIGHTBITS
    ser.parity = serial.PARITY_NONE
    ser.stopbits = serial.STOPBITS_ONE
    ser.xonxoff = False
    ser.rtscts = False
    ser.dsrdtr = False

    r = requests.get(config.SERVER_API['host'] + 'orders', params={'token': config.SERVER_API['token']})

    data = r.json()

    orders = []

    while True:

        for order in data:
            if order['order_no'] not in orders:
                orders.append(order['order_no'])
                print(order['order_no'] + '\n')
                print_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                ser.open()

                ser.write("------------MMIS.MEAGTERM.PL------------\r\n".encode())
                ser.write("DATE TIME: ".encode())
                ser.write(print_time.encode())
                ser.write("\r\n".encode())

                ser.write("ORDER ID: ".encode())
                ser.write(order['order_id'].encode())
                ser.write("\r\n".encode())

                ser.write("ORDER NO: ".encode())
                ser.write(order['order_no'].encode())
                ser.write("\r\n".encode())

                ser.write("DATE OF ORDER: ".encode())
                ser.write(order['date_of_order'].encode())
                ser.write("\r\n".encode())

                ser.write("ORDER BY: ".encode())
                ser.write(order['ordered_by'].encode())
                ser.write("\r\n".encode())
                ser.write("\r\n".encode())

                ser.flushInput()
                ser.close()
        print('Waiting forn new orders...')
        time.sleep(3600)


if __name__ == "__main__":
    main()
