---
title: Заполнить AcroForm - Заполнение PDF-формы с помощью Python
linktitle: Заполнить AcroForm
type: docs
weight: 20
url: /ru/python-net/fill-form/
description: Вы можете заполнять формы в вашем PDF‑документе с помощью библиотеки Aspose.PDF для Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как заполнить поле формы в PDF с помощью Python
Abstract: Статья предоставляет руководство о том, как заполнить поле формы в PDF‑документе с использованием библиотеки Aspose.PDF для Python. В ней объясняется процесс доступа к полю формы из коллекции форм документа и установки его значения через свойство value поля. Пример кода демонстрирует, как открыть PDF‑документ, перебрать его поля формы, чтобы найти конкретное поле по частичному имени (в данном случае "Field 1"), и изменить значение TextBoxField на "777". В конце обновлённый документ сохраняется в выходной файл. Предоставлены ссылки на соответствующую документацию Aspose для дальнейшего изучения.
---

## Заполнить поле формы в PDF‑документе

Следующий пример заполняет поля PDF‑формы новыми значениями с помощью Aspose.PDF для Python через .NET и сохраняет обновлённый документ. Поддерживает обновление нескольких полей путем указания словаря имён полей и их значений.

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Define the new field values
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New"
    }

    # Create a Form object from the input PDF file
    form = ap.facades.Form(path_infile)

    # Fill out the form fields with the new values
    for formField in form.field_names:
        if formField in new_field_values:
            form.fill_field(formField, new_field_values[formField])

    # Save the modified form to the output PDF file
    form.save(path_outfile)
```



