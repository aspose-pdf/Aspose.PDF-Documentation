---
title: Оптимизация, сжатие или уменьшение размера PDF в C#
linktitle: Оптимизация PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /ru/net/optimize-pdf/
description: Оптимизация PDF файла, сжатие всех изображений, уменьшение размера PDF, извлечение шрифтов, удаление неиспользуемых объектов с помощью C#.
lastmod: "2022-02-17"
sitemap:
changefreq: "monthly"
priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Optimize, Compress or Reduce PDF Size in C#",
    "alternativeHeadline": "Optimize PDF Files Efficiently with C#",
    "abstract": "Новая функция оптимизации PDF в C# позволяет разработчикам значительно уменьшать размеры PDF файлов, используя несколько стратегий, таких как сжатие изображений, извлечение шрифтов и удаление неиспользуемых объектов. Это улучшение повышает эффективность для веб-публикации, обмена по электронной почте и хранения, предоставляя эффективное решение для управления большими PDF документами.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "optimize pdf, compress pdf size, reduce pdf size, optimize pdf c#, unembed fonts, remove unused objects, shrink images, optimization methods, pdf document generation, Aspose.PDF",
    "wordcount": "2628",
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
    "url": "/net/optimize-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/optimize-pdf/"
    },
    "dateModified": "2025-04-01",
    "description": "Оптимизация PDF файла, сжатие всех изображений, уменьшение размера PDF, извлечение шрифтов, удаление неиспользуемых объектов с помощью C#."
}
</script>

PDF документ иногда может содержать дополнительные данные. Уменьшение размера PDF файла поможет вам оптимизировать сетевую передачу и хранение. Это особенно удобно для публикации на веб-страницах, обмена в социальных сетях, отправки по электронной почте или архивирования в хранилище. Мы можем использовать несколько техник для оптимизации PDF:

- Оптимизация содержимого страниц для онлайн-просмотра.
- Сжатие или уменьшение всех изображений.
- Включение повторного использования содержимого страниц.
- Объединение дублирующихся потоков.
- Извлечение шрифтов.
- Удаление неиспользуемых объектов.
- Удаление полей формы.
- Удаление или упрощение аннотаций.

{{% alert color="primary" %}}

Подробное объяснение методов оптимизации можно найти на странице Обзор методов оптимизации.

{{% /alert %}}

## Оптимизация PDF документа для веба

Оптимизация, или линейзация для веба, относится к процессу подготовки PDF файла для онлайн-просмотра с использованием веб-браузера. Чтобы оптимизировать файл для веб-отображения:

1. Откройте входной документ в объекте [Document](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document).
1. Используйте метод [Optimize](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/methods/optimize).
1. Сохраните оптимизированный документ с помощью метода [Save](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/methods/save).

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

Следующий фрагмент кода показывает, как оптимизировать PDF документ для веба.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Optimize for web
        document.Optimize();

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

## Уменьшение размера PDF

Метод [OptimizeResources()](https://reference.aspose.com/pdf/ru/net/aspose.pdf/document/methods/optimizeresources) позволяет уменьшить размер документа, устраняя ненужную информацию. По умолчанию этот метод работает следующим образом:

- Ресурсы, которые не используются на страницах документа, удаляются.
- Равные ресурсы объединяются в один объект.
- Неиспользуемые объекты удаляются.

Ниже приведен пример. Однако обратите внимание, что этот метод не может гарантировать уменьшение документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ShrinkDocument.pdf"))
    {
        // Optimize PDF document. Note, though, that this method cannot guarantee document shrinking
        document.OptimizeResources();

        // Save PDF document
        document.Save(dataDir + "ShrinkDocument_out.pdf");
    }
}
```

## Управление стратегией оптимизации

Мы также можем настроить стратегию оптимизации. В настоящее время метод [OptimizeResources()](https://reference.aspose.com/pdf/ru/net/aspose.pdf.document/optimizeresources/methods/1) использует 5 техник. Эти техники могут быть применены с помощью метода OptimizeResources() с параметром [OptimizationOptions](https://reference.aspose.com/pdf/ru/net/aspose.pdf.optimization/optimizationoptions).

### Уменьшение или сжатие всех изображений

У нас есть два способа работы с изображениями: уменьшение качества изображения и/или изменение их разрешения. В любом случае следует применять [ImageCompressionOptions](https://reference.aspose.com/pdf/ru/net/aspose.pdf.optimization/imagecompressionoptions). В следующем примере мы уменьшаем изображения, снижая [ImageQuality](https://reference.aspose.com/pdf/ru/net/aspose.pdf.optimization/imagecompressionoptions/properties/imagequality) до 50.

`ImageQuality` работает аналогично качеству JPEG, где значение 0 - это наименьшее, а значение 100 - наибольшее.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ShrinkImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 50;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "Shrinkimage_out.pdf");
    }
}
```

