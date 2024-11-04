---
title: Печать PDF на принтер XPS
linktitle: Печать PDF на принтер XPS (Facades)
type: docs
weight: 20
url: /net/printing-pdf-to-an-xps-printer-facades/
keywords: "print pdf to xps, print pdf to xps c#"
description: Эта страница показывает, как печатать PDF на принтере XPS с использованием класса PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Печать PDF на принтер XPS",
    "alternativeHeadline": "Как печатать PDF на принтере XPS",
    "author": {
        "@type": "Person",
        "name":"Анастасия Голуб",
        "givenName": "Анастасия",
        "familyName": "Голуб",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "генерация документов PDF",
    "keywords": "pdf, c#, pdf на принтере XPS",
    "wordcount": "302",
    "proficiencyLevel":"Новичок",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/net/printing-pdf-to-an-xps-printer-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-to-an-xps-printer-facades/"
    },
    "dateModified": "2022-02-04",
    "description": "Эта страница показывает, как печатать PDF на принтере XPS с использованием класса PdfViewer."
}
</script>
Следующий фрагмент кода также работает с библиотекой [Aspose.PDF.Drawing](/pdf/net/drawing/).

## **Печать PDF на принтер XPS в C#**

Вы можете напечатать PDF-файл на принтер XPS или на любой другой виртуальный принтер, используя класс [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). Для этого создайте объект класса PdfViewer и откройте PDF-файл с помощью метода [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). Вы можете настроить различные параметры печати, используя классы PrinterSettings и PageSettings. Также необходимо установить свойство PrinterName в XPS или другой виртуальный принтер, который у вас установлен.

Наконец, используйте метод [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings), чтобы напечатать PDF на XPS или другой виртуальный принтер. Следующий фрагмент кода показывает, как напечатать PDF-файл на принтере XPS.

```csharp
public static void PrintToXpsPrinter()
{
    // Создание объекта PdfViewer
    PdfViewer viewer = new PdfViewer();

    // Открытие входного PDF-файла
    viewer.BindPdf(_dataDir + "input.pdf");

    // Установка атрибутов для печати
    viewer.AutoResize = true;         // Печать файла с адаптированным размером
    viewer.AutoRotate = true;         // Печать файла с адаптированной ориентацией
    viewer.PrintPageDialog = false;   // Не выводить диалоговое окно номера страницы при печати

    // Создание объектов для настроек принтера и страницы и PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // Установка имени принтера XPS/PDF
    ps.PrinterName = "Microsoft XPS Document Writer";
    // Или установите название принтера PDF
    // Ps.PrinterName = "Adobe PDF";

    // Установка размера страницы (если требуется)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // Установка полей страницы (если требуется)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // Печать документа с использованием настроек принтера и страницы
    viewer.PrintDocumentWithSettings(pgs, ps);

    // Закрытие файла PDF после печати
    viewer.Close();
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Библиотека Aspose.PDF для .NET",
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
                "areaServed": "США",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "продажи",
                "areaServed": "Великобритания",
                "availableLanguage": "английский"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "продажи",
                "areaServed": "Австралия",
                "availableLanguage": "английский"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "Библиотека для манипуляций с PDF для .NET",
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
```

