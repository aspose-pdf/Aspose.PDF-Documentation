---
title: Печать PDF в .NET Framework
linktitle: Печать PDF в .NET Framework
type: docs
weight: 10
url: /ru/net/printing-pdf-in-net-framework/
description: Вы можете печатать файлы PDF на принтере по умолчанию, используя настройки принтера и страницы с помощью C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Печать PDF в .NET Framework",
    "alternativeHeadline": "Как печатать PDF в .NET Framework",
    "author": {
        "@type": "Person",
        "name":"Анастасия Холуб",
        "givenName": "Анастасия",
        "familyName": "Холуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация pdf документов",
    "keywords": "pdf, c#, pdf в .NET Framework",
    "wordcount": "302",
    "proficiencyLevel":"Начинающий",
    "publisher": {
        "@type": "Organization",
        "name": "Команда документации Aspose.PDF",
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
    "url": "/net/printing-pdf-in-net-framework/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-in-net-framework/"
    },
    "dateModified": "2022-02-04",
    "description": "Вы можете печатать файлы PDF на принтере по умолчанию, используя настройки принтера и страницы с помощью C#."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/ru/net/drawing/).

## **Печать PDF-файла в C# - Печать PDF-файла на принтере по умолчанию с использованием настроек принтера и страницы**

В этой статье описывается, как напечатать PDF-файл на принтере по умолчанию с использованием настроек принтера и страницы в C#.

Класс [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) позволяет напечатать PDF-файл на принтере по умолчанию. Вам нужно создать объект PdfViewer и открыть PDF с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). Для указания различных настроек печати используйте классы `PageSettings` и `PrinterSettings`. Наконец, вызовите метод [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings), чтобы напечатать PDF на принтере по умолчанию. Следующий фрагмент кода показывает, как напечатать PDF на принтере по умолчанию с настройками принтера и страницы.

```csharp
public static void SimplePrint()
{
    // Создать объект PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Открыть входной PDF-файл
    viewer.BindPdf(System.IO.Path.Combine(_dataDir, "input.pdf"));

    // Установить атрибуты для печати
    viewer.AutoResize = true;         // Печатать файл с корректировкой размера
    viewer.AutoRotate = true;         // Печатать файл с корректировкой поворота
    viewer.PrintPageDialog = false;   // Не выводить диалог номера страницы при печати

    // Создать объекты для настроек принтера и страницы и PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
    System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

    // Установить имя принтера
    ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

    // Установить размер страницы (если требуется)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // Установить поля страницы (если требуется)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Напечатать документ, используя настройки принтера и страницы
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Закрыть PDF-файл после печати
    viewer.Close();
}
```
Для отображения диалога печати используйте следующий фрагмент кода:

```csharp
System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
    // Здесь идет код печати документа
    // Печать документа с использованием настроек принтера и страницы
    viewer.PrintDocumentWithSettings(pgs, ps);
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
                "contactType": "продажи",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
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
    "applicationCategory": "Библиотека для манипуляции PDF для .NET",
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


