---
title: Конвертация форматов изображений в PDF на Python
linktitle: Конвертация изображений в PDF
type: docs
weight: 60
url: /ru/python-net/convert-images-format-to-pdf/
lastmod: "2026-04-14"
description: Узнайте, как конвертировать BMP, CGM, DICOM, PNG, TIFF, EMF, SVG и другие форматы изображений в PDF на Python с помощью Aspose.PDF для Python через .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true 
AlternativeHeadline: Как конвертировать изображения в PDF на Python
Abstract: В этой статье представлено подробное руководство по конвертации различных форматов изображений в PDF с использованием Python, в частности с применением библиотеки Aspose.PDF для Python через .NET. Статья охватывает ряд форматов изображений, включая BMP, CGM, DICOM, EMF, GIF, PNG, SVG и TIFF. В каждом разделе подробно описаны шаги, необходимые для выполнения конвертации, с примерами кода для иллюстрации процесса. Например, конвертация BMP в PDF включает создание нового PDF-документа, определение размещения изображения, вставку изображения и сохранение документа. Аналогично, для таких форматов, как CGM, DICOM и других, описаны конкретные параметры загрузки и шаги обработки. В статье также подчёркиваются преимущества использования Aspose.PDF для таких задач, такие как поддержка различных методов кодирования и возможность обработки как одностраничных, так и многостраничных изображений.
---

## Связанные конвертации

- [Конвертация PDF в форматы изображений](/pdf/python-net/convert-pdf-to-images-format/) — когда вам нужен обратный процесс.
- [Конвертация HTML в PDF](/pdf/python-net/convert-html-to-pdf/) — для веб-содержимого и источников MHTML.
- [Конвертация других файловых форматов в PDF](/pdf/python-net/convert-other-files-to-pdf/) — для EPUB, XPS, текста и других не-графических входных данных.

## Конвертация изображений в PDF на Python

**Aspose.PDF для Python через .NET** позволяет конвертировать различные форматы изображений в PDF-файлы. Наша библиотека демонстрирует примеры кода для конвертации наиболее популярных форматов изображений, таких как BMP, CGM, DICOM, EMF, JPG, PNG, SVG и TIFF.

## Конвертация BMP в PDF

Конвертируйте файлы BMP в PDF-документ с помощью библиотеки **Aspose.PDF для Python через .NET**.

<abbr title="Bitmap Image File">BMP</abbr> — это файлы с расширением .BMP. BMP представляют файлы растровых изображений, которые используются для хранения цифровых растровых изображений. Эти изображения не зависят от графического адаптера и также называются форматом растровых изображений, не зависящих от устройства (DIB).

Вы можете конвертировать файлы BMP в PDF с помощью API Aspose.PDF для Python через .NET. Для этого выполните следующие шаги для конвертации изображений BMP:

Шаги для конвертации BMP в PDF на Python:

1. Создайте пустой PDF-документ.
1. Создайте нужную страницу, например, мы создали A4, но вы можете указать свой формат.
1. Разместите изображение (из входного файла) на странице, используя определённый прямоугольник.
1. Сохраните документ как PDF.

Следующий фрагмент кода демонстрирует эти шаги и показывает, как конвертировать BMP в PDF с помощью Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать BMP в PDF онлайн**

