---
title: Преобразовать другие форматы файлов в PDF на Python
linktitle: Преобразовать другие форматы файлов в PDF
type: docs
weight: 80
url: /ru/python-net/convert-other-files-to-pdf/
lastmod: "2026-04-14"
description: Узнайте, как преобразовать файлы EPUB, Markdown, PCL, XPS, PostScript, XML и LaTeX в PDF на Python с помощью Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true 
AlternativeHeadline: Как конвертировать другие форматы файлов в PDF на Python
Abstract: В этой статье представлено полное руководство по конвертации различных форматов файлов в PDF с использованием Python, используя возможности Aspose.PDF for Python via .NET. Документ описывает процессы конвертации для нескольких форматов, включая EPUB, Markdown, PCL, Text, XPS, PostScript, XML, XSL-FO и LaTeX/TeX. Каждый раздел предоставляет конкретные фрагменты кода и инструкции по реализации этих конвертаций. Статья подчеркивает полезность функций Aspose.PDF, таких как параметры загрузки, адаптированные под каждый тип файла, чтобы обеспечить точную и эффективную конвертацию. Кроме того, она выделяет наличие онлайн‑приложений для конвертации, позволяющих пользователям самостоятельно познакомиться с функциональностью. Руководство служит практическим ресурсом для разработчиков, желающих интегрировать возможности конвертации PDF в свои Python‑приложения.
---

В этой статье объясняется, как **конвертировать различные типы файлов в PDF с помощью Python**. Она охватывает следующие темы.

## Конвертировать OFD в PDF

OFD расшифровывается как Open Fixed-layout Document (также называется форматом Open Fixed Document). Это национальный китайский стандарт (GB/T 33190-2016) для электронных документов, представленный в качестве альтернативы PDF.

Шаги конвертации OFD в PDF на Python:

1. Настройте параметры загрузки OFD, используя OfdLoadOptions().
1. Загрузите документ OFD.
1. Сохраните как PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.OfdLoadOptions()
document = ap.Document(path_infile, load_options)
document.save(path_outfile)

print(infile + " converted into " + outfile)
```

## Конвертировать LaTeX/TeX в PDF

Формат файла LaTeX — это текстовый файловый формат с разметкой в производном от семейства языков TeX варианте LaTeX, и LaTeX является производным форматом системы TeX. LaTeX (ˈleɪtɛk/lay-tek или lah-tek) — это система подготовки документов и язык разметки документов. Он широко используется для обмена и публикации научных документов во многих областях, включая математику, физику и информатику. Он также играет ключевую роль в подготовке и публикации книг и статей, содержащих сложный многоязычный материал, такой как корейский, японский, китайские иероглифы и арабский, включая специальные издания.

LaTeX использует программу наборного оформления TeX для форматирования своего вывода и сам написан на макроязыке TeX.

{{% alert color="success" %}}
**Попробуйте конвертировать LaTeX/TeX в PDF онлайн**

Aspose.PDF for Python via .NET предлагает вам онлайн-приложение ["LaTex в PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), где вы можете попытаться исследовать функциональность и качество, как это работает.

[![Aspose.PDF Конвертация LaTeX/TeX в PDF с приложением](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Шаги преобразования TEX в PDF в Python:

1. Настройте параметры загрузки LaTeX, используя LatexLoadOptions().
1. Загрузите документ LaTeX.
1. Сохраните как PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.LatexLoadOptions()
document = ap.Document(path_infile, load_options)
document.save(path_outfile)

print(infile + " converted into " + outfile)
```

## Конвертировать OFD в PDF

OFD расшифровывается как Open Fixed-layout Document (иногда называется форматом Open Fixed Document). Это китайский национальный стандарт (GB/T 33190-2016) для электронных документов, введённый как альтернатива PDF.

Шаги конвертации OFD в PDF на Python:

1. Настройте параметры загрузки OFD, используя OfdLoadOptions().
1. Загрузите документ OFD.
1. Сохраните как PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.OfdLoadOptions()
document = ap.Document(path_infile, load_options)
document.save(path_outfile)

