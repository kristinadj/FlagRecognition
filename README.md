# FlagRecognition

### Instalacija:
Otvoriti FlagRecognition/jupyter-notebooks/TrainYoloWithCUDA.ipynb u Google Collab okruženju i povezati sa GoogleDrive-om (link ispod podnaslova Weights).
Za treniranje ispočetka pokrenuti sve korake redom, a za korišćenje postojećih težina i predikciju koristiti korake ipod podnaslova Testing (u notebook-u).

### Tim:
Kristina Đereg SW36/2016

### Definicija problema:
Program treba da detektuje i prepozna zastavu na fotografiji (srpska, grčka ili mađarska)

### Skup podataka:
Skup podataka uključuje 10 država Evrope:

- Srbija
- Grčka
- Mađarska
- Francuska
- Nemačka
- Švajcarska
- Slovenija
- Portugal
- Španija
- Crna Gora

### Metodologija:
Za detekciju i prepoznavanje koristi se YOLO algoritam.

### Weights: https://drive.google.com/drive/folders/1enXnh_Rb_98O6TQozATFE6vvzAFAvbB9?usp=sharing

### Evaluacija:
Skup podataka je podeljen na test, trening i validacioni u razmeri 70:15:15. Kao metrika evaluacije se koristi mAP.
