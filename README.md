# Docker Nginx + Python Projesi

Docker öğrenirken öğrendiğim konuları tek bir projede uygulamak için bu projeyi oluşturdum.

Projede basit bir Python backend uygulamasını Dockerfile ile container haline getirdim. Nginx'i reverse proxy olarak kullanarak gelen istekleri Python backend'e yönlendirdim. Servisleri Docker Compose ile birlikte çalıştırdım.

## Proje Yapısı

İsteklerin izlediği yol:

Client
↓
localhost:8085
↓
Nginx :80
↓
Python Backend :8000

Nginx ve backend aynı Docker network üzerinden haberleşiyor. Backend'in host'a ayrıca bir portu açılmıyor, istekler Nginx üzerinden backend'e gidiyor.

## Bu projede kullandıklarım

- Docker
- Dockerfile
- Docker Compose
- Nginx Reverse Proxy
- Python
- Docker Networking
- Environment Variables (.env)
- Healthcheck
- .dockerignore

## Öğrendiklerim

Bu projeyi yaparken Dockerfile ile image oluşturmayı, image ve container arasındaki farkı, port mapping mantığını ve container'ların aynı network üzerinde nasıl haberleştiğini uygulamalı olarak çalıştım.

Ayrıca Nginx'i reverse proxy olarak kullanıp backend servisine yönlendirme yaptım. Healthcheck ile backend servisinin durumunu kontrol ettim ve environment variable kullanarak bazı ayarları koddan ayırdım.

Troubleshooting çalışması sırasında backend servisini durdurarak Nginx üzerinde 502 Bad Gateway hatası oluşturdum ve Docker Compose servis durumları ile container loglarını kontrol ederek hatanın kaynağını inceledim.

## Projeyi Çalıştırma

```bash
docker compose up -d --build
```

Uygulama:

```text
http://localhost:8085
```

Healthcheck endpoint:

```text
http://localhost:8085/health
```

Projeyi durdurmak için:

```bash
docker compose down
```
