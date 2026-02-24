---
title: Извлечение данных из AcroForm с помощью Python
linktitle: Извлечение данных из AcroForm
type: docs
weight: 50
url: /ru/python-net/extract-data-from-acroform/
description: Aspose.PDF упрощает извлечение данных полей форм из PDF‑файлов. Узнайте, как извлекать данные из AcroForms и сохранять их в форматах JSON, XML или FDF.
lastmod: "2025-03-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как извлечь данные из AcroForm с помощью Python
Abstract: Статья представляет собой всестороннее руководство по использованию Aspose.PDF для Python для управления полями форм в PDF‑документах. В ней подробно описываются различные методы извлечения, манипуляции и экспорта данных форм из PDF. Статья начинается с демонстрации того, как извлекать значения полей формы и сохранять их в словарь, а затем выводить данные в формате JSON. Далее она показывает экспорт данных формы непосредственно в файлы JSON, улучшая возможности сериализации данных. Кроме того, статья охватывает экспорт данных формы в другие форматы, такие как XML, FDF (Forms Data Format) и XFDF, которые полезны для обмена данными и структурированного хранения. Каждый раздел содержит фрагменты кода на Python, помогающие понять и реализовать решение. В целом, статья служит практическим ресурсом для разработчиков, желающих интегрировать работу с формами PDF в свои Python‑приложения.
---

## Извлечение полей формы из PDF‑документа

В дополнение к возможности генерировать и заполнять поля формы, Aspose.PDF для Python упрощает извлечение данных полей формы или информации о полях формы из PDF‑файлов.

Фрагмент кода создает словарь для хранения значений всех полей в PDF‑форме. Он перебирает имена полей формы, получает их значения и заполняет словарь этими данными. В конце выводит собранные значения полей.

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

## Получить значение поля формы по заголовку

## Извлечение полей формы из PDF‑документа в JSON

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

Предоставленный фрагмент кода на Python извлекает значения его полей и сериализует эти данные в формат JSON. Он импортирует необходимые модули, формирует пути входного и выходного файлов, получает имена полей и их значения из PDF‑формы и записывает сериализованную строку JSON в указанный файл вывода.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    form = apdf.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if need
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    # Output the JSON string
    print(json_string)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Извлечение данных в XML из PDF‑файла

Следующий фрагмент кода на Python создает объект формы, привязывает к нему PDF‑документ и экспортирует данные формы в XML‑файл. Код автоматически извлекает данные из PDF‑формы и сохраняет их в структурированном формате XML.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

## Экспорт данных в FDF из PDF‑файла

Следующий фрагмент кода создает объект формы, привязывает к нему PDF‑документ и затем экспортирует данные формы в файл FDF (Forms Data Format). Файл FDF — это формат, используемый для хранения данных форм из PDF‑документов, позволяющий легко обмениваться данными.

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

## Экспорт данных в XFDF из PDF‑файла

```python

    import aspose.pdf as apdf
    from io import FileIO
    from os import path
    import json
    from aspose.pycore import cast, is_assignable

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

