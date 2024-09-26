---
title: הגדר הרשאות, הצפן ופענח קובץ PDF
linktitle: הצפן ופענח קובץ PDF
type: docs
weight: 20
url: /net/set-privileges-encrypt-and-decrypt-pdf-file/
description: הצפן קובץ PDF ב-C# באמצעות סוגי הצפנה ואלגוריתמים שונים. כמו כן, פענח קבצי PDF באמצעות סיסמת בעלים.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "הגדר הרשאות, הצפן ופענח קובץ PDF",
    "alternativeHeadline": "איך להצפין ולפענח קובץ PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמך PDF",
    "keywords": "pdf, c#, הצפנת pdf, פענוח pdf",
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
    "url": "/net/set-privileges-encrypt-and-decrypt-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/set-privileges-encrypt-and-decrypt-pdf-file/"
    },
    "dateModified": "2022-02-04",
    "description": "הצפן קובץ PDF ב-C# באמצעות סוגי הצפנה ואלגוריתמים שונים. כמו כן, פענח קבצי PDF באמצעות סיסמת בעלים."
}
</script>
הקוד הבא עובד גם עם הספרייה [Aspose.PDF.Drawing](/pdf/net/drawing/).

## הגדרת הרשאות על קובץ PDF קיים

כדי להגדיר הרשאות על קובץ PDF, יש ליצור אובייקט של המחלקה [DocumentPrivilege](https://reference.aspose.com/pdf/net/aspose.pdf.facades/documentprivilege) ולציין את הזכויות שברצונך להחיל על המסמך. לאחר שההרשאות הוגדרו, העבר את האובייקט הזה כארגומנט למתודת [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) של אובייקט ה[Document](https://reference.aspose.com/pdf/net/aspose.pdf). הקטע הבא מראה איך להגדיר את הרשאות של קובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// טעינת קובץ PDF מקורי
using (Document document = new Document(dataDir + "input.pdf"))
{
    // יצירת אובייקט הרשאות מסמך
    // החלת הגבלות על כל ההרשאות
    DocumentPrivilege documentPrivilege = DocumentPrivilege.ForbidAll;
    // אפשר קריאה במסך בלבד
    documentPrivilege.AllowScreenReaders = true;
    // הצפנת הקובץ עם סיסמת משתמש ובעלים.
    // יש להגדיר את הסיסמה, כך שכאשר המשתמש יצפה בקובץ עם סיסמת משתמש,
    // תהיה אפשרות קריאה במסך בלבד
    document.Encrypt("user", "owner", documentPrivilege, CryptoAlgorithm.AESx128, false);
    // שמירת המסמך המעודכן
    document.Save(dataDir + "SetPrivileges_out.pdf");
}
```
## הצפנת קובץ PDF באמצעות סוגים ואלגוריתמים שונים של הצפנה

תוכלו להשתמש במתודת [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1) של אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) כדי להצפין קובץ PDF. תוכלו להעביר את סיסמת המשתמש, סיסמת הבעלים והרשאות למתודת [Encrypt](https://reference.aspose.com/pdf/net/aspose.pdf.document/encrypt/methods/1). בנוסף לכך, תוכלו להעביר כל ערך של איחוד [CryptoAlgorithm](https://reference.aspose.com/pdf/net/aspose.pdf/cryptoalgorithm). האיחוד הזה מספק שילובים שונים של אלגוריתמי הצפנה וגדלי מפתחות. תוכלו להעביר את הערך שבחרתם. לבסוף, שמרו את קובץ ה-PDF המוצפן באמצעות מתודת [Save](https://reference.aspose.com/pdf/net/aspose.pdf.document/save/methods/4) של אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>נא לציין סיסמאות שונות למשתמש ולבעלים בעת הצפנת קובץ ה-PDF.

- **סיסמת המשתמש**, אם הוגדרה, היא מה שתצטרכו לספק כדי לפתוח PDF.
- **סיסמת המשתמש**, אם הוגדרה, היא מה שנדרש להזנה כדי לפתוח קובץ PDF.
- **סיסמת הבעלים**, אם הוגדרה, שולטת בהרשאות כמו הדפסה, עריכה, חילוץ, הערת תגובה וכו'. Acrobat/Reader ימנעו פעולות אלו בהתאם להגדרות ההרשאות. Acrobat ידרוש את הסיסמה הזו אם תרצה להגדיר/לשנות הרשאות.

הקטע קוד הבא מראה איך להצפין קבצי PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לבקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// פתיחת מסמך
Document document = new Document(dataDir+ "Encrypt.pdf");
// הצפנת PDF
document.Encrypt("user", "owner", 0, CryptoAlgorithm.RC4x128);
dataDir = dataDir + "Encrypt_out.pdf";
// שמירת ה-PDF המעודכן
document.Save(dataDir);
```

## פענוח קובץ PDF באמצעות סיסמת בעלים

לאורך זמן, משתמשים מחליפים קבצי PDF מוצפנים כדי למנוע גישה לא מורשית למסמכים, כגון הדפסה/העתקה/שיתוף/חילוץ מידע על תוכן קובץ ה-PDF.
מתמיד, משתמשים מחליפים קבצי PDF מוצפנים כדי למנוע גישה לא מורשית למסמכים, כגון הדפסה/העתקה/שיתוף/חילוץ מידע על תוכן הקובץ PDF.
בהקשר זה, קיימת צורך לגשת לקובץ PDF מוצפן, מאחר שגישה כזו יכולה להתקבל רק על ידי משתמש מורשה. כמו כן, אנשים מחפשים פתרונות שונים לפענוח קבצי PDF באינטרנט.

עדיף לפתור את הבעיה הזו פעם אחת באמצעות שימוש בספריית Aspose.PDF.

על מנת לפענח את קובץ ה-PDF, יש ליצור תחילה אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) ולפתוח את ה-PDF באמצעות סיסמת הבעלים.
כדי לפענח את קובץ ה-PDF, תחילה עליך ליצור אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document) ולפתוח את ה-PDF באמצעות סיסמת הבעלים.

