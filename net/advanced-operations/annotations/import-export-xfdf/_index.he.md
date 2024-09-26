---
title: ייבוא ויצוא של הערות לפורמט XFDF
linktitle: ייבוא ויצוא של הערות לפורמט XFDF
type: docs
weight: 40
url: /net/import-export-xfdf/
description: תוכלו לייבא ולייצא הערות בפורמט XFDF באמצעות C# וספריית Aspose.PDF ל-.NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "יבוא ויצוא של הערות לפורמט XFDF",
    "alternativeHeadline": "שיטות לייבוא ויצוא נתוני הערות לקבצי XFDF",
    "author": {
        "@type": "Person",
        "name": "אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, ייבוא יצוא לXFDF",
    "wordcount": "302",
    "proficiencyLevel": "מתחיל",
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
    "url": "/net/import-export-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-xfdf/"
    },
    "dateModified": "2022-02-04",
    "description": "תוכלו לייבא ולייצא הערות בפורמט XFDF באמצעות C# וספריית Aspose.PDF ל-.NET."
}
</script>
{{% alert color="primary" %}}

XFDF הוא ראשי תיבות של XML Forms Data Format. זהו פורמט קובץ מבוסס XML. פורמט קובץ זה משמש לייצוג נתוני טופס או הערות המכילות בטופס PDF. XFDF יכול לשמש למטרות שונות, אך במקרה שלנו, הוא יכול לשמש לשליחה או קבלה של נתוני טופס או הערות למחשבים או שרתים אחרים וכן לארכוב נתוני הטופס או ההערות. במאמר זה, נראה כיצד Aspose.Pdf.Facades לקחה את הרעיון הזה בחשבון וכיצד אנו יכולים לייבא ולייצא נתוני הערות לקובץ XFDF.

{{% /alert %}}

**Aspose.PDF for .NET** הוא רכיב עשיר בתכונות לעריכת מסמכי PDF. כפי שאנו יודעים, XFDF הוא אספקט חשוב בניהול טפסי PDF, המרחב השם Aspose.Pdf.Facades ב-Aspose.PDF for .NET שקל זאת היטב, וסיפק שיטות לייבוא וייצוא נתוני הערות לקבצי XFDF.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) מכיל שתי שיטות לעבודה עם ייבוא וייצוא של הערות לקובץ XFDF.
[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) מכיל שתי מתודות לעבודה עם ייבוא ויצוא של הערות לקובץ XFDF.

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

הקטע קוד הבא מראה כיצד לייצא הערות לקובץ XFDF:

```csharp
using Aspose.Pdf.Annotations;
using Aspose.Pdf.Facades;
using System.IO;

namespace Aspose.Pdf.Examples.Advanced
{
    class ExampleAnnotationImportExport
    {
        // הנתיב לתיקיית המסמכים.
        private const string _dataDir = "..\\..\\..\\..\\Samples";
        /// <summary>
        /// ייבוא הערות מקובץ XFDF
        /// קובץ בפורמט XML Forms Data Format (XFDF) שנוצר על ידי Adobe Acrobat, יישום ליצירת PDF;
        /// שומר תיאורים של אלמנטים בטופס הדף והערכים שלהם, כגון שמות וערכים עבור שדות טקסט; משמש לשמירת נתוני טופס שניתן לייבא למסמך PDF.
        /// ניתן לייבא נתוני הערות מקובץ XFDF ל-PDF באמצעות
        /// המתודה ImportAnnotationsFromXfdf במחלקה PdfAnnotationEditor.
        /// </summary>       
   
        public static void ExportAnnotationXFDF()
        {
            // יצירת אובייקט PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();

            // קישור מסמך PDF לעורך ההערות
            AnnotationEditor.BindPdf(Path.Combine(_dataDir, "AnnotationDemo1.pdf"));
           
            // יצוא הערות
            var fileStream = File.OpenWrite(Path.Combine(_dataDir, "exportannotations.xfdf"));
            var annotType = new AnnotationType[] { AnnotationType.Line, AnnotationType.Square };
            AnnotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
            fileStream.Close();
        }
        //...
    }
}
```
הקטע הבא מתאר כיצד לייבא הערות לקובץ XFDF:

```csharp
public static void ImportAnnotationXFDF()
{
    // יצירת אובייקט PdfAnnotationEditor
    PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
    // יצירת מסמך PDF חדש
    var document = new Document();
    document.Pages.Add();
    AnnotationEditor.BindPdf(document);

    var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
    if (!File.Exists(exportFileName))
        ExportAnnotationXFDF();

    // ייבוא הערה
    AnnotationEditor.ImportAnnotationsFromXfdf(exportFileName);

    // שמירת ה-PDF הסופי
    document.Save(Path.Combine(_dataDir, "AnnotationDemo2.pdf"));
}
```

## דרך נוספת לייבא/לייצא הערות בבת אחת

בקוד שלהלן שיטת ImportAnnotations מאפשרת ייבוא הערות ישירות ממסמך PDF אחר.

```csharp
        /// <summary>
        /// שיטת ImportAnnotations מאפשרת ייבוא הערות ישירות ממסמך PDF אחר
        /// </summary>

        public static void ImportAnnotationFromPDF()
        {
            // יצירת אובייקט PdfAnnotationEditor
            PdfAnnotationEditor AnnotationEditor = new PdfAnnotationEditor();
            // יצירת מסמך PDF חדש
            var document = new Document();
            document.Pages.Add();
            AnnotationEditor.BindPdf(document);
            var exportFileName = Path.Combine(_dataDir, "exportannotations.xfdf");
            if (!File.Exists(exportFileName))
                ExportAnnotationXFDF();

            // עורך ההערות מאפשר ייבוא הערות ממספר מסמכי PDF,
            // אך בדוגמה זו אנו משתמשים במסמך אחד בלבד.
            AnnotationEditor.ImportAnnotations(new[] { Path.Combine(_dataDir, "AnnotationDemo1.pdf") });

            // שמירת ה-PDF הסופי
            document.Save(Path.Combine(_dataDir, "AnnotationDemo3.pdf"));
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

