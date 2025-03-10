---
title: Извлечение изображений с помощью PdfExtractor
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/extract-images/
description: Этот раздел объясняет, как извлекать изображения с помощью Aspose.PDF Facades, используя класс PdfExtractor.
lastmod: "2021-07-15"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Images using PdfExtractor",
    "alternativeHeadline": "Extract Images from PDF with PdfExtractor Class",
    "abstract": "Функция PdfExtractor от Aspose.PDF позволяет пользователям эффективно извлекать изображения из PDF-документов, предлагая несколько вариантов, таких как извлечение изображений из всего документа, определенных страниц или заданных диапазонов. Она поддерживает сохранение изображений непосредственно в файлы или потоки памяти, что повышает гибкость для разработчиков, работающих с PDF-ресурсами. Эта мощная функциональность позволяет точно контролировать режимы извлечения изображений, упрощая работу с различными типами содержимого PDF.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1789",
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
    "url": "/net/extract-images/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-images/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Извлечение изображений из всего PDF в файлы (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) класс позволяет извлекать изображения из PDF-файла. Прежде всего, вам нужно создать объект класса [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) и связать входной PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). После этого вызовите метод [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage), чтобы извлечь все изображения в память. После извлечения изображений вы можете получить эти изображения с помощью методов [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) и [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Вам нужно пройтись по всем извлеченным изображениям с помощью цикла while. Чтобы сохранить изображения на диск, вы можете вызвать перегрузку метода [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1), который принимает путь к файлу в качестве аргумента. Следующий фрагмент кода показывает, как извлечь изображения из всего PDF в файлы.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract all the images
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg");
        }
    }
}
```

## Извлечение изображений из всего PDF в потоки (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) класс позволяет извлекать изображения из PDF-файла в потоки. Прежде всего, вам нужно создать объект класса [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) и связать входной PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). После этого вызовите метод [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage), чтобы извлечь все изображения в память. После извлечения изображений вы можете получить эти изображения с помощью методов [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) и [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Вам нужно пройтись по всем извлеченным изображениям с помощью цикла while. Чтобы сохранить изображения в поток, вы можете вызвать перегрузку метода [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1), который принимает Stream в качестве аргумента. Следующий фрагмент кода показывает, как извлечь изображения из всего PDF в потоки.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesWholePDFStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Extract images
        extractor.ExtractImage();
        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Извлечение изображений с определенной страницы PDF (Facades)

Вы можете извлекать изображения с определенной страницы PDF-файла. Для этого вам нужно установить свойства [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) и [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) на конкретную страницу, с которой вы хотите извлечь изображения. Прежде всего, вам нужно создать объект класса [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) и связать входной PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Во-вторых, вам нужно установить свойства [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) и [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage). После этого вызовите метод [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage), чтобы извлечь все изображения в память. После извлечения изображений вы можете получить эти изображения с помощью методов [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) и [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Вам нужно пройтись по всем извлеченным изображениям с помощью цикла while. Вы можете сохранить изображения на диск или в поток. Вам нужно просто вызвать соответствующую перегрузку метода [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Следующий фрагмент кода показывает, как извлечь изображения с определенной страницы PDF в потоки.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesParticularPage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();
        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Извлечение изображений из диапазона страниц PDF (Facades)

Вы можете извлекать изображения из диапазона страниц PDF-файла. Для этого вам нужно установить свойства [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) и [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage) на диапазон страниц, из которого вы хотите извлечь изображения. Прежде всего, вам нужно создать объект класса [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) и связать входной PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Во-вторых, вам нужно установить свойства [StartPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/startpage) и [EndPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/endpage). После этого вызовите метод [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage), чтобы извлечь все изображения в память. После извлечения изображений вы можете получить эти изображения с помощью методов [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) и [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Вам нужно пройтись по всем извлеченным изображениям с помощью цикла while. Вы можете сохранить изображения на диск или в поток. Вам нужно просто вызвать соответствующую перегрузку метода [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Следующий фрагмент кода показывает, как извлечь изображения из диапазона страниц PDF в потоки.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesRangePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open input PDF
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Set StartPage and EndPage properties to the page number to
        // You want to extract images from
        extractor.StartPage = 2;
        extractor.EndPage = 2;

        // Extract images
        extractor.ExtractImage();

        // Get extracted images
        while (extractor.HasNextImage())
        {
            // Read image into memory stream
            MemoryStream memoryStream = new MemoryStream();
            extractor.GetNextImage(memoryStream);

            // Write to disk, if you like, or use it otherwise
            using (FileStream fileStream = new
            FileStream(dataDir + DateTime.Now.Ticks.ToString() + "_out.jpg", FileMode.Create))
            {
                memoryStream.WriteTo(fileStream);
            }
        }
    }
}
```

