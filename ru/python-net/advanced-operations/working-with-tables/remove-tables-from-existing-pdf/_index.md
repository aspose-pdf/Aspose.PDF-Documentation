---
title: Удалить таблицы из существующего PDF
linktitle: Удалить таблицы
type: docs
weight: 50
url: /ru/python-net/removing-tables/
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как удалить таблицы из PDF с помощью Python
Abstract: Эта статья обсуждает функциональность Aspose.PDF для Python через .NET, сосредотачивая внимание на работе с таблицами в PDF‑документах. Библиотека позволяет пользователям вставлять или создавать таблицы как в новых, так и в существующих PDF‑файлах, а также манипулировать или удалять таблицы из существующих PDF. В статье представляется класс `TableAbsorber`, который является ключевым для идентификации и взаимодействия с таблицами в PDF. Был добавлен новый метод `remove()`, позволяющий удалять таблицы. В документе приведены два примера кода — один демонстрирует, как удалить одну таблицу из PDF, а другой иллюстрирует удаление нескольких таблиц. Эти примеры подчёркивают практическое применение класса `TableAbsorber` для удаления таблиц из PDF‑документов.
---

## Удалить таблицу из PDF‑документа

Aspose.PDF for Python позволяет удалить таблицу из PDF. Он открывает существующий PDF, обнаруживает первую таблицу на первой странице с помощью TableAbsorber, удаляет эту таблицу, используя [remove_one_table](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/tableabsorber/#methods). После сохранения обновлённый PDF сохраняется в новый файл.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit first page with absorber
    absorber.visit(document.pages[1])
    # Get first table on the page
    table = absorber.table_list[0]
    # Remove the table
    absorber.remove(table)
    # Save PDF
    document.save(path_outfile)
```

## Удалить все таблицы из PDF‑документа

С помощью нашей библиотеки вы можете удалить все таблицы с определённой страницы PDF. Код открывает существующий PDF, обнаруживает все таблицы на второй странице с помощью TableAbsorber, проходит по найденным таблицам, удаляет каждую из них и затем сохраняет изменённый PDF в новый файл. Это полезно, когда необходимо массово удалить таблицы со страницы, оставив остальное содержание PDF нетронутым.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    # Load existing PDF document
    document = ap.Document(path_infile)

    # Create TableAbsorber object to find tables
    absorber = ap.text.TableAbsorber()
    # Visit second page with absorber
    absorber.visit(document.pages[1])
    #  Loop through the copy of collection and removing tables
    tables = list(absorber.table_list)
    for table in tables:
        absorber.remove(table)

    # Save document
    document.save(path_outfile)
```


