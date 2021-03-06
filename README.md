# Электронный дневник отличника
Проект предназначен для:
1) Исправления оценок.
2) Удаления замечаний.
3) Записи в дневник похвалы.

### Как установить
Ознакомьтесь и скачайте: [электроный дневник](https://github.com/devmanorg/e-diary). \
Скопируйте файл `scripts.py` в директорию с проектом.
### Как запустить
Все команды выполняем исключительно в терминале.
1) Запустите команду: 
```
$ python get_statistics.py
```
2) Скопируйте и запустите:
```
from scripts import (
    get_schoolkid,
    fix_marks,
    remove_chastisements,
    create_commendation
)
```
3) Укажите нужные данные и запустите:

```
name = 'Фролов Иван'
subject = 'Физкультура'
```

4) Последний шаг. Исправляем оценки, получаем похвалу, удаляем замечания!

Находим школьника:
```
schoolkid = get_schoolkid(name)

```
Исправляем оценки на 4, 5:
```
fix_marks(schoolkid)

```
Удаляем замечания:
```
remove_chastisements(schoolkid)

```
Создаем похвалу:
```
create_commendation(schoolkid, subject)
```
## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
