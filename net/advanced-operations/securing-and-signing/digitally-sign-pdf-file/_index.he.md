---
title: הוסף חתימה דיגיטלית או חתום דיגיטלית על PDF ב-C#
linktitle: חתימה דיגיטלית על PDF
type: docs
weight: 10
url: /net/digitally-sign-pdf-file/
description: חתום דיגיטלית על מסמכי PDF באמצעות C# או VB.NET. אמת או ולידציה של חתימות דיגיטליות על PDF באמצעות C# או VB.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "איך לחתום דיגיטלית על PDF",
    "alternativeHeadline": "עבודה עם חתימה דיגיטלית על PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, חתימה דיגיטלית על pdf",
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
    "url": "/net/digitally-sign-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/digitally-sign-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "חתום דיגיטלית על מסמכי PDF באמצעות C# או VB.NET. אמת או ולידציה של חתימות דיגיטליות על PDF באמצעות C# או VB.NET."
}
</script>
Aspose.PDF for .NET תומך בתכונה לחתימה דיגיטלית על קבצי PDF באמצעות מחלקת SignatureField. ניתן גם לאמת קובץ PDF באמצעות תעודת PKCS12-Certificate. משהו דומה ל-[הוספת חתימות ואבטחה ב-Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

כאשר חותמים על מסמך PDF באמצעות חתימה, אתה למעשה מאשר את תוכנו "כפי שהוא". כתוצאה מכך, כל שינויים נוספים שנעשים לאחר מכן מבטלים את החתימה ובכך, תדע אם המסמך שונה. לעומת זאת, אימות מסמך ראשון מאפשר לך לציין את השינויים שמשתמש יכול לבצע במסמך ללא ביטול האימות.

במילים אחרות, המסמך עדיין ייחשב כשומר על שלמותו והמקבל עדיין יכול לסמוך על המסמך. לפרטים נוספים, אנא בקר באימות וחתימה של PDF. באופן כללי, אימות מסמך ניתן להשוואה לחתימת קוד של קובץ בציע .NET.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).
הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## תכונות חתימה של Aspose.PDF עבור .NET

ניתן להשתמש במחלקות ושיטות הבאות לחתימת PDF

- מחלקה [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature)
- אוסף [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions)
- תכונה [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) במחלקה [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)

## חתימה על PDF עם חתימות דיגיטליות

```csharp
public static void SignDocument()
{
    string inFile = System.IO.Path.Combine(_dataDir,"DigitallySign.pdf");
    string outFile = System.IO.Path.Combine(_dataDir,"DigitallySign_out.pdf");
    using (Document document = new Document(inFile))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Pa$$w0rd2020"); // השתמש באובייקטים PKCS7/PKCS7Detached
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // שמור את הקובץ PDF המוצא
            signature.Save(outFile);
        }
    }
}
```
## הוספת חותמת זמן לחתימה דיגיטלית

### איך לחתום על קובץ PDF עם חותמת זמן

Aspose.PDF עבור .NET תומך בחתימה דיגיטלית על קובץ PDF עם שרת חותמת זמן או שירות רשת.

כדי לעמוד בדרישה זו, המחלקה [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) נוספה למרחב השמות Aspose.PDF. אנא הסתכלו על קטע הקוד הבא שמשיג חותמת זמן ומוסיף אותה למסמך PDF:

```csharp
public static void SignWithTimeStampServer()
{
    using (Document document = new Document(System.IO.Path.Combine(_dataDir,"SimpleResume.pdf")))
    {
        using (PdfFileSignature signature = new PdfFileSignature(document))
        {
            PKCS7 pkcs = new PKCS7(@"C:\Keys\test.pfx", "Start2020");
            TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", string.Empty); // ניתן להשמיט שם משתמש/סיסמה
            pkcs.TimestampSettings = timestampSettings;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(100, 100, 200, 100);
            // יצירת אחד משלושת סוגי החתימות
            signature.Sign(1, "סיבת החתימה", "קשר", "מיקום", true, rect, pkcs);
            // שמירת קובץ PDF המוצא
            signature.Save(System.IO.Path.Combine(_dataDir, "DigitallySignWithTimeStamp_out.pdf"));
        }
    }
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

