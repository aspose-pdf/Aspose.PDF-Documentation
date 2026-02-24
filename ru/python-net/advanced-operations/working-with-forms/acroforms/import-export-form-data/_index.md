---
title: Импорт и экспорт данных форм
type: docs
weight: 80
url: /ru/python-net/import-export-form-data/
description: В этом разделе объясняется, как импортировать и экспортировать данные форм.
lastmod: "2025-08-05"
TechArticle: true
AlternativeHeadline: Техники импорта и экспорта с использованием Aspose.PDF для Python через .NET.
Abstract: Эта подборка представляет комплексный набор техник импорта и экспорта данных форм с использованием Aspose.PDF для Python через .NET. Она охватывает рабочие процессы интеграции PDF‑форм с внешними форматами данных, включая XML, FDF, XFDF и JSON. Пользователи могут автоматизировать массовое заполнение форм, импортируя структурированные данные в интерактивные поля, либо извлекать значения полей для анализа, резервного копирования или интеграции с другими системами. Примеры демонстрируют, как привязывать PDF‑формы, передавать данные между форматами и сохранять обновленные документы, обеспечивая масштабируемую и последовательную обработку документов в различных приложениях.
---

## Импорт данных формы из XML‑файла

Следующий пример демонстрирует, как импортировать данные формы из XML‑файла в существующую PDF‑форму с помощью Aspose.PDF для Python. Привязав PDF‑форму, загрузив XML‑данные и сохранив обновлённый файл, вы можете быстро заполнять интерактивные поля формы без ручного редактирования каждой страницы. Этот метод идеален для автоматизации массового заполнения форм, обработки больших наборов данных и обеспечения согласованности данных в нескольких документах.

Используйте следующие шаги:

1. Создайте объект Form с помощью Aspose.PDF.
1. Привяжите PDF‑форму.
1. Загрузите XML‑данные.
1. Импортируйте XML в PDF.
1. Сохраните обновлённый PDF.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Define the working directory path
    workdir_path = "/path/to/working/directory"

    # Construct full file paths using the working directory
    path_infile = path.join(workdir_path, infile)
    path_datafile = path.join(workdir_path, datafile)
    path_outfile = path.join(workdir_path, outfile)

    # Create a Form object from Aspose.PDF
    form = ap.facades.Form()

    # Bind the input PDF form
    form.bind_pdf(path_infile)

    # Import XML data into the form
    with FileIO(path_datafile, "r") as f:
        form.import_xml(f)

    # Save the form with imported data to a new PDF file
    form.save(path_outfile)
```

## Экспорт данных полей формы из PDF‑документа в XML‑файл

Библиотека Python показывает, как экспортировать данные полей формы из PDF‑документа в XML‑файл с использованием Aspose.PDF для Python. Привязав PDF‑форму и сохранив её значения полей в формате XML, вы можете легко хранить, обрабатывать или повторно использовать данные формы в других приложениях или рабочих процессах. Этот подход идеален для резервного копирования данных, анализа и интеграции с внешними системами.

Используйте следующие шаги:

1. Создайте объект Form с помощью Aspose.PDF.
1. Привяжите PDF‑форму
1. Экспортируйте данные формы
1. Сохраните значения полей в XML

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    # Combine the working directory path with the input PDF file name
    path_infile = path.join(self.workdir_path, infile)

    # Combine the working directory path with the output XML file name
    path_outfile = path.join(self.workdir_path, datafile)

    # Create a Form object to work with PDF form fields
    form = ap.facades.Form()

    # Bind the PDF document containing the form
    form.bind_pdf(path_infile)

    # Open the XML file in write mode to store exported form data
    with FileIO(path_outfile, "w") as f:
        # Export form field data from the PDF to the XML file
        form.export_xml(f)
```

## Импорт данных полей формы из FDF

Метод 'import_data_from_fdf' импортирует данные полей формы из файла FDF (Forms Data Format) в существующую PDF‑форму и сохраняет обновлённый документ. Этот подход полезен для предварительного заполнения или обновления PDF‑форм программно без изменения структуры документа.

Используйте следующие шаги:

