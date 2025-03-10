---
title: Получение и установка свойств страниц
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
url: /ru/net/get-and-set-page-properties/
description: Узнайте, как получать и устанавливать свойства страниц для PDF-документов с использованием Aspose.PDF for .NET, что позволяет настраивать форматирование документов.
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get and Set Page Properties",
    "alternativeHeadline": "Manage PDF Page Properties with Ease",
    "abstract": "Функция получения и установки свойств страниц в Aspose.PDF for .NET позволяет разработчикам без труда получать доступ и изменять атрибуты страниц PDF. Эта функциональность позволяет пользователям извлекать критически важную информацию, такую как количество страниц и конкретные свойства, такие как типы цвета, медиабоксы и обрезные боксы, всего лишь с несколькими строками кода. Улучшите свои возможности управления PDF-документами сегодня, используя эту мощную функцию для эффективной манипуляции PDF в приложениях .NET",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1117",
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
    "url": "/net/get-and-set-page-properties/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-and-set-page-properties/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF может выполнять не только простые и легкие задачи, но и справляться с более сложными целями. Проверьте следующий раздел для опытных пользователей и разработчиков."
}
</script>

Aspose.PDF for .NET позволяет вам читать и устанавливать свойства страниц в PDF-файле в ваших приложениях .NET. Этот раздел показывает, как получить количество страниц в PDF-файле, получить информацию о свойствах страниц PDF, таких как цвет, и установить свойства страниц. Приведенные примеры написаны на C#, но вы можете использовать любой язык .NET, такой как VB.NET, для достижения того же результата.

Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Получение количества страниц в PDF-файле

При работе с документами вы часто хотите знать, сколько страниц они содержат. С Aspose.PDF это занимает не более двух строк кода.

Чтобы получить количество страниц в PDF-файле:

1. Откройте PDF-файл с помощью класса [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Затем используйте свойство Count коллекции [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) (из объекта Document), чтобы получить общее количество страниц в документе.

Следующий фрагмент кода показывает, как получить количество страниц PDF-файла.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetNumberOfPagesInAPdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetNumberofPages.pdf"))
    {
        // Get page count
        System.Console.WriteLine("Page Count : {0}", document.Pages.Count);
    }
}
```

### Получение количества страниц без сохранения документа

Иногда мы генерируем PDF-файлы на лету, и во время создания PDF-файла у нас может возникнуть необходимость (создание оглавления и т. д.) получить количество страниц PDF-файла без сохранения файла в системе или потоке. Поэтому, чтобы удовлетворить эту потребность, в классе Document был введен метод [ProcessParagraphs](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/processparagraphs). Пожалуйста, посмотрите следующий фрагмент кода, который показывает шаги для получения количества страниц без сохранения документа.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetPageCountWithoutSavingTheDocument()
{
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        // Create loop instance
        for (var i = 0; i < 300; i++)
        {
            // Add TextFragment to paragraphs collection of page object
            page.Paragraphs.Add(new Aspose.Pdf.Text.TextFragment("Pages count test"));
        }
        // Process the paragraphs in PDF file to get accurate page count
        document.ProcessParagraphs();
        // Print number of pages in document
        Console.WriteLine("Number of pages in document = " + document.Pages.Count);
    }
}
```

## Получение свойств страницы

Каждая страница в PDF-файле имеет ряд свойств, таких как ширина, высота, обрезной, обрезной и обрезной боксы. Aspose.PDF позволяет вам получать доступ к этим свойствам.

### **Понимание свойств страницы: разница между Artbox, BleedBox, CropBox, MediaBox, TrimBox и Rect свойством**

- **Медиабокс**: Медиабокс — это самый большой боксовый размер страницы. Он соответствует размеру страницы (например, A4, A5, US Letter и т. д.), выбранному при печати документа в PostScript или PDF. Другими словами, медиабокс определяет физический размер носителя, на котором отображается или печатается PDF-документ.
- **Bleed box**: Если документ имеет обрезку, PDF также будет иметь обрезной боксовый размер. Обрезка — это количество цвета (или графики), которое выходит за край страницы. Он используется для того, чтобы гарантировать, что когда документ печатается и обрезается до размера (“обрезается”), чернила будут доходить до самого края страницы. Даже если страница неправильно обрезана - слегка срезана от обрезных меток - на странице не появятся белые края.
- **Trim box**: Обрезной боксовый размер указывает окончательный размер документа после печати и обрезки.
- **Art box**: Арт-бокс — это боксовый размер, нарисованный вокруг фактического содержимого страниц в ваших документах. Этот боксовый размер используется при импорте PDF-документов в другие приложения.
- **Crop box**: Обрезной боксовый размер — это размер “страницы”, при котором ваш PDF-документ отображается в Adobe Acrobat. В обычном представлении только содержимое обрезного бокса отображается в Adobe Acrobat.
  Для подробных описаний этих свойств прочитайте спецификацию Adobe.Pdf, в частности 10.10.1 Границы страниц.
- **Page.Rect**: пересечение (обычно видимый прямоугольник) MediaBox и DropBox. На рисунке ниже иллюстрируются эти свойства.

