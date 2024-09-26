---
title: עבודה עם גרפיקה וקטורית
linktitle: עבודה עם גרפיקה וקטורית
type: docs
weight: 120
url: /net/working-with-vector-graphics/
description: המאמר מתאר את התכונות של עבודה עם כלי GraphicsAbsorber באמצעות C#.
lastmod: "2024-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "עבודה עם GraphicsAbsorber",
    "alternativeHeadline": "איך לקבל את מיקום התמונה בקובץ PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "יצירת מסמכי PDF",
    "keywords": "pdf, c#, GraphicsAbsorber ב-pdf",
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
    "url": "/net/working-with-vector-graphics/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-vector-graphics/"
    },
    "dateModified": "2022-02-04",
    "description": "הפרק מתאר את התכונות של עבודה עם קובץ PDF של GraphicsAbsorber באמצעות ספריית C#."
}
</script>
בפרק זה, נבחן איך להשתמש במחלקה החזקה `GraphicsAbsorber` כדי להתערב בגרפיקה וקטורית במסמכי PDF. בין אם אתה צריך להזיז, להסיר או להוסיף גרפיקה, המדריך הזה יראה לך איך לבצע את המשימות הללו ביעילות. בואו נתחיל!

## מבוא<a name="introduction"></a>

גרפיקה וקטורית היא רכיב קריטי במסמכי PDF רבים, המשמשת לייצוג תמונות, צורות ואלמנטים גרפיים אחרים. Aspose.PDF מספקת את מחלקת `GraphicsAbsorber`, שמאפשרת למפתחים לגשת ולשלוט בגרפיקה הזו באופן תכנותי. באמצעות שימוש במתודת `Visit` של `GraphicsAbsorber`, אתה יכול לחלץ גרפיקה וקטורית מדף מסוים ולבצע מגוון פעולות, כמו להזיז, להסיר או להעתיק אותם לדפים אחרים.

## 1. חילוץ גרפיקה עם `GraphicsAbsorber`<a name="extracting-graphics"></a>

השלב הראשון בעבודה עם גרפיקה וקטורית הוא לחלץ אותה ממסמך PDF. הנה איך אפשר לעשות זאת באמצעות מחלקת `GraphicsAbsorber`:

```csharp
public static void UsingGraphicsAbsorber()
{
    // שלב 1: יצירת אובייקט מסמך.
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");

    // שלב 2: יצירת מופע של GraphicsAbsorber.
    var graphicsAbsorber = new GraphicsAbsorber();

    // בחירת הדף הראשון של המסמך.
    var page = document.Pages[1];

    // שלב 3: שימוש במתודת `Visit` לחילוץ הגרפיקה מהדף.
    graphicsAbsorber.Visit(page);

    // הצגת מידע על האלמנטים שנחלצו.
    foreach (var element in graphicsAbsorber.Elements)
    {
        Console.WriteLine($"מספר דף: {element.SourcePage.Number}");
        Console.WriteLine($"מיקום: ({element.Position.X}, {element.Position.Y})");
        Console.WriteLine($"מספר מפעילים: {element.Operators.Count}");
    }
}
```
### הסבר:

1. **יצירת אובייקט מסמך**: אובייקט `Document` חדש מופעל עם הנתיב לקובץ PDF המטרה.
2. **יצירת מופע של `GraphicsAbsorber`**: מחלקה זו תופסת את כל אלמנטי הגרפיקה מדף נתון.
3. **שיטת ביקור**: השיטה `Visit` נקראת על הדף הראשון, מאפשרת ל`GraphicsAbsorber` לספוג את הגרפיקה הווקטורית.
4. **עיון באלמנטים שנשלפו**: הקוד עובר על כל אלמנט שנשלף, ומדפיס מידע כגון מספר עמוד, מיקום, ומספר האופרטורים הגרפיים המעורבים.

## 2. העברת גרפיקה

לאחר ששלפת את הגרפיקה, תוכל להעבירה למיקום אחר באותו עמוד. כך תוכל להשיג זאת:

