---
title: Заполнить AcroForm — заполнить PDF‑форму с помощью Python
linktitle: Заполнить AcroForm
type: docs
weight: 20
url: /python-net/fill-form/
description: Заполнить поля AcroForm в PDF‑документе, используя Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как заполнить поле формы в PDF с помощью Python
Abstract: В этой статье объясняется, как заполнить поля AcroForm в PDF‑документе, используя Aspose.PDF for Python via .NET. В примере используется фасад Form, отображаются имена полей на новые значения в словаре, обновляются совпадающие поля и сохраняется результирующий PDF. Такой подход полезен для автоматизированных рабочих процессов завершения документов и массовой обработки форм.
---

## Заполнить поле формы в PDF‑документе

В следующем примере заполняются несколько полей в существующей PDF‑форме с помощью [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад.

Выполните следующие шаги:

1. Создайте словарь с именами полей и значениями.
1. Свяжите входной PDF с объектом Form.
1. Итерируйте доступные поля формы.
1. Заполните поля, которые существуют в словаре.
1. Сохраните обновлённый PDF.

```python
import aspose.pdf as ap

def fill_form(input_file_name, output_file_name):
    new_field_values = {
        "First Name": "Alexander_New",
        "Last Name": "Greenfield_New",
        "City": "Yellowtown_New",
        "Country": "Redland_New",
    }

    form = ap.facades.Form(input_file_name)

    for field_name in form.field_names:
        if field_name in new_field_values:
            form.fill_field(field_name, new_field_values[field_name])

    form.save(output_file_name)
```

## Связанные темы

- [Создать AcroForm](/pdf/ru/python-net/create-form/)
- [Извлечь AcroForm](/pdf/ru/python-net/extract-form/)
- [Импорт и экспорт данных формы](/pdf/ru/python-net/import-export-form-data/)