print(infile + " converted into " + outfile)
```

## Конвертировать LaTeX/TeX в PDF

Формат файла LaTeX — это текстовый формат файла с разметкой в производном от TeX семействе языков LaTeX, и LaTeX является производным форматом системы TeX. LaTeX (ˈleɪtɪk/lay-tek или lah-tek) — система подготовки документов и язык разметки документов. Он широко используется для общения и публикации научных документов во многих областях, включая математику, физику и информатику. Он также играет важную роль в подготовке и публикации книг и статей, содержащих сложные многоязычные материалы, такие как санскрит и арабский, включая критические издания. LaTeX использует программу верстки TeX для форматирования своего вывода и сам написан на макроязыке TeX.

{{% alert color="success" %}}
**Попробуйте конвертировать LaTeX/TeX в PDF онлайн**

Aspose.PDF for Python via .NET предлагает вам онлайн-приложение ["LaTex в PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), где вы можете попытаться исследовать функциональность и качество, как это работает.

[![Aspose.PDF Конвертация LaTeX/TeX в PDF с онлайн-приложением](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Шаги преобразования TEX в PDF в Python:

1. Настройте параметры загрузки LaTeX, используя LatexLoadOptions().
1. Загрузите документ LaTeX.
1. Сохраните как PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.LatexLoadOptions()
document = ap.Document(path_infile, load_options)
document.save(path_outfile)

print(infile + " converted into " + outfile)
```

## Конвертировать EPUB в PDF

**Aspose.PDF for Python via .NET** позволяет вам просто конвертировать файлы EPUB в формат PDF.

EPUB (сокращение от electronic publication) — свободный и открытый стандарт электронной книги от Международного форума цифровой публикации (IDPF). Файлы имеют расширение .epub. EPUB предназначен для контента, который может перестраиваться, что означает, что читалка EPUB может оптимизировать текст под конкретное устройство отображения.

<abbr title="electronic publication">EPUB</abbr> Также поддерживает контент фиксированного макета. Этот формат предназначен как единый формат, который издатели и конверсионные компании могут использовать внутри компании, а также для распространения и продажи. Он заменяет стандарт Open eBook. Версия EPUB 3 также одобрена Book Industry Study Group (BISG), ведущей ассоциацией книжной индустрии, занимающейся стандартизированными лучшими практиками, исследованиями, информацией и мероприятиями по упаковке контента.

{{% alert color="success" %}}
**Попробуйте конвертировать EPUB в PDF онлайн**