Для получения дополнительной информации, пожалуйста, посетите [эту страницу](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

### **Доступ к свойствам страницы**

Класс [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) предоставляет все свойства, связанные с конкретной страницей PDF. Все страницы PDF-файлов содержатся в коллекции [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

Оттуда можно получить доступ либо к отдельным объектам Page, используя их индекс, либо перебрать коллекцию, используя цикл foreach, чтобы получить все страницы. Как только доступ к отдельной странице получен, мы можем получить ее свойства. Следующий фрагмент кода показывает, как получить свойства страницы.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AccessingPageProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetProperties.pdf"))
    {
        // Get page collection
        var pageCollection = document.Pages;
        // Get particular page
        var pdfPage = pageCollection[1];
        // Get page properties
        System.Console.WriteLine("ArtBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.ArtBox.Height, pdfPage.ArtBox.Width, pdfPage.ArtBox.LLX,
            pdfPage.ArtBox.LLY, pdfPage.ArtBox.URX, pdfPage.ArtBox.URY);
        System.Console.WriteLine("BleedBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.BleedBox.Height, pdfPage.BleedBox.Width, pdfPage.BleedBox.LLX,
            pdfPage.BleedBox.LLY, pdfPage.BleedBox.URX, pdfPage.BleedBox.URY);
        System.Console.WriteLine("CropBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.CropBox.Height, pdfPage.CropBox.Width, pdfPage.CropBox.LLX,
            pdfPage.CropBox.LLY, pdfPage.CropBox.URX, pdfPage.CropBox.URY);
        System.Console.WriteLine("MediaBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.MediaBox.Height, pdfPage.MediaBox.Width, pdfPage.MediaBox.LLX,
            pdfPage.MediaBox.LLY, pdfPage.MediaBox.URX, pdfPage.MediaBox.URY);
        System.Console.WriteLine("TrimBox : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.TrimBox.Height, pdfPage.TrimBox.Width, pdfPage.TrimBox.LLX,
            pdfPage.TrimBox.LLY, pdfPage.TrimBox.URX, pdfPage.TrimBox.URY);
        System.Console.WriteLine("Rect : Height={0},Width={1},LLX={2},LLY={3},URX={4},URY={5}", pdfPage.Rect.Height, pdfPage.Rect.Width, pdfPage.Rect.LLX, pdfPage.Rect.LLY,
            pdfPage.Rect.URX, pdfPage.Rect.URY);
        System.Console.WriteLine("Page Number : {0}", pdfPage.Number);
        System.Console.WriteLine("Rotate : {0}", pdfPage.Rotate);
    }
}
```

## Получение конкретной страницы PDF-файла

Aspose.PDF позволяет вам [разделить PDF на отдельные страницы](/pdf/net/split-pdf-document/) и сохранить их как PDF-файлы. Получение указанной страницы в PDF-файле и сохранение ее как нового PDF является очень похожей операцией: откройте исходный документ, получите доступ к странице, создайте новый документ и добавьте страницу в него.

Коллекция [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection) объекта [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) содержит страницы в PDF-файле. Чтобы получить конкретную страницу из этой коллекции:

1. Укажите индекс страницы, используя свойство Pages.
1. Создайте новый объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Добавьте объект [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) в новый объект [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
1. Сохраните выходные данные, используя метод [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4).

Следующий фрагмент кода показывает, как получить конкретную страницу из PDF-файла и сохранить ее как новый файл.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetAParticularPageOfThePdfFile()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get particular page
        var pdfPage = document.Pages[2];
        // Save the page as PDF file
        using (var newDocument = new Aspose.Pdf.Document())
        {
            newDocument.Pages.Add(pdfPage);
            // Save PDF document
            newDocument.Save(dataDir + "GetParticularPage_out.pdf");
        }
    }
}
```

## Определение цвета страницы

Класс [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page) предоставляет свойства, связанные с конкретной страницей в PDF-документе, включая тип цвета - RGB, черно-белый, градации серого или неопределенный - который использует страница.

Все страницы PDF-файлов содержатся в коллекции [PageCollection](https://reference.aspose.com/pdf/net/aspose.pdf/pagecollection). Свойство ColorType указывает цвет элементов на странице. Чтобы получить или определить информацию о цвете для конкретной страницы PDF, используйте свойство [ColorType](https://reference.aspose.com/pdf/net/aspose.pdf/page/properties/colortype) объекта [Page](https://reference.aspose.com/pdf/net/aspose.pdf/page).

Следующий фрагмент кода показывает, как перебрать отдельные страницы PDF-файла, чтобы получить информацию о цвете.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeterminePageColor()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Pages();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Iterate through all the page of PDF file
        for (var pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
        {
            // Get the color type information for particular PDF page
            Aspose.Pdf.ColorType pageColorType = document.Pages[pageCount].ColorType;
            switch (pageColorType)
            {
                case Aspose.Pdf.ColorType.BlackAndWhite:
                    Console.WriteLine("Page # -" + pageCount + " is Black and white..");
                    break;
                case Aspose.Pdf.ColorType.Grayscale:
                    Console.WriteLine("Page # -" + pageCount + " is Gray Scale...");
                    break;
                case Aspose.Pdf.ColorType.Rgb:
                    Console.WriteLine("Page # -" + pageCount + " is RGB..", pageCount);
                    break;
                case Aspose.Pdf.ColorType.Undefined:
                    Console.WriteLine("Page # -" + pageCount + " Color is undefined..");
                    break;
            }
        }
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