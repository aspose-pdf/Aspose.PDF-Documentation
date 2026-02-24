---
title: Извлечение AcroForm — извлечение данных формы из PDF на Python
linktitle: Извлечение AcroForm
type: docs
weight: 30
url: /ru/python-net/extract-form/
description: Извлеките форму из вашего PDF‑документа с помощью библиотеки Aspose.PDF для Python. Получите значение отдельного поля PDF‑файла.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как получить данные формы из PDF с помощью Python
Abstract: Эта статья представляет руководство по извлечению данных из полей формы в PDF‑документе с использованием Python. В ней описывается, как перемещаться по всем полям с помощью библиотеки Aspose.PDF, конкретно путём доступа к коллекции `Form` и использованию типа `Field` и его свойства `value`. Включён пример кода на Python, демонстрирующий, как открыть PDF‑документ, пройтись по его полям формы и вывести имя и значение каждого поля. Этот метод полезен для программного получения данных формы из PDF‑файлов.
---

## Извлечение данных из формы

### Получить значения всех полей PDF‑документа

Чтобы получить значения всех полей в PDF‑документе, необходимо пройти по всем полям формы и затем получить значение, используя свойство Value. Получите каждое поле из коллекции Form, в базовом типе поля, называемом [Поле](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/) и доступ к его свойству [value](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/field/#properties).

Следующие фрагменты кода на Python показывают, как получить значения всех полей из PDF‑документа.

```python

    import aspose.pdf as ap

    # Construct the full path to the input PDF file
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    # Create a Form object from the PDF file
    form = ap.facades.Form(path_infile)

    # Initialize an empty dictionary to store form values
    form_values = {}

    # Iterate through all form fields in the PDF
    for formField in form.field_names:
        # Retrieve the value for each form field and store in the dictionary
        form_values[formField] = form.get_field(formField)

    # Print and return the extracted form values
    print(form_values)
```

