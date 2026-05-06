---
title: Конвертировать форматы изображений в PDF на Python
linktitle: Конвертировать изображения в PDF
type: docs
weight: 60
url: /python-net/convert-images-format-to-pdf/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать BMP, CGM, DICOM, PNG, TIFF, EMF, SVG и другие форматы изображений в PDF на Python с помощью Aspose.PDF for Python via .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true 
AlternativeHeadline: Как конвертировать изображения в PDF на Python
Abstract: В этой статье представлено полное руководство по конвертации различных форматов изображений в PDF с использованием Python, в частности с применением библиотеки Aspose.PDF for Python via .NET. В статье рассматривается ряд форматов изображений, включая BMP, CGM, DICOM, EMF, GIF, PNG, SVG и TIFF. Каждый раздел подробно описывает шаги, необходимые для выполнения конвертации, предоставляя фрагменты кода для иллюстрации процесса. Например, преобразование BMP в PDF включает создание нового PDF Document, определение размещения изображения, вставку изображения и сохранение документа. Аналогично для форматов, таких как CGM, DICOM и других, описываются специфические параметры загрузки и этапы обработки. Статья также подчёркивает преимущества использования Aspose.PDF для подобных задач, такие как поддержка различных методов кодирования и возможность обработки как однокадровых, так и многокадровых изображений.
---

## Связанные преобразования

- [Преобразовать PDF в форматы изображений](/pdf/ru/python-net/convert-pdf-to-images-format/) когда вам нужен обратный рабочий процесс.
- [Преобразовать HTML в PDF](/pdf/ru/python-net/convert-html-to-pdf/) для веб‑контента и источников MHTML.
- [Конвертировать другие форматы файлов в PDF](/pdf/ru/python-net/convert-other-files-to-pdf/) для EPUB, XPS, текста и других вводов, не являющихся изображениями.

## Преобразование изображений Python в PDF

**Aspose.PDF for Python via .NET** позволяет конвертировать различные форматы изображений в PDF‑файлы. Наша библиотека демонстрирует примеры кода для преобразования самых популярных форматов изображений, таких как - BMP, CGM, DICOM, EMF, JPG, PNG, SVG и TIFF.

## Конвертировать BMP в PDF

Преобразуйте BMP‑файлы в PDF‑документ с помощью библиотеки **Aspose.PDF for Python via .NET**.

<abbr title="Bitmap Image File">BMP</abbr> Изображения — это файлы с расширением. BMP представляет файлы Bitmap Image, которые используются для хранения bitmap‑цифровых изображений. Эти изображения независимы от графического адаптера и также называются форматом device independent bitmap (DIB).

Вы можете конвертировать BMP в PDF‑файлы с помощью Aspose.PDF for Python via .NET API. Поэтому вы можете следовать следующим шагам для преобразования BMP‑изображений:

Шаги по преобразованию BMP в PDF с помощью Python:

1. Создайте пустой PDF-документ.
1. Создайте нужную страницу, например, мы создали A4, но вы можете указать свой собственный формат.
1. Помещает изображение (из infile) на страницу, используя определённый прямоугольник.
1. Сохранить документ в формате PDF.

Следующий фрагмент кода выполнит эти шаги и покажет, как преобразовать BMP в PDF с помощью Python:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_BMP_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать BMP в PDF онлайн**

