---
title: Конвертировать другие форматы файлов в PDF в Python
linktitle: Конвертировать другие форматы файлов в PDF
type: docs
weight: 80
url: /python-net/convert-other-files-to-pdf/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать файлы EPUB, Markdown, PCL, XPS, PostScript, XML и LaTeX в PDF на Python с помощью Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true 
AlternativeHeadline: Как конвертировать другие форматы файлов в PDF на Python
Abstract: В этой статье представлено всестороннее руководство по конвертации различных форматов файлов в PDF с использованием Python, используя возможности Aspose.PDF for Python via .NET. В документе описаны процессы конвертации для нескольких форматов, включая EPUB, Markdown, PCL, Text, XPS, PostScript, XML, XSL-FO и LaTeX/TeX. Каждый раздел предоставляет конкретные фрагменты кода и инструкции по реализации этих конвертаций. В статье подчеркивается полезность функций Aspose.PDF, таких как параметры загрузки, адаптированные под каждый тип файла, чтобы обеспечить точную и эффективную конвертацию. Кроме того, отмечается наличие онлайн‑приложений для конвертации, позволяющих пользователям самостоятельно опробовать функциональность. Это руководство служит практическим ресурсом для разработчиков, желающих интегрировать возможности конвертации в PDF в свои Python‑приложения.
---

В этой статье объясняется, как **конвертировать различные типы файлов в PDF с использованием Python**. Она охватывает следующие темы.

## Преобразовать OFD в PDF

OFD обозначает Open Fixed-layout Document (также называемый форматом Open Fixed Document). Это китайский национальный стандарт (GB/T 33190-2016) для электронных документов, представленный в качестве альтернативы PDF.

Шаги преобразования OFD в PDF на Python:

1. Настройте параметры загрузки OFD, используя OfdLoadOptions().
1. Загрузите документ OFD.
1. Сохраните как PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_OFD_to_PDF(infile, outfile):
    load_options = ap.OfdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Конвертировать LaTeX/TeX в PDF

Формат файла LaTeX — это текстовый формат файла с разметкой в производной LaTeX из семейства языков TeX, а LaTeX является производным форматом системы TeX. LaTeX (ˈleɪtæk/lay-tek или lah-tek) — это система подготовки документов и язык разметки документов. Он широко используется для коммуникации и публикации научных документов во многих областях, включая математику, физику и информатику. Он также играет ключевую роль в подготовке и публикации книг и статей, содержащих сложные многоязычные материалы, такие как корейский, японский, китайские иероглифы и арабский, включая специальные издания.

LaTeX использует программу набора TeX для форматирования своего вывода и сам написан на макроязыке TeX.

