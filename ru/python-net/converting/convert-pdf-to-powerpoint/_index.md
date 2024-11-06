---
title: Преобразование PDF в PowerPoint на Python
linktitle: Преобразование PDF в PowerPoint
type: docs
weight: 30
url: ru/python-net/convert-pdf-to-powerpoint/
description: Aspose.PDF позволяет преобразовать PDF в формат PPT (PowerPoint) с использованием Python. Один из способов — преобразование PDF в PPTX с изображениями слайдов.
lastmod: "2022-12-23"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Обзор

Возможно ли преобразовать PDF-файл в PowerPoint? Да, вы можете! И это просто!
Эта статья объясняет, как **преобразовать PDF в PowerPoint с использованием Python**. Она охватывает следующие темы.

_Формат_: **PPTX**
- [Python PDF в PPTX](#python-pdf-to-pptx)
- [Python Преобразование PDF в PPTX](#python-pdf-to-pptx)
- [Python Как преобразовать PDF-файл в PPTX](#python-pdf-to-pptx)

_Формат_: **PowerPoint**
- [Python PDF в PowerPoint](#python-pdf-to-powerpoint)
- [Python Преобразование PDF в PowerPoint](#python-pdf-to-powerpoint)
- [Python Как преобразовать PDF-файл в PowerPoint](#python-pdf-to-powerpoint)


## Преобразование PDF в PowerPoint и PPTX на Python

**Aspose.PDF for Python via .NET** позволяет отслеживать процесс преобразования PDF в PPTX.

У нас есть API под названием Aspose.Slides, который предлагает возможность создавать и изменять презентации PPT/PPTX. Этот API также предоставляет возможность конвертировать файлы PPT/PPTX в формат PDF. Во время этого преобразования отдельные страницы PDF файла конвертируются в отдельные слайды в файле PPTX.

Во время преобразования PDF в <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> текст отображается как текст, который вы можете выбрать/обновить. Пожалуйста, обратите внимание, что для конвертации PDF файлов в формат PPTX, Aspose.PDF предоставляет класс под названием [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Объект класса PptxSaveOptions передается в качестве второго аргумента в метод [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods). Следующий фрагмент кода демонстрирует процесс преобразования PDF файлов в формат PPTX.

## Простое преобразование PDF в PowerPoint с использованием Python и Aspose.PDF для Python

Для конвертации PDF в PPTX, Aspose.PDF для Python советует использовать следующие шаги кода.

<a name="csharp-pdf-to-powerpoint"><strong>Шаги: Конвертация PDF в PowerPoint на Python</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Шаги: Конвертация PDF в PPTX на Python</strong></a>

1. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
2. Создайте экземпляр класса [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/)
3. Используйте метод **Save** объекта **Document** для сохранения PDF как PPTX

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx.pptx"
    # Открыть PDF документ
    document = ap.Document(input_pdf)
    # Создать экземпляр PptxSaveOptions
    save_option = ap.PptxSaveOptions()
    # Сохранить файл в формате MS PowerPoint
    document.save(output_pdf, save_option)
```

## Конвертация PDF в PPTX с слайдами как изображения


{{% alert color="success" %}}
 **Попробуйте конвертировать PDF в PowerPoint онлайн**

Aspose.PDF для Python представляет вам бесплатное онлайн-приложение ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в PPTX с бесплатным приложением](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Если вам нужно конвертировать PDF в PPTX в виде изображений вместо выделяемого текста, Aspose.PDF предоставляет такую возможность через класс [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Для этого установите свойство [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) класса [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) в 'true', как показано в следующем примере кода.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_pptx_with_slides_as_images.pptx"
    # Открыть PDF-документ
    document = ap.Document(input_pdf)
    # Создать экземпляр PptxSaveOptions
    save_option = ap.PptxSaveOptions()
    save_option.slides_as_images = True
    # Сохранить файл в формате MS PowerPoint
    document.save(output_pdf, save_option)
```


## См. также

Эта статья также охватывает следующие темы. Код такой же, как выше.

_Формат_: **PowerPoint**
- [Python PDF в PowerPoint Код](#python-pdf-to-powerpoint)
- [Python PDF в PowerPoint API](#python-pdf-to-powerpoint)
- [Python PDF в PowerPoint Программно](#python-pdf-to-powerpoint)
- [Python PDF в PowerPoint Библиотека](#python-pdf-to-powerpoint)
- [Python Сохранить PDF как PowerPoint](#python-pdf-to-powerpoint)
- [Python Создать PowerPoint из PDF](#python-pdf-to-powerpoint)
- [Python Генерация PowerPoint из PDF](#python-pdf-to-powerpoint)
- [Python PDF в PowerPoint Конвертер](#python-pdf-to-powerpoint)

_Формат_: **PPTX**
- [Python PDF в PPTX Код](#python-pdf-to-pptx)
- [Python PDF в PPTX API](#python-pdf-to-pptx)
- [Python PDF в PPTX Программно](#python-pdf-to-pptx)
- [Python PDF в PPTX Библиотека](#python-pdf-to-pptx)
- [Python Сохранить PDF как PPTX](#python-pdf-to-pptx)
- [Python Создать PPTX из PDF](#python-pdf-to-pptx)
- [Python Генерация PPTX из PDF](#python-pdf-to-pptx)
- [Python PDF в PPTX Конвертер](#python-pdf-to-pptx)