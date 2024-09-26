---
title: הסר שולחנות מ-PDF קיים
linktitle: הסרת שולחנות
type: docs
weight: 50
url: /net/remove-tables-from-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הסר שולחנות מ-PDF קיים",
    "alternativeHeadline": "איך למחוק שולחנות מ-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, הסרת שולחן, מחיקת שולחנות",
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
    "url": "/net/remove-tables-from-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/remove-tables-from-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
{{% alert color="primary" %}}

Aspose.PDF עבור NET מציע את היכולת להוסיף/ליצור טבלה בתוך מסמך PDF בזמן שהוא נוצר מאפס או שאתה יכול גם להוסיף את אובייקט הטבלה בכל מסמך PDF קיים. עם זאת, ייתכן שיש לך דרישה ל[ערוך טבלאות במסמך PDF קיים](https://docs.aspose.com/pdf/net/manipulate-tables-in-existing-pdf/) שם אתה יכול לעדכן את התוכן בתאי הטבלה הקיימים. עם זאת, ייתכן שתיתקל בדרישה להסיר אובייקטי טבלה ממסמך PDF קיים.

{{% /alert %}}

כדי להסיר את הטבלאות, אנו צריכים להשתמש במחלקת [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) כדי לאחוז בטבלאות במסמך PDF הקיים ולאחר מכן לקרוא ל[הסר](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber/methods/remove).

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## הסרת טבלה ממסמך PDF

הוספנו פונקציה חדשה כלומר
הוספנו פונקציה חדשה כלומר:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// טען מסמך PDF קיים
Document pdfDocument = new Document(dataDir + "Table_input.pdf");

// צור אובייקט TableAbsorber כדי למצוא טבלאות
TableAbsorber absorber = new TableAbsorber();

// בקר בעמוד הראשון עם ה-absorber
absorber.Visit(pdfDocument.Pages[1]);

// קבל את הטבלה הראשונה בעמוד
AbsorbedTable table = absorber.TableList[0];

// הסר את הטבלה
absorber.Remove(table);

// שמור את ה-PDF
pdfDocument.Save(dataDir + "Table_out.pdf");
```

## הסרת מספר טבלאות ממסמך PDF

לפעמים מסמך PDF עשוי להכיל יותר מטבלה אחת ועשוי להיות לך דרישה להסיר מספר טבלאות ממנו. כדי להסיר מספר טבלאות ממסמך PDF, אנא השתמש בקטע הקוד הבא:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקרו ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// טען מסמך PDF קיים
Document pdfDocument = new Document(dataDir + "Table_input2.pdf");

// צור אובייקט TableAbsorber כדי למצוא טבלאות
TableAbsorber absorber = new TableAbsorber();

// בקר בעמוד השני עם ה-absorber
absorber.Visit(pdfDocument.Pages[1]);

// קבל עותק של אוסף הטבלאות
AbsorbedTable[] tables = new AbsorbedTable[absorber.TableList.Count];
absorber.TableList.CopyTo(tables, 0);

// עבור על עותק האוסף והסר טבלאות
foreach (AbsorbedTable table in tables)
    absorber.Remove(table);

// שמור את המסמך
pdfDocument.Save(dataDir + "Table2_out.pdf");
```
{{% alert color="primary" %}}

נא לקחת בחשבון שהסרה או החלפה של טבלה משנה את אוסף TableList. לכן, במקרה של הסרה/החלפה של טבלאות בלולאה, העתקת אוסף TableList היא חיונית.

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

