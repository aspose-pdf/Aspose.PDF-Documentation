---
title: Конвертировать PDF в форматы PDF/x на Python
linktitle: Конвертировать PDF в форматы PDF/x
type: docs
weight: 120
url: /ru/python-net/convert-pdf-to-pdf_x/
lastmod: "2025-09-27"
description: В этой теме показано, как конвертировать PDF в форматы PDF/x с помощью Aspose.PDF для Python через .NET.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Как конвертировать PDF в форматы PDF/x
Abstract: Статья предоставляет всестороннее руководство по конвертации PDF в форматы PDF/A, PDF/E и PDF/X с использованием Aspose.PDF для Python.
---

**Формат PDF в PDF/x означает возможность конвертировать PDF в дополнительные форматы, а именно PDF/A, PDF/E и PDF/X.**

## Конвертировать PDF в PDF/A

**Aspose.PDF for Python** позволяет конвертировать файл PDF в соответствующий PDF/A файл <abbr title="Portable Document Format / A">PDF/A</abbr>. Перед этим файл должен быть проверен. В этой теме объясняется как.

{{% alert color="primary" %}}

Обратите внимание, что мы используем Adobe Preflight для проверки соответствия PDF/A. Все инструменты на рынке имеют своё «представление» соответствия PDF/A. Пожалуйста, ознакомьтесь с этой статьей о инструментах проверки PDF/A для справки. Мы выбрали продукты Adobe для проверки того, как Aspose.PDF создает PDF‑файлы, потому что Adobe является центральным элементом всего, что связано с PDF.

{{% /alert %}}

Конвертируйте файл, используя метод Convert класса Document. Перед конвертацией PDF в соответствующий PDF/A файл проверьте PDF с помощью метода Validate. Результат проверки сохраняется в XML‑файле, после чего этот результат также передаётся методу Convert. Вы также можете указать действие для элементов, которые нельзя конвертировать, используя перечисление ConvertErrorAction.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PDF/A онлайн**

