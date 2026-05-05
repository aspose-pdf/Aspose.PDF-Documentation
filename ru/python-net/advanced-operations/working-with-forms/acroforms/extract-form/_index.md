---
title: Извлечь AcroForm - извлечь данные формы из PDF на Python
linktitle: Извлечь AcroForm
type: docs
weight: 30
url: /ru/python-net/extract-form/
description: Извлечь значения из полей AcroForm в PDF‑документах, используя Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как получить данные формы из PDF с помощью Python
Abstract: В этой статье показано, как извлечь данные из полей AcroForm в PDF‑документах, используя Aspose.PDF for Python via .NET. Пример проходит по именам полей формы, считывает значения с помощью фасада Form и возвращает словарь для последующей обработки. Этот рабочий процесс полезен для формирования отчётов, проверки и интеграции с внешними системами.
---

## Извлечь данные из Form

### Получить значения всех полей в PDF‑документе

Чтобы прочитать значения из всех полей PDF‑документа, пройдите по именам полей формы и получите каждое значение из [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад.

Выполните следующие шаги:

1. Привяжите входной PDF к `Form` объект.
1. Итерировать по `field_names`.
1. Считайте каждое значение с `get_field()`.
1. Сохраните значения в словаре.
1. Верните или обработайте извлечённые значения.

Следующий фрагмент кода Python демонстрирует этот подход.

```python
import aspose.pdf as ap


def get_values_from_all_fields(input_file_name):
    form = ap.facades.Form(input_file_name)

    form_values = {}
    for field_name in form.field_names:
        form_values[field_name] = form.get_field(field_name)

    print(form_values)
    return form_values
```

## Связанные темы

- [Создать AcroForm](/pdf/ru/python-net/create-form/)
- [Заполнить AcroForm](/pdf/ru/python-net/fill-form/)
- [Импорт и экспорт данных формы](/pdf/ru/python-net/import-export-form-data/)
- [Изменение AcroForm](/pdf/ru/python-net/modifying-form/)