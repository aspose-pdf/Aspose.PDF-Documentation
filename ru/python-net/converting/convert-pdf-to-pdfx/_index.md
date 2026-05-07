---
title: Конвертировать PDF в PDF/A, PDF/E и PDF/X в Python
linktitle: Конвертировать PDF в PDF/A, PDF/E и PDF/X
type: docs
weight: 120
url: /python-net/convert-pdf-to-pdf_x/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать файлы PDF в PDF/A, PDF/E и PDF/X на Python с помощью Aspose.PDF for Python via .NET для архивных, доступных и печатных рабочих процессов.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: Как конвертировать PDF в форматы PDF/X
Abstract: Статья предоставляет полное руководство по преобразованию PDF в форматы PDF/A, PDF/E и PDF/X с помощью Aspose.PDF for Python.
---

**PDF в формат PDF/x означает возможность конвертировать PDF в дополнительные форматы, а именно PDF/A, PDF/E и PDF/X.**

## Конвертировать PDF в PDF/A

**Aspose.PDF for Python** позволяет вам конвертировать PDF‑файл в <abbr title="Portable Document Format / A">PDF/A</abbr> соответствующий файл PDF. Прежде чем это сделать, файл должен быть проверен. Эта тема объясняет, как это сделать.

{{% alert color="primary" %}}

Обратите внимание, что мы используем Adobe Preflight для проверки соответствия PDF/A. Все инструменты на рынке имеют своё “representation” соответствия PDF/A. Пожалуйста, ознакомьтесь с этой статьёй о инструментах проверки PDF/A для справки. Мы выбрали продукты Adobe для проверки того, как Aspose.PDF создаёт PDF‑файлы, потому что Adobe находится в центре всего, что связано с PDF.

{{% /alert %}}

Конвертируйте файл, используя метод Convert класса Document. Перед преобразованием PDF в файл, соответствующий PDF/A, проверьте PDF, используя метод Validate. Результат проверки сохраняется в XML‑файл, после чего этот результат также передаётся методу Convert. Вы также можете указать действие для элементов, которые нельзя преобразовать, используя перечисление ConvertErrorAction.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PDF/A онлайн**