Другой способ - изменить размер изображений с более низким разрешением. В этом случае мы должны установить ResizeImages в true и MaxResolution в соответствующее значение.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ResizeImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ResizeImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set ResizeImage option
        // If this flag set to true and CompressImages is true images will be resized if image resolution is greater then specified MaxResolution parameter
        optimizeOptions.ImageCompressionOptions.ResizeImages = true;

        // Set MaxResolution option
        // Specifies maximum resolution of images. If image has higher resolition it will be scaled
        optimizeOptions.ImageCompressionOptions.MaxResolution = 300;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "ResizeImages_out.pdf");
    }
}
```

Еще одной важной проблемой является время выполнения. Но снова мы можем управлять этой настройкой. В настоящее время мы можем использовать два алгоритма - Стандартный и Быстрый. Чтобы контролировать время выполнения, мы должны установить свойство [Version](https://reference.aspose.com/pdf/ru/net/aspose.pdf.optimization/imagecompressionoptions/properties/version). Следующий фрагмент демонстрирует быстрый алгоритм:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FastShrinkImages()
{
    // Initialize Time
    var time = DateTime.Now.Ticks;

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "Shrinkimage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // Set CompressImages option
        // If this flag is set to true images will be compressed in the document
        optimizeOptions.ImageCompressionOptions.CompressImages = true;

        // Set ImageQuality option
        // Specifies level of image compression when CompressImages flag is used
        optimizeOptions.ImageCompressionOptions.ImageQuality = 75;

        // Set Image Compression Version to fast
        // Version of compression algorithm. Possible values are:
        // 1. standard compression
        // 2. fast (improved compression which is faster then standard but may be applicable not for all images)
        // 3. mixed (standard compression is applied to images which can not be compressed by faster algorithm, 
        // this may give best compression but more slow then "fast" algorithm. Version "Fast" is not applicable for 
        // resizing images (standard method will be used). Default is "Standard"
        optimizeOptions.ImageCompressionOptions.Version = Aspose.Pdf.Optimization.ImageCompressionVersion.Fast;

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "FastShrinkImages_out.pdf");
    }

    // Output the time taken for the operation
    Console.WriteLine("Ticks: {0}", DateTime.Now.Ticks - time);
}
```

### Удаление неиспользуемых объектов

PDF документ иногда содержит объекты PDF, которые не ссылаются ни на какой другой объект в документе. Это может произойти, например, когда страница удаляется из дерева страниц документа, но сам объект страницы не удаляется. Удаление этих объектов не делает документ недействительным, а скорее уменьшает его размер.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedObject option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedObjects = true
        };
        
        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### Удаление неиспользуемых потоков

