# Reading-Data-From-Serial-Port-With-Python

Bu projede STM32 geliştirme kartından USART portundan gelen mesaj verisini Python ile okunmasını sağlayan kod yazılmıştır.

# STM32 Geliştirme Kartı İle Gönderilen Verinin Seri Monitörden Okunan Mesaj:
![git1](https://user-images.githubusercontent.com/74931027/158084905-bc255bd5-8358-4322-91bd-35d51508f364.png)

# STM32 Geliştirme Kartı İle Gönderilen Verinin Python Kodundan Okunan Mesaj:
![gitgit](https://user-images.githubusercontent.com/74931027/158281892-6ac1d0a4-a422-4700-af93-81bcd8094232.png)

Not: Gecikmeden kaynaklı TEST mesajı ardı ardına yazılıyor. STM32 geliştirme kartının yolladığı veri kodunda gecikme var ve aynı şekilde Python kodunda da bir gecikme var. Ufak bi düzenleme ile bu sorunun üstesinden gelinebilir.

# STM32 Geliştirme Kartı Gönderilen Mesajın Kodu:
![stm32kod](https://user-images.githubusercontent.com/74931027/158085426-854d6287-a107-4f29-814c-b4ed50bb65af.png)

# STM32 Geliştirme Kartı USART Ayarı:
![stm32ioc](https://user-images.githubusercontent.com/74931027/158085433-ad24a111-05ea-493a-8418-2bd5a8f6983d.png)