```csharp
// לדוגמאות מלאות וקבצי נתונים, אנא עבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// פתיחת מסמך
Document document = new Document(dataDir+ "Decrypt.pdf", "password");
// פענוח PDF
document.Decrypt();
dataDir = dataDir + "Decrypt_out.pdf";
// שמירת PDF מעודכן
document.Save(dataDir);
```

## שינוי סיסמה של קובץ PDF

אם ברצונך לשנות את הסיסמה של קובץ PDF, תחילה עליך לפתוח את קובץ ה-PDF באמצעות סיסמת הבעלים באמצעות אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).
אם אתה רוצה לשנות את הסיסמה של קובץ PDF, תחילה עליך לפתוץ את הקובץ ה-PDF באמצעות סיסמת בעלים באמצעות אובייקט [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document).

>- סיסמת משתמש, אם הוגדרה, היא מה שעליך לספק כדי לפתוח PDF. Acrobat/Reader יבקש מהמשתמש להזין את סיסמת המשתמש. אם היא לא נכונה, המסמך לא ייפתח.
>- סיסמת בעלים, אם הוגדרה, שולטת בהרשאות, כגון הדפסה, עריכה, חילוץ, הערות ועוד. Acrobat/Reader ימנעו דברים אלו בהתאם להגדרות ההרשאות. Acrobat ידרוש את הסיסמה הזו אם תרצה לקבוע/לשנות הרשאות.

הקטע קוד הבא מראה לך איך לשנות את הסיסמה של קובץ PDF.

