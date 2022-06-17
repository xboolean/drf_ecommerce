![drf_e_commerce](/img/drf_e.jpg)
___
![db_design](/img/db_design.jpeg)
# WIP
___
Учебный проект серверной части интернет-магазина, в котором покупатели имеют возможность заказывать товары, добавленные сотрудниками магазина. Регистрация пользователей осуществляется посредством e-mail, активация аккаунта происходит также через почту. На платформе есть два типа пользователей: админы, у которых есть возможность добавлять, изменять товарные позиции и покупатели, которые могут формировать заказы из имеющихся позиций. Каждому товару должна быть присвоена как минимум одна товарная позиция, определяемая значением SKU. К примеру, товарные позиции могут представлять собой разные размеры одной и той же футболки.  Проект будет запускаться в docker на сервере Ubuntu.

Стек: Django, Redis, Celery, Docker, Elasticsearch.
___
<details>
<summary>Реализованные задачи.</summary>
    &check; готов костяк базы данных: Order, Product, ProductUnit, M2M model tables.<br>
    &check; имплементирована расширенная модель пользователей.<br>
    &check; сериализаторы и вьюсеты для товаров и заказа.<br>
    &check; возможность создания заказа покупателем.<br>
</details>

<details>
<summary>Запланированные задачи.</summary>
    - настройка Docker-compose<br>
    - написание юнит-тестов<br>
    - имплементация jwt-аутентификации, хранение токенов в Redis<br>
    - активация аккаунта посредством почты<br>
    - добавление промо-акций на товары <br>
</details>
