---
title: עבודה עם תיק עבודות ב-PDF
linktitle: תיק עבודות
type: docs
weight: 40
url: /net/portfolio/
description: איך ליצור תיק עבודות ב-PDF באמצעות C#. עליך להשתמש בקובץ אקסל של מיקרוסופט, מסמך וורד, וקובץ תמונה כדי ליצור תיק עבודות ב-PDF.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עבודה עם תיק עבודות ב-PDF",
    "alternativeHeadline": "יצירת תיק עבודות במסמך PDF",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה חולוב",
        "givenName": "אנסטסיה",
        "familyName": "חולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, תיק עבודות",
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
    "url": "/net/portfolio/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/portfolio/"
    },
    "dateModified": "2022-02-04",
    "description": "איך ליצור תיק עבודות ב-PDF באמצעות C#. עליך להשתמש בקובץ אקסל של מיקרוסופט, מסמך וורד, וקובץ תמונה כדי ליצור תיק עבודות ב-PDF."
}
</script>
## איך ליצור תיק עבודות ב-PDF

Aspose.PDF מאפשר יצירת מסמכי תיק עבודות ב-PDF באמצעות המחלקה [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). הוסף קובץ לאובייקט Document.Collection לאחר קבלתו באמצעות המחלקה [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification). לאחר שהקבצים נוספו, השתמש בשיטת Save של המחלקה Document כדי לשמור את מסמך התיק.

הדוגמה הבאה משתמשת בקובץ אקסל של מיקרוסופט, מסמך וורד וקובץ תמונה כדי ליצור תיק PDF.

הקוד להלן מביא לתוצאה הבאה של התיק.

הקטע קוד הבא גם עובד עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

### תיק PDF שנוצר עם Aspose.PDF

![תיק PDF שנוצר עם Aspose.PDF ל-.NET](working-with-pdf-portfolio_1.jpg)

```csharp
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// צור אובייקט מסמך
Document doc = new Document();

// צור אובייקט אוסף מסמכים
doc.Collection = new Collection();

// קבל קבצים להוספה לתיק
FileSpecification excel = new FileSpecification( dataDir + "HelloWorld.xlsx");
FileSpecification word = new FileSpecification( dataDir + "HelloWorld.docx");
FileSpecification image = new FileSpecification(dataDir + "aspose-logo.jpg");

// ספק תיאור של הקבצים
excel.Description = "קובץ אקסל";
word.Description = "קובץ וורד";
image.Description = "קובץ תמונה";

// הוסף קבצים לאוסף המסמכים
doc.Collection.Add(excel);
doc.Collection.Add(word);
doc.Collection.Add(image);

// שמור את מסמך התיק
doc.Save(dataDir + "CreatePDFPortfolio_out.pdf");
```
## חילוץ קבצים מתוך תיקיית PDF

תיקיות PDF מאפשרות לך לאחד תוכן ממגוון מקורות (לדוגמא, PDF, Word, Excel, קבצי JPEG) לתוך מיכל אחד מאוחד. הקבצים המקוריים שומרים על זהותם האישית אך מורכבים לתוך קובץ PDF Portfolio. המשתמשים יכולים לפתוח, לקרוא, לערוך ולעצב כל קובץ רכיב בנפרד משאר קבצי הרכיבים.

Aspose.PDF מאפשרת יצירת מסמכי PDF Portfolio באמצעות המחלקה [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document). היא גם מציעה את היכולת לחלץ קבצים מתוך תיקיית PDF.

הקטע קוד הבא מראה את השלבים לחילוץ קבצים מתוך תיקיית PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבורו ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// טעינת תיקיית PDF Portfolio מקורית
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
// קבלת אוסף הקבצים המוטמעים
EmbeddedFileCollection embeddedFiles = pdfDocument.EmbeddedFiles;
// חזרה על כל קובץ בתיקייה
foreach (FileSpecification fileSpecification in embeddedFiles)
{
    // קבלת הקובץ המצורף וכתיבה לקובץ או לזרם
    byte[] fileContent = new byte[fileSpecification.Contents.Length];
    fileSpecification.Contents.Read(fileContent, 0, fileContent.Length);
    string filename = Path.GetFileName(fileSpecification.Name);
    // שמירת הקובץ החולץ במיקום מסוים
    FileStream fileStream = new FileStream(dataDir + "_out" + filename, FileMode.Create);
    fileStream.Write(fileContent, 0, fileContent.Length);
    // סגירת אובייקט הזרם
    fileStream.Close();
}
```
![הסר קבצים מתיק PDF](working-with-pdf-portfolio_2.jpg)

## הסרת קבצים מתיק PDF

בכדי למחוק/להסיר קבצים מתיק PDF, נסה להשתמש בשורות הקוד הבאות.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_TechnicalArticles();

// טען את תיק PDF המקורי
Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "PDFPortfolio.pdf");
pdfDocument.Collection.Delete();
pdfDocument.Save(dataDir + "No_PortFolio_out.pdf");
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

