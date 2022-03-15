# Reading-Data-From-Serial-Port-With-Python

Bu projede STM32-F103C6TX2 mikrodenetleyicisinin USART portundan gelen mesaj verisinin Python aracılığı ile okunmasını sağlayan kod yazılmıştır. Bu mantığı kullanarak STM32 'nin USART portundan gelen veriyi okuyabilir ve bu gelen veriyi işleyebilirsiniz. Kodu çalıştırdığınızda açık olan Port 'ları görüntüleyebilir, Portu seçebilir ve Haberleşme Hızını(Boud Rate) girebilirsiniz. İlgili değerler girildikten sonra kod gelen veriyi okumaya başlayacaktır.

![gif](https://user-images.githubusercontent.com/74931027/158283795-3b6d448a-f70c-4dc8-9b43-796dfad063cb.gif)


Gerekli Kütüphaneler:

-> import serial -- Komut satırına **pip install pyserial** yazarak bu kütüphaneyi kolayca kurabilirsiniz.

-> import serial.tools.list_ports

-> import time

# STM32-F103C6TX Mikrodenetleyicisi İle Gönderilen Verinin Seri Monitörden Okunan Mesajı:
[putyyyy](https://user-images.githubusercontent.com/74931027/158284236-49620d0a-6119-4714-96a4-863be1c54627.gif)

# STM32-F103C6TX Mikrodenetleyicisi İle Gönderilen Verinin Python Kodundan Okunan Mesajı:
![gitgit](https://user-images.githubusercontent.com/74931027/158281892-6ac1d0a4-a422-4700-af93-81bcd8094232.png)

Not: Gecikmeden kaynaklı TEST mesajı ardı ardına yazılıyor. STM32 geliştirme kartının yolladığı veri kodunda gecikme var ve aynı şekilde Python kodunda da bir gecikme var. Ufak bi düzenleme ile bu sorunun üstesinden gelinebilir.

# STM32 Mikrodenetleyici İle Gönderilen Mesajın Kodu: (STM32CubeIDE yazılımı kullanılarak yazılmıştır.)
![stm32kod](https://user-images.githubusercontent.com/74931027/158085426-854d6287-a107-4f29-814c-b4ed50bb65af.png)

# STM32-F103C6TX Mikrodenetleyicisinin USART Ayarı: (STM32CubeIDE yazılımı kullanılarak yazılmıştır.)
![stm32ioc](https://user-images.githubusercontent.com/74931027/158085433-ad24a111-05ea-493a-8418-2bd5a8f6983d.png)