1. Создайте объект Form с помощью Aspose.PDF.
1. Привяжите входной PDF.
1. Импортируйте данные формы с помощью import_fdf().
1. Сохраните PDF с импортированными данными по указанному пути выходного файла.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form()
    form.bind_pdf(path_infile)

    with FileIO(path_datafile, "r") as f:
        form.import_fdf(f)
        form.save(path_outfile)
```

## Экспорт данных полей формы в FDF

Этот пример демонстрирует, как экспортировать данные формы из PDF‑документа в файл FDF (Forms Data Format) с использованием Aspose.PDF для Python через .NET.

1. Создайте объект Form с помощью Aspose.PDF.
1. Привяжите PDF‑документ.
1. Экспортируйте данные формы с помощью export_fdf().

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_fdf(f)
```

## Импорт данных полей формы из XFDF

Этот пример экспортирует данные полей формы из PDF‑документа в файл XFDF (XML Forms Data Format), а затем сохраняет обновлённый PDF с помощью Aspose.PDF для Python через .NET.

1. Создайте объект Form с помощью Aspose.PDF.
1. Привяжите PDF‑документ к форме.
1. Экспортируйте данные формы в файл XFDF.
1. Сохраните обработанную форму.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_datafile = path.join(self.workdir_path, datafile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an XFDF file
    with FileIO(path_datafile, "w") as f:
        form.export_xfdf(f)
        form.save(path_outfile)
```

## Экспорт данных полей формы в XFDF

Этот код извлекает данные полей формы из PDF‑документа и экспортирует их в файл XFDF (XML Forms Data Format) с использованием Aspose.PDF для Python.

1. Создайте объект Form с помощью Aspose.PDF.
1. Привяжите PDF‑документ к форме.
1. Экспортируйте данные формы в файл FDF.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form = ap.facades.Form()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Export form data to an FDF file
    with FileIO(path_outfile, "w") as f:
        form.export_xfdf(f)
```

## Импорт данных из другого PDF

Этот фрагмент кода демонстрирует, как перенести данные полей формы из исходного PDF в целевой PDF. Данные формы экспортируются в поток XFDF из исходного PDF, а затем импортируются в целевой PDF с помощью Aspose.PDF для Python через .NET.

1. Создайте объект Form с помощью Aspose.PDF.
1. Привяжите PDF‑документ к форме.
1. Экспортируйте данные формы из исходного PDF.
1. Импортируйте данные формы в целевой PDF.
1. Сохраните обновлённый целевой PDF.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    # Create Form object
    form_source = ap.facades.Form()
    form_dest = ap.facades.Form()

    # Bind PDF document
    form_source.bind_pdf(path_infile)
    form_dest.bind_pdf(path_outfile)

    # Export form data to an FDF file
    with StringIO() as f:
        form_source.export_xfdf(f)
        form_dest.import_xfdf(f)
        form_dest.save()
```

## Извлечение полей формы в Json

Этот метод извлекает поля формы из входного файла и экспортирует их в файл JSON.

1. Создайте объект Form с помощью Aspose.PDF.
1. Откройте выходной файл в режиме записи, используя FileIO().
1. Экспортируйте поля формы в файл JSON, используя метод form.export_json().

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    with FileIO(path_outfile, "w") as json_file:
        form.export_json(json_file, True)
```

## Извлечение полей формы в документ JSON

1. Создайте объект Form из входного файла.
1. Инициализируйте пустой словарь для хранения данных полей формы.
1. Пройдитесь по всем полям формы и извлеките их значения.
1. Сериализуйте словарь данных формы в строку JSON с отступом в 4 пробела.
1. Запишите строку JSON в выходной файл с кодировкой UTF-8.

```python

    from io import FileIO, StringIO
    import json
    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.workdir_path, infile)
    path_outfile = path.join(self.workdir_path, outfile)

    form = ap.facades.Form(path_infile)
    form_data = {}
    # Get values from all fields
    for formField in form.field_names:
        # Analyze names and values if needed
        form_data[formField] = form.get_field(formField)

    # Serialize to JSON
    json_string = json.dumps(form_data, indent=4)

    with open(path_outfile, "w", encoding="utf-8") as json_file:
        json_file.write(json_string)
```

