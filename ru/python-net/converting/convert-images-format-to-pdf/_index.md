---
title: Преобразование различных форматов изображений в PDF на Python
linktitle: Преобразовать изображения в PDF
type: docs
weight: 60
url: /ru/python-net/convert-images-format-to-pdf/
lastmod: "2025-09-01"
description: Преобразуйте различные форматы изображений, такие как BMP, CGM, DICOM, PNG, TIFF, EMF и SVG, в PDF с помощью Python.
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Как преобразовать изображения в PDF на Python
Abstract: В этой статье представлено всестороннее руководство по преобразованию различных форматов изображений в PDF с использованием Python, в частности с использованием библиотеки Aspose.PDF для Python через .NET. В статье рассматриваются форматы изображений, включая BMP, CGM, DICOM, EMF, GIF, PNG, SVG и TIFF. Каждый раздел подробно описывает шаги, необходимые для выполнения преобразования, предоставляя фрагменты кода для иллюстрации процесса. Например, преобразование BMP в PDF включает создание нового PDF‑документа, определение размещения изображения, вставку изображения и сохранение документа. Аналогично для форматов, таких как CGM, DICOM и других, описываются конкретные параметры загрузки и шаги обработки. Статья также подчёркивает преимущества использования Aspose.PDF для подобных задач, такие как поддержка различных методов кодирования и возможность обработки как однокадровых, так и многокадровых изображений.
---

## Преобразования изображений в PDF на Python

**Aspose.PDF for Python via .NET**  позволяет конвертировать различные форматы изображений в PDF‑файлы. Наша библиотека демонстрирует фрагменты кода для преобразования самых популярных форматов изображений, таких как BMP, CGM, DICOM, EMF, JPG, PNG, SVG и TIFF.

## Преобразовать BMP в PDF

Преобразуйте файлы BMP в PDF‑документ с использованием библиотеки **Aspose.PDF for Python via .NET**.

<abbr title="Bitmap Image File">BMP</abbr> изображения — это файлы с расширением. BMP представляет файлы растровых изображений, которые используются для хранения цифровых растровых изображений. Эти изображения независимы от графического адаптера и также называются независимыми от устройства битмапами (DIB).

Вы можете преобразовать BMP в PDF‑файлы с помощью Aspose.PDF for Python via .NET API. Поэтому вы можете выполнить следующие шаги для преобразования изображений BMP:

Шаги для преобразования BMP в PDF на Python:

1. Создайте пустой PDF‑документ.
1. Создайте нужную страницу, например, мы создали A4, но вы можете указать свой собственный формат.
1. Размещает изображение (из infile) на странице, используя заданный прямоугольник.
1. Сохраните документ в формате PDF.

Следующий фрагмент кода следует этим шагам и показывает, как преобразовать BMP в PDF с помощью Python:

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
**Попробуйте преобразовать BMP в PDF онлайн**