```csharp
public static void MoveGraphics()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);

    // עצירה זמנית של עדכונים כדי לשפר ביצועים.
    graphicsAbsorber.SuppressUpdate();

    foreach (var element in graphicsAbsorber.Elements)
    {
        var position = element.Position;
        // הזזת הגרפיקה על ידי הזזת קואורדינטות ה- X ו- Y שלה.
        element.Position = new Point(position.X + 150, position.Y - 10);
    }

    // חידוש עדכונים והחלת שינויים.
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### נקודות מרכזיות:

- **SuppressUpdate**: שיטה זו משהה זמנית עדכונים כדי לשפר ביצועים בעת ביצוע מספר שינויים.
- **ResumeUpdate**: שיטה זו מחדשת את העדכונים ומחילה את השינויים שנעשו במיקומי הגרפיקה.
- **מיקום האלמנט**: מיקום כל גרפיק מותאם על ידי שינוי הקואורדינטות `X` ו-`Y` שלו.

## 3. הסרת גרפיקות<a name="removing-graphics"></a>

ישנם תרחישים בהם ייתכן שתרצה להסיר גרפיקות מסוימות מדף. Aspose.PDF מציעה שתי שיטות לביצוע זה:

### שיטה 1: באמצעות גבול מלבני

```csharp
public static void RemoveGraphicsMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    graphicsAbsorber.Visit(page);
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        // בדוק אם מיקום הגרפיק נמצא בתוך המלבן.
        if (rectangle.Contains(element.Position))
        {
            element.Remove(); // הסר את אלמנט הגרפיק.
        }
    }
    graphicsAbsorber.ResumeUpdate();
    document.Save("test.pdf");
}
```
### שיטה 2: שימוש באוסף של אלמנטים שהוסרו

```csharp
public static void RemoveGraphicsMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page = document.Pages[1];
    var rectangle = new Rectangle(70, 248, 170, 252);

    graphicsAbsorber.Visit(page);
    var removedElementsCollection = new GraphicElementCollection();
    foreach (var item in graphicsAbsorber.Elements.Where(el => rectangle.Contains(el.Position)))
    {
        removedElementsCollection.Add(item);
    }

    page.Contents.SuppressUpdate();
    page.DeleteGraphics(removedElementsCollection);
    page.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### הסבר:

- **Rectangle Boundary**: הגדרת אזור מלבני לצורך ציון אילו גרפיקות להסיר.
- **Suppress and Resume Updates**: מבטיח הסרה יעילה ללא עיבוד ביניים.

## 4. הוספת גרפיקה לדף אחר<a name="adding-graphics"></a>

גרפיקה שנבלעה מדף אחד ניתן להוסיף לדף אחר בתוך אותו מסמך.
גרפיקה שנקלטה מעמוד אחד ניתן להוסיף לעמוד אחר בתוך אותו מסמך.

### שיטה 1: הוספת גרפיקה באופן יחיד

```csharp
public static void AddToAnotherPageMethod1()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    foreach (var element in graphicsAbsorber.Elements)
    {
        element.AddOnPage(page2); // הוסף כל אלמנט גרפי לעמוד השני.
    }
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```

### שיטה 2: הוספת גרפיקה כאוסף

```csharp
public static void AddToAnotherPageMethod2()
{
    var document = new Document(@"C:\Samples\Sample-Document-01.pdf");
    var graphicsAbsorber = new GraphicsAbsorber();
    var page1 = document.Pages[1];
    var page2 = document.Pages[2];

    graphicsAbsorber.Visit(page1);
    page2.Contents.SuppressUpdate();
    page2.AddGraphics(graphicsAbsorber.Elements); // הוסף את כל הגרפיקות בבת אחת.
    page2.Contents.ResumeUpdate();
    document.Save("test.pdf");
}
```
### נקודות מרכזיות:

- **SuppressUpdate ו-ResumeUpdate**: שיטות אלה עוזרות לשמור על ביצועים בעת ביצוע שינויים המוניים.
- **AddOnPage לעומת AddGraphics**: השתמש ב-`AddOnPage` להוספות יחידות וב-`AddGraphics` להוספות המוניות.

## מסקנה

בפרק זה חקרנו איך להשתמש במחלקת `GraphicsAbsorber` לחילוץ, הזזה, הסרה והוספה של גרפיקה וקטורית במסמכי PDF באמצעות Aspose.PDF. על ידי שליטה בטכניקות אלה, תוכל לשפר משמעותית את המצגת הוויזואלית של ה-PDFs שלך וליצור מסמכים דינמיים ומושכים מבחינה חזותית.

אל תהסס להתנסות בדוגמאות הקוד ולהתאים אותן למקרי השימוש הספציפיים שלך. קידוד מהנה!