Aspose.PDF for Python предлагает вам бесплатное онлайн‑приложение ["PDF в PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), где вы можете проверить функциональность и качество работы.

[![Aspose.PDF Конверсия PDF в PDF/A с бесплатным приложением](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

Метод 'document.validate()' проверяет, соответствует ли PDF-файл стандарту PDF/A-1B (ISO‑стандартизованной версии PDF, предназначенной для длительного архивирования). Результаты проверки сохраняются в лог‑файле.

1. Загрузите PDF‑документ с помощью 'ap.Document'.
1. Вызовите метод validate с уровнем соответствия (ap.PdfFormat.PDF_A_1B).
1. Результаты проверки записываются в указанный лог‑файл.

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_A_1B)
```

### Конвертировать PDF в PDF/A-1B

В следующем фрагменте кода показано, как конвертировать PDF‑файлы в формат PDF/A-1B:

1. Загрузите PDF‑документ с помощью 'ap.Document'.
1. Вызовите метод convert со следующими параметрами:
- Путь к лог‑файлу — сохраняет детали процесса конвертации и проверки соответствия.
- Целевой формат — 'ap.PdfFormat.PDF_A_1B' (стандарт архивирования).
- Действие при ошибке — 'ap.ConvertErrorAction.DELETE' — автоматически удаляет элементы, мешающие соответствию.
1. Сохраните полученный PDF/A‑совместимый файл в указанный путь вывода.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.convert(
        self.data_dir + "pdf_pdfa.log",
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### Конвертировать PDF в PDF 2.0 и PDF/A-4

Этот пример демонстрирует, как конвертировать PDF‑документ в новые стандартизированные форматы: PDF 2.0 и PDF/A-4.
Обе конвертации помогают обеспечить соответствие современным спецификациям и требованиям архивирования.

1. Загрузите входной документ с помощью ap.Document.
1. Выполните первую конвертацию в PDF 2.0, вызвав document.convert с:
- Путь к лог‑файлу для деталей конвертации.
- Целевой формат — 'ap.PdfFormat.V_2_0'.
- Действие при ошибке — 'ap.ConvertErrorAction.DELETE' для удаления несоответствующих элементов.
1. Выполните вторую конвертацию в PDF/A-4, используя тот же метод, гарантируя, что файл также соответствует архивным стандартам.
1. Сохраните полученный документ в указанный путь вывода.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)

    document.convert(path_logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

### Конвертировать PDF в PDF/A-3A с вложенными файлами

Следующий фрагмент кода демонстрирует, как встроить внешние файлы в PDF, а затем конвертировать PDF в формат PDF/A-3A, который поддерживает вложения и подходит для длительного архивирования с вложенным контентом.

1. Загрузите входной PDF с помощью 'ap.Document'.
1. Создайте объект 'FileSpecification', указывающий файл для вложения (например, "aspose-logo.jpg") с описанием.
1. Добавьте спецификацию файла в коллекцию 'embedded_files' PDF.
1. Преобразуйте документ в PDF/A-3A с помощью 'document.convert', указав:
- Путь к файлу журнала.
- Целевой формат - 'ap.PdfFormat.PDF_A_3A'.
- Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления несоответствующих элементов.
1. Сохраните преобразованный PDF по указанному пути вывода.
1. Выведите сообщение подтверждения.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)

    fileSpecification = ap.FileSpecification(self.data_dir + "aspose-logo.jpg", "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### Преобразование PDF в PDF/A-1B с заменой шрифтов

Эта функция преобразует PDF в формат PDF/A-1B, заменяя отсутствующие шрифты доступными. Это гарантирует визуальную согласованность преобразованного PDF и соответствие архивным требованиям.

1. Загрузите PDF с помощью 'ap.Document'.
1. Преобразуйте PDF в PDF/A-1B с помощью 'document.convert', указав:
- Путь к файлу журнала.
- Целевой формат - 'ap.PdfFormat.PDF_A_1B'.
- Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления несоответствующих элементов.
1. Сохраните преобразованный PDF по указанному пути вывода.
1. Выведите сообщение подтверждения.

```python

    from os import path
    import aspose.pdf as ap 

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(path_infile)
    document.convert(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

### Преобразование PDF в PDF/A-1B с автоматической разметкой

Эта функция преобразует документ PDF в формат PDF/A-1B, автоматически помечая контент для доступности и структурной согласованности. Автоматическая разметка улучшает удобство использования документа скрин‑ридерами и обеспечивает правильную семантическую структуру.

1. Загрузите PDF с помощью 'ap.Document'.
1. Создайте 'PdfFormatConversionOptions', указав:
- Путь к файлу журнала.
- Целевой формат - 'ap.PdfFormat.PDF_A_1B'.
- Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления несоответствующих элементов.
1. Настройте 'AutoTaggingSettings':
- Включите 'enable_auto_tagging = True'.
- Установите 'heading_recognition_strategy = AUTO' для автоматического обнаружения заголовков.
1. Присвойте настройки автоматической разметки параметрам конверсии.
1. Преобразуйте PDF с помощью 'document.convert(options)'.
1. Сохраните преобразованный PDF по указанному пути вывода.
1. Выведите сообщение подтверждения.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = ap.HeadingRecognitionStrategy.AUTO

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Преобразование PDF в PDF/E

Этот фрагмент проверяет, соответствует ли PDF-документ стандарту PDF/E-1, который является ISO‑стандартом, разработанным для инженерных и технических документов. Результаты проверки сохраняются в файл журнала.

1. Загрузите PDF-документ с помощью 'ap.Document'.
1. Вызовите метод validate, указав:
- Путь к файлу журнала для сохранения результатов проверки.
- Целевой формат - 'ap.PdfFormat.PDF_E_1'.
1. Результаты проверки сохраняются в файл журнала для ознакомления.

```python

    path_infile = path.join(self.data_dir, infile)
    path_logfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.validate(path_logfile, ap.PdfFormat.PDF_E_1)
```

Следующий пример демонстрирует, как преобразовать PDF в формат PDF/E-1, который является ISO‑стандартом, разработанным для инженерной и технической документации. Этот формат сохраняет точную верстку, графику и метаданные, необходимые для инженерных рабочих процессов.

1. Загрузите исходный PDF с помощью 'ap.Document'.
1. Создайте 'PdfFormatConversionOptions', указав:
- Путь к файлу журнала для отслеживания проблем конверсии.
- Целевой формат - 'ap.PdfFormat.PDF_E_1'.
- Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления несоответствующих элементов.
1. Преобразуйте PDF с помощью 'document.convert(options)'.
1. Сохраните преобразованный PDF по указанному пути вывода.
1. Выведите сообщение подтверждения.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE)

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Преобразование PDF в PDF/X

Следующий фрагмент кода преобразует PDF‑документ в формат PDF/X-4, который является ISO‑стандартом, широко используемым в полиграфии и издательском деле. PDF/X-4 обеспечивает точность цветов, сохраняет прозрачность и встраивает ICC‑профили для единообразного вывода на разных устройствах.

1. Загрузите исходный PDF с помощью 'ap.Document'.
1. Создайте 'PdfFormatConversionOptions', указывая:
- Путь к файлу журнала.
- Целевой формат - 'ap.PdfFormat.PDF_X_4'.
- Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления несоответствующих элементов.
1. Укажите **ICC‑профиль** для управления цветом через 'icc_profile_file_name'.
1. Укажите **OutputIntent** с идентификатором условия (например, "FOGRA39") для требований к печати.
1. Преобразуйте PDF, используя 'document.convert()'.
1. Сохраните преобразованный PDF в указанный путь вывода.
1. Выведите сообщение подтверждения.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)
    path_logfile = path_outfile.replace(".pdf","_log.xml")

    document = ap.Document(path_infile)
    options =  ap.PdfFormatConversionOptions(path_logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE)

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(self.data_dir,"ISOcoated_v2_eci.icc")
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```
