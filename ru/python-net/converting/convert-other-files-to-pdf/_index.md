---
title: Преобразовать другие форматы файлов в PDF с помощью Python
linktitle: Преобразовать другие форматы файлов в PDF
type: docs
weight: 80
url: /ru/python-net/convert-other-files-to-pdf/
lastmod: "2025-09-01"
description: В этой теме показано, как Aspose.PDF позволяет преобразовывать другие форматы файлов, такие как EPUB, MD, PCL, XPS, PS, XML и LaTeX, в PDF‑документ.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Как преобразовать другие форматы файлов в PDF с помощью Python
Abstract: Эта статья предоставляет всестороннее руководство по преобразованию различных форматов файлов в PDF с помощью Python, используя возможности Aspose.PDF for Python via .NET. В документе описаны процессы конвертации нескольких форматов, включая EPUB, Markdown, PCL, Text, XPS, PostScript, XML, XSL-FO и LaTeX/TeX. Каждый раздел содержит конкретные фрагменты кода и инструкции по реализации этих преобразований. Статья подчёркивает полезность функций Aspose.PDF, таких как параметры загрузки, адаптированные к каждому типу файла, чтобы обеспечить точное и эффективное преобразование. Кроме того, она выделяет наличие бесплатных онлайн‑приложений для конвертации, позволяющих пользователям лично ознакомиться с функциональностью. Руководство служит практическим ресурсом для разработчиков, желающих интегрировать возможности конвертации PDF в свои Python‑приложения.
---

Эта статья объясняет, как **преобразовать различные другие типы форматов файлов в PDF с помощью Python**. Она охватывает следующие темы.

## Преобразовать OFD в PDF

OFD обозначает Open Fixed-layout Document (также называемый форматом Open Fixed Document). Это национальный китайский стандарт (GB/T 33190-2016) для электронных документов, представленный как альтернатива PDF.

Шаги по преобразованию OFD в PDF с помощью Python:

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

## Преобразовать LaTeX/TeX в PDF

Формат файлов LaTeX — это текстовый формат с разметкой на основе производного от семейства языков TeX формата LaTeX, а LaTeX является производным форматом системы TeX. LaTeX (ˈleɪtɛk/lay-tek или ла‑тек) — система подготовки документов и язык разметки документов. Он широко используется для создания и публикации научных документов во многих областях, включая математику, физику и информатику. Он также играет ключевую роль в подготовке и публикации книг и статей, содержащих сложные многоязычные материалы, такие как корейский, японский, китайские иероглифы и арабский, включая специальные издания.

LaTeX использует программу типографики TeX для форматирования своего вывода и сам написан на макроязыке TeX.

