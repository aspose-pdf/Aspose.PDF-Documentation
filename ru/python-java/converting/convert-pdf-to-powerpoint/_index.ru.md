---
title: Convert PDF to PowerPoint in Python
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: /python-java/convert-pdf-to-powerpoint/
description: Aspose.PDF позволяет преобразовывать PDF в формат PPT (PowerPoint) с использованием Python. Один из способов - это возможность конвертировать PDF в PPTX слайдов в виде изображений.
lastmod: "2023-04-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Обзор

Можно ли преобразовать PDF файл в PowerPoint? Да, можно! И это просто!
Эта статья объясняет, как **конвертировать PDF в PowerPoint с помощью Python**. Она охватывает следующие темы.

_Формат_: **PPTX**
- [Python PDF в PPTX](#python-pdf-to-pptx)
- [Python Конвертировать PDF в PPTX](#python-pdf-to-pptx)
- [Python Как конвертировать PDF файл в PPTX](#python-pdf-to-pptx)

_Формат_: **PowerPoint**
- [Python PDF в PowerPoint](#python-pdf-to-powerpoint)
- [Python Конвертировать PDF в PowerPoint](#python-pdf-to-powerpoint)
- [Python Как конвертировать PDF файл в PowerPoint](#python-pdf-to-powerpoint)

## Конвертация PDF в PowerPoint и PPTX с использованием Python

**Aspose.PDF for Python via Java** позволяет отслеживать прогресс конвертации PDF в PPTX.

У нас есть API под названием Aspose.Slides, который предлагает возможность создавать, а также изменять презентации PPT/PPTX. Этот API также предоставляет возможность конвертировать файлы PPT/PPTX в формат PDF. Во время этой конвертации отдельные страницы PDF файла преобразуются в отдельные слайды в файле PPTX.

Во время конвертации PDF в <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr> текст отображается как текст, чтобы вы могли его выбрать/обновить. Пожалуйста, обратите внимание, что для конвертации PDF файлов в формат PPTX, Aspose.PDF предоставляет класс под названием [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions). Объект класса PptxSaveOptions передается в качестве второго аргумента в метод [`Document.Save(..) method`](https://reference.aspose.com/pdf/java/aspose.pdf/document/methods/save). Следующий кодовый фрагмент показывает процесс конвертации PDF файлов в формат PPTX.

## Простая конвертация PDF в PowerPoint с использованием Python и Aspose.PDF для Python

В целях конвертации PDF в PPTX, Aspose.PDF для Python предлагает использовать следующие шаги кода.

<a name="csharp-pdf-to-powerpoint"><strong>Шаги: Конвертация PDF в PowerPoint на Python</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Шаги: Конвертация PDF в PPTX на Python</strong></a>

1. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/java/aspose.pdf/document)
2. Создайте экземпляр класса [PptxSaveOptions](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions)
3. Используйте метод **Save** объекта **Document**, чтобы сохранить PDF как PPTX

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# Открыть PDF документ
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SeparateImages = True
save_options._OptimizeTextBoxes = True

# Сохранить файл в формате документа MS Word
document.save(output_pdf, save_options)
```


## Преобразование PDF в PPTX с слайдами в виде изображений

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в PowerPoint онлайн**

Aspose.PDF для Python предлагает вам бесплатное онлайн-приложение ["PDF в PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), где вы можете попробовать изучить функциональность и качество его работы.

[![Aspose.PDF Преобразование PDF в PPTX с использованием бесплатного приложения](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

В случае, если вам нужно преобразовать PDF с возможностью поиска в PPTX в виде изображений вместо выделяемого текста, Aspose.PDF предоставляет такую функцию через класс [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/). Чтобы достичь этого, установите свойство [SlidesAsImages](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/#properties) класса [PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/) в 'true', как показано в следующем примере кода.

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# Открытие PDF документа
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SlidesAsImages = True

# Сохраните файл в формате документа MS Word
document.save(output_pdf, save_options)
```


## См. также

Эта статья также охватывает следующие темы. Коды такие же, как выше.

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