## Извлечение изображений с использованием режима извлечения изображений (Facades)

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) класс позволяет извлекать изображения из PDF-файла. Aspose.PDF поддерживает два режима извлечения; первый - ActuallyUsedImage, который извлекает изображения, фактически используемые в PDF-документе. Второй режим - [DefinedInResources](https://reference.aspose.com/pdf/net/aspose.pdf/extractimagemode), который извлекает изображения, определенные в ресурсах PDF-документа (режим извлечения по умолчанию). Сначала вам нужно создать объект класса [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) и связать входной PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). После этого укажите режим извлечения изображений с помощью свойства [PdfExtractor.ExtractImageMode](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/properties/extractimagemode). Затем вызовите метод [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extractimage), чтобы извлечь все изображения в память в зависимости от указанного вами режима. После извлечения изображений вы можете получить эти изображения с помощью методов [HasNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextimage) и [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1). Вам нужно пройтись по всем извлеченным изображениям с помощью цикла while. Чтобы сохранить изображения на диск, вы можете вызвать перегрузку метода [GetNextImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfextractor/getnextimage/methods/1), который принимает путь к файлу в качестве аргумента.

Следующий фрагмент кода показывает, как извлечь изображения из PDF-файла, используя опцию ExtractImageMode.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesImageExtractionMode()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "sample_cats_dogs.pdf");

        // Specify Image Extraction Mode
        //extractor.ExtractImageMode = ExtractImageMode.ActuallyUsed;
        extractor.ExtractImageMode = Aspose.Pdf.ExtractImageMode.DefinedInResources;

        // Extract Images based on Image Extraction Mode
        extractor.ExtractImage();

        // Get all the extracted images
        while (extractor.HasNextImage())
        {
            extractor.GetNextImage(dataDir + DateTime.Now.Ticks.ToString() + "_out.png", System.Drawing.Imaging.ImageFormat.Png);
        }
    }
}
```

Для проверки, содержит ли PDF текст или изображения, используйте следующий фрагмент кода:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CheckIfPdfContainsTextOrImages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Instantiate a memoryStream object to hold the extracted text from Document
    MemoryStream ms = new MemoryStream();
    // Instantiate PdfExtractor object
    using (var extractor = new Aspose.Pdf.Facades.PdfExtractor())
    {
        // Bind PDF document
        extractor.BindPdf(dataDir + "FilledForm.pdf");
        // Extract text from the input PDF document
        extractor.ExtractText();
        // Save the extracted text to a text file
        extractor.GetText(ms);
        // Check if the MemoryStream length is greater than or equal to 1

        bool containsText = ms.Length >= 1;

        // Extract images from the input PDF document
        extractor.ExtractImage();

        // Calling HasNextImage method in while loop. When images will finish, loop will exit
        bool containsImage = extractor.HasNextImage();

        // Now find out whether this PDF is text only or image only

        if (containsText && !containsImage)
        {
            Console.WriteLine("PDF contains text only");
        }
        else if (!containsText && containsImage)
        {
            Console.WriteLine("PDF contains image only");
        }
        else if (containsText && containsImage)
        {
            Console.WriteLine("PDF contains both text and image");
        }
        else if (!containsText && !containsImage)
        {
            Console.WriteLine("PDF contains neither text or nor image");
        }
    }
}
```