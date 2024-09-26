---
title: ייצוא WebForms DataGridView ל-PDF
linktitle: ייצוא WebForms DataGridView ל-PDF
type: docs
weight: 20
url: /net/render-webforms-datagridview-to-pdf/
description: דוגמה זו מראה כיצד להשתמש בספריית Aspose.PDF כדי לייצר WebForm ל-PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## כיצד לייצא WebForm ל-PDF באמצעות Aspose.PDF/Aspose.HTML

### הקדמה

בדרך כלל, להמיר WebForm למסמך PDF נדרשים כלים נוספים. דוגמה זו מראה כיצד להשתמש בספריית Aspose.PDF כדי לייצר WebForm ל-PDF. רכיב Aspose Export GridView To Pdf Control כלול גם בדוגמה זו כדי להראות כיצד לייצר _בקרת GridView למסמך PDF._

## כיצד לייצר WebForm ל-PDF

הרעיון המקורי לייצור WebForm ל-PDF הוא ליצור מחלקת עזר, המורשת מ-[System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx), ולדרוס את שיטת Render.</em></p>

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // render web page for PDF document
    }
    else
    {
        // render web page in browser
        base.Render(writer);
    }
}
```
ישנם שני כלים של Aspose שניתן להשתמש בהם להפוך HTML ל-PDF:

- Aspose.PDF ל-.NET
- בקרת GridView לייצוא של Aspose (מבוססת על Aspose.PDF)

## קבצי מקור

בדוגמה זו יש לנו 2 דוחות הדגמה.

- _Default.aspx_ מדגים ייצוא ל-PDF באמצעות Aspose.PDF
- _Report2.aspx_ מדגים ייצוא ל-PDF באמצעות בקרת GridView לייצוא של Aspose (מבוססת על Aspose.PDF)

## קבצים נוספים

`Helpers\PdfPage.cs` - מכיל מחלקת עזר, המראה כיצד להשתמש ב-API של Aspose.PDF.

פרויקט Aspose.Pdf.GridViewExport מכיל בקרת GridView מורחבת להדגמה ב-`Report2.aspx`
