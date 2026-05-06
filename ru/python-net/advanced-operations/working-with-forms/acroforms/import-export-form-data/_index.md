---
title: Импорт и экспорт данных формы
linktitle: Импорт и экспорт данных формы
type: docs
weight: 80
url: /ru/python-net/import-export-form-data/
description: Импортировать и экспортировать данные полей AcroForm в форматах XML, FDF, XFDF и JSON с использованием Aspose.PDF for Python via .NET.
lastmod: "2026-04-28"
TechArticle: true
AlternativeHeadline: Техники импорта и экспорта с использованием Aspose.PDF for Python via .NET.
Abstract: Этот сборник представляет собой комплексный набор техник импорта и экспорта данных форм с использованием Aspose.PDF for Python via .NET. Он охватывает рабочие процессы интеграции PDF форм с внешними форматами данных, включая XML, FDF, XFDF и JSON. Пользователи могут автоматизировать массовое заполнение форм, импортируя структурированные данные в интерактивные поля, или извлекать значения полей для анализа, резервного копирования или интеграции с другими системами. Примеры демонстрируют, как связывать PDF формы, передавать данные между форматами и сохранять обновлённые документы, обеспечивая масштабируемую и последовательную обработку документов в различных приложениях.
---

Эта страница демонстрирует типовые рабочие процессы импорта и экспорта данных AcroForm с помощью Aspose.PDF for Python via .NET. Все операции используют [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/form/) фасад.

## Импортировать данные полей формы из XML

Используйте этот подход для заполнения PDF-формы данными из внешнего XML.

1. Создайте `Form` объект.
1. Привяжите входной PDF.
1. Откройте XML‑файл данных.
1. Импортируйте данные XML в форму.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xml(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xml(f)

    form.save(output_file_name)
```

## Экспортировать данные полей формы в XML

Этот метод экспортирует значения полей формы из PDF‑документа в XML.

1. Создайте `Form` объект.
1. Привяжите входной PDF.
1. Откройте файл вывода XML.
1. Экспортируйте данные формы в XML.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xml(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)
    with FileIO(output_file_name, "w") as f:
        form.export_xml(f)
```

## Импортировать данные полей формы из FDF

Определённый `import_data_from_fdf` метод импортирует данные полей формы из файла FDF (Формат данных форм) в форму PDF.

1. Создайте `Form` объект.
1. Привяжите входной PDF.
1. Импортируйте данные формы с `import_fdf()`.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_fdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_fdf(f)
        form.save(output_file_name)
```

## Экспортировать данные полей формы в FDF

В этом примере данные формы экспортируются из PDF‑документа в файл FDF.

1. Создайте `Form` объект.
1. Свяжите PDF‑документ.
1. Экспортируйте данные формы с `export_fdf()`.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_fdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_fdf(f)
```

## Импортировать данные полей формы из XFDF

Используйте этот метод для импорта данных полей формы из файла XFDF (XML Forms Data Format) в PDF-форму.

1. Создайте `Form` объект.
1. Привяжите входной PDF.
1. Импортируйте данные формы из файла XFDF.
1. Сохраните обновлённый PDF.

```python
from io import FileIO
import aspose.pdf as ap

def import_data_from_xfdf(input_file_name, data_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(data_file_name, "r") as f:
        form.import_xfdf(f)
        form.save(output_file_name)
```

## Экспортировать данные полей формы в XFDF

Этот код экспортирует данные полей формы из PDF‑документа в файл XFDF.

1. Создайте `Form` объект.
1. Привяжите входной PDF.
1. Экспортируйте данные формы в XFDF.

```python
from io import FileIO
import aspose.pdf as ap

def export_data_to_xfdf(input_file_name, output_file_name):
    form = ap.facades.Form()
    form.bind_pdf(input_file_name)

    with FileIO(output_file_name, "w") as f:
        form.export_xfdf(f)
```

## Импортировать данные из другого PDF

Этот пример переносит данные полей формы из исходного PDF в целевой PDF, экспортируя XFDF в поток в памяти и импортируя его в целевую форму.

1. Создайте источник и назначение `Form` объекты.
1. Объедините исходный и целевой PDF.
1. Экспортируйте данные формы из исходного PDF.
1. Импортируйте данные формы в целевой PDF.
1. Сохраните обновлённый PDF назначения.

```python
from io import StringIO
import aspose.pdf as ap

def import_data_from_another_pdf(source_pdf_name, destination_pdf_name, output_file_name):
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    form_source.bind_pdf(source_pdf_name)
    form_dest.bind_pdf(destination_pdf_name)

    with StringIO() as xfdf_stream:
        form_source.export_xfdf(xfdf_stream)
        xfdf_stream.seek(0)
        form_dest.import_xfdf(xfdf_stream)

    form_dest.save(output_file_name)
```

## Извлечь поля формы в JSON

Этот метод экспортирует поля формы в JSON‑файл, используя `export_json()`.

1. Создайте `Form` объект.
1. Откройте файл вывода JSON.
1. Экспортируйте поля формы с помощью `export_json()`.

```python
from io import FileIO
import aspose.pdf as ap

def extract_form_fields_to_json(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    with FileIO(output_file_name, "w") as json_file:
        form.export_json(json_file, True)
```

## Извлечь FormField в JSON Document

Этот пример создает пользовательский JSON‑документ из имён полей формы и их значений.

1. Создайте объект Form из входного файла.
1. Инициализируйте пустой словарь для хранения данных полей формы.
1. Пройдите по всем полям формы и извлеките их значения.
1. Сериализуйте словарь данных формы в строку JSON с отступом в 4 пробела.
1. Запишите строку JSON в выходной файл с кодировкой UTF-8.

```python
import json
import aspose.pdf as ap

def extract_form_fields_to_json_doc(input_file_name, output_file_name):
    form = ap.facades.Form(input_file_name)
    form_data = {}
    for field_name in form.field_names:
        form_data[field_name] = form.get_field(field_name)

    json_string = json.dumps(form_data, indent=4)

    with open(output_file_name, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

## Связанные темы (подход фасадов)

- [Импортировать XML-данные](/pdf/ru/python-net/import-xml-data/)
- [Импортировать данные FDF](/pdf/ru/python-net/import-fdf-data/)
- [Импортировать данные XFDF](/pdf/ru/python-net/import-xfdf-data/)
- [Импортировать данные JSON](/pdf/ru/python-net/import-json-data/)
- [Экспорт в XML](/pdf/ru/python-net/export-to-xml/)
- [Экспорт в FDF](/pdf/ru/python-net/export-to-fdf/)
- [Экспорт в XFDF](/pdf/ru/python-net/export-to-xfdf/)
- [Экспорт в JSON](/pdf/ru/python-net/export-to-json/)
