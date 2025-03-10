---
title: Генерация эскизов изображений из PDF
linktitle: Генерация эскизов изображений
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /ru/net/generate-thumbnail-images-from-pdf-documents/
description: Этот раздел описывает, как генерировать эскизы изображений из PDF-документов
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate Thumbnail Images from PDF",
    "alternativeHeadline": "Generate Thumbnails from PDF Documents Effortlessly",
    "abstract": "Новая функция позволяет пользователям эффективно генерировать эскизы изображений непосредственно из PDF-документов. Эта функциональность улучшает управление документами, преобразуя страницы PDF в легко делимые форматы изображений, упрощая рабочие процессы как для разработчиков, так и для пользователей. С поддержкой различных форматов изображений эта функция упрощает процесс визуализации содержимого PDF без необходимости в стороннем программном обеспечении, таком как Adobe Acrobat",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Generate Thumbnail Images, PDF documents, Aspose.PDF for .NET, Acrobat SDK, image formats, PDF Manipulation Library, JavaScript, interapplication communication, thumbnail images, JPEG conversion",
    "wordcount": "767",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "Этот раздел описывает, как генерировать эскизы изображений из PDF-документов"
}
</script>

{{% alert color="primary" %}}

SDK Adobe Acrobat — это набор инструментов, который помогает вам разрабатывать программное обеспечение, взаимодействующее с технологией Acrobat. SDK содержит заголовочные файлы, библиотеки типов, простые утилиты, образцы кода и документацию.

Используя SDK Acrobat, вы можете разрабатывать программное обеспечение, которое интегрируется с Acrobat и Adobe Reader несколькими способами:

- **JavaScript** — Пишите скрипты, либо в отдельном PDF-документе, либо внешне, чтобы расширить функциональность Acrobat или Adobe Reader.
- **Плагины** — Создавайте плагины, которые динамически связаны и расширяют функциональность Acrobat или Adobe Reader.
- **Межпрограммная связь** — Пишите отдельный процесс приложения, который использует межпрограммную связь (IAC) для управления функциональностью Acrobat. DDE и OLE поддерживаются на Microsoft® Windows®, а события Apple/AppleScript на Mac OS®. IAC недоступна на UNIX®.

Aspose.PDF for .NET предоставляет много той же функциональности, освобождая вас от зависимости от автоматизации Adobe Acrobat. Эта статья показывает, как генерировать эскизы изображений из PDF-документов, сначала используя SDK Acrobat, а затем Aspose.PDF.

{{% /alert %}}

## Разработка приложения с использованием API межпрограммной связи Acrobat

Думайте о API Acrobat как о двух различных слоях, которые используют объекты межпрограммной связи Acrobat (IAC):

- Слой приложения Acrobat (AV). Слой AV позволяет вам контролировать, как документ отображается. Например, представление объекта документа находится в слое, связанном с Acrobat.
- Слой переносимого документа (PD). Слой PD предоставляет доступ к информации внутри документа, такой как страница. Из слоя PD вы можете выполнять основные манипуляции с PDF-документами, такие как удаление, перемещение или замена страниц, а также изменение атрибутов аннотаций. Вы также можете печатать страницы PDF, выделять текст, получать доступ к измененному тексту и создавать или удалять эскизы.

Поскольку наша цель — преобразовать страницы PDF в эскизы изображений, мы сосредоточены больше на IAC. API IAC содержит такие объекты, как PDDoc, PDPage, PDAnnot и другие, которые позволяют пользователю работать со слоем переносимого документа (PD). Следующий пример кода сканирует папку и преобразует страницы PDF в эскизы изображений. Используя SDK Acrobat, мы также можем читать метаданные PDF и получать количество страниц в документе.

### Подход Acrobat

Для генерации эскизов изображений для каждого документа мы использовали SDK Adobe Acrobat 7.0 и Microsoft .NET 2.0 Framework.

[SDK Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/) в сочетании с полной версией Adobe Acrobat предоставляет библиотеку объектов COM (к сожалению, бесплатный Adobe Reader не предоставляет интерфейсы COM), которые можно использовать для манипуляции и доступа к информации PDF. Используя эти объекты COM через COM Interop, загрузите PDF-документ, получите первую страницу и отобразите эту страницу в буфере обмена. Затем с помощью .NET Framework скопируйте это в битмап, масштабируйте и объедините изображение и сохраните результат в виде файла GIF или PNG.

После установки Adobe Acrobat используйте regedit.exe и посмотрите в HKEY_CLASSES_ROOT на запись, называемую AcroExch.PDDoc.

