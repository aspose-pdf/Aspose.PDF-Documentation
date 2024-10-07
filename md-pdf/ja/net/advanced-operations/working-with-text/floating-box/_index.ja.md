---
title: テキスト生成のためのFloatingBoxの使用
linktitle: FloatingBoxの使用
type: docs
weight: 30
url: /net/floating-box/
description: このページでは、フローティングボックス内でテキストをフォーマットする方法について説明します。
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

この機能は[Aspose.PDF.Drawing](/pdf/net/drawing/)ライブラリでも動作します。

## FloatingBoxツールの基本

Floating Boxツールは、PDFページ上にテキストやその他のコンテンツを配置するための特殊なツールです。その主な特徴は、FloatingBoxのサイズを超えるとテキストがクリッピングされることです。

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

上記の例では、幅400pt、高さ30ptのFloatingBoxを作成しています。
また、この例では、指定されたサイズに収まるよりも多くのテキストが意図的に作成されました。
その結果、テキストは切り取られました。

![Image 1](image01.png)

プロパティ `IsNeedRepeating` に `false` の値を設定すると、テキストは1ページに制限されます。

このプロパティを `true` に設定すると、テキストは次のページに同じ位置で再流されます。

![Image 2](image02.png)

## FloatingBoxの高度な機能

### マルチカラムサポート

#### マルチカラムレイアウト（簡単なケース）

`FloatingBox`はマルチカラムレイアウトをサポートしています。このようなレイアウトを作成するには、ColumnInfoプロパティの値を定義する必要があります。

* `ColumnWidths` はptで列挙された幅の文字列です。
* `ColumnSpacing` は列間の隙間の幅の文字列です。
* `ColumnCount` は列の数です。

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
上記の例では、追加のライブラリLoremNETを使用し、20の段落を作成しました。これらの段落は3つのカラムに分けられ、テキストが尽きるまで次のページに埋められました。

#### 複数カラムレイアウトでの強制的なカラム開始

前の例と同じことを次の例で行います。違いは、3つの段落を作成したことです。FloatingBoxを使って各段落を新しいカラムにレンダリングするように強制することができます。それを行うためには、FloatingBoxオブジェクトにテキストを追加するときに`IsFirstParagraphInColumn`を設定する必要があります。

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
### 背景サポート

望ましい背景色を `BackgroundColor` プロパティを使用して設定できます。

```cs
// ドキュメントオブジェクトの初期化
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

### オフセットサポート

FloatingBoxは `Top` と `Left` の値を設定することによって別の位置にシフトできます。

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

