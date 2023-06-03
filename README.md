# Reading Data From Serial Port With Python

Bu projede STM32-F103C6TX2 mikrodenetleyicisinin USART portundan gelen mesaj verisinin Python aracılığı ile okunmasını sağlayan kod yazılmıştır. Bu mantığı kullanarak STM32 'nin USART portundan gelen veriyi okuyabilir ve bu gelen veriyi işleyebilirsiniz. Kodu çalıştırdığınızda açık olan Port 'ları görüntüleyebilir, Portu seçebilir ve Haberleşme Hızını(Boud Rate) girebilirsiniz. İlgili değerler girildikten sonra kod gelen veriyi okumaya başlayacaktır.

![prg hk gif](https://user-images.githubusercontent.com/74931027/158285012-bb844194-e7ff-400f-a767-5ee9ab53ae1f.gif)

Gerekli Kütüphaneler:
```bash
-> import serial -- Komut satırına **pip install pyserial** yazarak bu kütüphaneyi kolayca kurabilirsiniz.

-> import serial.tools.list_ports

-> import time
```
# STM32-F103C6TX Mikrodenetleyicisi İle Gönderilen Verinin Seri Monitörden Okunan Mesajı:
![putyyyy](https://user-images.githubusercontent.com/74931027/158284236-49620d0a-6119-4714-96a4-863be1c54627.gif)

# STM32-F103C6TX Mikrodenetleyicisi İle Gönderilen Verinin Python Kodundan Okunan Mesajı:
![gitgit](https://user-images.githubusercontent.com/74931027/158281892-6ac1d0a4-a422-4700-af93-81bcd8094232.png)

Not: Gecikmeden kaynaklı TEST mesajı ardı ardına yazılıyor. STM32 geliştirme kartının yolladığı veri kodunda gecikme var ve aynı şekilde Python kodunda da bir gecikme var. Ufak bi düzenleme ile bu sorunun üstesinden gelinebilir.

# STM32 Mikrodenetleyici İle Gönderilen Mesajın Kodu: (STM32CubeIDE yazılımı kullanılarak yazılmıştır.)
![stm32kod](https://user-images.githubusercontent.com/74931027/158085426-854d6287-a107-4f29-814c-b4ed50bb65af.png)

# STM32-F103C6TX Mikrodenetleyicisinin USART Ayarı: (STM32CubeIDE yazılımı kullanılarak yazılmıştır.)
![stm32ioc](https://user-images.githubusercontent.com/74931027/158085433-ad24a111-05ea-493a-8418-2bd5a8f6983d.png)

# Faydalı olması dileğimle... İyi çalışmalar.
**İSMAİL SELÇUK ÇINAR / Electrical and Electronics & Aeronautical Engineering Student - 3rd Year**

📧 &nbsp;If you have any problems you can send me an email at cinarismailselcuk@gmail.com I will try to answer as soon as possible.
### 🤝🏻 &nbsp;Contact Me & Social Media

<p align="center">
<a href="mailto:cinarismailselcuk@gmail.com"><img src="https://img.shields.io/badge/-Mail-D14836?style=flat&logo=Gmail&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/ismailselcukcinar/"><img src="https://img.shields.io/badge/-LinkedIn-0077B5?style=flat&logo=Linkedin&logoColor=white%22"/</a>
<a href="https://instagram.com/ismail_selcuks"><img src="https://img.shields.io/badge/-Instagram_-E4405F?style=flat&logo=Instagram&logoColor=white"/></a>
<a href="https://twitter.com/ismail_selcuks"><img src="https://img.shields.io/badge/-Twitter_-1976c2?style=flat&logo=Twitter&logoColor=white"/></a>
<a href="https://www.youtube.com/channel/UCSt6rE5y6iklyFBpm-0xOYA"><img src="https://img.shields.io/badge/-YouTube_-c4302b?style=flat&logo=YouTube&logoColor=white"/></a>
<a href="https://discordapp.com/users/652243845790302239/"><img src="https://img.shields.io/badge/-Discord_-6A5ACD?style=flat&logo=Discord&logoColor=white"/></a>
</p>