**Реестр, показывающий запись AcroExch.PDDDoc**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // Acrobat objects
    Acrobat.CAcroPDDoc pdfDoc;
    Acrobat.CAcroPDPage pdfPage;
    Acrobat.CAcroRect pdfRect;
    Acrobat.CAcroPoint pdfPoint;

    AppSettingsReader appSettings = new AppSettingsReader();
    string pdfInputPath = appSettings.GetValue("pdfInputPath", typeof(string)).ToString();
    string pngOutputPath = appSettings.GetValue("pngOutputPath", typeof(string)).ToString();
    string templatePortraitFile = Application.StartupPath + @"\pdftemplate_portrait.gif";
    string templateLandscapeFile = Application.StartupPath + @"\pdftemplate_landscape.gif";

    // Get list of files to process from the input path
    string[] files = Directory.GetFiles(pdfInputPath, "*.pdf");

    for (int n = 0; n < files.Length; n++)
    {
        string inputFile = files[n];
        string outputFile = Path.Combine(pngOutputPath, Path.GetFileNameWithoutExtension(inputFile) + ".png");

        // Create PDF document
        pdfDoc = (Acrobat.CAcroPDDoc)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.PDDoc", "");

        if (pdfDoc.Open(inputFile) == 0)
        {
            throw new FileNotFoundException($"Unable to open PDF file: {inputFile}");
        }

        int pageCount = pdfDoc.GetNumPages();
        pdfPage = (Acrobat.CAcroPDPage)pdfDoc.AcquirePage(0);
        pdfPoint = (Acrobat.CAcroPoint)pdfPage.GetSize();

        pdfRect = (Acrobat.CAcroRect)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.Rect", "");
        pdfRect.Left = 0;
        pdfRect.right = pdfPoint.x;
        pdfRect.Top = 0;
        pdfRect.bottom = pdfPoint.y;

        pdfPage.CopyToClipboard(pdfRect, 0, 0, 100);
        IDataObject clipboardData = Clipboard.GetDataObject();

        if (clipboardData.GetDataPresent(DataFormats.Bitmap))
        {
            Bitmap pdfBitmap = (Bitmap)clipboardData.GetData(DataFormats.Bitmap);

            int thumbnailWidth = 45;
            int thumbnailHeight = 59;
            string templateFile = pdfPoint.x < pdfPoint.y ? templatePortraitFile : templateLandscapeFile;

            if (pdfPoint.x > pdfPoint.y)
            {
                // Swap width and height for landscape orientation
                (thumbnailWidth, thumbnailHeight) = (thumbnailHeight, thumbnailWidth);
            }

            Bitmap templateBitmap = new Bitmap(templateFile);
            Image pdfImage = pdfBitmap.GetThumbnailImage(thumbnailWidth, thumbnailHeight, null, IntPtr.Zero);

            Bitmap thumbnailBitmap = new Bitmap(thumbnailWidth + 7, thumbnailHeight + 7, System.Drawing.Imaging.PixelFormat.Format32bppArgb);

            templateBitmap.MakeTransparent();

            using (Graphics thumbnailGraphics = Graphics.FromImage(thumbnailBitmap))
            {
                thumbnailGraphics.DrawImage(pdfImage, 2, 2, thumbnailWidth, thumbnailHeight);
                thumbnailGraphics.DrawImage(templateBitmap, 0, 0);
                thumbnailBitmap.Save(outputFile, System.Drawing.Imaging.ImageFormat.Png);
            }

            Console.WriteLine("Generated thumbnail: {0}", outputFile);

            pdfDoc.Close();
            Marshal.ReleaseComObject(pdfPage);
            Marshal.ReleaseComObject(pdfRect);
            Marshal.ReleaseComObject(pdfDoc);
        }
    }
}
```

## Подход Aspose.PDF for .NET

Aspose.PDF for .NET предоставляет обширную поддержку для работы с PDF-документами. Он также поддерживает возможность конвертации страниц PDF-документов в различные форматы изображений. Описанная выше функциональность может быть легко достигнута с помощью Aspose.PDF for .NET.

Aspose.PDF имеет явные преимущества:

- Вам не нужно устанавливать Adobe Acrobat на своем компьютере для работы с PDF-файлами.
- Использование Aspose.PDF for .NET просто и легко для понимания по сравнению с автоматизацией Acrobat.

Если нам нужно преобразовать страницы PDF в JPEG, пространство имен [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) предоставляет класс [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) для рендеринга страниц PDF в изображения JPEG. Пожалуйста, посмотрите следующий фрагмент кода.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Retrieve names of all the PDF files in a particular directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

    // Iterate through all the files entries in array
    for (int counter = 0; counter < fileEntries.Length; counter++)
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(fileEntries[counter]))
        {
            for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
            {
                using (FileStream imageStream = new FileStream(dataDir + @"\Thumbanils" + counter.ToString() + "_" + pageCount + ".jpg", FileMode.Create))
                {
                    var resolution = new Aspose.Pdf.Devices.Resolution(300);
                    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice(45, 59, resolution, 100);
                    // Convert a particular page and save the image to stream
                    jpegDevice.Process(document.Pages[pageCount], imageStream);
                }
            }
        }
    }
}
```

{{% alert color="primary" %}}

- Спасибо CodeProject за [Генерацию эскизов изображений из PDF-документа](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- Спасибо Acrobat за [ссылку на SDK Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

{{% /alert %}}

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