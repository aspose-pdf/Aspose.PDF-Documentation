---
title: Добавить штамп страницы PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ru/net/add-pdf-page-stamp/
description: Узнайте, как добавлять штампы на страницы PDF в .NET, включая текст и изображения, для водяных знаков или брендинга с использованием Aspose.PDF.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add PDF Page Stamp",
    "alternativeHeadline": "Enhance PDFs with Custom Stamps and Page Numbers",
    "abstract": "Представляем функцию штампа страницы PDF, которая позволяет пользователям без труда добавлять настраиваемые штампы на все или определенные страницы PDF-документа с помощью класса PdfFileStamp. Эта функциональность улучшает персонализацию документа, позволяя использовать различные атрибуты, такие как поворот, фон и стили пользовательской нумерации для штампов страниц, делая ваши PDF-файлы не только уникальными, но и профессионально оформленными.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1309",
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
    "url": "/net/add-pdf-page-stamp/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-pdf-page-stamp/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для продвинутых пользователей и разработчиков."
}
</script>

## Добавить штамп страницы PDF на всех страницах PDF-файла

[PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) класс позволяет добавлять штамп страницы PDF на всех страницах PDF-файла. Для добавления штампа страницы PDF вам сначала нужно создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Вам также нужно создать штамп страницы PDF с помощью метода [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) класса [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Вы также можете установить другие атрибуты, такие как происхождение, поворот, фон и т. д., используя объект [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Затем вы можете добавить штамп в PDF-файл, используя метод [AddStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Наконец, сохраните выходной PDF-файл, используя метод [Close](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Следующий фрагмент кода показывает, как добавить штамп страницы PDF на всех страницах PDF-файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnAllPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "AddPageStampOnAllPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnAllPages_out.pdf");
    }
}
```

## Добавить штамп страницы PDF на определенных страницах PDF-файла

[PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) класс позволяет добавлять штамп страницы PDF на определенных страницах PDF-файла. Для добавления штампа страницы PDF вам сначала нужно создать объекты классов [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) и [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Вам также нужно создать штамп страницы PDF, используя метод [BindPdf](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.facade/bindpdf/methods/3) класса [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Вы можете установить другие атрибуты, такие как происхождение, поворот, фон и т. д., используя объект [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Поскольку вы хотите добавить штамп страницы PDF на определенных страницах PDF-файла, вам также нужно установить свойство [Pages](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/stamp/properties/pages) класса [Stamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf/stamp). Это свойство требует целочисленного массива, содержащего номера страниц, на которых вы хотите добавить штамп. Затем вы можете добавить штамп в PDF-файл, используя метод [AddStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Наконец, сохраните выходной PDF-файл, используя метод [Close](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Следующий фрагмент кода показывает, как добавить штамп страницы PDF на определенных страницах PDF-файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageStampOnCertainPages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "SourcePDF.pdf");

        // Create stamp
        var stamp = new Aspose.Pdf.Facades.Stamp();
        // Bind PDF document
        stamp.BindPdf(dataDir + "PageStampOnCertainPages.pdf", 1);
        stamp.SetOrigin(20, 20);
        stamp.Rotation = 90.0F;
        stamp.IsBackground = true;
        stamp.Pages = new[] { 1, 3 };  // Apply stamp to specific pages (1 and 3)

        // Add stamp to PDF file
        fileStamp.AddStamp(stamp);

        // Save PDF document
        fileStamp.Save(dataDir + "PageStampOnCertainPages_out.pdf");
    }
}
```

## Добавить номер страницы в PDF-файл

[PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp) класс позволяет добавлять номера страниц в PDF-файл. Для добавления номеров страниц вам сначала нужно создать объект класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Если вы хотите показать номер страницы в формате "Страница X из N", где X - это текущий номер страницы, а N - общее количество страниц в PDF-файле, то вам сначала нужно получить количество страниц с помощью свойства [NumberOfpages](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) класса [PdfFileInfo](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffileinfo). Чтобы получить текущий номер страницы, вы можете использовать знак **#** в вашем тексте в любом месте, где вам нравится. Вы можете отформатировать текст номера страницы, используя класс [FormattedText](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/formattedtext). Если вы хотите начать нумерацию страниц с определенного числа, вы можете установить свойство [StartingNumber](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber). Когда вы будете готовы добавить номер страницы в файл, вам нужно вызвать метод [AddPageNumber](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Наконец, сохраните выходной PDF-файл, используя метод [Close](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/facade/methods/close) класса [PdfFileStamp](https://reference.aspose.com/pdf/ru/net/aspose.pdf.facades/pdffilestamp). Следующий фрагмент кода показывает, как добавить номер страницы в PDF-файл.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;
        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```

### Пользовательский стиль нумерации

Класс PdfFileStamp предлагает возможность добавлять информацию о номере страницы в качестве объекта штампа внутри PDF-документа. До этого релиза класс поддерживал только стиль нумерации 1,2,3,4. Однако некоторые клиенты потребовали использовать пользовательский стиль нумерации при размещении штампа номера страницы внутри PDF-документа. Для выполнения этого требования было введено свойство [NumberingStyle](https://reference.aspose.com/pdf/ru/net/aspose.pdf/numberingstyle), которое принимает значения из перечисления [NumberingStyle](https://reference.aspose.com/pdf/ru/net/aspose.pdf/numberingstyle). Ниже указаны значения, предлагаемые в этом перечислении.

- Буквы строчные.
- Буквы прописные.
- Арабские цифры.
- Римские цифры строчные.
- Римские цифры прописные.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddCustomPageNumberInPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Create PdfFileStamp object
    using (var fileStamp = new Aspose.Pdf.Facades.PdfFileStamp())
    {
        // Bind PDF document
        fileStamp.BindPdf(dataDir + "StampPDF.pdf");

        // Get total number of pages
        int totalPages = new Aspose.Pdf.Facades.PdfFileInfo(dataDir + "StampPDF.pdf").NumberOfPages;

        // Create formatted text for page number
        var formattedText = new Aspose.Pdf.Facades.FormattedText($"Page # of {totalPages}",
            System.Drawing.Color.AntiqueWhite,
            System.Drawing.Color.Gray,
            Aspose.Pdf.Facades.FontStyle.TimesBoldItalic,
            Aspose.Pdf.Facades.EncodingType.Winansi,
            false, 12);

        // Specify numbering style as Numerals Roman UpperCase
        fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

        // Set starting number for first page; you might want to start from 2 or more
        fileStamp.StartingNumber = 1;

        // Add page number in upper right corner
        fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

        // Save PDF document
        fileStamp.Save(dataDir + "AddCustomPageNumber_out.pdf");
    }
}

// Add PDF Page Numbers
public enum PageNumPosition
{
    PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
}
```