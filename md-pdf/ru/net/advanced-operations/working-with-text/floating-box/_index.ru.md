---
title: Использование FloatingBox для генерации текста
linktitle: Использование FloatingBox
type: docs
weight: 30
url: /net/floating-box/
description: Эта страница объясняет, как форматировать текст внутри плавающего блока.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

Эта функция также работает в библиотеке [Aspose.PDF.Drawing](/pdf/net/drawing/).

## Основы использования инструмента FloatingBox

Инструмент Floating Box - это специальный инструмент для размещения текста и другого содержимого на странице PDF. Его основная особенность - обрезка текста, когда он выходит за размеры FloatingBox.

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

В приведенном выше примере мы создаем FloatingBox шириной 400 pt и высотой 30 pt.
Также в этом примере было намеренно создано больше текста, чем могло поместиться в заданном размере.
В результате текст был обрезан.

![Image 1](image01.png)

Свойство `IsNeedRepeating` со значением `false` ограничивает текст одной страницей.

Если мы установим это свойство в `true`, текст будет перенесен на следующую страницу в той же позиции.

![Image 2](image02.png)

## Расширенные возможности FloatingBox

### Поддержка многоколоночного вывода

#### Многоколоночное расположение (простой случай)

`FloatingBox` поддерживает многоколоночное расположение. Чтобы создать такое расположение, вы должны определить значения свойств ColumnInfo.

* `ColumnWidths` - строка с перечислением ширины в pt.
* `ColumnSpacing` - строка с шириной зазора между колонками.
* `ColumnCount` - количество колонок.

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
Мы использовали дополнительную библиотеку LoremNET в приведенном выше примере и создали 20 абзацев. Эти абзацы были разделены на три колонки и заполнили следующие страницы, пока текст не закончился.

#### Макет многостолбцовой компоновки с принудительным началом колонки

Мы сделаем то же самое с следующим примером, как и в предыдущем. Разница в том, что мы создали 3 абзаца. Мы можем заставить FloatingBox отрисовывать каждый абзац в новой колонке. Для этого нам нужно установить `IsFirstParagraphInColumn` при добавлении текста в объект FloatingBox.

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
### Поддержка фона

Вы можете установить желаемый цвет фона, используя свойство `BackgroundColor`.

```cs
// Инициализация объекта документа
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

### Поддержка смещения

FloatingBox может быть смещён в другое место, установив значения `Top` и `Left`.

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