Aspose.PDF for Python представляет вам онлайн‑приложение ["PDF в PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), где вы можете попытаться изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в PDF/A с приложением](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

Метод 'document.validate()' проверяет, соответствует ли PDF‑файл стандарту PDF/A-1B (стандарту ISO для PDF, предназначенному для длительного архивирования). Результаты проверки сохраняются в файл журнала.

### Конвертировать PDF в PDF/A-1B

Следующий фрагмент кода показывает, как преобразовать PDF‑файлы в формат PDF/A‑1B:

1. Загрузите PDF‑документ, используя 'ap.Document'.
1. Вызовите метод convert со следующими параметрами:
    - Путь к файлу журнала - хранит детали процесса конвертации и проверок соответствия.
    - Целевой формат - 'ap.PdfFormat.PDF_A_1B' (стандарт архивирования).
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' — автоматически удаляет элементы, препятствующие соответствию.
1. Сохраните преобразованный файл, совместимый с PDF/A, в путь вывода.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA(infile, outfile):
    """Convert PDF to PDF/A-1B format."""

    document = ap.Document(infile)
    document.convert(
        outfile.replace(".pdf", "-log.xml"),
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

### Преобразовать PDF в PDF 2.0 и PDF/A-4

В этом примере показывается, как преобразовать PDF‑документ в более новые стандартизированные форматы: PDF 2.0 и PDF/A‑4.
Оба преобразования помогают обеспечить соответствие современным спецификациям и требованиям к архивированию.

1. Загрузите входной документ, используя ap.Document.
1. Выполните первое преобразование в PDF 2.0, вызвав document.convert с:
    - Путь к файлу журнала для деталей конвертации.
    - Целевой формат - 'ap.PdfFormat.V_2_0'.
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления несоответствующих элементов.
1. Выполните второе преобразование в PDF/A-4 тем же методом, обеспечив соответствие файла архивационным стандартам.
1. Сохраните полученный документ в указанном пути вывода.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA4(infile, outfile):
    logfile = outfile.replace(".pdf", "_log.xml")

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)
    document.convert(logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### Конвертировать PDF в PDF/A-3A с встроенными файлами

Следующий фрагмент кода демонстрирует, как внедрять внешние файлы в PDF, а затем преобразовать PDF в формат PDF/A-3A, который поддерживает вложения и подходит для долгосрочного архивирования с внедренным содержимым.

1. Загрузите входной PDF, используя 'ap.Document'.
1. Создайте объект 'FileSpecification', указывающий на файл для встраивания (например, "aspose-logo.jpg") с описанием.
1. Добавьте спецификацию файла в коллекцию ‘embedded_files’ PDF.
1. Конвертируйте документ в PDF/A-3A, используя 'document.convert', указывая:
    - Путь к файлу журнала.
    - Целевой формат - 'ap.PdfFormat.PDF_A_3A'.
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления несоответствующих элементов.
1. Сохраните преобразованный PDF в путь вывода.


```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_attachment(infile, attachement_file, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    document = ap.Document(infile)

    fileSpecification = ap.FileSpecification(attachement_file, "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(
        logfile, ap.PdfFormat.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE
    )
    document.save(outfile)
```

### Конвертировать PDF в PDF/A-1B с заменой шрифтов

Эта функция преобразует PDF в формат PDF/A-1B, заменяя отсутствующие шрифты доступными. Это гарантирует, что преобразованный PDF останется визуально согласованным и соответствующим требованиям архивных стандартов.

1. Загрузите PDF, используя 'ap.Document'.
1. Конвертировать PDF в PDF/A-1B с помощью 'document.convert', указывая:
    - Путь к файлу журнала.
    - Целевой формат - 'ap.PdfFormat.PDF_A_1B'.
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления несоответствующих элементов.
1. Сохраните преобразованный PDF в путь вывода.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_replace_missing_fonts(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### Преобразовать PDF в PDF/A-1B с автоматическим тегированием

Эта функция преобразует PDF‑документ в формат PDF/A-1B, автоматически добавляя теги к содержимому для обеспечения доступности и структурной согласованности. Автоматическое тегирование улучшает удобство использования документа для программ чтения с экрана и обеспечивает правильную семантическую структуру.

1. Загрузите PDF, используя 'ap.Document'.
1. Создайте 'PdfFormatConversionOptions', указывая:
    - Путь к файлу журнала.
    - Целевой формат - 'ap.PdfFormat.PDF_A_1B'.
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления несоответствующих элементов.
1. Настройте 'AutoTaggingSettings':
    - Включить 'enable_auto_tagging = True'.
    - Установите 'heading_recognition_strategy = AUTO' для автоматического определения заголовков.
1. Назначьте настройки авторазметки параметрам конвертации.
1. Преобразуйте PDF, используя 'document.convert(options)'.
1. Сохраните преобразованный PDF в путь вывода.


```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_automatic_tagging(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE
    )

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = (
        ap.HeadingRecognitionStrategy.AUTO
    )

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Конвертировать PDF в PDF/E

Этот фрагмент кода демонстрирует, как преобразовать PDF‑документ в формат PDF/E-1, который является стандартом ISO, предназначенным для инженерной и технической документации. Этот формат сохраняет точный макет, графику и метаданные, необходимые для инженерных рабочих процессов.

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте 'PdfFormatConversionOptions', указывая:
    - Путь к файлу журнала для отслеживания проблем преобразования.
    - Целевой формат - 'ap.PdfFormat.PDF_E_1'.
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления несоответствующих элементов.
1. Преобразуйте PDF, используя 'document.convert(options)'.
1. Сохраните преобразованный PDF в указанный путь вывода.
1. Выведите сообщение подтверждения.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_E(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE
    )

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Конвертировать PDF в PDF/X

Следующий фрагмент кода преобразует PDF‑документ в формат PDF/X-4, который является стандартом ISO, часто используемым в полиграфии и издательской индустрии. PDF/X-4 обеспечивает точность цветов, сохраняет прозрачность и встраивает ICC‑профили для обеспечения согласованного вывода на разных устройствах.

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте 'PdfFormatConversionOptions', указывая:
    - Путь к файлу журнала.
    - Целевой формат - 'ap.PdfFormat.PDF_X_4'.
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления несоответствующих элементов.
1. Предоставьте **файл ICC‑профиля** для управления цветом через 'icc_profile_file_name'.
1. Укажите **OutputIntent** с идентификатором условия (например, "FOGRA39") для требований к печати.
1. Преобразуйте PDF, используя 'document.convert()'.
1. Сохраните преобразованный PDF в указанный путь вывода.


```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_X(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE
    )

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(
        path.dirname(infile), "ISOcoated_v2_eci.icc"
    )
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Связанные преобразования

- [Конвертировать PDF в Word](/pdf/ru/python-net/convert-pdf-to-word/) для рабочих процессов редактируемого контента после проверки соответствия стандартам.
- [Конвертировать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) когда ваш целевой вывод готов к вебу, а не основан на стандартах PDF.