Иногда документ содержит неиспользуемые потоки ресурсов. Эти потоки не являются "неиспользуемыми объектами", потому что они ссылаются из словаря ресурсов страницы. Таким образом, они не удаляются с помощью метода "удалить неиспользуемые объекты". Но эти потоки никогда не используются с содержимым страницы. Это может произойти в случаях, когда изображение было удалено со страницы, но не из ресурсов страницы. Также эта ситуация часто возникает, когда страницы извлекаются из документа, и страницы документа имеют "общие" ресурсы, то есть один и тот же объект Resources. Содержимое страниц анализируется, чтобы определить, используется ли поток ресурса или нет. Неиспользуемые потоки удаляются. Это иногда уменьшает размер документа. Использование этой техники похоже на предыдущий шаг:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set RemoveUsedStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            RemoveUnusedStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### Связывание дублирующих потоков

Некоторые документы могут содержать несколько идентичных потоков ресурсов (например, изображения). Это может произойти, скажем, когда документ конкатенируется сам с собой. Выходной документ содержит две независимые копии одного и того же потока ресурса. Мы анализируем все потоки ресурсов и сравниваем их. Если потоки дублируются, они объединяются, то есть остается только одна копия. Ссылки изменяются соответствующим образом, и копии объекта удаляются. В некоторых случаях это помогает уменьшить размер документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithLinkDuplicateStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set LinkDuplicateStreams option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            LinkDuplicateStreams = true
        };

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

Кроме того, мы можем использовать настройки [AllowReusePageContent](https://reference.aspose.com/pdf/ru/net/aspose.pdf.optimization/optimizationoptions/properties/allowreusepagecontent). Если это свойство установлено в true, содержимое страницы будет повторно использоваться при оптимизации документа для идентичных страниц.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithReusePageContent()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set AllowReusePageContent option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            AllowReusePageContent = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }

    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

### Извлечение шрифтов

Если документ использует встроенные шрифты, это означает, что все данные шрифта хранятся в документе. Преимущество заключается в том, что документ можно просматривать независимо от того, установлен шрифт на машине пользователя или нет. Но встраивание шрифтов увеличивает размер документа. Метод извлечения шрифтов удаляет все встроенные шрифты. Таким образом, размер документа уменьшается, но сам документ может стать нечитаемым, если правильный шрифт не установлен.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizePdfDocumentWithUnembedFonts()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Set UnembedFonts option
        var optimizeOptions = new Aspose.Pdf.Optimization.OptimizationOptions
        {
            UnembedFonts = true
        };

        Console.WriteLine("Start");

        // Optimize PDF document using OptimizationOptions
        document.OptimizeResources(optimizeOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");	
    }
	
    Console.WriteLine("Finished");

    // Calculate and display file sizes
    var fi1 = new FileInfo(dataDir + "OptimizeDocument.pdf");
    var fi2 = new FileInfo(dataDir + "OptimizeDocument_out.pdf");
    Console.WriteLine("Original file size: {0}. Reduced file size: {1}", fi1.Length, fi2.Length);
}
```

Ресурсы оптимизации применяют эти методы к документу. Если какой-либо из этих методов применяется, размер документа, скорее всего, уменьшится. Если ни один из этих методов не применяется, размер документа не изменится, что очевидно.

## Дополнительные способы уменьшения размера PDF документа

### Удаление или упрощение аннотаций

Аннотации могут быть удалены, когда они не нужны. Когда они нужны, но не требуют дополнительного редактирования, их можно упростить. Оба этих метода уменьшат размер файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationsInPdfDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "OptimizeDocument.pdf"))
    {
        // Flatten annotations
        foreach (var page in document.Pages)
        {
            foreach (var annotation in page.Annotations)
            {
                annotation.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "OptimizeDocument_out.pdf");
    }
}
```

### Удаление полей формы