Aspose представляет вам бесплатное онлайн-приложение ["BMP в PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), где вы можете попробовать изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация BMP в PDF с помощью бесплатного приложения](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Конвертация CGM в PDF

Конвертируйте файл CGM (Computer Graphics Metafile) в PDF (или другой поддерживаемый формат) с помощью Aspose.PDF для Python через .NET.

<abbr title="Computer Graphics Metafile">CGM</abbr> — это расширение файла для формата Computer Graphics Metafile, обычно используемого в CAD (автоматизированном проектировании) и приложениях графики для презентаций. CGM — это векторный графический формат, который поддерживает три различных метода кодирования: двоичный (лучший для скорости чтения программой), символьный (создаёт наименьший размер файла и обеспечивает более быструю передачу данных) или текстовое кодирование (позволяет пользователям читать и редактировать файл с помощью текстового редактора).

Проверьте следующий фрагмент кода для конвертации файлов CGM в формат PDF.

Шаги для конвертации CGM в PDF на Python:

1. Определите пути к файлам
1. Установите параметры загрузки для CGM.
1. Конвертируйте CGM в PDF
1. Выведите сообщение о конвертации

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    options = apdf.CgmLoadOptions()

    # Open PDF document
    document = apdf.Document(path_infile, options)
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

## Конвертация DICOM в PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> — это стандарт медицинской индустрии для создания, хранения, передачи и визуализации цифровых медицинских изображений и документов обследованных пациентов.

**Aspose.PDF для Python** позволяет конвертировать изображения DICOM и SVG, но по техническим причинам для добавления изображений вам нужно указать тип файла, который будет добавлен в PDF.

Следующий фрагмент кода показывает, как конвертировать файлы DICOM в формат PDF с помощью Aspose.PDF. Вы должны загрузить изображение DICOM, разместить изображение на странице в PDF-файле и сохранить результат как PDF. Мы используем дополнительную библиотеку pydicom для установки размеров этого изображения. Если вы хотите позиционировать изображение на странице, вы можете пропустить этот фрагмент кода.

1. Инициализируйте новый 'ap.Document()' и добавьте страницу
1. Вставьте изображение DICOM. Создайте apdf.Image(), установите его тип в DICOM и назначьте путь к файлу.
1. Настройте размер страницы. Согласуйте размеры страницы PDF с размером изображения DICOM, уберите поля.
1. Добавьте изображение на страницу, сохраните документ в выходной файл.

1. Загрузите файл DICOM.
1. Извлеките размеры изображения.
1. Выведите размер изображения.
1. Создайте новый PDF-документ.
1. Подготовьте изображение DICOM для PDF.
1. Установите размер страницы PDF и поля.
1. Добавьте изображение на страницу.
1. Сохраните PDF.
1. Выведите сообщение о конвертации.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom


    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    # Load the DICOM file
    dicom_file = pydicom.dcmread(path_infile)

    # Get the dimensions of the image
    rows = dicom_file.Rows
    columns = dicom_file.Columns

    # Print the dimensions
    print(f"DICOM image size: {rows} x {columns} pixels")

    # Initialize new Document
    document = apdf.Document()
    page = document.pages.add()
    image = apdf.Image()
    image.file_type = apdf.ImageFileType.DICOM
    image.file = path_infile

    # Set page dimensions

    page.page_info.height = rows
    page.page_info.width = columns
    page.page_info.margin.bottom = 0
    page.page_info.margin.top = 0
    page.page_info.margin.right = 0
    page.page_info.margin.left = 0
    page.paragraphs.add(image)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать DICOM в PDF онлайн**

Aspose представляет вам бесплатное онлайн-приложение ["DICOM в PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), где вы можете попробовать изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация DICOM в PDF с помощью бесплатного приложения](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Конвертация EMF в PDF

<abbr title="Enhanced metafile format">EMF</abbr> хранит графические изображения независимо от устройства. Метафайлы EMF состоят из записей переменной длины в хронологическом порядке, которые могут отображать сохранённое изображение после анализа на любом устройстве вывода.

Следующий фрагмент кода показывает, как конвертировать EMF в PDF с помощью Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom
    
    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    # add image to new pdf page
    page.add_image(path_infile, rectangle)

    # Save the file into PDF format
    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать EMF в PDF онлайн**

Aspose представляет вам бесплатное онлайн-приложение ["EMF в PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), где вы можете попробовать изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация EMF в PDF с помощью бесплатного приложения](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Конвертация GIF в PDF

Конвертируйте файлы GIF в PDF-документ с помощью библиотеки **Aspose.PDF для Python через .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> способен хранить сжатые данные без потери качества в формате не более 256 цветов. Не зависящий от оборудования формат GIF был разработан в 1987 году (GIF87a) компанией CompuServe для передачи растровых изображений по сетям.

Следующий фрагмент кода демонстрирует эти шаги и показывает, как конвертировать BMP в PDF с помощью Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать GIF в PDF онлайн**

Aspose представляет вам бесплатное онлайн-приложение ["GIF в PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), где вы можете попробовать изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация GIF в PDF с помощью бесплатного приложения](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Конвертация PNG в PDF

**Aspose.PDF для Python через .NET** поддерживает функцию конвертации изображений PNG в формат PDF. Проверьте следующий фрагмент кода для выполнения вашей задачи.

<abbr title="Portable Network Graphics">PNG</abbr> относится к типу формата файлов растровых изображений, который использует сжатие без потерь, что делает его популярным среди пользователей.

Вы можете конвертировать PNG в PDF-изображение, выполнив следующие шаги:

1. Создайте новый PDF-документ.
1. Определите размещение изображения.
1. Сохраните PDF.
1. Выведите сообщение о конвертации.

Кроме того, фрагмент кода ниже показывает, как конвертировать PNG в PDF с помощью Python:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**Попробуйте конвертировать PNG в PDF онлайн**

Aspose представляет вам бесплатное онлайн-приложение ["PNG в PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), где вы можете попробовать изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация PNG в PDF с помощью бесплатного приложения](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Конвертация SVG в PDF

**Aspose.PDF для Python через .NET** объясняет, как конвертировать изображения SVG в формат PDF и как получить размеры исходного файла SVG.

Масштабируемая векторная графика (SVG) — это семейство спецификаций XML-основанного формата файлов для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG — это открытый стандарт, который с 1999 года разрабатывается Консорциумом Всемирной паутины (W3C).

<abbr title="Scalable Vector Graphics">SVG</abbr> изображения и их поведение определены в текстовых файлах XML. Это означает, что их можно искать, индексировать, скриптовать и, при необходимости, сжимать. Как XML-файлы, изображения SVG могут создаваться и редактироваться с помощью любого текстового редактора, но часто удобнее создавать их с помощью таких программ рисования, как Inkscape.

{{% alert color="success" %}}
**Попробуйте конвертировать формат SVG в PDF онлайн**

Aspose.PDF для Python через .NET представляет вам бесплатное онлайн-приложение ["SVG в PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), где вы можете попробовать изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация SVG в PDF с помощью бесплатного приложения](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

Следующий фрагмент кода показывает процесс конвертации файла SVG в формат PDF с помощью Aspose.PDF для Python.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = apdf.SvgLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Конвертация TIFF в PDF

Формат файла **Aspose.PDF** поддерживается, будь то одностраничное или многостраничное изображение TIFF. Это означает, что вы можете конвертировать изображение TIFF в PDF.

TIFF или TIF, Tagged Image File Format, представляет растровые изображения, которые предназначены для использования на различных устройствах, соответствующих этому стандарту формата файлов. Изображение TIFF может содержать несколько кадров с разными изображениями. Формат файла Aspose.PDF также поддерживается, будь то одностраничное или многостраничное изображение TIFF.

Вы можете конвертировать TIFF в PDF так же, как и остальные растровые графические форматы:

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Конвертация CDR в PDF

Следующий фрагмент кода показывает, как загрузить файл CorelDRAW (CDR) и сохранить его как PDF с помощью 'CdrLoadOptions' в Aspose.PDF для Python через .NET.

1. Создайте 'CdrLoadOptions()' для настройки способа загрузки файла CDR.
1. Инициализируйте объект Document с файлом CDR и параметрами загрузки.
1. Сохраните документ как PDF.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    load_options = apdf.CdrLoadOptions()
    document = apdf.Document(path_infile, load_options)
    document.save(path_outfile)

    print(infile + " converted into " + outfile)
```

## Конвертация JPEG в PDF

Этот пример показывает, как конвертировать файл JPEG в PDF с помощью Aspose.PDF для Python через .NET.

1. Создайте новый PDF-документ.
1. Добавьте новую страницу.
1. Определите прямоугольник размещения (размер A4: 595x842 точки).
1. Вставьте изображение на страницу.
1. Сохраните PDF.

```python

    from io import FileIO
    from os import path
    import os
    import shutil
    import aspose.pdf as apdf
    import inspect
    import pydicom

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document()
    page = document.pages.add()
    rectangle = apdf.Rectangle(0, 0, 595, 842, True)  # A4 size in points
    page.add_image(path_infile, rectangle)

    document.save(path_outfile)
    print(infile + " converted into " + outfile)
```