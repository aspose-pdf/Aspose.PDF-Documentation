---
title: Добавление изображений и текста
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/adding-images-and-text-using-pdffilemend-class/
description: В этом разделе объясняется, как добавлять изображения и текст с помощью класса PdfFileMend.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Adding Images and Text",
    "alternativeHeadline": "Enhance PDF by Adding Images and Text Precisely",
    "abstract": "Улучшите ваши PDF-документы без усилий с новым классом PdfFileMend, который позволяет добавлять изображения и текст в указанных местах существующих PDF. Используйте интуитивно понятные методы AddImage и AddText для интеграции различных форматов изображений и форматированного текста, обеспечивая точность в размещении и выборе страниц. Упростите свои задачи по манипуляции PDF с возможностью настраивать наложения изображений и обтекание текста, делая ваши документы визуально привлекательными и информативными.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1324",
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
    "url": "/net/adding-images-and-text-using-pdffilemend-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/adding-images-and-text-using-pdffilemend-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

[PdfFileMend](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilemend) класс может помочь вам добавить изображения и текст в существующий PDF-документ в указанном месте. Он предоставляет два метода с названиями [AddImage](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) и [AddText](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilemend/methods/addtext/index). Метод [AddImage](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) позволяет добавлять изображения форматов JPG, GIF, PNG и BMP. Метод [AddText](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilemend/methods/addtext/index) принимает аргумент типа [FormattedText](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formattedtext) и добавляет его в существующий PDF-файл. Изображения и текст могут быть добавлены в прямоугольную область, заданную координатами нижнего левого и верхнего правого углов. При добавлении изображений вы можете указать либо путь к файлу изображения, либо поток файла изображения. Чтобы указать номер страницы, на которую нужно добавить изображение или текст, оба этих метода предоставляют аргумент номера страницы. Таким образом, вы можете не только добавлять изображения и текст в указанном месте, но и на указанной странице.

Изображения являются важной частью содержания PDF-документа. Манипуляция изображениями в существующем PDF-файле является распространенной задачей для людей, работающих с PDF-файлами. В этой статье мы рассмотрим, как можно манипулировать изображениями в существующем PDF-файле с помощью [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades) класса [Aspose.PDF for .NET](/pdf/ru/net/). Все операции, связанные с изображениями, в пространстве имен [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades), были собраны в этой статье.

## Подробности реализации

[Пространство имен Aspose.Pdf.Facades](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades) позволяет добавлять новые изображения в существующий PDF-файл. Вы также можете заменить или удалить существующее изображение. PDF-файл также может быть преобразован в изображения. Вы можете либо преобразовать каждую отдельную страницу в одно изображение, либо весь PDF-файл в одно изображение. Он поддерживает форматы, такие как JPEG, BMP, PNG и TIFF и т.д. Вы также можете извлекать изображения из PDF-файла. Вы можете использовать четыре класса из [пространства имен Aspose.Pdf.Facades](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades) для выполнения этих операций, а именно [PdfFileMend](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilemend), [PdfContentEditor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfcontenteditor), [PdfExtractor](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfextractor) и [PdfConverter](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfconverter).

## Операции с изображениями

В этом разделе мы подробно рассмотрим эти операции с изображениями. Мы также увидим фрагменты кода, чтобы показать использование связанных классов и методов. Прежде всего, давайте посмотрим, как добавить изображение в существующий PDF-файл. Мы можем использовать метод [AddImage](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilemend/methods/addimage/index) класса [PdfFileMend](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilemend) для добавления нового изображения. С помощью этого метода вы можете не только указать номер страницы, на которую хотите добавить изображение, но и указать местоположение изображения.

## Добавить изображение в существующий PDF-файл (Facades)

Вы можете использовать метод [AddImage](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilemend/methods/addimage) класса [PdfFileMend](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilemend). Метод [AddImage](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilemend/methods/addimage) требует изображение для добавления, номер страницы, на которую нужно добавить изображение, и информацию о координатах. После этого сохраните обновленный PDF-файл, используя метод [Close](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdfcontenteditor/methods/close).

