# DroneKit ile Drone Simulasyon

Bu repo Dronekit ile MissionPlanner üzerinden yazılan scriptleri simüle etmek için oluşturulmuştur.  Güncellenecektir.

## İlk Çalışma Olarak
İlk çalışma olarak udp üzerinden araca bağlanılmıştır. Araç istenilen yüksekliğe çıkartılıp geri indirilmiştir. 

## Bağlantı
Aşama 1 : 
**dronekit-sitl copter** ile copter objesi oluşturulur. İnternet bağlantısı gerektirmektedir.
 Aşama 2 :
 Mavlink bağlantısı için **mavproxy.py --master tcp:127.0.0.1:5760  --out 127.0.0.1:14550 --out 127.0.0.1:14551** yazılır.
 Aşama 3 : 
 MissionPlanner üzerinden görüntüleyebilmek için **udp** bağlantısı seçilir. Baudrate **57600** olarak seçilmelidir. Bu aşamada **listen port** sorusu ile karşılaşayacağız. Burada **14551** seçilmelidir.

Böylelikle aynı anda scriptin çalışmasını ve simüle edilen aracın hareketlerini görebileceğiz. 



