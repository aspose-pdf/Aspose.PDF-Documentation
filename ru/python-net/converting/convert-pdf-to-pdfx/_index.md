---
title: Преобразовать PDF в PDF/A, PDF/E и PDF/X с Python
linktitle: Преобразовать PDF в PDF/A, PDF/E и PDF/X
type: docs
weight: 120
url: /python-net/convert-pdf-to-pdf_x/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать PDF‑файлы в форматы PDF/A, PDF/E и PDF/X с помощью Python и Aspose.PDF for Python via .NET для архивирования, обеспечения доступности и печатных рабочих процессов.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true 
AlternativeHeadline: Как конвертировать PDF в форматы PDF/x
Abstract: В статье представлено подробное руководство по преобразованию PDF в форматы PDF/A, PDF/E и PDF/X с использованием Aspose.PDF for Python.
---

**PDF в формат PDF/x означает возможность конвертировать PDF в дополнительные форматы, а именно PDF/A, PDF/E и PDF/X.**

## Преобразовать PDF в PDF/A

**Aspose.PDF for Python** позволяет вам конвертировать PDF‑файл в <abbr title="Portable Document Format / A">PDF/A</abbr> соответствующий PDF‑файл. Прежде чем это сделать, файл необходимо проверить. Эта тема объясняет, как это сделать.

{{% alert color="primary" %}}

Обратите внимание, что мы следуем Adobe Preflight для проверки соответствия PDF/A. Все инструменты на рынке имеют своё “representation” соответствия PDF/A. Пожалуйста, ознакомьтесь с этой статьей о средствах проверки PDF/A для справки. Мы выбрали продукты Adobe для проверки того, как Aspose.PDF создаёт PDF‑файлы, поскольку Adobe находится в центре всего, что связано с PDF.

{{% /alert %}}

Конвертируйте файл, используя метод Convert класса Document. Перед тем как конвертировать PDF в файл, соответствующий PDF/A, проверьте PDF с помощью метода Validate. Результат проверки сохраняется в файл XML, а затем этот результат также передаётся в метод Convert. Вы также можете указать действие для элементов, которые невозможно конвертировать, используя перечисление ConvertErrorAction.

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PDF/A онлайн**

