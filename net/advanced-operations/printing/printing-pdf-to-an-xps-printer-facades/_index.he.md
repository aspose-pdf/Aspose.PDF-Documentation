---
title: הדפסת PDF למדפסת XPS
linktitle: הדפסת PDF למדפסת XPS (Facades)
type: docs
weight: 20
url: /net/printing-pdf-to-an-xps-printer-facades/
keywords: "print pdf to xps, print pdf to xps c#"
description: דף זה מציג איך להדפיס PDF למדפסת XPS באמצעות מחלקת PdfViewer.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הדפסת PDF למדפסת XPS",
    "alternativeHeadline": "איך להדפיס PDF למדפסת XPS",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמך PDF",
    "keywords": "pdf, c#, pdf למדפסת XPS",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות מסמכים של Aspose.PDF",
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
    "url": "/net/printing-pdf-to-an-xps-printer-facades/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/printing-pdf-to-an-xps-printer-facades/"
    },
    "dateModified": "2022-02-04",
    "description": "דף זה מציג איך להדפיס PDF למדפסת XPS באמצעות מחלקת PdfViewer."
}
</script>
הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## **הדפסת PDF למדפסת XPS ב-C#**

ניתן להדפיס קובץ PDF למדפסת XPS, או לכל מדפסת רכה אחרת, באמצעות מחלקת [PdfViewer](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer). לשם כך, יש ליצור אובייקט של מחלקת PdfViewer ולפתוח את קובץ ה-PDF באמצעות המתודה [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfviewer/bindpdf/methods/2). ניתן להגדיר הגדרות הדפסה שונות באמצעות מחלקות PrinterSettings ו-PageSettings. יש גם להגדיר את תכונת PrinterName למדפסת XPS או למדפסת רכה אחרת שהותקנה.

לבסוף, השתמש במתודה [PrintDocumentWithSettings](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfviewer/methods/printdocumentwithsettings) כדי להדפיס את ה-PDF ל-XPS או למדפסת רכה אחרת. הקטע קוד הבא מראה לך איך להדפיס את קובץ ה-PDF למדפסת XPS.

```csharp
public static void PrintToXpsPrinter()
{
    // יצירת אובייקט PdfViewer
    PdfViewer viewer = new PdfViewer();

    // פתיחת קובץ PDF קלט
    viewer.BindPdf(_dataDir + "input.pdf");

    // הגדרת מאפיינים להדפסה
    viewer.AutoResize = true;         // הדפסת הקובץ עם גודל מותאם
    viewer.AutoRotate = true;         // הדפסת הקובץ עם סיבוב מותאם
    viewer.PrintPageDialog = false;   // אין לייצר דיאלוג מספר עמוד בעת ההדפסה

    // יצירת אובייקטים להגדרות מדפסת ודף ול-PrintDocument
    System.Drawing.Printing.PrinterSettings ps = new System.Drawing.Printing.PrinterSettings();
    System.Drawing.Printing.PageSettings pgs = new System.Drawing.Printing.PageSettings();

    // הגדרת שם מדפסת XPS/PDF
    ps.PrinterName = "Microsoft XPS Document Writer";
    // או הגדרת מדפסת PDF
    // Ps.PrinterName = "Adobe PDF";

    // הגדרת גודל דף (אם נדרש)
    pgs.PaperSize = new System.Drawing.Printing.PaperSize("A4", 827, 1169);

    // הגדרת שוליים לדף (אם נדרש)
    pgs.Margins = new System.Drawing.Printing.Margins(0, 0, 0, 0);

    // הדפסת המסמך באמצעות הגדרות מדפסת ודף
    viewer.PrintDocumentWithSettings(pgs, ps);

    // סגירת קובץ ה-PDF לאחר ההדפסה
    viewer.Close();
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "ספריית Aspose.PDF עבור .NET",
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
                "areaServed": "ארה\"ב",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "בריטניה",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "אוסטרליה",
                "availableLanguage": "אנגלית"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "ספריית עיבוד PDF עבור .NET",
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

