---

# 📊 Finance Tracker API

## 📌 Описание проекта

Finance Tracker API — это REST API для учёта личных финансов.
Позволяет добавлять доходы и расходы, распределять их по категориям и получать финансовую статистику.

---

# ⚙️ Технологии

* Python 3
* Django
* Django REST Framework
* SQLite / PostgreSQL
* drf-spectacular (Swagger)
* Git / GitHub

---

# 📁 Структура проекта

```
PyFinance/
│
├── Finance/              # приложение
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── migrations/
│
├── PyFinance/           # настройки проекта
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
```

---

# 🧠 Модели

## 📁 Category (Категория)

| Поле       | Тип      | Описание                        |
| ---------- | -------- | ------------------------------- |
| id         | int      | ID                              |
| name       | string   | Название категории (уникальное) |
| type       | string   | income / expense                |
| created_at | datetime | Дата создания                   |

Примеры:

* Зарплата (income)
* Еда (expense)

---

## 💸 Transaction (Транзакция)

| Поле             | Тип      | Описание          |
| ---------------- | -------- | ----------------- |
| id               | int      | ID                |
| title            | string   | Название операции |
| amount           | decimal  | Сумма             |
| type             | string   | income / expense  |
| category         | FK       | Категория         |
| transaction_date | date     | Дата операции     |
| comment          | text     | Комментарий       |
| created_at       | datetime | Дата создания     |

---

# 🔗 API Endpoints

---

## 📁 Categories

### Получить список категорий

```
GET /api/categories/
```

### Создать категорию

```
POST /api/categories/
```

### Получить категорию

```
GET /api/categories/{id}/
```

### Удалить категорию

```
DELETE /api/categories/{id}/
```

---

## 💸 Transactions

### Получить список транзакций

```
GET /api/transactions/
```

### Создать транзакцию

```
POST /api/transactions/
```

### Получить транзакцию

```
GET /api/transactions/{id}/
```

### Удалить транзакцию

```
DELETE /api/transactions/{id}/
```

---

## 📊 Statistics

### Получить финансовую статистику

```
GET /api/statistics/
```

### Ответ:

```json
{
  "total_income": 50000,
  "total_expense": 15000,
  "balance": 35000
}
```

---

# 🧠 Бизнес-логика

## ❗ Проверки

* сумма транзакции > 0
* income не может быть с expense категорией
* expense не может быть с income категорией
* имя категории уникально

---

## ❗ Ограничения

* нельзя удалить категорию, если она используется в транзакциях
* транзакции сортируются по дате (новые сверху)

```python
ordering = ["-transaction_date"]
```

---

# 📊 Формула баланса

```
Баланс = Доходы - Расходы
```

---

# 🎯 Примеры JSON

## 📁 Category

```json
{
  "id": 1,
  "name": "Еда",
  "type": "expense"
}
```

---

## 💸 Transaction

```json
{
  "id": 5,
  "title": "Покупка продуктов",
  "amount": 2500,
  "type": "expense",
  "category": 1,
  "transaction_date": "2026-06-01"
}
```

---

# 🧪 Swagger / Документация

## 📄 Schema

```
/api/schema/
```

## 🎨 Swagger UI

```
/api/docs/
```

---

# 🚀 Как запустить проект

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

# 🧾 GitHub требования

* публичный репозиторий
* весь код загружен
* README.md добавлен
* проект запускается

---

# 🏁 Итог

Проект включает:

✔ CRUD категории
✔ CRUD транзакции
✔ финансовую статистику
✔ бизнес-валидацию
✔ Swagger документацию

---
