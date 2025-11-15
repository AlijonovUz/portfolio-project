# Django Portfolio – Serverga o'rnatish bo'yicha qo'llanma

Ushbu qo'llanma Django asosidagi portfolio loyihasini serverga to'g'ri joylashtirish va ishga tushirish jarayonlarini bosqichma-bosqich tushuntiradi.

---

## 1. Loyihani serverga nusxalash

Avval loyihani serveringizdagi domain papkasiga nusxalaysiz. Git orqali klon qilinganda, odatda loyiha nomi bilan papka hosil bo'ladi.

Misol path:

```
/var/www/example.com/
```

Agar loyiha boshqa papkada (`portfolio/` kabi) turgan bo'lsa, uni to'g'ridan-to'g'ri domain papkasiga ko'chiring.

---

## 2. Static fayllarni yig'ish

Loyihadagi barcha static fayllarni quyidagi buyruq orqali yig'ing:

```bash
python3 manage.py collectstatic
```

Bu buyruq static fayllarni `static/` papkasiga jamlaydi. Shundan so'ng Nginx orqali static fayllarni xizmat qilish uchun mos konfiguratsiya kiritish kerak bo'ladi.

Agar Nginx sozlamalari murakkab tuyulsa, loyihani to'g'ridan-to'g'ri `example.com/` papkasi ichiga joylashtirsangiz ham bo'ladi.

---

## 3. settings.py dagi asosiy sozlamalar

### DEBUG qiymatini o'zgartirish

```python
DEBUG = False
```

Deploy jarayonida doim `False` bo'lishi kerak.

### CSRF_TRUSTED_ORIGINS sozlamasi

```python
CSRF_TRUSTED_ORIGINS = [
    "https://example.com",
    "https://www.example.com",
    "http://example.com",
    "http://www.example.com",
]
```

Bu yerda `example.com` o'rniga o'z domain nomingizni yozing. Aks holda, bog'lanish (contact) formasi ishlamaydi.

---

## 4. index.html faylini yangilash

`templates/index.html` faylida quyidagilarni o'zgartiring:

- Ism-familiya
- Navbar qismidagi `Abdulbosit-dev`
- "Men haqimda" bo'limidagi matn

Faqat yuqoridagi qismlarni o'zgartiring. Shablonning qolgan strukturasi va kodlariga tegmaslik tavsiya etiladi.

---

## 5. Loyihani fon rejimida ishga tushirish

Quyidagi misol `screen` yordamida loyihani fon rejimida ishga tushirishni ko'rsatadi:

```bash
screen -S portfolio
python3 manage.py runserver 0.0.0.0:8000
```

Ekrandan ajralish uchun:

```
Ctrl + A, D
```

Istasangiz Gunicorn, Supervisor yoki boshqa production serverlarni ham ishlatishingiz mumkin.

---

## 6. Admin panelga kirish

Admin panelga kirish uchun brauzerda quyidagi manzilga murojaat qiling:

```
https://example.com/admin/
```

Kirish ma'lumotlari:

- Login: admin
- Parol: admin

Xavfsizlik sababli parolni keyinchalik albatta o'zgartiring.

---

**Frontend dasturchi:** https://github.com/Saboo24/
**Backend dasturchi:** https://github.com/AlijonovUz/
