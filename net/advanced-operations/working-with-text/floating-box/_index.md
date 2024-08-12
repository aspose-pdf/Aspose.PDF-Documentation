---
title: Using FloatingBox for text generation
linktitle: Using FloatingBox
type: docs
weight: 30
url: /net/floating-box/
description: This page explains how to format text inside floating box. 
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

This feature also work in [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

## Basics of using the FloatingBox tool

The Floating Box tool is a special tool for placing text and other content on a PDF page. Its main feature is text clipping when it overlaps the size of the FloatingBox.

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

In the example above, we are creating a FloatingBox with a width of 400 pt and a height of 30 pt.
Also, in this example, more text was intentionally created than could fit in the given size.
As a result, the text was cut off.

![Image 1](image01.png)

Property `IsNeedRepeating` with `false` vaule limit text with 1 page.

If we set this property to `true` the text will be reflow to the next page in the same position.

![Image 2](image02.png)

## Advanced features of FloatingBox

### Multi-column support

#### Multi-column layout (simple case)

`FloatingBox` supports multi-column layout. To create such a layout, you must define the values ​​of the ColumnInfo properties.

* `ColumnWidths` is a string with enumeration of width in pt.
* `ColumnSpacing` is a string with width of the gap between columns.
* `ColumnCount` is a number of columns.

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
box.ColumnInfo.ColumnCount = columnCount;
var paragraphs = LoremNET.Lorem.Paragraphs(20, 8, 20);
foreach (var paragraph in paragraphs)
{
    box.Paragraphs.Add(new TextFragment(paragraph));
}

page.Paragraphs.Add(box);

document.Save("sample.pdf");
```

We used the additional library LoremNET in the above example and created 20 paragraphs. These paragraphs were divided into three columns and filled the following pages until the text ran out.

#### Multi-column layout with forced column start

We will do the same with the following example as the previous one. The difference is that we created 3 paragraphs. We can force FloatingBox to render each paragraph in the new column. To do that we need to set `IsFirstParagraphInColumn` when we adding text to the FloatingBox object.

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

### Background support

You can set desired background color by using `BackgroundColor` property.

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

### Offset support

FloatingBox can be shifted to another location by setting the `Top` and `Left` values.

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