{{% alert color="success" %}}
**Попробуйте преобразовать LaTeX/TeX в PDF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн‑бесплатное приложение ["LaTex в PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), где вы можете попробовать изучить его функциональность и качество работы.

[![Aspose.PDF Convertion LaTeX/TeX to PDF with Free App](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Шаги по преобразованию TEX в PDF с помощью Python:

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
## Преобразовать OFD в PDF

OFD обозначает Open Fixed-layout Document (иногда называемый форматом Open Fixed Document). Это национальный китайский стандарт (GB/T 33190-2016) для электронных документов, представленный как альтернатива PDF.

Шаги по преобразованию OFD в PDF с помощью Python:

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

## Преобразовать LaTeX/TeX в PDF

Формат файлов LaTeX — это текстовый формат с разметкой на основе производного от семейства языков TeX формата LaTeX, а LaTeX является производным форматом системы TeX. LaTeX (ˈleɪtɛk/lay-tek или ла‑тек) — система подготовки документов и язык разметки документов. Он широко используется для создания и публикации научных документов во многих областях, включая математику, физику и информатику. Он также играет заметную роль в подготовке и публикации книг и статей, содержащих сложные многоязычные материалы, такие как санскрит и арабский, включая критические издания. LaTeX использует программу типографики TeX для форматирования своего вывода, и сам написан на макроязыке TeX.

{{% alert color="success" %}}
**Попробуйте преобразовать LaTeX/TeX в PDF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн‑бесплатное приложение ["LaTex в PDF"](https://products.aspose.app/pdf/conversion/tex-to-pdf), где вы можете попробовать изучить его функциональность и качество работы.

[![Aspose.PDF Convertion LaTeX/TeX to PDF with Free App](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

Шаги по преобразованию TEX в PDF с помощью Python:

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

## Преобразовать EPUB в PDF

**Aspose.PDF for Python via .NET** позволяет вам просто конвертировать файлы EPUB в формат PDF.

EPUB (сокращение от electronic publication) — это бесплатный и открытый стандарт электронных книг от International Digital Publishing Forum (IDPF). Файлы имеют расширение .epub. EPUB разработан для контента с изменяемой разметкой, что значит, что читалка EPUB может оптимизировать текст под конкретное устройство отображения.

<abbr title="electronic publication">EPUB</abbr> также поддерживает контент с фиксированной разметкой. Формат предназначен как единый формат, который издатели и конвертеры могут использовать внутри компании, а также для распространения и продажи. Он заменил стандарт Open eBook. Версия EPUB 3 также одобрена Book Industry Study Group (BISG), ведущей ассоциацией книжной отрасли для стандартизированных лучших практик, исследований, информации и мероприятий, связанных с упаковкой контента.

{{% alert color="success" %}}
**Попробуйте конвертировать EPUB в PDF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн бесплатное приложение ["EPUB to PDF"](https://products.aspose.app/pdf/conversion/epub-to-pdf), где вы можете попробовать исследовать функциональность и качество его работы.

[![Конвертация Aspose.PDF EPUB в PDF с бесплатным приложением](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

Шаги Конвертации EPUB в PDF в Python:

1. Загрузите EPUB документ с помощью EpubLoadOptions().
1. Конвертируйте EPUB в PDF.
1. Выведите подтверждение.

Далее приведённый фрагмент кода показывает, как конвертировать файлы EPUB в формат PDF с помощью Python.

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

**Эта функция поддерживается версиями 19.6 и выше.**

{{% alert color="success" %}}
**Попробуйте конвертировать Markdown в PDF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн бесплатное приложение ["Markdown to PDF"](https://products.aspose.app/pdf/conversion/md-to-pdf), где вы можете попробовать исследовать функциональность и качество его работы.

[![Конвертация Aspose.PDF Markdown в PDF с бесплатным приложением](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

Этот фрагмент кода от Aspose.PDF for Python via .NET помогает конвертировать файлы Markdown в PDF, позволяя лучше делиться документами, сохранять форматирование и обеспечивать совместимость при печати.

Следующий фрагмент кода показывает, как использовать эту возможность с библиотекой Aspose.PDF:

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

<abbr title="Printer Command Language">PCL</abbr> (Printer Command Language) — это язык принтера Hewlett-Packard, разработанный для доступа к стандартным функциям принтера. Уровни PCL от 1 до 5e/5c являются языками команд, использующими управляющие последовательности, которые обрабатываются и интерпретируются в порядке получения. На уровне потребителя потоки данных PCL генерируются драйвером печати. Вывод PCL также может быть легко сгенерирован пользовательскими приложениями.

{{% alert color="success" %}}
**Попробуйте конвертировать PCL в PDF онлайн**

Aspose.PDF for for .NET представляет вам онлайн бесплатное приложение ["PCL to PDF"](https://products.aspose.app/pdf/conversion/pcl-to-pdf), где вы можете попробовать исследовать функциональность и качество его работы.

[![Конвертация Aspose.PDF PCL в PDF с бесплатным приложением](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

Чтобы разрешить конвертацию из PCL в PDF, Aspose.PDF имеет класс [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions), который используется для инициализации объекта LoadOptions. Позже этот объект передаётся как аргумент при инициализации объекта Document и помогает движку рендеринга PDF определить входной формат исходного документа.

Следующий фрагмент кода показывает процесс конвертации файла PCL в формат PDF.

Шаги Конвертации PCL в PDF в Python:

1. Загрузите параметры для PCL с помощью PclLoadOptions().
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

## Конвертировать Предформатированный Текст в PDF

**Aspose.PDF for Python via .NET** поддерживает функцию конвертации обычного текста и предформатированных текстовых файлов в формат PDF.

Конвертация текста в PDF означает добавление фрагментов текста на страницу PDF. Что касается текстовых файлов, мы имеем дело с 2 типами текста: предформатированный (например, 25 строк по 80 символов в строке) и неформатированный (обычный текст). В зависимости от наших потребностей, мы можем контролировать это добавление сами или доверить его алгоритмам библиотеки.

{{% alert color="success" %}}
**Попробуйте конвертировать ТЕКСТ в PDF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн бесплатное приложение ["Text to PDF"](https://products.aspose.app/pdf/conversion/txt-to-pdf), где вы можете попробовать исследовать функциональность и качество его работы.

[![Конвертация Aspose.PDF TEXT в PDF с бесплатным приложением](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

Шаги Конвертации ТЕКСТА в PDF в Python:

1. Читайте входной текстовый файл построчно.
1. Настройте моноширинный шрифт (Courier New) для согласованного выравнивания текста.
1. Создайте новый PDF документ и добавьте первую страницу с пользовательскими полями и настройками шрифта.
1. Итерация по строкам текстового файла. Чтобы имитировать пишущую машинку, мы используем шрифт 'monospace_font' размером 12.
1. Ограничьте создание страниц до 4 страниц.
1. Сохраните финальный PDF по указанному пути.

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

Этот пример демонстрирует, как преобразовать файл PostScript в PDF‑документ с использованием Aspose.PDF for Python via .NET.

1. Создайте экземпляр 'PsLoadOptions' для правильной интерпретации файла PS.
1. Загрузите файл 'PostScript' в объект Document, используя параметры загрузки.
1. Сохраните документ в формате PDF в указанный путь вывода.

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

**Aspose.PDF for Python via .NET** поддерживает функцию конвертации файлов <abbr title="XML Paper Specification">XPS</abbr> в формат PDF. Ознакомьтесь с этой статьей, чтобы решить свои задачи.

Тип файла XPS в первую очередь связан со спецификацией XML Paper Specification компании Microsoft. Спецификация XML Paper Specification (XPS), ранее известная под кодовым названием Metro и включающая маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

Следующий фрагмент кода показывает процесс преобразования файла XPS в формат PDF с помощью Python.

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

Aspose.PDF for Python via .NET представляет вам онлайн бесплатное приложение ["XPS в PDF"](https://products.aspose.app/pdf/conversion/xps-to-pdf/), где вы можете попробовать исследовать его функциональность и качество работы.

[![Aspose.PDF Конвертация XPS в PDF с бесплатным приложением](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
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

## Преобразовать XML с XSLT в PDF

Этот пример демонстрирует, как преобразовать XML‑файл в PDF, сначала преобразовав его в HTML с помощью шаблона XSLT, а затем загрузив HTML в Aspose.PDF.

1. Создайте экземпляр 'HtmlLoadOptions' для настройки конвертации HTML в PDF.
1. Загрузите преобразованный HTML‑файл в объект Document библиотеки Aspose.PDF.
1. Сохраните документ как PDF по указанному пути вывода.
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
        with open(html_file, 'w', encoding='utf-8') as f:
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