Aspose.PDF for Python via .NET предлагает вам онлайн-приложение ["EPUB в PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), где вы можете попытаться исследовать функциональность и качество, как это работает.

[![Aspose.PDF Конвертация EPUB в PDF с онлайн-приложением](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

Шаги преобразования EPUB в PDF на Python:

1. Загрузите EPUB документ с помощью EpubLoadOptions().
1. Конвертируйте EPUB в PDF.
1. Подтверждение печати.

Следующий фрагмент кода покажет вам, как конвертировать файлы EPUB в формат PDF с помощью Python.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.EpubLoadOptions()
document = ap.Document(path_infile, load_options)

document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Конвертировать Markdown в PDF

**Эта возможность поддерживается версии 19.6 и выше.**

{{% alert color="success" %}}
**Попробуйте конвертировать Markdown в PDF онлайн**

Aspose.PDF for Python via .NET предлагает вам онлайн-приложение ["Markdown в PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), где вы можете попытаться исследовать функциональность и качество, как это работает.

[![Aspose.PDF Конвертация Markdown в PDF с онлайн-приложением](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Этот фрагмент кода от Aspose.PDF for Python via .NET помогает преобразовать файлы Markdown в PDF, обеспечивая более удобный обмен документами, сохранение форматирования и совместимость при печати.o

Следующий фрагмент кода демонстрирует, как использовать эту функциональность с библиотекой Aspose.PDF:

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.MdLoadOptions()
document = ap.Document(path_infile, load_options)
document.save(path_outfile)
print(infile + " converted into " + outfile)
```

## Конвертировать PCL в PDF

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) — язык принтеров Hewlett-Packard, разработанный для доступа к стандартным функциям принтера. Уровни PCL 1‑5e/5c представляют собой основанные на командах языки, использующие управляющие последовательности, которые обрабатываются и интерпретируются в порядке их получения. На уровне потребителя потоки данных PCL генерируются драйвером печати. Вывод PCL также может быть легко сгенерирован пользовательскими приложениями.

{{% alert color="success" %}}
**Попробуйте преобразовать PCL в PDF онлайн**

Aspose.PDF for for .NET представляет вам онлайн-приложение ["PCL в PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), где вы можете попытаться исследовать функциональность и качество, как это работает.

[![Aspose.PDF Конвертация PCL в PDF с онлайн-приложением](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

Чтобы позволить преобразование из PCL в PDF, Aspose.PDF имеет класс [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) который используется для инициализации объекта LoadOptions. Позже этот объект передаётся в качестве аргумента при инициализации объекта Document и помогает движку рендеринга PDF определить входной формат исходного документа.

Следующий фрагмент кода демонстрирует процесс преобразования файла PCL в формат PDF.

Шаги преобразования PCL в PDF на Python:

1. Параметры загрузки для PCL с помощью PclLoadOptions().
1. Загрузите документ.
1. Сохраните как PDF.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.PclLoadOptions()
load_options.supress_errors = True

document = ap.Document(path_infile, load_options)
document.save(path_outfile)

print(infile + " converted into " + outfile)
```

## Конвертировать предварительно отформатированный текст в PDF

**Aspose.PDF for Python via .NET** поддерживает функцию конвертации простого текста и предварительно отформатированного текстового файла в формат PDF.

Преобразование текста в PDF означает добавление текстовых фрагментов на страницу PDF. Что касается текстовых файлов, мы имеем дело с 2 типами текста: предформатированный (например, 25 строк по 80 символов в строке) и неформатированный текст (plain text). В зависимости от наших потребностей мы можем контролировать это добавление самостоятельно или доверить его алгоритмам библиотеки.

{{% alert color="success" %}}
**Попробуйте конвертировать TEXT в PDF онлайн**

Aspose.PDF for Python via .NET предлагает вам онлайн-приложение ["Текст в PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), где вы можете попытаться исследовать функциональность и качество, как это работает.

[![Конвертация TEXT в PDF с онлайн-приложением Aspose.PDF](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

Шаги преобразования TEXT в PDF на Python:

1. Читайте входной текстовый файл построчно.
1. Настройте моноширинный шрифт (Courier New) для согласованного выравнивания текста.
1. Создайте новый PDF Document и добавьте первую страницу с пользовательскими отступами и настройками шрифта.
1. Итерируйте строки текстового файла Чтобы имитировать пишущую машинку, мы используем шрифт 'monospace_font' размером 12.
1. Ограничьте создание страниц до 4 страниц.
1. Сохраните итоговый PDF по указанному пути.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

with open(path_infile, "r") as file:
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

document.save(path_outfile)

print(infile + " converted into " + outfile)
```

## Преобразовать PostScript в PDF

Этот пример демонстрирует, как преобразовать файл PostScript в документ PDF с использованием Aspose.PDF for Python via .NET.

1. Создайте экземпляр 'PsLoadOptions', чтобы корректно интерпретировать файл PS.
1. Загрузите файл 'PostScript' в объект Document, используя параметры загрузки.
1. Сохраните документ в формате PDF в желаемый путь вывода.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.PsLoadOptions()

document = ap.Document(path_infile, load_options)
document.save(path_outfile)

print(infile + " converted into " + outfile)
```

## Преобразовать XPS в PDF

**Aspose.PDF for Python via .NET** поддерживает функцию конвертации <abbr title="XML Paper Specification">XPS</abbr> файлы в формат PDF. Ознакомьтесь с этой статьей, чтобы решить ваши задачи.

Тип файла XPS в первую очередь связан со спецификацией XML Paper Specification компании Microsoft Corporation. Спецификация XML Paper Specification (XPS), ранее имевшая кодовое название Metro и включающая маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в её операционную систему Windows.

Следующий фрагмент кода показывает процесс конвертации файла XPS в формат PDF с помощью Python.

```python
from os import path
import aspose.pdf as ap

path_infile = path.join(self.data_dir, infile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.XpsLoadOptions()
document = ap.Document(path_infile, load_options)
document.save(path_outfile)

print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать формат XPS в PDF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн-приложение ["XPS в PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), где вы можете попытаться исследовать функциональность и качество, как это работает.

[![Конверсия XPS в PDF с онлайн-приложением Aspose.PDF](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## Преобразовать XSL-FO в PDF

Следующий фрагмент кода можно использовать для преобразования XSLFO в формат PDF с помощью Aspose.PDF for Python via .NET:

```python
from os import path
import aspose.pdf as ap

path_xsltfile = path.join(self.data_dir, xsltfile)
path_xmlfile = path.join(self.data_dir, xmlfile)
path_outfile = path.join(self.data_dir, "python", outfile)

load_options = ap.XslFoLoadOptions(path_xsltfile)
load_options.parsing_errors_handling_type = (
    ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.ThrowExceptionImmediately
)
document = ap.Document(path_xmlfile, load_options)
document.save(path_outfile)

print(xmlfile + " converted into " + outfile)
```

## Преобразовать XML с помощью XSLT в PDF

В этом примере демонстрируется, как преобразовать файл XML в PDF, сначала преобразовав его в HTML с помощью шаблона XSLT, а затем загрузив HTML в Aspose.PDF.

1. Создайте экземпляр 'HtmlLoadOptions' для настройки преобразования HTML в PDF.
1. Загрузите преобразованный HTML‑файл в объект Aspose.PDF Document.
1. Сохраните документ в формате PDF по указанному пути вывода.
1. Удалите временный HTML‑файл после успешного преобразования.

```python
from os import path
import aspose.pdf as ap


def transform_xml_to_html(xml_file, xslt_file, html_file):
    from lxml import etree

    """
    Transform XML to HTML using XSLT and return as a stream
    """
    # Parse XML document
    xml_doc = etree.parse(xml_file)

    # Parse XSLT stylesheet
    xslt_doc = etree.parse(xslt_file)
    transform = etree.XSLT(xslt_doc)

    # Apply transformation
    result = transform(xml_doc)

    # Save result to HTML file
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(str(result))


def convert_XML_to_PDF(template, infile, outfile):
    path_infile = path.join(data_dir, infile)
    path_outfile = path.join(data_dir, "python", outfile)
    path_template = path.join(data_dir, template)
    path_temp_file = path.join(data_dir, "temp.html")

    load_options = ap.HtmlLoadOptions()
    transform_xml_to_html(path_infile, path_template, path_temp_file)

    document = ap.Document(path_temp_file, load_options)
    document.save(path_outfile)

    if path.exists(path_temp_file):
        os.remove(path_temp_file)

    print(infile + " converted into " + outfile)
```

## Связанные преобразования

- [Конвертировать HTML в PDF](/pdf/ru/python-net/convert-html-to-pdf/) для сценариев конвертации HTML и MHTML.
- [Конвертировать форматы изображений в PDF](/pdf/ru/python-net/convert-images-format-to-pdf/) когда ваши входные данные — PNG, JPEG, TIFF, SVG или другие изображения.
- [Конвертировать PDF в другие форматы](/pdf/ru/python-net/convert-pdf-to-other-files/) если вам также нужны обратные конверсии, такие как PDF в EPUB, Markdown или текст.
