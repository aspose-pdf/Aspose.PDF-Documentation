---
title: 텍스트 생성을 위한 FloatingBox 사용하기
linktitle: FloatingBox 사용하기
type: docs
weight: 30
url: ko/net/floating-box/
description: 이 페이지는 플로팅 박스 내부에서 텍스트를 포맷하는 방법에 대해 설명합니다.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

이 기능은 [Aspose.PDF.Drawing](/pdf/net/drawing/) 라이브러리에서도 작동합니다.

## FloatingBox 도구 사용 기초

Floating Box 도구는 PDF 페이지에 텍스트 및 기타 콘텐츠를 배치하기 위한 특별한 도구입니다. 주요 기능은 FloatingBox의 크기를 넘어서는 텍스트가 겹칠 때 텍스트를 자르는 것입니다.

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

위 예제에서는 폭이 400pt, 높이가 30pt인 FloatingBox를 생성하고 있습니다.
또한 이 예제에서는 주어진 크기에 맞지 않을 정도로 더 많은 텍스트가 의도적으로 생성되었습니다.
그 결과, 텍스트가 잘렸습니다.

![Image 1](image01.png)

속성 `IsNeedRepeating`을 `false` 값으로 설정하면 텍스트가 1페이지로 제한됩니다.

이 속성을 `true`로 설정하면 텍스트가 다음 페이지로 넘어가 같은 위치에서 다시 흐릅니다.

![Image 2](image02.png)

## FloatingBox의 고급 기능

### 다중 열 지원

#### 다중 열 레이아웃(간단한 경우)

`FloatingBox`는 다중 열 레이아웃을 지원합니다. 이러한 레이아웃을 생성하려면 ColumnInfo 속성의 값을 정의해야 합니다.

* `ColumnWidths`는 pt 단위로 열거된 폭을 나타내는 문자열입니다.
* `ColumnSpacing`은 열 사이의 간격을 나타내는 문자열입니다.
* `ColumnCount`는 열의 수입니다.

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
위의 예에서 LoremNET 추가 라이브러리를 사용하고 20개의 문단을 만들었습니다. 이 문단들은 세 개의 칼럼으로 나누어지고 다음 페이지들을 채울 때까지 텍스트가 소진될 때까지 채워졌습니다.

#### 강제 칼럼 시작을 가진 다중 칼럼 레이아웃

이전 예제와 마찬가지로 다음 예제도 수행할 것입니다. 차이점은 3개의 문단을 만들었다는 것입니다. 각 문단을 새로운 칼럼에 렌더링하도록 FloatingBox를 강제할 수 있습니다. 이를 위해 FloatingBox 객체에 텍스트를 추가할 때 `IsFirstParagraphInColumn`을 설정해야 합니다.

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
### 배경 지원

원하는 배경색을 `BackgroundColor` 속성을 사용하여 설정할 수 있습니다.

```cs
// 문서 객체 초기화
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

### 오프셋 지원

FloatingBox는 `Top`과 `Left` 값을 설정하여 다른 위치로 이동할 수 있습니다.

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

