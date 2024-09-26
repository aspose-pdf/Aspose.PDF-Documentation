---
title: קיצוץ דפי PDF באופן תכנותי ב-C#
linktitle: קיצוץ דפים
type: docs
weight: 80
url: /net/crop-pages/
description: תוכל לקבל תכונות של דף, כגון רוחב, גובה ותיבות קיצוץ באמצעות Aspose.PDF עבור .NET.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "קיצוץ דפי PDF באופן תכנותי ב-C#",
    "alternativeHeadline": "איך לקצץ דפי PDF ב-.NET",
    "author": {
        "@type": "Person",
        "name":"אנסטסיה הולוב",
        "givenName": "אנסטסיה",
        "familyName": "הולוב",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, קיצוץ דפי pdf",
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
    "url": "/net/crop-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/crop-pages/"
    },
    "dateModified": "2022-02-04",
    "description": "תוכל לקבל תכונות של דף, כגון רוחב, גובה ותיבות קיצוץ באמצעות Aspose.PDF עבור .NET."
}
</script>
## קבלת מאפייני דף

לכל דף בקובץ PDF יש מספר מאפיינים, כגון רוחב, גובה, תיבות דם, חיתוך וחיתוך סופי. Aspose.PDF מאפשר לך לגשת למאפיינים אלו.

- **תיבת מדיה**: תיבת המדיה היא תיבת הדף הגדולה ביותר. היא תואמת לגודל הדף (לדוגמה A4, A5, מכתב אמריקאי וכו') שנבחר כאשר המסמך הודפס ל-PostScript או PDF. במילים אחרות, תיבת המדיה קובעת את הגודל הפיזי של התקשורת שעליה מוצג או מודפס המסמך PDF.
- **תיבת דם**: אם למסמך יש דם, גם ל-PDF תהיה תיבת דם. דם הוא כמות הצבע (או האמנות) המתפשטת מעבר לשולי הדף. היא משמשת לוודא שכאשר המסמך מודפס ונחתך לגודל ("מחותך"), הדיו יגיע עד לשולי הדף. אפילו אם הדף נחתך בטעות - חתוך מעט מחוץ לסימני החיתוך - לא יופיעו שוליים לבנים על הדף.
- **תיבת חיתוך**: תיבת החיתוך מציינת את הגודל הסופי של מסמך לאחר הדפסה וחיתוך.
- **תיבת אומנות**: תיבת האומנות היא התיבה שמצוירת סביב תוכן הדפים הממשיים במסמכים שלך.
- **תיבת אמנות**: תיבת האמנות היא התיבה שמצוירת סביב התוכן האמיתי של הדפים במסמכים שלך.
- **תיבת חיתוך**: תיבת החיתוך היא "גודל הדף" בו מוצג המסמך PDF שלך ב-Adobe Acrobat. בתצוגה רגילה, רק תוכן תיבת החיתוך מוצג ב-Adobe Acrobat. לתיאורים מפורטים של התכונות האלו, קרא את המפרט של Adobe.Pdf, במיוחד 10.10.1 גבולות דף.
- **Page.Rect**: החיתוך (המלבן הנראה בדרך כלל) של MediaBox ו-DropBox. התמונה למטה ממחישה את התכונות האלו.
לפרטים נוספים, בקר ב[דף זה](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html).

הקטע הבא מציג כיצד לחתוך דף:

```csharp
public static void CropPagesPDF()
{
    var pdfDocument1 = new Aspose.Pdf.Document("crop_page.pdf");
    Console.WriteLine(pdfDocument1.Pages[1].CropBox);
    Console.WriteLine(pdfDocument1.Pages[1].TrimBox);
    Console.WriteLine(pdfDocument1.Pages[1].ArtBox);
    Console.WriteLine(pdfDocument1.Pages[1].BleedBox);
    Console.WriteLine(pdfDocument1.Pages[1].MediaBox);

    // יצירת תיבת חיתוך חדשה
    var newBox = new Rectangle(200, 220, 2170, 1520);
    pdfDocument1.Pages[1].CropBox = newBox;
    pdfDocument1.Pages[1].TrimBox = newBox;
    pdfDocument1.Pages[1].ArtBox = newBox;
    pdfDocument1.Pages[1].BleedBox = newBox;
   
    pdfDocument1.Save("crop_page_modified.pdf");           
}
```
בדוגמה זו השתמשנו בקובץ דוגמה [כאן](crop_page.pdf). בהתחלה הדף שלנו נראה כפי שמוצג בתמונה 1.
![תמונה 1. דף מוחתך](crop_page.png)

לאחר השינוי, הדף ייראה כמו בתמונה 2.
![תמונה 2. דף מוחתך](crop_page2.png)

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

