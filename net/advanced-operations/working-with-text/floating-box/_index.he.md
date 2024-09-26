---
title: שימוש ב-FloatingBox ליצירת טקסט
linktitle: שימוש ב-FloatingBox
type: docs
weight: 30
url: /net/floating-box/
description: דף זה מסביר כיצד לעצב טקסט בתוך קופסה צפה.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

תכונה זו פועלת גם בספריית [Aspose.PDF.Drawing](/pdf/net/drawing/).

## יסודות שימוש בכלי FloatingBox

כלי ה-Floating Box הוא כלי מיוחד להצבת טקסט ותוכן אחר בעמוד PDF. התכונה העיקרית שלו היא חיתוך טקסט כאשר הוא חורג מגודל ה-FloatingBox.

```cs
Document document = new Document();
Page page = document.Pages.Add();
var box = new FloatingBox(400, 30)
{
    Border = new BorderInfo(BorderSide.All, 1.5f, Color.DarkGreen),
    IsNeedRepeating = false,
};
var text = LoremNET.Lorem.Paragraph(20, 6);
box.Paragraphs.Add(new TextFragment(text));
page.Paragraphs.Add(box);
```  

בדוגמה לעיל, אנו יוצרים FloatingBox ברוחב של 400 נקודות וגובה של 30 נקודות.
כמו כן, בדוגמה זו נוצר יותר טקסט ממה שיכול היה להתאים בגודל הנתון.
כתוצאה מכך, הטקסט נחתך.

![תמונה 1](image01.png)

תכונת `IsNeedRepeating` עם ערך `false` מגבילה את הטקסט לעמוד אחד.

אם נקבע את התכונה הזו ל-`true` הטקסט יופץ לעמוד הבא באותה המיקום.

![תמונה 2](image02.png)

## תכונות מתקדמות של FloatingBox

### תמיכה במרובה טורים

#### פריסת מרובה טורים (מקרה פשוט)

`FloatingBox` תומך בפריסת מרובה טורים. כדי ליצור פריסה כזו, עליך להגדיר את ערכי התכונות של ColumnInfo.

* `ColumnWidths` היא מחרוזת עם אימות של רוחב בנקודות.
* `ColumnSpacing` היא מחרוזת עם רוחב המרווח בין הטורים.
* `ColumnCount` הוא מספר הטורים.

```cs
Document document = new Document();
Page page = document.Pages.Add();
page.PageInfo.Margin = new MarginInfo(36, 18, 36, 18);
var columnCount = 3;
var spacing = 10;
var width = page.PageInfo.Width 
    - page.PageInfo.Margin.Left 
    - page.PageInfo.Margin.Right 
    - (columnCount - 1) * spacing;
var columnWidth = width / 3;
var box = a FloatingBox()
{
    IsNeedRepeating = true
};
box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
box.ColumnInfo.ColumnSpacing = "{spacing}";
box.ColumnInfo.ColumnCount = columnCount;
var paragraphs = LoremNET.Lorem.Paragraphs(20, 8, 20);
foreach (var paragraph in paragraphs)
{
    box.Paragraphs.Add(new TextFragment(paragraph));
}

page.Paragraphs.Add(box);

document.Save("sample.pdf");
```
השתמשנו בספריית LoremNET נוספת בדוגמא לעיל ויצרנו 20 פסקאות. פסקאות אלה חולקו לשלוש עמודות ומילאו את הדפים הבאים עד שהטקסט אזל.

#### פריסת עמודות מרובות עם התחלת עמודה מאולצת

נעשה את אותו הדבר עם הדוגמא הבאה כמו בקודמת. ההבדל הוא שיצרנו 3 פסקאות. אנו יכולים לכפות על FloatingBox להציג כל פסקה בעמודה חדשה. כדי לעשות זאת עלינו להגדיר `IsFirstParagraphInColumn` בעת הוספת טקסט לאובייקט FloatingBox.

```cs
Document document = new Document();
Page page = document.Pages.Add();
page.PageInfo.Margin = new MarginInfo(36, 18, 36, 18);
var columnCount = 3;
var spacing = 10;
var width = page.PageInfo.Width 
    - page.PageInfo.Margin.Left 
    - page.PageInfo.Margin.Right 
    - (columnCount - 1) * spacing;
var columnWidth = width / 3;
var box = new FloatingBox()
{
    IsNeedRepeating = true
};
box.ColumnInfo.ColumnWidths = $"{columnWidth} {columnWidth} {columnWidth}";
box.ColumnInfo.ColumnSpacing = "{spacing}";
box.ColumnInfo.ColumnCount = 3;

var paragraphs = LoremNET.Lorem.Paragraphs(20, 8, 3);
foreach (var paragraph in paragraphs)
{
    var text = new TextFragment(paragraph)
    {
        IsFirstParagraphInColumn = true
    };
    box.Paragraphs.Add(text);
}

page.Paragraphs.Add(box);

document.Save("sample.pdf");
```
### תמיכה ברקע

ניתן להגדיר צבע רקע רצוי באמצעות המאפיין `BackgroundColor`.

```cs
// Initialize document object
Document document = new Document();
Page page = document.Pages.Add();
var box = new FloatingBox(400, 60)
{
    IsNeedRepeating = false,
    BackgroundColor = Color.LightGreen,
};
var text = LoremNET.Lorem.Paragraph(20, 6);
box.Paragraphs.Add(new TextFragment(text));
page.Paragraphs.Add(box);
```

### תמיכה בהיסט

ניתן להזיז את FloatingBox למיקום אחר על ידי הגדרת הערכים `Top` ו-`Left`.

```cs
Document document = new Document();
Page page = document.Pages.Add();

var box = new FloatingBox()
{
    Top = -45,
    Left = 15,
    Border = new BorderInfo(BorderSide.All, 1.5f, Color.DarkGreen)
};
var text = LoremNET.Lorem.Paragraph(20, 6);
box.Paragraphs.Add(new TextFragment(text));

page.Paragraphs.Add(new TextFragment(LoremNET.Lorem.Paragraph(20, 6)));
page.Paragraphs.Add(box);            
page.Paragraphs.Add(new TextFragment(LoremNET.Lorem.Paragraph(20, 6)));
```