Aspose представляет вам онлайн‑приложение ["BMP в PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), где вы можете попытаться исследовать, как работает функциональность и качество.

[![Aspose.PDF Конвертация BMP в PDF с помощью App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Преобразовать CGM в PDF

Конвертировать CGM (Computer Graphics Metafile) в PDF (или другой поддерживаемый формат) с использованием Aspose.PDF for Python via .NET.

<abbr title="Computer Graphics Metafile">CGM</abbr> это расширение файла формата Computer Graphics Metafile, обычно используемого в CAD (computer-aided design) и приложениях для презентационной графики. CGM — векторный графический формат, поддерживающий три разных метода кодирования: бинарный (лучший по скорости чтения программой), символьный (создаёт самый маленький размер файла и позволяет быстрее передавать данные) или кодирование в открытом виде (позволяет пользователям читать и изменять файл с помощью текстового редактора).

Проверьте следующий фрагмент кода для преобразования файлов CGM в формат PDF.

Шаги по конвертации CGM в PDF на Python:

1. Определить пути к файлам
1. Установите параметры загрузки для CGM.
1. Преобразовать CGM в PDF
1. Сообщение о конвертации печати

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CGM_to_PDF(infile, outfile):
    options = ap.CgmLoadOptions()
    document = ap.Document(infile, options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Преобразовать DICOM в PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> format является отраслевым стандартом в медицинской индустрии для создания, хранения, передачи и визуализации цифровых медицинских изображений и документов обследуемых пациентов.

**Aspose.PDF for Python** позволяет конвертировать изображения DICOM и SVG, но по техническим причинам при добавлении изображений нужно указывать тип файла, который будет добавлен в PDF.

В следующем фрагменте кода показано, как преобразовать файлы DICOM в формат PDF с помощью Aspose.PDF. Вам нужно загрузить изображение DICOM, разместить его на странице PDF‑файла и сохранить результат в виде PDF. Мы используем дополнительную библиотеку pydicom для задания размеров этого изображения. Если вы хотите позиционировать изображение на странице, вы можете пропустить этот фрагмент кода.

1. Загрузите файл DICOM.
1. Извлеките размеры изображения.
1. Печатайте размер изображения.
1. Создайте новый PDF-документ.
1. Подготовьте изображение DICOM для PDF.
1. Установите размер страницы PDF и поля.
1. Добавьте изображение на страницу.
1. Сохраните PDF.
1. Сообщение о конвертации при печати.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_DICOM_to_PDF(infile, outfile):
    # Load the DICOM file
    import pydicom

    dicom_file = pydicom.dcmread(infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = ap.Document()
    page = document.pages.add()
    image = ap.Image()
    image.file_type = ap.ImageFileType.DICOM
    image.file = infile

    # Set page dimensions
    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробовать конвертировать DICOM в PDF онлайн**

Aspose представляет вам онлайн‑приложение ["DICOM в PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), где вы можете попытаться исследовать, как работает функциональность и качество.

[![Aspose.PDF Конвертация DICOM в PDF с использованием приложения](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Преобразовать EMF в PDF

<abbr title="Enhanced metafile format">EMF</abbr> хранит графические изображения независимо от устройства. Метафайлы EMF состоят из записей переменной длины в хронологическом порядке, которые могут отобразить сохранённое изображение после разбора на любом выходном устройстве.

В следующем фрагменте кода показано, как преобразовать EMF в PDF с помощью Python:

```python

import aspose.pdf as ap
from os import path
import sys

def convert_EMF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(infile, rectangle)

    # Save the file into PDF format
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать EMF в PDF онлайн**

Aspose представляет вам онлайн‑приложение ["EMF в PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), где вы можете попытаться исследовать, как работает функциональность и качество.

[![Aspose.PDF Преобразование EMF в PDF с помощью App](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Конвертировать GIF в PDF

Конвертировать GIF‑файлы в PDF‑документ, используя библиотеку **Aspose.PDF for Python via .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> может хранить сжатые данные без потери качества в формате, содержащем не более 256 цветов. Аппаратно-независимый формат GIF был разработан в 1987 году (GIF87a) компанией CompuServe для передачи растровых изображений по сетям.

Следующий фрагмент кода выполнит эти шаги и покажет, как преобразовать BMP в PDF с помощью Python:

```python

import aspose.pdf as ap
from os import path
import sys

def convert_GIF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать GIF в PDF онлайн**

Aspose представляет вам онлайн‑приложение ["GIF в PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), где вы можете попытаться исследовать, как работает функциональность и качество.

[![Aspose.PDF Конвертация GIF в PDF с помощью App](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Конвертировать PNG в PDF

**Aspose.PDF for Python via .NET** поддерживает функцию конвертации PNG‑изображений в формат PDF. Посмотрите следующий фрагмент кода для выполнения вашей задачи.

<abbr title="Portable Network Graphics">PNG</abbr> относится к типу растрового файлового формата, который использует без потерь сжатие, что делает его популярным среди пользователей.

Вы можете конвертировать PNG в PDF‑изображение, используя указанные ниже шаги:

1. Создайте новый PDF Document.
1. Определите размещение изображения.
1. Сохраните PDF.
1. Сообщение о конвертации при печати.

Кроме того, приведенный ниже фрагмент кода показывает, как преобразовать PNG в PDF с помощью Python:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PNG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать PNG в PDF онлайн**

Aspose представляет вам онлайн‑приложение ["PNG в PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), где вы можете попытаться исследовать, как работает функциональность и качество.

[![Aspose.PDF Конвертация PNG в PDF с использованием приложения](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Конвертировать SVG в PDF

**Aspose.PDF for Python via .NET** объясняет, как преобразовать изображения SVG в формат PDF и как получить размеры исходного файла SVG.

Scalable Vector Graphics (SVG) — это семейство спецификаций формата файлов на основе XML для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается World Wide Web Consortium (W3C) с 1999 года.

<abbr title="Scalable Vector Graphics">SVG</abbr> изображения и их поведение определяются в текстовых файлах XML. Это означает, что их можно искать, индексировать, скриптовать и, при необходимости, сжимать. Будучи файлами XML, SVG‑изображения можно создавать и редактировать в любом текстовом редакторе, но часто удобнее создавать их в графических программах, таких как Inkscape.

{{% alert color="success" %}}
**Попробуйте конвертировать формат SVG в PDF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн‑приложение ["SVG в PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), где вы можете попытаться исследовать, как работает функциональность и качество.

[![Конвертация SVG в PDF с Aspose.PDF в приложении](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

Следующий фрагмент кода демонстрирует процесс преобразования SVG‑файла в формат PDF с помощью Aspose.PDF for Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_SVG_to_PDF(infile, outfile):
    load_options = ap.SvgLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Конвертировать TIFF в PDF

**Aspose.PDF** поддерживается файловый формат, будь то однокадровое или многокадровое изображение TIFF. Это означает, что вы можете преобразовать изображение TIFF в PDF.

TIFF или TIF, Tagged Image File Format, представляет растровые изображения, предназначенные для использования на различных устройствах, соответствующих этому стандарту формата файлов. Изображение TIFF может содержать несколько кадров с разными изображениями. Формат файлов Aspose.PDF также поддерживается, будь то однокадровое или многокадровое изображение TIFF.

Вы можете конвертировать TIFF в PDF так же, как и остальные графические форматы растровых файлов:

```python
import aspose.pdf as ap
from os import path
import sys

def convert_TIFF_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Конвертировать CDR в PDF

Следующий фрагмент кода показывает, как загрузить файл CorelDRAW (CDR) и сохранить его как PDF, используя 'CdrLoadOptions' в Aspose.PDF for Python via .NET.

1. Создайте 'CdrLoadOptions()', чтобы настроить, как должен загружаться файл CDR.
1. Инициализируйте объект Document с файлом CDR и параметрами загрузки.
1. Сохраните документ в формате PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_CDR_to_PDF(infile, outfile):
    load_options = ap.CdrLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## Конвертировать JPEG в PDF

Этот пример показывает, как конвертировать JPEG в PDF‑файл с помощью Aspose.PDF for Python via .NET.

1. Создайте новый PDF-документ.
1. Добавьте новую страницу.
1. Определите прямоугольник размещения (размер A4: 595×842 пункта).
1. Вставьте изображение на страницу.
1. Сохранить PDF.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_JPEG_to_PDF(infile, outfile):
    document = ap.Document()
    page = document.pages.add()
    rectangle = ap.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(infile, rectangle)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```
