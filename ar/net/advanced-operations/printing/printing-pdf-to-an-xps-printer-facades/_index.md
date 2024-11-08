---
title: طباعة PDF إلى طابعة XPS
linktitle: طباعة PDF إلى طابعة XPS (واجهات)
type: docs
weight: 20
url: /ar/net/printing-pdf-to-an-xps-printer-facades/
keywords: "print pdf to xps, print pdf to xps c#"
description: توضح هذه الصفحة كيفية طباعة PDF إلى طابعة XPS باستخدام فئة PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "طباعة PDF إلى طابعة XPS",
    "alternativeHeadline": "كيفية طباعة PDF إلى طابعة XPS",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "إنشاء مستند PDF",
    "keywords": "pdf, c#, pdf to an XPS printer",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق Aspose.PDF Doc",
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
    "description": "توضح هذه الصفحة كيفية طباعة PDF إلى طابعة XPS باستخدام فئة PdfViewer."
}
</script>

## **طباعة ملف PDF على طابعة XPS باستخدام C#**

يمكنك طباعة ملف PDF على طابعة XPS، أو أي طابعة رقمية أخرى، باستخدام فئة [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). للقيام بذلك، قم بإنشاء كائن من فئة PdfViewer وافتح ملف PDF باستخدام الطريقة [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). يمكنك تعيين إعدادات الطباعة المختلفة باستخدام فئات PrinterSettings و PageSettings. كما يجب عليك تعيين خاصية PrinterName إلى الطابعة XPS أو أي طابعة رقمية أخرى لديك.

أخيرًا، استخدم الطريقة [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) لطباعة ملف PDF على طابعة XPS أو طابعة رقمية أخرى. يوضح الجزء التالي من الكود كيفية طباعة ملف PDF على طابعة XPS.

```csharp
public static void PrintToXpsPrinter()
{
    // إنشاء كائن PdfViewer
    PdfViewer viewer = new PdfViewer();

    // فتح ملف PDF الإدخال
    viewer.BindPdf(_dataDir + "input.pdf");

    // تعيين خصائص الطباعة
    viewer.AutoResize = true;         // طباعة الملف بحجم معدل
    viewer.AutoRotate = true;         // طباعة الملف بدوران معدل
    viewer.PrintPageDialog = false;   // عدم إظهار حوار رقم الصفحة عند الطباعة

    // إنشاء كائنات لإعدادات الطابعة والصفحة وPrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // تعيين اسم طابعة XPS/PDF
    ps.PrinterName = "Microsoft XPS Document Writer";
    // أو تعيين الطابعة PDF
    // Ps.PrinterName = "Adobe PDF";

    // تعيين حجم الصفحة (إذا لزم الأمر)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // تعيين هوامش الصفحة (إذا لزم الأمر)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // طباعة المستند باستخدام إعدادات الطابعة والصفحة
    viewer.PrintDocumentWithSettings(pgs, ps);

    // إغلاق ملف PDF بعد الطباعة
    viewer.Close();
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "مكتبة Aspose.PDF لـ .NET",
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
                "contactType": "مبيعات",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
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
    "applicationCategory": "مكتبة التلاعب بملفات PDF لـ .NET",
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