Если PDF документ содержит AcroForms, мы можем попытаться уменьшить размер файла, упрощая поля формы.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenPdfForms()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load source PDF form
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Flatten Forms
        if (document.Form.Fields.Lenght > 0)
        {
            foreach (var item in document.Form.Fields)
            {
                item.Flatten();
            }
        }

        // Save PDF document
        document.Save(dataDir + "FlattenForms_out.pdf");
    }
}
```

### Конвертация PDF из цветового пространства RGB в градации серого

PDF файл состоит из текста, изображений, вложений, аннотаций, графиков и других объектов. Вы можете столкнуться с необходимостью конвертировать PDF из цветового пространства RGB в градации серого, чтобы он быстрее печатался. Также, когда файл конвертируется в градации серого, размер документа также уменьшается, но это может также привести к снижению качества документа. Эта функция в настоящее время поддерживается функцией Pre-Flight Adobe Acrobat, но когда речь идет об автоматизации Office, Aspose.PDF является идеальным решением для предоставления таких возможностей для манипуляций с документами. Для выполнения этого требования можно использовать следующий фрагмент кода.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertRgbToGrayScale()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create RGB to DeviceGray conversion strategy
        var strategy = new Aspose.Pdf.RgbToDeviceGrayConversionStrategy();

        // Iterate through each page
        for (int idxPage = 1; idxPage <= document.Pages.Count; idxPage++)
        {
            // Get instance of particular page inside PDF
            var page = document.Pages[idxPage];

            // Convert the RGB colorspace image to GrayScale colorspace
            strategy.Convert(page);
        }

        // Save PDF document
        document.Save(dataDir + "TestGray_out.pdf");
    }
}
```

### Сжатие FlateDecode

{{% alert color="primary" %}}

Эта функция поддерживается версией 18.12 или выше.

{{% /alert %}}

Aspose.PDF for .NET предоставляет поддержку сжатия FlateDecode для функциональности оптимизации PDF. Следующий фрагмент кода показывает, как использовать эту опцию в оптимизации для хранения изображений с **FlateDecode** сжатием:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void OptimizeDocumentImagesWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        // Initialize OptimizationOptions
        var optimizationOptions = new Aspose.Pdf.Optimization.OptimizationOptions();

        // To optimize images using FlateDecode compression, set optimization options to Flate
        optimizationOptions.ImageCompressionOptions.Encoding = Aspose.Pdf.Optimization.ImageEncoding.Flate;

        // Set optimization options
        document.OptimizeResources(optimizationOptions);

        // Save PDF document
        document.Save(dataDir + "OptimizeDocumentImagesWithFlateCompression_out.pdf");
    }
}
```

### Хранение изображения в XImageCollection

Aspose.PDF for .NET предоставляет возможность хранить новые изображения в **XImageCollection** с сжатием FlateDecode. Чтобы включить эту опцию, вы можете использовать флаг **ImageFilterType.Flate**. Следующий фрагмент кода показывает, как использовать эту функциональность:

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageToPdfWithFlateCompression()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();

        // Open the image file stream
        using (var imageStream = new FileStream(dataDir + "aspose-logo.jpg", FileMode.Open))
        {
            // Add the image to the page resources with Flate compression
            page.Resources.Images.Add(imageStream, Aspose.Pdf.ImageFilterType.Flate);
        }

        // Get the added image
        var ximage = page.Resources.Images[page.Resources.Images.Count];

        // Save the current graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GSave());

        // Set coordinates for the image placement
        int lowerLeftX = 0;
        int lowerLeftY = 0;
        int upperRightX = 600;
        int upperRightY = 600;

        var rectangle = new Aspose.Pdf.Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        var matrix = new Aspose.Pdf.Matrix(new double[]
        {
            rectangle.URX - rectangle.LLX, 0, 0, rectangle.URY - rectangle.LLY, rectangle.LLX, rectangle.LLY
        });

        // Use ConcatenateMatrix operator to define how the image must be placed
        page.Contents.Add(new Aspose.Pdf.Operators.ConcatenateMatrix(matrix));
        page.Contents.Add(new Aspose.Pdf.Operators.Do(ximage.Name));

        // Restore the graphics state
        page.Contents.Add(new Aspose.Pdf.Operators.GRestore());

        // Save the document
        document.Save(dataDir + "AddImageToPdfWithFlateCompression_out.pdf");
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>