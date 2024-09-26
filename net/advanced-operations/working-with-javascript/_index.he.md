---
title: עבודה עם JavaScript
type: docs
url: /net/working-with-javascript/
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עבודה עם JavaScript",
    "alternativeHeadline": "איך לעבוד עם JavaScript ב-PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, javascript ב-pdf",
    "wordcount": "302",
    "proficiencyLevel":"מתחיל",
    "publisher": {
        "@type": "Organization",
        "name": "צוות Aspose.PDF Doc",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2022-02-04",
    "description": ""
}
</script>
## הוספת JavaScript (DOM)

### מהו JavaScript של Acrobat?

JavaScript של Acrobat הוא שפה המבוססת על ליבת JavaScript גרסה 1.5 של ISO-16262, שהייתה ידועה בעבר כ-ECMAScript, שפת תכנות מונחה-עצמים שפותחה על ידי Netscape Communications. JavaScript נוצר בכדי להעביר את עיבוד דפי האינטרנט מהשרת אל הלקוח ביישומים מבוססי אינטרנט. JavaScript של Acrobat מיישם הרחבות, בצורת אובייקטים חדשים והמתודות והתכונות המלוות אותם, לשפת JavaScript. אובייקטים אלה, שספציפיים ל-Acrobat, מאפשרים למפתח לנהל אבטחת מסמכים, לתקשר עם מסד נתונים, לטפל בקבצים מצורפים, לעצב קובץ PDF כך שיתנהג כטופס אינטראקטיבי, מותאם לאינטרנט, וכו'. מכיוון שהאובייקטים הספציפיים ל-Acrobat מתווספים על גבי JavaScript הקוריאני, עדיין יש לך גישה למחלקות הסטנדרטיות שלו, כולל Math, String, Date, Array, ו-RegExp.

### JavaScript של Acrobat לעומת JavaScript של HTML (אינטרנט)

מסמכי PDF נחשבים גמישים מאוד מכיוון שניתן להציג אותם גם בתוך תוכנת Acrobat וגם בדפדפן אינטרנט.
מסמכי PDF מציעים גמישות רבה מכיוון שניתן להציג אותם הן בתוך תוכנת Acrobat והן בדפדפן אינטרנט.

- JavaScript של Acrobat אינו יכול לגשת לאובייקטים בתוך דף HTML. באופן דומה, JavaScript של HTML אינו יכול לגשת לאובייקטים בתוך קובץ PDF.
- JavaScript של HTML יכול לתפעל אובייקטים כמו Window. JavaScript של Acrobat אינו יכול לגשת לאובייקט זה אך הוא יכול לתפעל אובייקטים ספציפיים ל-PDF.

ניתן להוסיף JavaScript ברמת המסמך והדף באמצעות [Aspose.PDF for .NET](/pdf/net/). להוספת JavaScript:

### הוספת JavaScript לפעולת מסמך או דף

1. הצהר ויישם אובייקט JavascriptAction עם משפט JavaScript רצוי כארגומנט לבנאי.
1. הקצה את אובייקט JavascriptAction לפעולה הרצויה של מסמך ה-PDF או הדף.

הדוגמה למטה מיישמת את ה-OpenAction למסמך מסוים.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddJavaScriptToPage-AddJavaScriptToPage.cs" >}}

### **הוספה/הסרה של JavaScript לרמת מסמך**
### **הוספה/הסרה של JavaScript לרמת המסמך**

נכס חדש בשם JavaScript נוסף למחלקת המסמך שיש לו סוג אוסף JavaScript ומספק גישה לתרחישי JavaScript דרך המפתח שלו. הנכס הזה משמש להוספת JavaScript ברמת המסמך. לאוסף ה-JavaScript יש את התכונות והמתודות הבאות:

- string this(string key) – מקבל או מגדיר JavaScript לפי שמו
- IList Keys – מספק רשימה של מפתחות קיימים באוסף ה-JavaScript
- bool Remove(string key) – מסיר JavaScript לפי המפתח שלו.

{{< gist "aspose-pdf" "7e1330795d76012fcb04248bb81d45b3" "Examples-CSharp-AsposePDF-Working-Document-AddRemoveJavascriptToDoc-AddRemoveJavascriptToDoc.cs" >}}

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

