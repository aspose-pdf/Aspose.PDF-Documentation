---
title: Извлечение данных из AcroForm с помощью Python
linktitle: Извлечение данных из AcroForm
type: docs
weight: 50
url: /ru/python-net/extract-data-from-acroform/
description: Aspose.PDF упрощает извлечение данных полей формы из PDF-файлов. Узнайте, как извлекать данные из AcroForm и сохранять их в формате JSON, XML или FDF.
lastmod: "2025-03-13"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь данные из AcroForm через Python
Abstract: Эта статья содержит подробное руководство по использованию Aspose.PDF for Python для работы с полями форм в PDF-документах. В ней описаны разные способы извлечения, обработки и экспорта данных форм из PDF. Сначала показано, как извлечь значения полей формы и сохранить их в словарь с последующим выводом данных в формате JSON. Затем демонстрируется экспорт данных формы напрямую в JSON-файлы, что упрощает сериализацию данных. Кроме того, статья рассматривает экспорт данных формы в другие форматы, такие как XML, FDF (Forms Data Format) и XFDF, которые удобны для обмена данными и структурированного хранения. Каждый раздел содержит фрагменты кода Python, помогающие разобраться в реализации. В целом статья служит практическим материалом для разработчиков, которым нужно встроить обработку PDF-форм в свои Python-приложения.
---

## Извлеките поля формы из PDF-документа

[Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) из пространства имен `aspose.pdf.facades` предоставляет простой способ читать данные полей AcroForm без открытия полной объектной модели документа. Переберите `form.field_names`, чтобы получить имена всех полей формы, затем вызовите `form.get_field(name)`, чтобы получить их текущие значения.

1. Создайте объект `Form`, передав путь к входному файлу.
1. Переберите `form.field_names`, чтобы перечислить все имена полей.
1. Вызовите `form.get_field(name)` для каждого имени и сохраните результат в словарь.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = self.dataDir + infile
    form = apdf.facades.Form(path_infile)

    form_values = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_values[formField] = form.get_field(formField)

    print(form_values)
```

## Получите значение поля формы по заголовку

Если вы знаете точное имя поля формы, заданное в PDF, вы можете получить его значение напрямую с помощью `form.get_field(name)`, не перебирая всю коллекцию полей. Это самый быстрый подход, когда нужны только отдельные поля.

1. Создайте объект [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form), передав путь к входному файлу.
1. Вызовите `form.get_field("FieldName")`, указав точный заголовок поля, как он задан в PDF.
1. Используйте возвращённое строковое значение в приложении.

```python

    import aspose.pdf as apdf

    form = apdf.facades.Form(path_infile)

    # Retrieve a single field value by its name
    value = form.get_field("FirstName")
    print(value)
```

## Извлеките поля формы из PDF-документа в JSON

Существует два способа экспортировать данные AcroForm в JSON. Первый использует встроенный метод `export_json` класса [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form), который сериализует все данные полей напрямую в файловый поток за один вызов.

1. Создайте объект `Form`, передав путь к входному файлу.
1. Откройте выходной файл как двоичный поток с помощью `FileIO`.
1. Вызовите `form.export_json(stream, True)`, чтобы записать JSON-вывод.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

Второй подход строит словарь Python из `field_names` и `get_field`, а затем сериализует его с помощью `json.dumps`. Используйте этот вариант, если нужно преобразовать или отфильтровать данные перед записью.

1. Переберите `form.field_names` и заполните словарь значениями полей.
1. Сериализуйте словарь с помощью `json.dumps(form_data, indent=4)`.
1. Запишите полученную JSON-строку в выходной файл.

```python

    import aspose.pdf as apdf
    from os import path
    import json

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Извлеките данные в XML из PDF-файла

Экспорт в XML полезен при интеграции данных PDF-форм с системами, которые принимают структурированные XML-каналы или схемы. Класс [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form) предоставляет метод `export_xml`, выполняющий преобразование за один шаг.

1. Создайте экземпляр `Form` и привяжите PDF с помощью `form.bind_pdf(path)`.
1. Откройте выходной файл как двоичный поток.
1. Вызовите `form.export_xml(stream)`, чтобы записать все данные полей в формате XML.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export data to XML file
    with FileIO(path_outfile, "w") as f:
        form.export_xml(f)
```

## Экспортируйте данные в FDF из PDF-файла

FDF (Forms Data Format) является стандартным форматом обмена данными AcroForm и широко поддерживается PDF-просмотрщиками и инструментами обработки. Используйте `export_fdf` класса [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form), чтобы создать отдельный FDF-файл, который можно импортировать обратно в исходный PDF или другую совместимую форму.

1. Создайте экземпляр `Form` и привяжите исходный PDF с помощью `form.bind_pdf(path)`.
1. Откройте выходной файл как двоичный поток.
1. Вызовите `form.export_fdf(stream)`, чтобы записать данные FDF.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## Экспортируйте данные в XFDF из PDF-файла

XFDF (XML Forms Data Format) является XML-ориентированным развитием FDF и лучше подходит для использования в веб-сервисах и современных конвейерах обработки данных. Как и FDF, XFDF-файл можно импортировать обратно в совместимую PDF-форму. Используйте `export_xfdf` класса [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form), чтобы сформировать выходной файл.

1. Создайте экземпляр `Form` и привяжите исходный PDF с помощью `form.bind_pdf(path)`.
1. Откройте выходной файл как двоичный поток.
1. Вызовите `form.export_xfdf(stream)`, чтобы записать данные XFDF.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Create Form object
    form = apdf.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```
