---
title: יצירת PDF/3-A תואם PDF וצירוף חשבונית ZUGFeRD ב-C#
linktitle: צירוף ZUGFeRD ל-PDF
type: docs
weight: 10
url: /net/attach-zugferd/
description: למד כיצד ליצור מסמך PDF עם ZUGFeRD ב-Aspose.PDF עבור .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## צירוף ZUGFeRD ל-PDF

הקטע קוד הבא עובד גם עם ספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

אנו ממליצים לבצע את השלבים הבאים כדי לצרף ZUGFeRD ל-PDF:

* הגדר משתנה נתיב המצביע לתיקייה בה נמצאים קבצי ה-PDF לקלט ולפלט.
* צור אובייקט מסמך על ידי טעינת קובץ PDF קיים (לדוגמא "ZUGFeRD-test.pdf") מהנתיב.
* צור אובייקט [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) על ידי ספק את הנתיב ותיאור של קובץ אחר בשם "factur-x.xml", המכיל מטא-נתונים של חשבונית התואמים לתקן ZUGFeRD.
* הוסף תכונות לאובייקט המפרט הקובץ, כגון התיאור, סוג MIME, ויחס AF.
* הוסף תכונות לאובייקט מפרט הקובץ, כמו התיאור, סוג MIME, והקשר AF.
* הוסף את אובייקט מפרט הקובץ לאוסף הקבצים המוטמעים במסמך. שם הקובץ צריך להיות מצוין לפי תקן ZUGFeRD, לדוגמה "factur-x.xml".
* המר את המסמך לפורמט PDF/A-3U, תת-קבוצה של PDF המבטיחה שימור ארוך טווח של מסמכים אלקטרוניים. PDF/A-3U מאפשר הטמעת קבצים מכל פורמט במסמכי PDF.
* שמור את המסמך המומר כקובץ PDF חדש (לדוגמה, "ZUGFeRD-res.pdf").

```cs
var path = @"C:\Samples\ZUGFeRD\";

var document = new Aspose.Pdf.Document(Path.Combine(path,"ZUGFeRD-test.pdf"));
// Setup new file to be added as attachment
var description = "מטא נתונים של חשבונית התואמת לתקן ZUGFeRD";
var fileSpecification = new Aspose.Pdf.FileSpecification(Path.Combine(path, "factur-x.xml"), description)
{
    Description = "Zugferd",
    MIMEType = "text/xml",
    AFRelationship = Aspose.Pdf.AFRelationship.Alternative
};
// Add attachment to document's attachment collection
document.EmbeddedFiles.Add(fileSpecification);
document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.PDF_A_3U, Aspose.Pdf.ConvertErrorAction.Delete);
document.Save(Path.Combine(path, "ZUGFeRD-res.pdf"));
```
המתודה convert לוקחת זרם, פורמט PDF ופעולת שגיאת המרה כפרמטרים. פרמטר הזרם יכול לשמש לשמירת יומן ההמרה. פרמטר פעולת שגיאת ההמרה מציין מה לעשות אם מתרחשות שגיאות במהלך ההמרה. במקרה זה, הוא מוגדר כ"מחיקה", שפירושו שכל האלמנטים שאינם תואמים לפורמט PDF/A-3U יימחקו מהמסמך.