```csharp
// לדוגמאות מלאות וקבצי נתונים, בקר ב https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

// פתח מסמך
Document document = new Document(dataDir+ "ChangePassword.pdf", "owner");
// שנה סיסמה
document.ChangePasswords("owner", "newuser", "newowner");
dataDir = dataDir + "ChangePassword_out.pdf";
// שמור PDF מעודכן
document.Save(dataDir);
```
## איך לקבוע אם ה-PDF מוגן בסיסמה

**Aspose.PDF for .NET** מספק יכולות מעולות לעבודה עם מסמכי PDF. כאשר משתמשים במחלקת Document מתוך המרחב השם Aspose.PDF לפתיחת מסמך PDF המוגן בסיסמה, עלינו לספק את מידע הסיסמה כארגומנט לבנאי Document ובמקרה שמידע זה לא מוסר, הודעת שגיאה נוצרת. למעשה, כאשר מנסים לפתוח קובץ PDF עם אובייקט Document, הבנאי מנסה לקרוא את תוכן הקובץ PDF ובמקרה שהסיסמה הנכונה לא מועברת, הודעת שגיאה נוצרת (זה קורה כדי למנוע גישה לא מורשית למסמך).

כאשר מתמודדים עם קבצי PDF מוצפנים, יתכן שתתעניינו לגלות אם ל-PDF יש סיסמת פתיחה ו/או סיסמת עריכה.
כאשר אתה מתמודד עם קבצי PDF מוצפנים, ייתכן שתתקל בתרחיש בו יהיה לך עניין לזהות אם ל-PDF יש סיסמת פתיחה ו/או סיסמת עריכה.

### קבל מידע על אבטחת מסמך PDF

PdfFileInfo מכיל שלוש תכונות לקבלת מידע על אבטחת מסמך PDF.

1. property PasswordType מחזיר ערך של אנומרציה PasswordType:
    - PasswordType.None - המסמך אינו מוגן בסיסמה
    - PasswordType.User - המסמך נפתח עם סיסמת משתמש (או סיסמת פתיחת מסמך)
    - PasswordType.Owner - המסמך נפתח עם סיסמת בעלים (או סיסמת הרשאות, עריכה)
    - PasswordType.Inaccessible - המסמך מוגן בסיסמה אך נדרשת סיסמה לפתיחתו בעוד שסיסמה לא תקינה (או שלא הוזנה סיסמה) הוזנה.
2. boolean property HasOpenPassword - משמש לקביעה אם קובץ הקלט דורש סיסמה בעת פתיחתו.
3. boolean property HasEditPassword - משמש לקביעה אם קובץ הקלט דורש סיסמה לעריכת התוכן שלו.

### קבע את הסיסמה הנכונה ממערך
### קביעת הסיסמה הנכונה ממערך

לעיתים קיים דרישה לקבוע את הסיסמה הנכונה מתוך מערך של סיסמאות ולפתוח את המסמך עם הסיסמה הנכונה. קטע הקוד הבא מדגים את השלבים לעבור על המערך של סיסמאות ולנסות לפתוח את המסמך עם הסיסמה הנכונה.

```csharp
// לדוגמאות מלאות וקבצי נתונים, נא לעבור ל https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// הנתיב לתיקיית המסמכים.
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
// טעינת קובץ PDF מקורי
PdfFileInfo info = new PdfFileInfo();
info.BindPdf(dataDir + "IsPasswordProtected.pdf");
// קביעה אם ה-PDF המקורי מוצפן
Console.WriteLine("File is password protected " + info.IsEncrypted);
String[] passwords = new String[5] { "test", "test1", "test2", "test3", "sample" };
for (int passwordcount = 0; passwordcount < passwords.Length; passwordcount++)
{
    try
    {
        Document doc = new Document(dataDir + "IsPasswordProtected.pdf", passwords[passwordcount]);
        if (doc.Pages.Count > 0)
            Console.WriteLine("Number of Page in document are = " + doc.Pages.Count);
    }
    catch (InvalidPasswordException)
    {
        Console.WriteLine("Password = " + passwords[passwordcount] + "  is not correct");
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

