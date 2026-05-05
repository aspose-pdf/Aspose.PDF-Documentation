---
title: Удалить таблицы из существующего PDF
linktitle: Удалить таблицы
description: Узнайте, как удалить одну или несколько таблиц из существующих PDF‑документов на Python.
lastmod: "2026-04-17"
type: docs
weight: 50
url: /ru/python-net/removing-tables/
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как удалить таблицы из PDF с помощью Python
Abstract: В этой статье рассматривается функциональность Aspose.PDF for Python via .NET, с особым акцентом на работу с таблицами в PDF‑документах. Библиотека позволяет пользователям вставлять или создавать таблицы как в новых, так и в существующих PDF‑файлах, а также манипулировать и удалять таблицы из существующих PDF. В статье представляется класс `TableAbsorber`, который играет ключевую роль в идентификации и взаимодействии с таблицами в PDF. Добавлен новый метод `remove()`, позволяющий удалять таблицы. Документ содержит два фрагмента кода — один, демонстрирующий удаление одной таблицы из PDF, и второй, показывающий удаление множества таблиц. Эти примеры подчёркивают практическое применение класса `TableAbsorber` для удаления таблиц из PDF‑документов.
---

## Удалить таблицу из PDF‑документа

Aspose.PDF for Python позволяет удалить таблицу из PDF. Он открывает существующий PDF, обнаруживает первую таблицу на первой странице с помощью TableAbsorber, удаляет эту таблицу, используя [remove_one_table](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods). После сохранения обновлённого PDF в новый файл.

Используйте эту страницу, когда нужно очистить PDF, содержащие множество таблиц, удалить устаревшее табличное содержание или упростить документы перед повторным распространением.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_one_table(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(outfile)
```

## Удалить все таблицы из PDF‑документа

С помощью нашей библиотеки вы можете удалить все таблицы с конкретной страницы в PDF. Код открывает существующий PDF, обнаруживает все таблицы на второй странице с помощью TableAbsorber, перебирает обнаруженные таблицы, удаляет каждую из них и затем сохраняет изменённый PDF в новый файл. Это полезно, когда необходимо массово удалить таблицы со страницы, оставив остальное содержание PDF нетронутым.

```python
import aspose.pdf as ap
from os import path
import sys

def remove_all_tables(infile: str, outfile: str) -> None:
    # Load existing PDF document
    document = ap.Document(infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(outfile)
```

## Связанные темы таблицы

- [Работа с таблицами в PDF с использованием Python](/pdf/ru/python-net/working-with-tables/)
- [Добавить таблицы в PDF с помощью Python](/pdf/ru/python-net/adding-tables/)
- [Извлекать таблицы из PDF‑документов](/pdf/ru/python-net/extracting-table/)
- [Манипулировать таблицами в существующих PDF](/pdf/ru/python-net/manipulating-tables/)