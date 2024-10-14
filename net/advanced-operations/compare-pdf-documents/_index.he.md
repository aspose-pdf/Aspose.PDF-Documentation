---
title: השוואת מסמכי PDF
linktitle: השוואת PDF 
type: docs
weight: 180
url: /net/compare-pdf-documents/
description: החל מגרסה 24.7 ניתן להשוות תוכן מסמכי PDF עם סימוני הערות ופלט צד לצד
lastmod: "2024-08-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## השוואת מסמכי PDF עם Aspose.PDF עבור .NET

כאשר עובדים עם מסמכי PDF, ישנם מקרים בהם יש להשוות את תוכן שני מסמכים כדי לזהות הבדלים. ספריית Aspose.PDF עבור .NET מספקת ערכת כלים חזקה למטרה זו. במאמר זה, נחקור כיצד להשוות מסמכי PDF באמצעות כמה קטעי קוד פשוטים.

הפונקציונליות של השוואה ב-Aspose.PDF מאפשרת להשוות שני מסמכי PDF עמוד אחר עמוד. ניתן לבחור להשוות עמודים מסוימים או מסמכים שלמים. מסמך ההשוואה שנוצר מדגיש הבדלים, וכך מקל לזהות שינויים בין שני הקבצים.

### השוואת עמודים מסוימים

הקטע קוד הראשון מדגים כיצד להשוות את העמודים הראשונים של שני מסמכי PDF.

שלבים:

1. הפעלת מסמך.
הקוד מתחיל באתחול שני מסמכי PDF באמצעות נתיבי הקבצים שלהם (documentPath1 ו-documentPath2). הנתיבים מצוינים כמחרוזות ריקות כרגע, אך בפועל יש להחליף אותם בנתיבי הקבצים הממשיים.
2. תהליך השוואה.
- בחירת דף - ההשוואה מוגבלת לדף הראשון של כל מסמך ('Pages[1]').
- אפשרויות השוואה:

'AdditionalChangeMarks = true' - אפשרות זו מבטיחה שסימני שינוי נוספים יוצגו. סימנים אלו מדגישים הבדלים שעשויים להיות קיימים בדפים אחרים, גם אם הם אינם על הדף הנוכחי שמתבצעת בו ההשוואה.

'ComparisonMode = ComparisonMode.IgnoreSpaces' - מצב זה מורה למשווה להתעלם מרווחים בטקסט, ולהתמקד רק בשינויים בתוך המילים.

3. 
```

```cs
    string documentPath1 = "";
    string documentPath2= "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1.Pages[1], document2.Pages[1], resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

### השוואת מסמכים שלמים

הקטע השני מרחיב את ההיקף כדי להשוות את תוכן שני מסמכי PDF במלואם.

שלבים:

1. אתחול מסמך.
בדיוק כמו בדוגמה הראשונה, שני מסמכי PDF מאותחלים עם נתיבי הקבצים שלהם.
2. תהליך ההשוואה.
- השוואת מסמך שלם - בניגוד לקטע הראשון, קוד זה משווה את כל תוכן שני המסמכים.
- אפשרויות השוואה - האפשרויות זהות לקטע הראשון, תוך התעלמות מרווחים והצגת סימני שינוי נוספים.

3.
```cs
    string documentPath1 = "";
    string documentPath2 = "";

    string resultPdfPath ="";

    using (Document document1 = new Document(documentPath1), document2 = new Document(documentPath2))
    {
        SideBySidePdfComparer.Compare(document1, document2, resultPdfPath, new SideBySideComparisonOptions()
        {
            AdditionalChangeMarks = true,
            ComparisonMode = ComparisonMode.IgnoreSpaces
        });
    }
```

תוצאות ההשוואה שנוצרות על ידי קטעי הקוד הללו הן מסמכי PDF שניתן לפתוח בתוכנת צפייה כמו Adobe Acrobat. אם תשתמש בתצוגה דו-עמודית ב-Adobe Acrobat, תראה את השינויים זה לצד זה:

- מחיקות - מצוינות בעמוד השמאלי.
- הוספות - מצוינות בעמוד הימני.

על ידי הגדרת 'AdditionalChangeMarks' ל-'true', תוכל גם לראות סימונים לשינויים שעשויים להתרחש בעמודים אחרים, גם אם השינויים אינם על העמוד הנצפה כרגע.

**Aspose.PDF for .NET** מספק כלים חזקים להשוואת מסמכי PDF, בין אם אתה צריך להשוות עמודים מסוימים או מסמכים שלמים.

**Aspose.PDF for .NET** מספק כלים עמידים להשוואת מסמכי PDF, בין אם אתה צריך להשוות דפים מסוימים או מסמכים שלמים.
