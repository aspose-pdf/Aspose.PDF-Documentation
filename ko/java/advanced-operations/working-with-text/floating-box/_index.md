---
title: Java에서 PDF 레이아웃에 FloatingBox 사용
linktitle: FloatingBox 사용
type: docs
weight: 30
url: /java/floating-box/
description: Java를 사용하여 PDF 문서에서 텍스트 레이아웃, 다중 열 콘텐츠 및 정확한 위치 지정을 위해 FloatingBox를 사용하는 방법을 알아보세요.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Java를 사용하여 PDF에서 스타일이 지정된 FloatingBox 컨테이너 생성 및 배치
Abstract: 이 문서에서는 Java용 Aspose.PDF에서 FloatingBox를 사용하는 방법을 설명합니다. 테두리가 있는 부동 컨테이너에 텍스트 배치, 반복되는 다중 열 레이아웃 생성, 배경색 사용, 절대 오프셋 및 수평 또는 수직 정렬 옵션을 다룹니다.
---

Java용 Aspose.PDF는 `FloatingBox`을 사용하여 재사용 가능한 텍스트 컨테이너와 열 기반 레이아웃을 구축합니다.


## 
부동 상자 생성 및 추가



테두리가 있는 부동 컨테이너 내에 텍스트를 배치해야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
`FloatingBox`을 만들고 크기와 테두리를 설정하고 텍스트 내용을 추가합니다.

1. 
페이지에 상자를 추가하고 문서를 저장합니다.


```java
public static void createAndAddFloatingBox(Path outputFile) {
       try (Document document = new Document()) {
           Page page = document.getPages().add();

           FloatingBox box = new FloatingBox(400, 30);
           box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
           box.setNeedRepeating(false);
           String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
           box.getParagraphs().add(new TextFragment(phrase));

           page.getParagraphs().add(box);
           document.save(outputFile.toString());
       }
   }
```

## 
반복되는 다중 열 레이아웃 만들기



긴 텍스트가 하나의 부동 상자 안의 여러 열에 걸쳐 흘러야 하는 경우 이 예를 사용하십시오.


1. 
페이지를 만들고 여백을 구성합니다.

1. 
열 너비를 계산하고 `FloatingBox` 열 설정을 구성합니다.

1. 
반복되는 텍스트 조각을 상자에 추가하고 문서를 저장합니다.


```java
public static void multiColumnLayout(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            box.getParagraphs().add(new TextFragment(phrase));
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## 
각 조각을 열의 첫 번째 항목으로 시작



삽입된 각 조각이 새로운 열 흐름 세그먼트를 시작해야 하는 경우 이 예를 사용합니다.


1. 
페이지를 만들고 다중 열 `FloatingBox`을 구성합니다.

1. 
텍스트 조각을 생성하고 `setFirstParagraphInColumn(true)`으로 표시합니다.

1. 
페이지에 상자를 추가하고 PDF를 저장합니다.


```java
public static void multiColumnLayout2(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().setMargin(new MarginInfo(36, 18, 36, 18));

        int columnCount = 3;
        int spacing = 10;
        double width = page.getPageInfo().getWidth()
                - page.getPageInfo().getMargin().getLeft()
                - page.getPageInfo().getMargin().getRight()
                - (columnCount - 1) * spacing;
        double columnWidth = width / 3;

        FloatingBox box = new FloatingBox();
        box.setNeedRepeating(true);
        box.getColumnInfo().setColumnWidths(columnWidth + " " + columnWidth + " " + columnWidth);
        box.getColumnInfo().setColumnSpacing(String.valueOf(spacing));
        box.getColumnInfo().setColumnCount(3);

        String phrase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce quam odio, sollicitudin ac mauris vel, suscipit pellentesque nisi.";
        for (int i = 0; i < 10; i++) {
            TextFragment text = new TextFragment(phrase);
            text.setFirstParagraphInColumn(true);
            box.getParagraphs().add(text);
        }

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## 
배경색이 있는 부동 상자 추가



부동 컨테이너에 눈에 보이는 배경 채우기가 있어야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
`FloatingBox`을 만들고 배경색을 설정한 다음 텍스트를 추가합니다.

1. 
페이지에 상자를 놓고 문서를 저장합니다.


```java
public static void backgroundSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setBackgroundColor(Color.getLightGreen());
        box.setNeedRepeating(false);
        box.getParagraphs().add(new TextFragment("text example"));

        page.getParagraphs().add(box);
        document.save(outputFile.toString());
    }
}
```

## 
절대 오프셋을 사용하여 부동 상자 배치



부동 상자가 페이지의 정확한 오프셋에 나타나야 하는 경우 이 예를 사용하십시오.


1. 
페이지를 만들고 주변 텍스트 콘텐츠를 준비합니다.

1. 
`FloatingBox`을 만들고, 절대 위치를 설정하고, 위쪽 및 왼쪽 오프셋을 할당합니다.

1. 
페이지에 내용을 추가하고 문서를 저장합니다.


```java
public static void offsetSupport(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox box = new FloatingBox(400, 30);
        box.setTop(45);
        box.setLeft(15);
        box.setPositioningMode(ParagraphPositioningMode.Absolute);
        box.setBorder(new BorderInfo(BorderSide.All, 1.5f, Color.getDarkGreen()));
        box.getParagraphs().add(new TextFragment("text example 1"));

        page.getParagraphs().add(new TextFragment("text example 2"));
        page.getParagraphs().add(box);
        page.getParagraphs().add(new TextFragment("text example 3"));

        document.save(outputFile.toString());
    }
}
```

## 
부동 상자 내부의 텍스트 정렬



부동 상자가 동일한 수평 정렬로 다른 수직 정렬을 보여야 하는 경우 이 예를 사용하십시오.


1. 
새 PDF 문서를 만들고 페이지를 추가합니다.

1. 
서로 다른 정렬 설정을 사용하여 여러 `FloatingBox` 개체를 만듭니다.

1. 
페이지에 추가하고 결과를 저장합니다.

```java
public static void alignTextToFloat(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        FloatingBox floatBox = new FloatingBox(100, 100);
        floatBox.setVerticalAlignment(VerticalAlignment.Bottom);
        floatBox.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox.getParagraphs().add(new TextFragment("FloatingBox_bottom"));
        floatBox.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox);

        FloatingBox floatBox2 = new FloatingBox(100, 100);
        floatBox2.setVerticalAlignment(VerticalAlignment.Center);
        floatBox2.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox2.getParagraphs().add(new TextFragment("FloatingBox_center"));
        floatBox2.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox2);

        FloatingBox floatBox3 = new FloatingBox(100, 100);
        floatBox3.setVerticalAlignment(VerticalAlignment.Top);
        floatBox3.setHorizontalAlignment(HorizontalAlignment.Right);
        floatBox3.getParagraphs().add(new TextFragment("FloatingBox_top"));
        floatBox3.setBorder(new BorderInfo(BorderSide.All, Color.getBlue()));
        page.getParagraphs().add(floatBox3);

        document.save(outputFile.toString());
    }
}
```