В следующем примере мы добавляем изображение на страницу, используя imageStream:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images(); 

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                // Add image to first page
                mender.AddImage(imageStream, 1, 10, 650, 110, 750);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![Добавить изображение](/pdf/ru/net/images/add_image1.png)

С помощью [CompositingParameters](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.pdffilemend/addimage/methods/1) мы можем наложить одно изображение на другое:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PDF document and PdfFileMend objects
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters for the image
                var compositingParameters = new Aspose.Pdf.CompositingParameters(Aspose.Pdf.BlendMode.Multiply);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

![Добавить изображение](/pdf/ru/net/images/add_image2.png)

Существует несколько способов сохранить изображение в PDF-файле. Мы продемонстрируем один из них в следующем примере:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Exclusion and ImageFilterType.Flate
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Exclusion,
                    Aspose.Pdf.ImageFilterType.Flate);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_out.pdf");
            }
        }
    }
}
```

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImage04()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Load image into stream
            using (var imageStream = File.OpenRead(dataDir + "AddImage.png"))
            {
                // Bind PDF document
                mender.BindPdf(document);

                int pageNum = 1;
                int lowerLeftX = 10;
                int lowerLeftY = 650;
                int upperRightX = 110;
                int upperRightY = 750;

                // Use compositing parameters with BlendMode.Multiply, ImageFilterType.Flate and false
                var compositingParameters = new Aspose.Pdf.CompositingParameters(
                    Aspose.Pdf.BlendMode.Multiply,
                    Aspose.Pdf.ImageFilterType.Flate,
                    false);

                mender.AddImage(imageStream, pageNum, lowerLeftX, lowerLeftY, upperRightX, upperRightY, compositingParameters);

                // Save PDF document
                mender.Save(dataDir + "AddImage_outp.pdf");
            }
        }
    }
}
```

## Добавить текст в существующий PDF-файл (facades)

Мы можем добавлять текст несколькими способами. Рассмотрим первый. Мы берем [FormattedText](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formattedtext) и добавляем его на страницу. Затем мы указываем координаты нижнего левого угла, а затем добавляем наш текст на страницу.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText01()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

        // Add text to the first page at position (10, 750)
        mender.AddText(message, 1, 10, 750);

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

Проверьте, как это выглядит:

![Добавить текст](/pdf/ru/net/images/add_text.png)

Второй способ добавить [FormattedText](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formattedtext). Кроме того, мы указываем прямоугольник, в который должен поместиться наш текст.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText02()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileMend object
    using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
    {
        // Bind PDF document
        mender.BindPdf(dataDir + "AddImage.pdf");

        // Create formatted text
        var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose! Welcome to Aspose!");

        // Add text to the first page at the specified position with wrapping
        mender.AddText(message, 1, 10, 700, 55, 810);

        // Set word wrapping mode to wrap by words
        mender.WrapMode = Aspose.Pdf.Facades.WordWrapMode.ByWords;

        // Save PDF document
        mender.Save(dataDir + "AddText_out.pdf");
    }
}
```

Третий пример предоставляет возможность добавлять текст на указанные страницы. В нашем примере давайте добавим заголовок на страницы 1 и 3 документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddText03()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "AddImage.pdf"))
    {
        document.Pages.Add();
        document.Pages.Add();
        document.Pages.Add();

        // Create PdfFileMend object
        using (var mender = new Aspose.Pdf.Facades.PdfFileMend())
        {
            // Bind PDF document
            mender.BindPdf(document);

            // Create formatted text
            var message = new Aspose.Pdf.Facades.FormattedText("Welcome to Aspose!");

            // Specify the pages where text should be added
            int[] pageNums = new int[] { 1, 3 };

            // Add text to the specified pages at the specified coordinates
            mender.AddText(message, pageNums, 10, 750, 310, 760);

            // Save PDF document
            mender.Save(dataDir + "AddText_out.pdf");
        }
    }
}
```