Aspose представляет вам онлайн‑бесплатное приложение ["BMP в PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), где вы можете протестировать функциональность и качество работы.

[![Преобразование Aspose.PDF BMP в PDF с помощью бесплатного приложения](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Преобразовать CGM в PDF

Преобразуйте CGM (Computer Graphics Metafile) в PDF (или другой поддерживаемый формат) с помощью Aspose.PDF for Python via .NET.

<abbr title="Computer Graphics Metafile">CGM</abbr> — это расширение файла формата Computer Graphics Metafile, часто используемого в САПР (computer-aided design) и приложениях для презентационной графики. CGM — это векторный графический формат, поддерживающий три разных метода кодирования: бинарный (лучший для скорости чтения программой), символьный (даёт наименьший размер файла и позволяет более быстрые передачи данных) или текстовый (позволяет пользователям читать и изменять файл с помощью текстового редактора).

Посмотрите следующий фрагмент кода для преобразования файлов CGM в формат PDF.

Шаги для преобразования CGM в PDF на Python:

1. Задайте пути к файлам
1. Установите параметры загрузки для CGM.
1. Преобразуйте CGM в PDF
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

## Преобразовать DICOM в PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> формат является отраслевым стандартом в медицине для создания, хранения, передачи и визуализации цифровых медицинских изображений и документов обследованных пациентов.

**Aspose.PDF for Python** позволяет конвертировать изображения DICOM и SVG, но по техническим причинам при добавлении изображений необходимо указать тип файла, который будет добавлен в PDF.

Следующий фрагмент кода показывает, как преобразовать файлы DICOM в формат PDF с помощью Aspose.PDF. Вы должны загрузить изображение DICOM, разместить его на странице PDF‑файла и сохранить результат в PDF. Мы используем дополнительную библиотеку pydicom для задания размеров этого изображения. Если вы хотите позиционировать изображение на странице, можете пропустить этот фрагмент кода.

1. Инициализируйте новый 'ap.Document()' и добавьте страницу
1. Вставьте изображение DICOM. Создайте apdf.Image(), задайте его тип как DICOM и укажите путь к файлу.
1. Отрегулируйте размер страницы. Согласуйте размеры страницы PDF с размером изображения DICOM, уберите отступы.
1. Добавьте изображение на страницу, сохраните документ в выходной файл.

1. Загрузите файл DICOM.
1. Извлеките размеры изображения.
1. Выведите размер изображения.
1. Создайте новый PDF‑документ.
1. Подготовьте DICOM‑изображение для PDF.
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

Aspose представляет вам онлайн‑бесплатное приложение ["DICOM to PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), где вы можете попробовать исследовать его функциональность и качество работы.

[![Aspose.PDF Конверсия DICOM в PDF с помощью бесплатного приложения](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Конвертировать EMF в PDF

<abbr title="Enhanced metafile format">EMF</abbr> хранит графические изображения независимо от устройства. Метафайлы EMF состоят из записей переменной длины в хронологическом порядке, которые могут отобразить сохранённое изображение после анализа на любом выводном устройстве.

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

Aspose представляет вам онлайн‑бесплатное приложение ["EMF to PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), где вы можете попробовать исследовать его функциональность и качество работы.

[![Aspose.PDF Конверсия EMF в PDF с помощью бесплатного приложения](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Конвертировать GIF в PDF

Конвертировать файлы GIF в PDF‑документ с использованием библиотеки **Aspose.PDF for Python via .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> способен хранить сжатые данные без потери качества в формате не более 256 цветов. Аппаратно‑независимый формат GIF был разработан в 1987 году (GIF87a) компанией CompuServe для передачи растровых изображений по сетям.

Таким образом, следующий фрагмент кода следует этим шагам и показывает, как конвертировать BMP в PDF с помощью Python:

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

Aspose представляет вам онлайн‑бесплатное приложение ["GIF to PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), где вы можете попробовать исследовать его функциональность и качество работы.

[![Aspose.PDF Конверсия GIF в PDF с помощью бесплатного приложения](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Конвертировать PNG в PDF

**Aspose.PDF for Python via .NET** поддерживает функцию конвертации PNG‑изображений в формат PDF. Посмотрите следующий фрагмент кода для реализации вашей задачи.

<abbr title="Portable Network Graphics">PNG</abbr> относится к типу растрового формата файлов изображений, использующему безпотерьную компрессию, что делает его популярным среди пользователей.

Вы можете конвертировать PNG в PDF, используя следующие шаги:

1. Создайте новый PDF‑документ.
1. Определите размещение изображения.
1. Сохраните PDF.
1. Выведите сообщение о конвертации.

Кроме того, ниже приведённый фрагмент кода показывает, как конвертировать PNG в PDF с помощью Python:

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

Aspose представляет вам онлайн‑бесплатное приложение ["PNG to PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), где вы можете попробовать исследовать его функциональность и качество работы.

[![Aspose.PDF Конверсия PNG в PDF с помощью бесплатного приложения](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Конвертировать SVG в PDF

**Aspose.PDF for Python via .NET** объясняет, как конвертировать SVG‑изображения в формат PDF и как получить размеры исходного SVG‑файла.

Scalable Vector Graphics (SVG) — это семейство спецификаций XML‑основанного формата файлов для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, разрабатываемым World Wide Web Consortium (W3C) с 1999 года.

<abbr title="Scalable Vector Graphics">SVG</abbr> изображения и их поведение определяются в XML‑текстовых файлах. Это означает, что их можно искать, индексировать, скриптовать и при необходимости сжимать. Как XML‑файлы, SVG‑изображения могут быть созданы и отредактированы любым текстовым редактором, но часто удобнее создавать их в графических программах, таких как Inkscape.

{{% alert color="success" %}}
**Попробуйте конвертировать формат SVG в PDF онлайн**

Aspose.PDF for Python via .NET представляет вам онлайн‑бесплатное приложение ["SVG to PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), где вы можете попробовать исследовать его функциональность и качество работы.

[![Aspose.PDF Конверсия SVG в PDF с бесплатным приложением](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

Следующий фрагмент кода демонстрирует процесс преобразования SVG‑файла в формат PDF с помощью Aspose.PDF для Python.

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

## Конвертировать TIFF в PDF

**Aspose.PDF** поддерживает формат файла, будь то одно‑кадровое или многокадровое изображение TIFF. Это означает, что вы можете конвертировать изображение TIFF в PDF.

TIFF или TIF, Tagged Image File Format, представляет растрные изображения, предназначенные для использования на различных устройствах, которые поддерживают этот стандарт формата файлов. Изображение TIFF может содержать несколько кадров с разными изображениями. Формат файла Aspose.PDF также поддерживается, будь то одно‑кадровое или многокадровое изображение TIFF.

Вы можете конвертировать TIFF в PDF тем же способом, что и остальные растровые форматы графики:

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

## Конвертировать CDR в PDF

Следующий фрагмент кода показывает, как загрузить файл CorelDRAW (CDR) и сохранить его как PDF, используя 'CdrLoadOptions' в Aspose.PDF для Python через .NET.

1. Создайте 'CdrLoadOptions()', чтобы настроить, как следует загружать файл CDR.
1. Инициализируйте объект Document с файлом CDR и параметрами загрузки.
1. Сохраните документ в формате PDF.

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

## Конвертировать JPEG в PDF

Этот пример показывает, как конвертировать JPEG в PDF‑файл с использованием Aspose.PDF для Python через .NET.

1. Создайте новый PDF‑документ.
1. Добавьте новую страницу.
1. Определите прямоугольник размещения (размер A4: 595x842 пункта).
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

