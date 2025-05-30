---
title: Конвертация различных форматов изображений в PDF в .NET
linktitle: Конвертировать изображения в PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /ru/net/convert-images-format-to-pdf/
lastmod: "2021-11-01"
description: Конвертируйте различные форматы изображений, такие как CDR, DJVU, BMP, CGM, JPEG, DICOM, PNG, TIFF, EMF и SVG в PDF с использованием C# .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Convert various Images formats to PDF in .NET",
    "alternativeHeadline": "Convert Multiple Image Formats to PDF with C#",
    "abstract": "Представляем мощную функцию в Aspose.PDF for .NET, которая позволяет бесшовно конвертировать различные форматы изображений, включая BMP, CGM, DICOM, EMF, JPG, PNG, SVG, TIFF, CDR и DJVU в высококачественные PDF-документы. Эта функциональность предоставляет простой способ интеграции конвертации изображений в PDF в ваши .NET-приложения, обеспечивая эффективную обработку разнообразного графического контента.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "4593",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/convert-images-format-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/convert-images-format-to-pdf/"
    },
    "dateModified": "2025-04-04",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Обзор

Эта статья объясняет, как конвертировать различные форматы изображений в PDF с использованием C#. В ней рассматриваются следующие темы.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

- [Конвертировать BMP в PDF](#csharp-bmp-to-pdf)
- [Конвертировать CGM в PDF](#csharp-cgm-to-pdf)
- [Конвертировать DICOM в PDF](#csharp-dicom-to-pdf)
- [Конвертировать EMF в PDF](#csharp-emf-to-pdf)
- [Конвертировать GIF в PDF](#csharp-gif-to-pdf)
- [Конвертировать JPG в PDF](#csharp-jpg-to-pdf)
- [Конвертировать PNG в PDF](#csharp-png-to-pdf)
- [Конвертировать SVG в PDF](#csharp-svg-to-pdf)
- [Конвертировать TIFF в PDF](#csharp-tiff-to-pdf)
- [Конвертировать CDR в PDF](#csharp-cdr-to-pdf)
- [Конвертировать DJVU в PDF](#csharp-djvu-to-pdf)
- [Конвертировать HEIC в PDF](#csharp-heic-to-pdf)

## Конвертации изображений в PDF на C#

**Aspose.PDF for .NET** позволяет вам конвертировать различные форматы изображений в PDF-файлы. Наша библиотека демонстрирует фрагменты кода для конвертации самых популярных форматов изображений, таких как - BMP, CGM, DICOM, EMF, JPG, PNG, SVG, CDR, HEIC и TIFF.

## Конвертировать BMP в PDF

Конвертируйте BMP-файлы в PDF-документ с помощью библиотеки **Aspose.PDF for .NET**.

<abbr title="Bitmap Image File">BMP</abbr> изображения - это файлы с расширением. BMP представляют собой файлы растровых изображений, которые используются для хранения цифровых изображений. Эти изображения независимы от графического адаптера и также называются форматом файла независимого растрового изображения (DIB).
Вы можете конвертировать BMP в PDF-файлы с помощью API Aspose.PDF for .NET. Поэтому вы можете следовать следующим шагам для конвертации BMP-изображений:

<a name="csharp-bmp-to-pdf" id="csharp-bmp-to-pdf"><strong>Конвертировать BMP в PDF</strong></a>

1. Инициализируйте новый объект класса [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document).
2. Загрузите входное **BMP** изображение.
3. Наконец, сохраните выходной PDF-файл.

Таким образом, следующий фрагмент кода следует этим шагам и показывает, как конвертировать BMP в PDF с использованием C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertBMPtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load BMP file
        image.File = dataDir + "BMPtoPDF.bmp";
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "BMPtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать BMP в PDF онлайн**

Aspose предлагает вам онлайн бесплатное приложение ["BMP в PDF"](https://products.aspose.app/pdf/conversion/bmp-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация BMP в PDF с использованием бесплатного приложения](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/bmp-to-pdf/)
{{% /alert %}}

## Конвертировать CGM в PDF

<abbr title="Computer Graphics Metafile">CGM</abbr> - это расширение файла для формата Computer Graphics Metafile, который обычно используется в CAD (компьютерном проектировании) и приложениях для презентационной графики. CGM - это векторный графический формат, который поддерживает три различных метода кодирования: бинарный (лучший для скорости чтения программой), основанный на символах (создает наименьший размер файла и позволяет более быстрые передачи данных) или кодирование в открытом виде (позволяет пользователям читать и изменять файл с помощью текстового редактора).

Проверьте следующий фрагмент кода для конвертации файлов CGM в формат PDF.

<a name="csharp-cgm-to-pdf" id="csharp-cgm-to-pdf"><strong>Конвертировать CGM в PDF</strong></a>

1. Создайте экземпляр класса [CgmLoadOptions](https://reference.aspose.com/pdf/ru/net/aspose.pdf/cgmloadoptions).
2. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document) с указанием имени исходного файла и параметров.
3. Сохраните документ с желаемым именем файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertCGMtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    var option = new Aspose.Pdf.CgmLoadOptions();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "CGMtoPDF.cgm", option))
    {
        // Save PDF document
        document.Save(dataDir + "CGMtoPDF_out.pdf");
    }
}
```

## Конвертировать DICOM в PDF

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> формат является стандартом медицинской отрасли для создания, хранения, передачи и визуализации цифровых медицинских изображений и документов обследованных пациентов.

**Aspose.PDF для .NET** позволяет вам конвертировать DICOM и SVG изображения, но по техническим причинам для добавления изображений вам необходимо указать тип файла, который будет добавлен в PDF:

<a name="csharp-dicom-to-pdf" id="csharp-dicom-to-pdf"><strong>Конвертировать DICOM в PDF</strong></a>

1. Создайте объект класса Image.
2. Добавьте изображение в коллекцию Paragraphs страницы.
3. Укажите свойство [FileType](https://reference.aspose.com/pdf/ru/net/aspose.pdf/image/properties/filetype).
4. Укажите путь или источник файла.
    - Если изображение находится на жестком диске, укажите путь, используя свойство Image.File.
    - Если изображение помещено в MemoryStream, передайте объект, содержащий изображение, в свойство Image.ImageStream.

Следующий фрагмент кода показывает, как конвертировать DICOM файлы в формат PDF с помощью Aspose.PDF. Вы должны загрузить DICOM изображение, разместить изображение на странице в PDF-файле и сохранить выходной файл в формате PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDICOMtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        
        var image = new Aspose.Pdf.Image
        {
            FileType = ImageFileType.Dicom,
            File = dataDir + "DICOMtoPDF.dcm"
        };
        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "DICOMtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать DICOM в PDF онлайн**

Aspose предлагает вам онлайн бесплатное приложение ["DICOM в PDF"](https://products.aspose.app/pdf/conversion/dicom-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация DICOM в PDF с использованием бесплатного приложения](dicom_to_pdf.png)](https://products.aspose.app/pdf/conversion/dicom-to-pdf/)
{{% /alert %}}

## Конвертировать EMF в PDF

<abbr title="Enhanced metafile format">EMF</abbr> хранит графические изображения независимо от устройства. Метафайлы EMF состоят из записей переменной длины в хронологическом порядке, которые могут отображать сохраненное изображение после разбора на любом выходном устройстве. Более того, вы можете конвертировать EMF в PDF изображение, используя следующие шаги:

<a name="csharp-emf-to-pdf" id="csharp-emf-to-pdf"><strong>Конвертировать EMF в PDF</strong></a>

1. Сначала инициализируйте объект класса [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document).
2. Загрузите файл **EMF** изображения.
3. Добавьте загруженное EMF изображение на страницу.
4. Сохраните PDF-документ.

Более того, следующий фрагмент кода показывает, как конвертировать EMF в PDF с C# в вашем .NET коде:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertEMFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load EMF file
        image.File = dataDir + "EMFtoPDF.emf";

        // Specify page dimension properties
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Left = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Height = image.BitmapSize.Height;

        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "EMFtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать EMF в PDF онлайн**

Aspose предлагает вам онлайн бесплатное приложение ["EMF в PDF"](https://products.aspose.app/pdf/conversion/emf-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация EMF в PDF с использованием бесплатного приложения](emf_to_pdf.png)](https://products.aspose.app/pdf/conversion/emf-to-pdf/)
{{% /alert %}}

## Конвертировать GIF в PDF

Конвертируйте GIF-файлы в PDF-документ с помощью библиотеки **Aspose.PDF for .NET**.

<abbr title="Graphics Interchange Format">GIF</abbr> может хранить сжатые данные без потери качества в формате не более 256 цветов. Независимый от оборудования формат GIF был разработан в 1987 году (GIF87a) компанией CompuServe для передачи растровых изображений по сетям.
Вы можете конвертировать GIF в PDF-файлы с помощью API Aspose.PDF for .NET. Поэтому вы можете следовать следующим шагам для конвертации GIF-изображений:

<a name="csharp-gif-to-pdf" id="csharp-gif-to-pdf"><strong>Конвертировать GIF в PDF</strong></a>

1. Инициализируйте новый объект класса [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document).
2. Загрузите входное **GIF** изображение.
3. Наконец, сохраните выходной PDF-файл.

Таким образом, следующий фрагмент кода следует этим шагам и показывает, как конвертировать BMP в PDF с использованием C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertGIFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load sample GIF image file
        image.File = dataDir + "GIFtoPDF.gif";
        page.Paragraphs.Add(image);

        // Save PDF document
        document.Save(dataDir + "GIFtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать GIF в PDF онлайн**

Aspose предлагает вам онлайн бесплатное приложение ["GIF в PDF"](https://products.aspose.app/pdf/conversion/gif-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация GIF в PDF с использованием бесплатного приложения](bmp_to_pdf.png)](https://products.aspose.app/pdf/conversion/gif-to-pdf/)
{{% /alert %}}

## Конвертировать JPG в PDF

Не нужно удивляться, как конвертировать JPG в PDF, потому что библиотека **Aspose.PDF для .NET** имеет лучшее решение.

Вы можете очень легко конвертировать изображения JPG в PDF с помощью Aspose.PDF for .NET, следуя следующим шагам:

<a name="csharp-jpg-to-pdf" id="csharp-jpg-to-pdf"><strong>Конвертировать JPG в PDF</strong></a>

1. Инициализируйте объект класса [Document](https://reference.aspose.com/page/net/aspose.page/document).
2. Добавьте новую страницу в PDF-документ.
3. Загрузите **JPG** изображение и добавьте его в параграф.
4. Сохраните выходной PDF.

Ниже приведенный фрагмент кода показывает, как конвертировать изображение JPG в PDF с использованием C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertJPGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document 
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load input JPG file
        image.File = dataDir + "JPGtoPDF.jpg";
        
        // Add image on a page
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "JPGtoPDF_out.pdf");
    }
}
```

Затем вы можете увидеть, как конвертировать изображение в PDF с **той же высотой и шириной страницы**. Мы получим размеры изображения и соответственно установим размеры страницы PDF-документа с помощью следующих шагов:

1. Загрузите входной файл изображения.
1. Установите высоту, ширину и поля страницы.
1. Сохраните выходной PDF-файл.

Следующий фрагмент кода показывает, как конвертировать изображение в PDF с одинаковой высотой и шириной страницы с использованием C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertJPGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load JPEG file
        image.File = dataDir + "JPGtoPDF.jpg";
        
        // Read Height of input image
        page.PageInfo.Height = image.BitmapSize.Height;
        // Read Width of input image
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Margin.Left = 0;
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "JPGtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать JPG в PDF онлайн**

Aspose предлагает вам онлайн бесплатное приложение ["JPG в PDF"](https://products.aspose.app/pdf/conversion/jpg-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация JPG в PDF с использованием бесплатного приложения](jpg_to_pdf.png)](https://products.aspose.app/pdf/conversion/jpg-to-pdf/)
{{% /alert %}}

## Конвертировать PNG в PDF

**Aspose.PDF for .NET** поддерживает функцию конвертации изображений PNG в формат PDF. Проверьте следующий фрагмент кода для выполнения вашей задачи.

<abbr title="Portable Network Graphics">PNG</abbr> относится к типу растрового файла изображения, который использует безпотерянное сжатие, что делает его популярным среди пользователей.

Вы можете конвертировать PNG в PDF изображение, используя следующие шаги:

<a name="csharp-png-to-pdf" id="csharp-png-to-pdf"><strong>Конвертировать PNG в PDF</strong></a>

1. Загрузите входное **PNG** изображение.
2. Прочитайте значения высоты и ширины.
3. Создайте новый объект [Document](https://reference.aspose.com/page/net/aspose.page/document) и добавьте страницу.
4. Установите размеры страницы.
5. Сохраните выходной файл.

Более того, следующий фрагмент кода показывает, как конвертировать PNG в PDF с C# в ваших .NET приложениях:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertPNGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        // Load PNG file
        image.File = dataDir + "PNGtoPDF.png";
        
        // Read Height of input image
        page.PageInfo.Height = image.BitmapSize.Height;
        // Read Width of input image
        page.PageInfo.Width = image.BitmapSize.Width;
        page.PageInfo.Margin.Bottom = 0;
        page.PageInfo.Margin.Top = 0;
        page.PageInfo.Margin.Right = 0;
        page.PageInfo.Margin.Left = 0;
        page.Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "PNGtoPDF_out.pdf");
    }
}
```

{{% alert color="success" %}}
**Попробуйте конвертировать PNG в PDF онлайн**

Aspose предлагает вам онлайн бесплатное приложение ["PNG в PDF"](https://products.aspose.app/pdf/conversion/png-to-pdf/), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PNG в PDF с использованием бесплатного приложения](png_to_pdf.png)](https://products.aspose.app/pdf/conversion/png-to-pdf/)
{{% /alert %}}

## Конвертировать SVG в PDF

**Aspose.PDF for .NET** объясняет, как конвертировать изображения SVG в формат PDF и как получить размеры исходного <abbr title="Scalable Vector Graphics">SVG</abbr> файла.

Векторная графика (SVG) - это семейство спецификаций формата файла на основе XML для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается Консорциумом Всемирной паутины (W3C) с 1999 года.

Изображения SVG и их поведение определяются в текстовых файлах XML. Это означает, что их можно искать, индексировать, скриптовать, и при необходимости сжимать. Как XML-файлы, изображения SVG могут быть созданы и отредактированы с помощью любого текстового редактора, но часто удобнее создавать их с помощью графических программ, таких как Inkscape.

{{% alert color="success" %}}
**Попробуйте конвертировать формат SVG в PDF онлайн**

Aspose.PDF for .NET предлагает вам онлайн бесплатное приложение ["SVG в PDF"](https://products.aspose.app/pdf/conversion/svg-to-pdf), где вы можете попробовать исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация SVG в PDF с бесплатным приложением](svg_to_pdf.png)](https://products.aspose.app/pdf/conversion/svg-to-pdf)
{{% /alert %}}

Чтобы конвертировать файлы SVG в PDF, используйте класс под названием [SvgLoadOptions](https://reference.aspose.com/pdf/ru/net/aspose.pdf/svgloadoptions), который используется для инициализации объекта [`LoadOptions`](https://reference.aspose.com/pdf/ru/net/aspose.pdf/loadoptions). Позже этот объект передается в качестве аргумента при инициализации объекта Document и помогает движку рендеринга PDF определить входной формат исходного документа.

<a name="csharp-svg-to-pdf" id="csharp-svg-to-pdf"><strong>Конвертировать SVG в PDF</strong></a>

1. Создайте экземпляр класса [`SvgLoadOptions`](https://reference.aspose.com/pdf/ru/net/aspose.pdf/loadoptions).
2. Создайте экземпляр класса [`Document`](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document) с указанием имени исходного файла и параметров.
3. Сохраните документ с желаемым именем файла.

Следующий фрагмент кода показывает процесс конвертации файла SVG в формат PDF с помощью Aspose.PDF for .NET.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertSVGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    var option = new Aspose.Pdf.SvgLoadOptions();
    // Open SVG file 
    using (var document = new Aspose.Pdf.Document(dataDir + "SVGtoPDF.svg", option))
    {
        // Save PDF document
        document.Save(dataDir + "SVGtoPDF_out.pdf");
    }
}
```

## Получить размеры SVG

Также возможно получить размеры исходного файла SVG. Эта информация может быть полезна, если мы хотим, чтобы SVG занимал всю страницу выходного PDF. Свойство AdjustPageSize класса SvgLoadOption выполняет это требование. Значение по умолчанию для этого свойства - false. Если значение установлено в true, выходной PDF будет иметь такой же размер (размеры), как исходный SVG.

Следующий фрагмент кода показывает процесс получения размеров исходного файла SVG и генерации PDF-файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertSVGtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();

    var loadopt = new Aspose.Pdf.SvgLoadOptions();
    loadopt.AdjustPageSize = true;
    // Open SVG file
    using (var document = new Aspose.Pdf.Document(dataDir + "SVGtoPDF.svg", loadopt))
    {
        document.Pages[1].PageInfo.Margin.Top = 0;
        document.Pages[1].PageInfo.Margin.Left = 0;
        document.Pages[1].PageInfo.Margin.Bottom = 0;
        document.Pages[1].PageInfo.Margin.Right = 0;

        // Save PDF document
        document.Save(dataDir + "SVGtoPDF_out.pdf");
    }
    
}
```

### Поддерживаемые функции SVG

<table>
    <thead>
        <tr>
            <th>
                <p>SVG Тег</p>
            </th>
            <th>
                <p>Пример использования</p>
            </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>
                <p>circle</p>
            </td>
            <td>
                <code><pre>&lt circle id="r2" cx="10" cy="10" r="10" stroke="blue" stroke-width="2"&gt </pre></code>
            </td>
        </tr>
        <tr>
            <td>
                <p>defs</p>
            </td>
            <td>
                <code>&lt;defs&gt;&nbsp; <br> &lt;rect id="r1" width="15" height="15"
                    stroke="blue" stroke-width="2" /&gt;&nbsp; <br> &lt;circle id="r2"
                    cx="10" cy="10" r="10" stroke="blue" stroke-width="2"/&gt;&nbsp; <br>
                    &lt;circle id="r3" cx="10" cy="10" r="10" stroke="blue" stroke-width="3"/&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br> &lt;use
                    x="25" y="40" xlink:href="#r1" fill="red"/&gt;&nbsp; <br> &lt;use
                    x="35" y="15" xlink:href="#r2" fill="green"/&gt;&nbsp; <br> &lt;use
                    x="58" y="50" xlink:href="#r3" fill="blue"/&gt;</code>
            </td>
        </tr>
        <tr>
            <td>
                <p>tref</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text
                    id="ReferencedText"&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    Ссылаемые данные символов&nbsp; <br> &nbsp;&nbsp;&nbsp;
                    &lt;/text&gt;&nbsp; <br> &lt;/defs&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br
                        class="atl-forced-newline"> &nbsp;&nbsp;&nbsp; &lt;tref
                    xlink:href="#ReferencedText"/&gt;&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>use</p>
            </td>
            <td>
                <p>&lt;defs&gt;&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;text id="Text" x="400"
                    y="200"&nbsp; <br>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; font-family="Verdana" font-size="100"
                    text-anchor="middle" &gt;&nbsp; <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    Замаскированный текст&nbsp; <br> &nbsp;&nbsp;&nbsp; &lt;/text&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;use xlink:href="#Text" fill="blue"&nbsp; /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>ellipse&nbsp;</p>
            </td>
            <td>
                <p>&lt;ellipse cx="2.5" cy="1.5" rx="2" ry="1" fill="red" /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>g&nbsp;</p>
            </td>
            <td>
                <p>&lt;g fill="none" stroke="dimgray" stroke-width="1.5" &gt;&nbsp; <br>
                    &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7"
                    y1="-7" x2="-3" y2="-3"/&gt;&nbsp; <br> &nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="7" x2="3"
                    y2="3"/&gt;&nbsp; <br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="-7" y1="7" x2="-3" y2="3"/&gt;&nbsp;
                    <br> &nbsp;&nbsp; &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp; &nbsp;&lt;line x1="7" y1="-7" x2="3" y2="-3"/&gt;&nbsp; <br
                        class="atl-forced-newline"> &lt;/g&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>image</p>
            </td>
            <td>
                <p>&lt;image id="ShadedRelief" x="24" y="4" width="64" height="82" xlink:href="relief.jpg"
                    /&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>line</p>
            </td>
            <td>
                <p>&lt;line style="stroke:#eea;stroke-width:8" x1="10" y1="30" x2="260" y2="100"/&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>path</p>
            </td>
            <td>
                <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
                    "/&gt;&nbsp;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>style</p>
            </td>
            <td>
                <p>&lt;path style="fill:#daa;fill-rule:evenodd;stroke:red" d="M 230,150 C 290,30 10,255 110,140 z
                    "/&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>polygon</p>
            </td>
            <td>
                <p>&lt;polygon style="stroke:#24a;stroke-width:1.5;fill:#eefefe" points="10,10 180,10 10,250 10,10"
                    /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>polyline</p>
            </td>
            <td>
                <p>&lt;polyline fill="none" stroke="dimgray" stroke-width="1" points="-3,-6 3,-6 3,1 5,1 0,7 -5,1
                    -3,1 -3,-5"/&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>rect&nbsp;</p>
            </td>
            <td>
                <p>&lt;rect x="0" y="0" width="400" height="600" stroke="none" fill="aliceblue" /&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>svg</p>
            </td>
            <td>
                <p>&lt;svg xmlns="http://www.w3.org/2000/svg" version="1.1" width="10cm" height="5cm" &gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>text</p>
            </td>
            <td>
                <p>&lt;text font-family="sans-serif" fill="dimgray" font-size="22px" font-weight="bold" x="58"
                    y="30" pointer-events="none"&gt;Название карты&lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>font</p>
            </td>
            <td>
                <p>&lt;text x="10" y="100" font-size="15" fill="red" &gt;&nbsp; <br>
                    &nbsp;&nbsp;&nbsp; Пример текста&nbsp; <br> &lt;/text&gt;</p>
            </td>
        </tr>
        <tr>
            <td>
                <p>tspan</p>
            </td>
            <td>
                <p>&lt;tspan dy="25" x="25"&gt;шесть значений цвета чернил. Здесь это будет &lt;/tspan&gt;</p>
            </td>
        </tr>
    </tbody>
</table>

## Конвертировать TIFF в PDF

**Aspose.PDF** поддерживает формат файла, будь то однофреймовое или многофреймовое <abbr title="Tag Image File Format">TIFF</abbr> изображение. Это означает, что вы можете конвертировать TIFF изображение в PDF в ваших .NET приложениях.

TIFF или TIF, Tagged Image File Format, представляет собой растровые изображения, которые предназначены для использования на различных устройствах, соответствующих этому стандарту формата файла. TIFF изображение может содержать несколько кадров с разными изображениями. Формат файла Aspose.PDF также поддерживается, будь то однофреймовое или многофреймовое TIFF изображение.

Вы можете конвертировать TIFF в PDF тем же образом, что и остальные растровые графические форматы:

<a name="csharp-tiff-to-pdf" id="csharp-tiff-to-pdf"><strong>Конвертировать TIFF в PDF</strong></a>

1. Создайте новый объект класса [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document) и добавьте страницу.
2. Загрузите входное **TIFF** изображение.
3. Сохраните PDF-документ.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertTIFFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();
        var image = new Aspose.Pdf.Image();
        
        // Load sample Tiff image file
        image.File = dataDir + "TIFFtoPDF.tiff";
        document.Pages[1].Paragraphs.Add(image);
        
        // Save PDF document
        document.Save(dataDir + "TIFFtoPDF_out.pdf");
    }
}
```

В случае, если вам нужно конвертировать многостраничное TIFF изображение в многостраничный PDF документ и контролировать некоторые параметры, например, ширину или соотношение сторон, пожалуйста, выполните следующие шаги:

1. Создайте экземпляр класса Document.
1. Загрузите входное TIFF изображение.
1. Получите FrameDimension кадров.
1. Добавьте новую страницу для каждого кадра.
1. Наконец, сохраните изображения на страницах PDF.

Следующий фрагмент кода показывает, как конвертировать многостраничное или многофреймовое TIFF изображение в PDF с C#:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertTIFFtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        using (var bitmap = new System.Drawing.Bitmap(File.OpenRead(dataDir + "TIFFtoPDF.tif")))
        {
            // Convert multi page or multi frame TIFF to PDF
            var dimension = new FrameDimension(bitmap.FrameDimensionsList[0]);
            var frameCount = bitmap.GetFrameCount(dimension);

            // Iterate through each frame
            for (int frameIdx = 0; frameIdx <= frameCount - 1; frameIdx++)
            {
                var page = document.Pages.Add();

                bitmap.SelectActiveFrame(dimension, frameIdx);

                using (var currentImage = new MemoryStream())
                {
                    bitmap.Save(currentImage, ImageFormat.Tiff);

                    var imageht = new Aspose.Pdf.Image
                    {
                        ImageStream = currentImage,
                        //Apply some other options
                        //ImageScale = 0.5
                    };
                    page.Paragraphs.Add(imageht);
                }
            }
        }

        // Save PDF document
        document.Save(dataDir + "TIFFtoPDF_out.pdf");
    }
}
```

## Конвертировать CDR в PDF

<abbr title="CDR">CDR</abbr> - это формат файла, разработанный компанией Corel и в основном используемый для векторных графических изображений и рисунков. Формат файла CDR распознается большинством программ для редактирования изображений. Формат CDR является форматом по умолчанию для приложений Corel Draw.

Проверьте следующий фрагмент кода для конвертации файлов CDR в формат PDF.

<a name="csharp-cdr-to-pdf" id="csharp-cdr-to-pdf"><strong>Конвертировать CDR в PDF</strong></a>

1. Создайте экземпляр класса [CdrLoadOptions](https://reference.aspose.com/pdf/ru/net/aspose.pdf/cdrloadoptions/).
2. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document) с указанием имени исходного файла и параметров.
3. Сохраните документ с желаемым именем файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertCDRtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open CDR file
    using (var document = new Aspose.Pdf.Document(dataDir + "CDRtoPDF.cdr", new CdrLoadOptions()))
    {
        // Save PDF document
        document.Save(dataDir + "CDRtoPDF_out.pdf");
    }
}
```

## Конвертировать DJVU в PDF

<abbr title="DJVU">DjVu</abbr> - это сжатый формат изображения, разработанный компанией LizardTech. Этот формат файла был в первую очередь разработан для хранения различных типов отсканированных документов; особенно документов, содержащих комбинацию текста, изображений, индексированных цветных изображений и линейных рисунков.

Проверьте следующий фрагмент кода для конвертации файлов DJVU в формат PDF.

<a name="csharp-djvu-to-pdf" id="csharp-djvu-to-pdf"><strong>Конвертировать DJVU в PDF</strong></a>

1. Создайте экземпляр класса [DjvuLoadOptions](https://reference.aspose.com/pdf/ru/net/aspose.pdf/djvuloadoptions/).
2. Создайте экземпляр класса [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document) с указанием имени исходного файла и параметров.
3. Сохраните документ с желаемым именем файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDJVUtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    
    // Open DJVU file
    using (var document = new Aspose.Pdf.Document(dataDir + "CDRtoPDF.djvu", new DjvuLoadOptions()))
    {
        // Save PDF document
        document.Save(dataDir + "CDRtoPDF_out.pdf");
    }
}
```

## Конвертировать HEIC в PDF

<a name="csharp-heic-to-pdf" id="csharp-heic-to-pdf"><strong>Конвертировать HEIC в PDF</strong></a>

Файл HEIC - это формат файла High-Efficiency Container Image, который может хранить несколько изображений в виде коллекции в одном файле.
Для загрузки изображений heic вам необходимо добавить ссылку на пакет https://www.nuget.org/packages/FileFormat.Heic/.
Конвертируйте изображения HEIC в PDF с помощью Aspose.PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertHEICtoPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open HEIC file
    using (var fs = new FileStream(dataDir + "HEICtoPDF.heic", FileMode.Open))
    {
        var image = FileFormat.Heic.Decoder.HeicImage.Load(fs);
        var pixels = image.GetByteArray(PixelFormat.Rgb24);
        var width = (int)image.Width;
        var height = (int)image.Height;

        using (var document = new Aspose.Pdf.Document())
        {
            var page = document.Pages.Add();
            var asposeImage = new Aspose.Pdf.Image();
            asposeImage.BitmapInfo = new Aspose.Pdf.BitmapInfo(pixels, width, height, Aspose.Pdf.BitmapInfo.PixelFormat.Rgb24);
            page.PageInfo.Height = height;
            page.PageInfo.Width = width;
            page.PageInfo.Margin.Bottom = 0;
            page.PageInfo.Margin.Top = 0;
            page.PageInfo.Margin.Right = 0;
            page.PageInfo.Margin.Left = 0;

            page.Paragraphs.Add(asposeImage);

            // Save PDF document
            document.Save(dataDir + "HEICtoPDF_out.pdf");
        }
    }
}
```