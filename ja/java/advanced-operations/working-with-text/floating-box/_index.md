---
title: "Java での PDFレイアウトにFloatingBoxの使用"
linktitle: "FloatingBoxの使用"
type: docs
weight: 30
url: /ja/java/floating-box/
description: Java を使用して PDF ドキュメントでテキスト レイアウト、マルチカラム コンテンツ、正確な位置決めに FloatingBox を使用する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Java を使用して PDF 内にスタイル付き FloatingBox コンテナを作成し、配置します。
Abstract: この記事では、Aspose.PDF for Java の FloatingBox の使い方について説明します。境界付きのフローティングコンテナにテキストを配置する方法、繰り返し可能な多列レイアウトの作成、背景色の使用、絶対オフセット、および水平または垂直の配置オプションについてカバーしています。
---
Aspose.PDF for Java は使用します `FloatingBox` 再利用可能なテキストコンテナと列ベースのレイアウトを構築するために。

## フローティングボックスを作成して追加する

テキストを枠付きのフローティングコンテナ内に配置する必要がある場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. 作成 `FloatingBox`, サイズと枠線を設定し、テキストコンテンツを追加してください。
1. ボックスをページに追加し、ドキュメントを保存してください。

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

## 繰り返しのマルチカラムレイアウトの作成

長いテキストが1つのフローティングボックス内で複数の列にまたがって流れる場合は、この例を使用してください。

1. ページを作成し、余白を設定してください。
1. 列幅を計算し、設定する `FloatingBox` 列設定。
1. 繰り返しテキストフラグメントをボックスに追加して、ドキュメントを保存してください。

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

## 各フラグメントを列の最初の項目として開始する

各挿入フラグメントが新しい列フロー セグメントを開始すべき場合は、この例を使用してください。

1. ページを作成し、マルチカラムを設定する `FloatingBox`。
1. テキストフラグメントを作成し、それにマークを付けます `setFirstParagraphInColumn(true)`。
1. ボックスをページに追加し、PDFを保存してください。

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

## 背景色付きのフローティングボックスの追加

浮動コンテナに可視的な背景塗りつぶしが必要な場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. 作成 `FloatingBox`、背景色を設定し、テキストを追加してください。
1. ボックスをページに配置し、ドキュメントを保存してください。

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

## 絶対オフセットで浮動ボックスの位置の設定

ページ上でフローティングボックスを正確なオフセットで表示する必要がある場合は、この例を使用してください。

1. ページを作成し、周囲のテキストコンテンツを準備してください。
1. 作成 `FloatingBox`, 絶対位置指定を設定し、上部と左側のオフセットを割り当てます。
1. コンテンツをページに追加して、ドキュメントを保存してください。

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

## フローティングボックス内のテキストを揃える

同じ水平配置で、異なる垂直配置を示す浮動ボックスの場合は、この例を使用してください。

1. 新しい PDF ドキュメントを作成し、ページを追加してください。
1. 複数作成 `FloatingBox` 異なる配置設定を持つオブジェクト。
1. それらをページに追加して結果を保存してください。

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
