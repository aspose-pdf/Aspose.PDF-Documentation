---
title: הדפסת PDF ב-.NET Framework
linktitle: הדפסת PDF ב-.NET Framework
type: docs
weight: 10
url: /net/printing-pdf-in-net-framework/
keywords: "print pdf file c#, c# print pdf"
description: ניתן להדפיס קבצי PDF למדפסת המוגדרת כברירת מחדל באמצעות הגדרות המדפסת והדף עם C#.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הדפסת PDF ב-.NET Framework",
    "alternativeHeadline": "כיצד להדפיס PDF ב-.NET Framework",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, pdf in .NET Framework",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות מסמכי Aspose.PDF",
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
    "description": "ניתן להדפיס קבצי PDF למדפסת המוגדרת כברירת מחדל באמצעות הגדרות המדפסת והדף עם C#."
}
</script>
הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## **הדפס קובץ PDF ב-C# - הדפס קובץ PDF למדפסת ברירת המחדל באמצעות הגדרות מדפסת ודף**

מאמר זה מתאר איך להדפיס קובץ PDF למדפסת ברירת המחדל באמצעות הגדרות מדפסת ודף ב-C#.

המחלקה [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer) מאפשרת לך להדפיס קובץ PDF למדפסת ברירת המחדל. עליך ליצור אובייקט PdfViewer ולפתוח את ה-PDF באמצעות השיטה [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). כדי להגדיר הגדרות הדפסה שונות, השתמש במחלקות `PageSettings` ו-`PrinterSettings`. לבסוף, קרא לשיטה [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) כדי להדפיס את ה-PDF למדפסת ברירת המחדל. הקטע הבא מראה איך להדפיס PDF למדפסת ברירת המחדל עם הגדרות מדפסת ודף.

```csharp
public static void SimplePrint()
{
    // צור אובייקט PdfViewer
    PdfViewer viewer = new PdfViewer();

    // פתח קובץ PDF קלט
    viewer.BindPdf(System.IO.Path.Combine(_dataDir, "input.pdf"));

    // הגדר מאפיינים להדפסה
    viewer.AutoResize = true;         // הדפס את הקובץ עם גודל מותאם
    viewer.AutoRotate = true;         // הדפס את הקובץ עם סיבוב מותאם
    viewer.PrintPageDialog = false;   // אל תייצר דיאלוג מספר עמוד בעת ההדפסה

    // צור אובייקטים להגדרות מדפסת ודף ו-PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();
    System.Drawing.Printing.PrintDocument prtdoc = new System.Drawing.Printing.PrintDocument();

    // הגדר שם מדפסת
    ps.PrinterName = prtdoc.PrinterSettings.PrinterName;

    // הגדר גודל דף (אם נדרש)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // הגדר שוליים לדף (אם נדרש)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // הדפס מסמך באמצעות הגדרות מדפסת ודף
    viewer.PrintDocumentWithSettings(pgs, ps);

    // סגור את קובץ ה-PDF לאחר ההדפסה
    viewer.Close();
}
```
כדי להציג דיאלוג הדפסה, נסה להשתמש בקטע הקוד הבא:

```csharp
System.Windows.Forms.PrintDialog printDialog = new System.Windows.Forms.PrintDialog();
if (printDialog.ShowDialog() == System.Windows.Forms.DialogResult.OK)
{
    // קוד הדפסת מסמך נמצא כאן
    // הדפס מסמך באמצעות הדפסת מדפסת והגדרות דף
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
                "contactType": "מכירות",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
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
    "applicationCategory": "ספריית עיבוד PDF ל-.NET",
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


