---
title: מניפולציה של טבלאות ב- PDF קיים
linktitle: מניפולציה של טבלאות
type: docs
weight: 40
url: /net/manipulate-tables-in-existing-pdf/
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "מניפולציה של טבלאות ב- PDF קיים",
    "alternativeHeadline": "איך לעדכן תוכן של טבלאות ב- PDF קיים",
    "author": {
        "@type": "Person",
        "name": "אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "PDF, c#, מניפולציה של טבלאות",
    "wordcount": "302",
    "proficiencyLevel": "מתחילים",
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
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "מכירות",
                "areaServed": "GB",
                "availableLanguage": "אנגלית"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "מכירות",
                "areaServed": "AU",
                "availableLanguage": "אנגלית"
            }
        ]
    },
    "url": "/net/manipulate-tables-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/manipulate-tables-in-existing-pdf/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
## עיבוד טבלאות בקובצי PDF קיימים

אחת התכונות הראשונות שנתמכת על ידי Aspose.PDF עבור .NET היא היכולות לעבוד עם טבלאות והיא מספקת תמיכה נהדרת בהוספת טבלאות בקבצי PDF שנוצרים מחדש או בכל קובץ PDF קיים. כמו כן, אתה מקבל את היכולת לשלב טבלה עם מסד נתונים (DOM) כדי ליצור טבלאות דינמיות המבוססות על תוכן מסד הנתונים. בגרסה החדשה הזו, יישמנו תכונה חדשה של חיפוש וניתוח טבלאות פשוטות שכבר קיימות בדף של מסמך PDF. מחלקה חדשה בשם **Aspose.PDF.Text.TableAbsorber** מספקת את היכולות האלה. השימוש ב-TableAbsorber דומה מאוד למחלקה הקיימת TextFragmentAbsorber. קטע הקוד הבא מראה את השלבים לעדכון תוכן בתא מסוים בטבלה.

קטע הקוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור אל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// טעינת קובץ PDF קיים
Document pdfDocument = new Document(dataDir + "input.pdf");
// יצירת אובייקט TableAbsorber למציאת טבלאות
TableAbsorber absorber = new TableAbsorber();

// ביקור בדף הראשון עם ה-absorber
absorber.Visit(pdfDocument.Pages[1]);

// גישה לטבלה הראשונה בדף, התא הראשון שלהם והקטעי הטקסט בו
TextFragment fragment = absorber.TableList[0].RowList[0].CellList[0].TextFragments[1];

// שינוי טקסט של קטע הטקסט הראשון בתא
fragment.Text = "שלום עולם";
dataDir = dataDir + "ManipulateTable_out.pdf";
pdfDocument.Save(dataDir);
```
## החלף טבלה ישנה בחדשה במסמך PDF

אם אתה צריך למצוא טבלה מסוימת ולהחליפה ברצויה, תוכל להשתמש בשיטת Replace() של המחלקה [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber) כדי לעשות זאת. הדוגמה הבאה מדגימה את הפונקציונליות להחלפת הטבלה בתוך מסמך PDF:

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_Tables();

// טען מסמך PDF קיים
Document pdfDocument = new Document(dataDir + @"Table_input2.pdf");

// צור אובייקט TableAbsorber כדי למצוא טבלאות
TableAbsorber absorber = new TableAbsorber();

// בקר בעמוד הראשון עם ה-absorber
absorber.Visit(pdfDocument.Pages[1]);

// קבל את הטבלה הראשונה בעמוד
AbsorbedTable table = absorber.TableList[0];

// צור טבלה חדשה
Table newTable = new Table();
newTable.ColumnWidths = "100 100 100";
newTable.DefaultCellBorder = new BorderInfo(BorderSide.All, 1F);

Row row = newTable.Rows.Add();
row.Cells.Add("עמ' 1");
row.Cells.Add("עמ' 2");
row.Cells.Add("עמ' 3");

// החלף את הטבלה בחדשה
absorber.Replace(pdfDocument.Pages[1], table, newTable);

// שמור את המסמך
pdfDocument.Save(dataDir + "TableReplaced_out.pdf");
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

