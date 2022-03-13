import serial
import serial.tools.list_ports
import time

portlar = serial.tools.list_ports.comports() # Sistemdeki açık portları görüntüler

port_listesi = []

for port in portlar:
    port_listesi.append(str(port))
    print(str(port))

kullanici_girdisi_port = input("Port seciniz: COM")
kullanici_girdisi_seri_iletisim_hizi = input("Boud Rate 'i girin: ")
seri_iletisim_hizi = kullanici_girdisi_seri_iletisim_hizi
okunacak_port = str('COM' + kullanici_girdisi_port)

seri_haberlesme = serial.Serial(port = okunacak_port, baudrate = seri_iletisim_hizi)
seri_haberlesme.timeout = 2

if seri_haberlesme.is_open:
    print("Veri okunuyor...")
    while True:
        time.sleep(1)
        boyut = seri_haberlesme.inWaiting()
        if boyut:
            veri = seri_haberlesme.read(boyut)
            print(veri)
        else:
            print('Veri okunamadi!')
else:
    print('Port bulunamadi!')