{{% alert color="success" %}}
**Попробуйте преобразовать LaTeX/TeX в PDF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн‑приложение ["LaTex в PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), где вы можете попробовать исследовать, как работает функциональность и качество.

[![Конвертация LaTeX/TeX в PDF с приложением Aspose.PDF](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Шаги преобразования TEX в PDF на Python:

1. Настройте параметры загрузки LaTeX, используя LatexLoadOptions().
1. Загрузите документ LaTeX.
1. Сохраните как PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TEX_to_PDF(infile, outfile):
    load_options = ap.LatexLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Конвертировать EPUB в PDF

**Aspose.PDF for Python via .NET** позволяет вам просто конвертировать файлы EPUB в формат PDF.

EPUB (сокращение от electronic publication) — свободный и открытый стандарт электронных книг от International Digital Publishing Forum (IDPF). Файлы имеют расширение .epub. EPUB предназначен для перестраиваемого контента, что означает, что читатель EPUB может оптимизировать текст под конкретное устройство отображения.

<abbr title="electronic publication">EPUB</abbr> также поддерживает контент фиксированного макета. Формат предназначен как единый формат, который издатели и компании по конвертации могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook. Версия EPUB 3 также одобрена Book Industry Study Group (BISG), ведущей ассоциацией книжной индустрии, занимающейся стандартизированными лучшими практиками, исследованиями, информацией и мероприятиями по упаковке контента.

{{% alert color="success" %}}
**Попробуйте конвертировать EPUB в PDF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн‑приложение ["EPUB в PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), где вы можете попробовать исследовать, как работает функциональность и качество.

[![Aspose.PDF Конвертация EPUB в PDF с приложением](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

Шаги конвертации EPUB в PDF на Python:

1. Загрузите документ EPUB с помощью EpubLoadOptions().
1. Конвертируйте EPUB в PDF.
1. Подтверждение печати.

Следующий фрагмент кода показывает, как конвертировать файлы EPUB в формат PDF с помощью Python.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_EPUB_to_PDF(infile, outfile):
    load_options = ap.EpubLoadOptions()
    document = ap.Document(infile, load_options)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Преобразовать Markdown в PDF

**Эта функция поддерживается версией 19.6 или более новой.**

{{% alert color="success" %}}
**Попробуйте конвертировать Markdown в PDF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн‑приложение ["Markdown в PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), где вы можете попробовать исследовать, как работает функциональность и качество.

[![Aspose.PDF конвертация Markdown в PDF с приложением](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Этот фрагмент кода от Aspose.PDF for Python via .NET помогает конвертировать файлы Markdown в PDF, обеспечивая более удобный обмен документами, сохранение форматирования и совместимость при печати.o

Следующий фрагмент кода показывает, как использовать эту функциональность с библиотекой Aspose.PDF:

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_MD_to_PDF(infile, outfile):
    load_options = ap.MdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## Преобразовать PCL в PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) — язык печати Hewlett-Packard, разработанный для доступа к стандартным функциям принтера. Уровни PCL от 1 до 5e/5c являются языками, основанными на командах, использующими управляющие последовательности, которые обрабатываются и интерпретируются в порядке их получения. На уровне конечного пользователя потоки данных PCL генерируются драйвером печати. Вывод PCL также может быть легко сгенерирован пользовательскими приложениями.

{{% alert color="success" %}}
**Попробуйте конвертировать PCL в PDF онлайн**

Aspose.PDF for for .NET представляет вам онлайн приложение ["PCL в PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), где вы можете попробовать исследовать, как работает функциональность и качество.

[![Aspose.PDF Преобразование PCL в PDF с помощью приложения](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

Чтобы обеспечить конвертацию из PCL в PDF, Aspose.PDF имеет класс [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) который используется для инициализации объекта LoadOptions. Позднее этот объект передаётся в качестве аргумента при инициализации объекта Document, и он помогает механизму рендеринга PDF определить входной формат исходного документа.

Следующий фрагмент кода демонстрирует процесс конвертации файла PCL в формат PDF.

Шаги конвертации PCL в PDF на Python:

1. Параметры загрузки для PCL с помощью PclLoadOptions().
1. Загрузите документ.
1. Сохраните как PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PCL_to_PDF(infile, outfile):
    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Конвертировать предварительно отформатированный текст в PDF

**Aspose.PDF for Python via .NET** поддерживает функцию конвертации обычного текста и предварительно отформатированного текстового файла в формат PDF.

Преобразование текста в PDF означает добавление текстовых фрагментов на страницу PDF. Что касается текстовых файлов, мы имеем дело с двумя типами текста: предварительно отформатированным (например, 25 строк по 80 символов в каждой) и неотформатированным (обычный текст). В зависимости от наших потребностей мы можем контролировать это добавление самостоятельно или доверить его алгоритмам библиотеки.

{{% alert color="success" %}}
**Попробуйте конвертировать TEXT в PDF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн‑приложение ["Текст в PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), где вы можете попробовать исследовать, как работает функциональность и качество.

[![Aspose.PDF Конвертация TEXT в PDF с приложением](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

Шаги конвертации ТЕКСТА в PDF в Python:

1. Читать входной текстовый файл построчно.
1. Настройте моноширинный шрифт (Courier New) для согласованного выравнивания текста.
1. Создайте новый PDF Document и добавьте первую страницу с пользовательскими полями и настройками шрифта.
1. Итерировать по строкам текстового файла Чтобы имитировать печатающую машинку, мы используем шрифт 'monospace_font' размером 12.
1. Ограничить создание страниц до 4 страниц.
1. Сохраните окончательный PDF в указанный путь.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TXT_to_PDF(infile, outfile):
    with open(infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Конвертировать PostScript в PDF

В этом примере показано, как преобразовать файл PostScript в PDF‑документ с использованием Aspose.PDF for Python via .NET.

1. Создайте экземпляр 'PsLoadOptions' для корректного интерпретирования PS‑файла.
1. Загрузите файл 'PostScript' в объект Document, используя параметры загрузки.
1. Сохраните документ в формате PDF в желаемый путь вывода.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PS_to_PDF(infile, outfile):
    load_options = ap.PsLoadOptions()

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Конвертировать XPS в PDF

**Aspose.PDF for Python via .NET** поддерживает функцию конвертирования <abbr title="XML Paper Specification">XPS</abbr> файлы в формат PDF. Проверьте эту статью, чтобы решить ваши задачи.

Тип файла XPS в первую очередь связан со спецификацией XML Paper Specification, разработанной корпорацией Microsoft. Спецификация XML Paper Specification (XPS), ранее имевшая кодовое название Metro и включающая в себя маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

Следующий фрагмент кода показывает процесс преобразования файла XPS в формат PDF с использованием Python.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XPS_to_PDF(infile, outfile):
    load_options = ap.XpsLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать формат XPS в PDF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн‑приложение ["XPS в PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), где вы можете попробовать исследовать, как работает функциональность и качество.

[![Конвертация XPS в PDF с приложением Aspose.PDF](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Преобразовать XSL-FO в PDF

Следующий фрагмент кода можно использовать для преобразования XSLFO в формат PDF с помощью Aspose.PDF for Python via .NET:

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## Преобразовать XML с помощью XSLT в PDF

Этот пример демонстрирует, как преобразовать файл XML в PDF, сначала преобразовав его в HTML с помощью шаблона XSLT, а затем загрузив HTML в Aspose.PDF.

1. Создайте экземпляр 'HtmlLoadOptions' для настройки конвертации HTML в PDF.
1. Загрузите преобразованный HTML‑файл в объект Aspose.PDF Document.
1. Сохраните документ в формате PDF по указанному пути вывода.
1. Удалите временный файл HTML после успешного преобразования.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## Связанные преобразования

- [Преобразовать HTML в PDF](/pdf/ru/python-net/convert-html-to-pdf/) для сценариев преобразования HTML и MHTML.
- [Конвертировать форматы изображений в PDF](/pdf/ru/python-net/convert-images-format-to-pdf/) когда ваши входные данные — PNG, JPEG, TIFF, SVG или другие изображения.
- [Конвертировать PDF в другие форматы](/pdf/ru/python-net/convert-pdf-to-other-files/) если вам также нужны обратные конверсии, такие как PDF в EPUB, Markdown или текст.
