---
title: יצירת תמונות ממוזערות ממסמכי PDF
linktitle: יצירת תמונות ממוזערות
type: docs
weight: 110
url: /net/generate-thumbnail-images-from-pdf-documents/
description: פרק זה מתאר איך ליצור תמונות ממוזערות ממסמכי PDF
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "יצירת תמונות ממוזערות ממסמכי PDF",
    "alternativeHeadline": "איך ליצור תמונות ממוזערות מקובץ PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, יצירת תמונות ממוזערות",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2022-02-04",
    "description": "פרק זה מתאר איך ליצור תמונות ממוזערות ממסמכי PDF"
}
</script>
{{% alert color="primary" %}}

קיט הפיתוח של Adobe Acrobat הוא ערכת כלים המסייעת לך לפתח תוכנה המתקשרת עם טכנולוגיית Acrobat. קיט הפיתוח כולל קבצי כותרת, ספריות סוגים, כלים פשוטים, קוד לדוגמא ותיעוד.

בעזרת קיט הפיתוח של Acrobat, תוכל לפתח תוכנה שמשתלבת עם Acrobat ו-Adobe Reader במספר דרכים:

- **JavaScript** — כתוב סקריפטים, בין אם במסמך PDF יחיד או מחוץ לו, כדי להרחיב את הפונקציונליות של Acrobat או Adobe Reader.
- **תוספים** — צור תוספים המקושרים דינמית ומרחיבים את הפונקציונליות של Acrobat או Adobe Reader.
- **תקשורת בין יישומים** — כתוב תהליך יישום נפרד המשתמש בתקשורת בין יישומים (IAC) כדי לשלוט בפונקציונליות של Acrobat. DDE ו-OLE נתמכים ב-Microsoft® Windows®, ואירועים של Apple/AppleScript ב-Mac OS®. IAC אינו זמין ב-UNIX®.

Aspose.PDF ל-.NET מספק הרבה מאותה פונקציונליות, משחרר אותך מתלות באוטומציה של Adobe Acrobat.
Aspose.PDF for .NET מספק הרבה מהפונקציונליות הדומה, ומשחרר אותך מתלות באוטומציה של Adobe Acrobat.

{{% /alert %}}

## פיתוח יישום באמצעות Acrobat Interapplication communication API

חשוב על ה-API של Acrobat כמכיל שתי שכבות ברורות המשתמשות באובייקטים של תקשורת בין יישומים של Acrobat (IAC):

- שכבת היישום של Acrobat (AV). שכבת AV מאפשרת לך לשלוט כיצד המסמך מוצג. לדוגמה, התצוגה של אובייקט מסמך נמצאת בשכבה הקשורה ל-Acrobat.
- שכבת המסמך הנייד (PD). שכבת PD מספקת גישה למידע שבתוך מסמך, כמו דף. משכבת PD ניתן לבצע פעולות בסיסיות של עריכת מסמכי PDF, כמו מחיקה, העברה או החלפת דפים, כמו גם שינוי תכונות הערות. ניתן גם להדפיס דפי PDF, לבחור טקסט, לגשת לטקסט שעובד, וליצור או למחוק תמונות ממוזערות.

מכיוון שמטרתנו היא להמיר דפי PDF לתמונות ממוזערות, אנו מתמקדים יותר ב-IAC.
ככל שהמטרה שלנו היא להמיר דפי PDF לתמונות ממוזערות, אנו מתמקדים יותר ב-IAC.

### גישת Acrobat

על מנת ליצור תמונות ממוזערות עבור כל מסמך, השתמשנו ב-Adobe Acrobat 7.0 SDK וב-Microsoft .NET 2.0 Framework.

ה- [Acrobat SDK](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/) בשילוב עם הגרסה המלאה של Adobe Acrobat מציג ספריית COM של אובייקטים (לצערנו Adobe Reader החינמי אינו מציג את ממשקי ה-COM) שניתן להשתמש בהם כדי לשלוט ולגשת למידע ב-PDF. באמצעות אובייקטים אלו של COM דרך COM Interop, טען את מסמך ה-PDF, קבל את הדף הראשון והצג אותו בלוח הגזירים. לאחר מכן, עם .NET Framework, העתק זאת לתמונת bitmap, הקטן ושלב את התמונה ושמור את התוצאה כקובץ GIF או PNG.

לאחר התקנת Adobe Acrobat, השתמש ב-regedit.exe וחפש תחת HKEY_CLASSES_ROOT ערך בשם AcroExch.PDDoc.

**הרישום מציג את ערך ה-AcroExch.PDDDoc**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)
![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImagesUsingAdobe-CreateThumbnailImagesUsingAdobe.cs" >}}

## גישת Aspose.PDF עבור .NET

Aspose.PDF עבור .NET מספק תמיכה נרחבת בעבודה עם מסמכי PDF. הוא גם תומך ביכולת להמיר דפים של מסמכי PDF למגוון פורמטים של תמונות. הפונקציונליות שתוארה לעיל יכולה להשיג בקלות באמצעות Aspose.PDF עבור .NET.

Aspose.PDF יש יתרונות בולטים:

- אין צורך להתקין את Adobe Acrobat על המערכת שלך כדי לעבוד עם קבצי PDF.
- שימוש ב-Aspose.PDF עבור .NET הוא פשוט וקל להבנה בהשוואה לאוטומציה של Acrobat.

אם אנו צריכים להמיר דפי PDF ל-JPEGs, המרחב השם [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) מספק מחלקה בשם [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) לעיבוד דפי PDF לתמונות JPEG.
אם אנו צריכים להמיר דפי PDF לתמונות JPEG, המרחב השם [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) מספק מחלקה בשם [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) לעיבוד דפי PDF לתמונות JPEG.

{{< gist "aspose-com-gists" "63473b1ba28e09e229cfbf4430eabd8a" "Examples-CSharp-AsposePDF-Images-CreateThumbnailImages-CreateThumbnailImages.cs" >}}

{{% alert color="primary" %}}

- תודה ל-CodeProject על [יצירת תמונת ממוזער ממסמך PDF](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- תודה ל-Acrobat על [המדריך ל-SDK של Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

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