Aspose.PDF for Python представляет вам онлайн бесплатное приложение ["PDF в PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), где вы можете попытаться изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в PDF/A с бесплатным приложением](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

Метод 'document.validate()' проверяет, соответствует ли PDF‑файл стандарту PDF/A-1B (ISO‑стандартизированная версия PDF, предназначенная для долгосрочного архивирования). Результаты проверки сохраняются в файл журнала.

1. Загрузите PDF‑документ, используя 'ap.Document'.
1. Вызовите метод validate с целевым уровнем соответствия (ap.PdfFormat.PDF_A_1B).
1. Результаты валидации записываются в указанный файл журнала.

```python
path_infile = path.join(self.data_dir, infile)
path_logfile = path.join(self.data_dir, "python", outfile)

document = ap.Document(path_infile)
document.validate(path_logfile, ap.PdfFormat.PDF_A_1B)
```

### Конвертировать PDF в PDF/A-1B

Следующий фрагмент кода показывает, как преобразовать PDF‑файлы в формат PDF/A‑1B:

1. Загрузите PDF‑документ, используя 'ap.Document'.
1. Вызовите метод convert со следующими параметрами:
    - Путь к файлу журнала - хранит детали процесса конвертации и проверок соответствия.
    - Целевой формат - 'ap.PdfFormat.PDF_A_1B' (архивный стандарт).
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' — автоматически удаляет элементы, препятствующие соблюдению требований.
1. Сохраните преобразованный файл, соответствующий требованиям PDF/A, в указанный путь вывода.

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

Этот пример демонстрирует, как преобразовать документ PDF в более новые стандартизированные форматы: PDF 2.0 и PDF/A-4.
Оба преобразования помогают обеспечить соответствие современным спецификациям и требованиям архивирования.

1. Загрузите входной документ, используя ap.Document.
1. Выполните первое преобразование в PDF 2.0, вызвав document.convert со следующим:
    - Путь к файлу журнала для деталей конвертации.
    - Целевой формат - 'ap.PdfFormat.V_2_0'.
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления некорректных элементов.
1. Выполните второе преобразование в PDF/A-4, используя тот же метод, обеспечивая соответствие файла архивным стандартам.
1. Сохраните полученный документ в указанном пути вывода.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
path_logfile = path_outfile.replace(".pdf", "_log.xml")

document = ap.Document(path_infile)
document.convert(path_logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)

document.convert(path_logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
document.save(path_outfile)

print(infile + " converted into " + outfile)
```

### Конвертировать PDF в PDF/A-3A с вложенными файлами

Следующий фрагмент кода демонстрирует, как внедрить внешние файлы в PDF, а затем преобразовать PDF в формат PDF/A-3A, который поддерживает вложения и подходит для длительного архивирования с встроенным содержимым.

1. Загрузите входной PDF, используя 'ap.Document'.
1. Создайте объект 'FileSpecification', указывающий на файл для встраивания (например, "aspose-logo.jpg") с описанием.
1. Добавьте спецификацию файла в коллекцию 'embedded_files' PDF.
1. Конвертировать документ в PDF/A-3A с помощью 'document.convert', указав:
    - Путь к файлу журнала.
    - Целевой формат - 'ap.PdfFormat.PDF_A_3A'.
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления некорректных элементов.
1. Сохраните преобразованный PDF в выходной путь.
1. Вывести сообщение подтверждения.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
path_logfile = path_outfile.replace(".pdf", "_log.xml")

document = ap.Document(path_infile)

fileSpecification = ap.FileSpecification(
    self.data_dir + "aspose-logo.jpg", "Large Image file"
)
document.embedded_files.add(fileSpecification)
document.convert(path_logfile, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

### Конвертировать PDF в PDF/A-1B с заменой шрифтов

Эта функция преобразует PDF в формат PDF/A-1B, одновременно обрабатывая отсутствующие шрифты, заменяя их доступными. Это гарантирует, что преобразованный PDF сохраняет визуальную согласованность и соответствует архивным стандартам.

1. Загрузите PDF, используя 'ap.Document'.
1. Преобразуйте PDF в PDF/A-1B, используя 'document.convert', указав:
    - Путь к файлу журнала.
    - Формат назначения - 'ap.PdfFormat.PDF_A_1B'.
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления некорректных элементов.
1. Сохраните преобразованный PDF в выходной путь.
1. Вывести сообщение подтверждения.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
path_logfile = path_outfile.replace(".pdf", "_log.xml")

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

### Конвертировать PDF в PDF/A-1B с автоматическим тегированием

Эта функция конвертирует PDF‑документ в формат PDF/A-1B, при этом автоматически разметает содержимое для доступности и структурной согласованности. Автоматическая разметка улучшает удобство использования документа для программ чтения с экрана и обеспечивает правильную семантическую структуру.

1. Загрузите PDF, используя 'ap.Document'.
1. Создайте 'PdfFormatConversionOptions', указав:
    - Путь к файлу журнала.
    - Формат назначения - 'ap.PdfFormat.PDF_A_1B'.
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления некорректных элементов.
1. Настройте ‘AutoTaggingSettings’:
    - Включить 'enable_auto_tagging = True'.
    - Установите 'heading_recognition_strategy = AUTO' для автоматического обнаружения заголовков.
1. Назначьте параметры автотегирования параметрам конвертации.
1. Конвертируйте PDF, используя 'document.convert(options)'.
1. Сохраните преобразованный PDF в выходной путь.
1. Вывести сообщение подтверждения.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
path_logfile = path_outfile.replace(".pdf", "_log.xml")

document = ap.Document(path_infile)
options = ap.PdfFormatConversionOptions(
    path_logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE
)

auto_tagging_settings = ap.AutoTaggingSettings()
auto_tagging_settings.enable_auto_tagging = True

auto_tagging_settings.heading_recognition_strategy = ap.HeadingRecognitionStrategy.AUTO

options.auto_tagging_settings = auto_tagging_settings
document.convert(options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Преобразовать PDF в PDF/E

Этот фрагмент проверяет, соответствует ли PDF‑документ стандарту PDF/E-1, который является стандартом ISO, адаптированным для инженерных и технических документов. Результаты проверки сохраняются в файл журнала.

1. Загрузите PDF‑документ, используя 'ap.Document'.
1. Вызовите метод validate, указав:
    - Путь к файлу журнала для хранения результатов проверки.
    - Целевой формат - 'ap.PdfFormat.PDF_E_1'.
1. Результаты проверки сохраняются в файле журнала для последующего просмотра.

```python
path_infile = path.join(self.data_dir, infile)
path_logfile = path.join(self.data_dir, "python", outfile)

document = ap.Document(path_infile)
document.validate(path_logfile, ap.PdfFormat.PDF_E_1)
```

Следующий пример демонстрирует, как преобразовать PDF в формат PDF/E-1, который является стандартом ISO, адаптированным для инженерной и технической документации. Этот формат сохраняет точную верстку, графику и метаданные, необходимые для инженерных рабочих процессов.

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте 'PdfFormatConversionOptions', указав:
    - Путь к файлу журнала для отслеживания проблем преобразования.
    - Целевой формат - 'ap.PdfFormat.PDF_E_1'.
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления некорректных элементов.
1. Конвертируйте PDF, используя 'document.convert(options)'.
1. Сохраните преобразованный PDF в указанный путь вывода.
1. Вывести сообщение подтверждения.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
path_logfile = path_outfile.replace(".pdf", "_log.xml")

document = ap.Document(path_infile)
options = ap.PdfFormatConversionOptions(
    path_logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE
)

document.convert(options)

# Save PDF document
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Конвертировать PDF в PDF/X

Следующий фрагмент кода конвертирует документ PDF в формат PDF/X-4, который является ISO‑стандартом, часто используемым в полиграфии и издательской отрасли. PDF/X-4 обеспечивает точность цветов, сохраняет прозрачность и внедряет ICC‑профили для согласованного вывода на разных устройствах.

1. Загрузите исходный PDF, используя 'ap.Document'.
1. Создайте 'PdfFormatConversionOptions', указав:
    - Путь к файлу журнала.
    - Целевой формат - 'ap.PdfFormat.PDF_X_4'.
    - Действие при ошибке - 'ap.ConvertErrorAction.DELETE' для удаления некорректных элементов.
1. Предоставьте **ICC profile file** для управления цветом через 'icc_profile_file_name'.
1. Укажите **OutputIntent** с идентификатором условия (например, "FOGRA39") для требований печати.
1. Конвертировать PDF с помощью 'document.convert()'.
1. Сохраните преобразованный PDF в указанный путь вывода.
1. Вывести сообщение подтверждения.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)
path_logfile = path_outfile.replace(".pdf", "_log.xml")

document = ap.Document(path_infile)
options = ap.PdfFormatConversionOptions(
    path_logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE
)

# Provide the name of the external ICC profile file (optional)
options.icc_profile_file_name = path.join(self.data_dir, "ISOcoated_v2_eci.icc")
# Provide an output condition identifier and other necessary OutputIntent properties (optional)
options.output_intent = ap.OutputIntent("FOGRA39")

document.convert(options)

# Save PDF document
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Связанные преобразования

- [Преобразовать PDF в Word](/pdf/ru/python-net/convert-pdf-to-word/) для рабочих процессов редактируемого контента после проверки стандартов.
- [Конвертировать PDF в HTML](/pdf/ru/python-net/convert-pdf-to-html/) когда ваш целевой вывод предназначен для веб‑страниц, а не для PDF, основанного на стандартах.
