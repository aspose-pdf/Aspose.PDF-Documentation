---
title: استخدام FloatingBox لتوليد النص
linktitle: استخدام FloatingBox
type: docs
weight: 30
url: /net/floating-box/
description: تشرح هذه الصفحة كيفية تنسيق النص داخل صندوق عائم.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

هذه الميزة تعمل أيضًا في مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

## أساسيات استخدام أداة FloatingBox

أداة Floating Box هي أداة خاصة لوضع النصوص والمحتويات الأخرى على صفحة PDF. الميزة الرئيسية لها هي قص النص عندما يتداخل مع حجم الـFloatingBox.

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

في المثال أعلاه، نحن نقوم بإنشاء FloatingBox بعرض 400 نقطة وارتفاع 30 نقطة.
أيضًا، في هذا المثال، تم إنشاء نص أكثر مما يمكن أن يتسع في الحجم المحدد.
نتيجة لذلك، تم قطع النص.

![Image 1](image01.png)

خاصية `IsNeedRepeating` بقيمة `false` تحد من النص بصفحة واحدة.

إذا قمنا بتعيين هذه الخاصية إلى `true` فسيتم إعادة تدفق النص إلى الصفحة التالية في نفس الموضع.

![Image 2](image02.png)

## ميزات متقدمة لـFloatingBox

### دعم متعدد الأعمدة

#### تخطيط متعدد الأعمدة (حالة بسيطة)

`FloatingBox` يدعم تخطيط متعدد الأعمدة. لإنشاء مثل هذا التخطيط، يجب تحديد قيم خصائص ColumnInfo.

* `ColumnWidths` هي سلسلة بتعداد العرض بالنقاط.
* `ColumnSpacing` هي سلسلة بعرض الفجوة بين الأعمدة.
* `ColumnCount` هو عدد الأعمدة.

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
لقد استخدمنا مكتبة إضافية تُسمى LoremNET في المثال أعلاه وقمنا بإنشاء 20 فقرة. تم تقسيم هذه الفقرات إلى ثلاثة أعمدة وملأت الصفحات التالية حتى نفد النص.

#### تخطيط متعدد الأعمدة مع بدء العمود الإجباري

سنقوم بنفس الأمر في المثال التالي كما في السابق. الفرق هو أننا أنشأنا 3 فقرات. يمكننا إجبار FloatingBox على تقديم كل فقرة في عمود جديد. للقيام بذلك، نحتاج إلى تعيين `IsFirstParagraphInColumn` عند إضافة النص إلى كائن FloatingBox.

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
### دعم الخلفية

يمكنك تعيين لون الخلفية المطلوب باستخدام خاصية `BackgroundColor`.

```cs
// تهيئة كائن المستند
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

### دعم الإزاحة

يمكن تحريك FloatingBox إلى موقع آخر بضبط قيم `Top` و `Left`.

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

