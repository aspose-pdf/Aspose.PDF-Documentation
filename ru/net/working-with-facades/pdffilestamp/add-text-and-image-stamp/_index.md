---
title: Добавить текстовый и изображенческий штамп
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ru/net/add-text-and-image-stamp/
description: Этот раздел объясняет, как добавить текстовый и изображенческий штамп с помощью Aspose.PDF Facades, используя класс PdfFileStamp.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Text and Image Stamp",
    "alternativeHeadline": "Add Custom Text and Image Stamps in PDFs",
    "abstract": "Функции добавления текстового и изображенческого штампа в Aspose.PDF for .NET позволяют пользователям без усилий применять индивидуализированные текстовые и изображенческие штампы на всех или конкретных страницах PDF-документов. Эта функциональность улучшает персонализацию документов, позволяя детально контролировать атрибуты штампа, такие как позиция, поворот и качество, в конечном итоге улучшая презентацию и брендинг ваших PDF-файлов.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1435",
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
    "url": "/net/add-text-and-image-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-text-and-image-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Добавить текстовый штамп на всех страницах PDF-файла

[PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) класс позволяет вам добавлять текстовый штамп на всех страницах PDF-файла. Для того чтобы добавить текстовый штамп, вам сначала нужно создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Вам также нужно создать текстовый штамп, используя метод [BindLogo](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/stamp/methods/bindlogo) класса [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Вы также можете установить другие атрибуты, такие как начало, поворот, фон и т. д., используя объект [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Затем вы можете добавить штамп в PDF-файл, используя метод [AddStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Наконец, сохраните выходной PDF-файл, используя метод [Close](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Следующий фрагмент кода показывает, как добавить текстовый штамп на всех страницах PDF-файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));

        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnAllPages_out.pdf");
    }
}
```

## Добавить текстовый штамп на определенных страницах PDF-файла

[PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) класс позволяет вам добавлять текстовый штамп на определенных страницах PDF-файла. Для того чтобы добавить текстовый штамп, вам сначала нужно создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Вам также нужно создать текстовый штамп, используя метод [BindLogo](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/stamp/methods/bindlogo) класса [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Вы также можете установить другие атрибуты, такие как начало, поворот, фон и т. д., используя объект [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Поскольку вы хотите добавить текстовый штамп на определенные страницы PDF-файла, вам также нужно установить свойство [Pages](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/stamp/properties/pages) класса [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Это свойство требует целочисленного массива, содержащего номера страниц, на которые вы хотите добавить штамп. Затем вы можете добавить штамп в PDF-файл, используя метод [AddStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Наконец, сохраните выходной PDF-файл, используя метод [Close](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Следующий фрагмент кода показывает, как добавить текстовый штамп на определенных страницах PDF-файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTextStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindLogo(new Aspose.Pdf.Facades.FormattedText("Hello World!",
            System.Drawing.Color.Blue,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.Helvetica,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            true,
            14));
        stamp.SetOrigin(10, 400);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddTextStampOnParticularPages_out.pdf");
    }
}
```

## Добавить изображенческий штамп на всех страницах PDF-файла

[PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) класс позволяет вам добавлять изображенческий штамп на всех страницах PDF-файла. Для того чтобы добавить изображенческий штамп, вам сначала нужно создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Вам также нужно создать изображенческий штамп, используя метод [BindImage](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/stamp/methods/bindimage/index) класса [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Вы также можете установить другие атрибуты, такие как начало, поворот, фон и т. д., используя объект [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Затем вы можете добавить штамп в PDF-файл, используя метод [AddStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/page/methods/addstamp) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Наконец, сохраните выходной PDF-файл, используя метод [Close](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Следующий фрагмент кода показывает, как добавить изображенческий штамп на всех страницах PDF-файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnAllPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Set particular pages (page 2)
        stamp.Pages = new[] { 2 };

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnAllPages_out.pdf");
    }
}
```

### Контроль качества изображения при добавлении в качестве штампа

При добавлении изображения в качестве объекта штампа вы также можете контролировать качество изображения. Для выполнения этого требования свойство Quality добавлено для класса [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Оно указывает качество изображения в процентах (допустимые значения от 0 до 100).

## Добавить изображенческий штамп на определенных страницах PDF-файла

[PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) класс позволяет вам добавлять изображенческий штамп на определенных страницах PDF-файла. Для того чтобы добавить изображенческий штамп, вам сначала нужно создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Вам также нужно создать изображенческий штамп, используя метод [BindImage](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/stamp/methods/bindimage/index) класса [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Вы также можете установить другие атрибуты, такие как начало, поворот, фон и т. д., используя объект [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Поскольку вы хотите добавить изображенческий штамп на определенные страницы PDF-файла, вам также нужно установить свойство [Pages](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/stamp/properties/pages) класса [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Это свойство требует целочисленного массива, содержащего номера страниц, на которые вы хотите добавить штамп. Затем вы можете добавить штамп в PDF-файл, используя метод [AddStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/page/methods/addstamp) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Наконец, сохраните выходной PDF-файл, используя метод [Close](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Следующий фрагмент кода показывает, как добавить изображенческий штамп на определенных страницах PDF-файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddImageStampOnParticularPagesInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "sample.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        stamp.BindImage(dataDir + "StampImage.png");
        stamp.SetOrigin(10, 200);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "AddImageStampOnParticularPages_out.pdf");
    }
}
```