---
title: "Java でのベクター グラフィックスの操作"
linktitle: ベクター グラフィックスの操作
type: docs
weight: 100
url: /ja/java/working-with-vector-graphics/
description: Java を使用して PDF ドキュメント内のベクターグラフィックスを抽出、移動、削除、コピー、エクスポートする方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF のベクターグラフィックスを検査および操作するために GraphicsAbsorber の使用"
Abstract: 本稿では、GraphicsAbsorber クラスを使用して Aspose.PDF for Java でベクターグラフィックスを操作する方法を説明します。ページ上のベクター要素を検査し、移動または削除し、ページ間でグラフィックスをコピーし、ベクターコンテンツを SVG にエクスポートする方法を学びます。
---
Aspose.PDF for Java はベクトル コンテンツを通じて `GraphicsAbsorber` および `GraphicElement` オブジェクトを公開します。これにより、ページ上の低レベルのベクトル要素を検査し、更新、削除、コピー、またはエクスポートすることができます。

## ページ上のベクターグラフィックスの検査

ベクトル要素を列挙し、ページ、位置、および演算子数を確認する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) を作成し、対象ページにアクセスしてください。
1. 吸収された [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) オブジェクトを反復処理し、そのプロパティを出力してください。

```java
public static void usingGraphicsAbsorber(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                System.out.println("Page Number: " + element.getSourcePage().getNumber());
                System.out.println("Position: (" + element.getPosition().getX() + ", "
                        + element.getPosition().getY() + ")");
                System.out.println("Number of Operators: " + element.getOperators().size());
            }
        } finally {
            graphicsAbsorber.dispose();
        }
    }
}
```

## ページ上のベクターグラフィックの移動

検出されたすべてのベクトル要素を新しい位置にシフトする必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 対象ページに [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) を使用してアクセスし、一時的に更新を抑制してください。
1. 吸収された各要素の位置を変更し、更新を再開してドキュメントを保存してください。

```java
public static void moveGraphics(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                Point position = element.getPosition();
                element.setPosition(new Point(position.getX() + 150, position.getY() - 10));
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics moved in " + outputFile);
}
```

## 要素削除による位置指定でのベクトルグラフィックの削除

特定の矩形内のベクトル要素を1つずつ削除する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページに [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) を使用してアクセスし、対象となる [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) を定義してください。
1. 一致する要素を削除し、更新を再開して、ドキュメントを保存してください。

```java
public static void removeGraphicsMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            graphicsAbsorber.suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    element.remove();
                }
            }
            graphicsAbsorber.resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 1 in " + outputFile);
}
```

## コレクションを削除してベクターグラフィックを削除

ベクトル要素のマッチングを最初に収集し、1ページの操作で削除する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページに [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) を適用し、一致する要素を収集してください。
1. ページの内容から収集されたグラフィックを削除し、更新されたドキュメントを保存してください。

```java
public static void removeGraphicsMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page = document.getPages().get_Item(1);
            Rectangle rectangle = new Rectangle(70, 248, 170, 252, true);
            graphicsAbsorber.visit(page);
            GraphicElementCollection removedElements = new GraphicElementCollection();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                if (rectangle.contains(element.getPosition(), false)) {
                    removedElements.add(element);
                }
            }
            page.getContents().suppressUpdate();
            page.deleteGraphics(removedElements);
            page.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics removed with method 2 in " + outputFile);
}
```

## ベクトルグラフィックを別ページへ要素ごとにコピー

各吸収されたベクトル要素を新しいページに個別に追加する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、宛先ページを追加してください。
1. ソースページに [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) を適用してください。
1. それぞれの [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicelement/) を宛先ページに追加し、ドキュメントを保存してください。

```java
public static void addToAnotherPageMethod1(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            for (GraphicElement element : graphicsAbsorber.getElements()) {
                element.addOnPage(page2);
            }
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 1 in " + outputFile);
}
```

## ベクタ画像を別のページにコレクションとしてコピー

吸収されたベクタ画像のコレクション全体を一度の呼び出しで別のページにコピーする必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、宛先ページを追加してください。
1. ソースページに [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/vector/graphicsabsorber/) を適用してください。
1. 吸収されたグラフィック コレクションを宛先ページに追加し、ドキュメントを保存してください。

```java
public static void addToAnotherPageMethod2(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        try {
            Page page1 = document.getPages().get_Item(1);
            Page page2 = document.getPages().add();
            graphicsAbsorber.visit(page1);
            page2.getContents().suppressUpdate();
            page2.addGraphics(graphicsAbsorber.getElements());
            page2.getContents().resumeUpdate();
        } finally {
            graphicsAbsorber.dispose();
        }
        document.save(outputFile.toString());
    }
    System.out.println("Vector graphics copied with method 2 in " + outputFile);
}
```
