---
title: "Java を使用した PDF ファイルからベクトル データの抽出"
linktitle: "PDF からベクトル データの抽出"
type: docs
weight: 80
url: /ja/java/extract-vector-data-from-pdf/
description: "Aspose.PDF を使用すると、PDF ファイルからベクトル データを簡単に抽出できます。位置や矩形の境界、SVG 出力などのベクトル データを取得できます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## PDF ドキュメントからベクトル データにアクセス

`GraphicsAbsorber` を使用して、ページ上のベクトル グラフィック要素を検査し、その基本的な形状情報をテキスト ファイルに書き出します。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) を作成し、対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を訪問してベクトル グラフィック操作を収集してください。
1. 抽出された [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) オブジェクトを反復処理し、各オブジェクトの矩形、位置、およびオペレーター コレクションを読み取ってください。
1. 各要素について、ジオメトリとオペレーター数の詳細を含む出力テキストを作成してください。
1. 抽出されたベクトル データを出力ファイルに書き込んでください。

```java
public static void extractGraphicsElements(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder text = new StringBuilder();
        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            text.append("Element ").append(index)
                    .append(": Rectangle = ").append(element.getRectangle())
                    .append(", Position = ").append(element.getPosition())
                    .append(", Operators = ").append(element.getOperators().size())
                    .append("\n");
            index++;
        }
        Files.writeString(outputFile, text.toString());
    }
}
```

## ページのベクターグラフィックを SVG に保存

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. ドキュメントからターゲットの [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を取得してください。
1. `page.trySaveVectorGraphics(outputFile.toString())` を呼び出して、そのページのベクトル グラフィック コンテンツを直接 SVG にエクスポートしてください。

```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## 抽出された各要素の個別の SVG への保存

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) を作成し、対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を訪問してください。
1. ファイルを書き込む前に、抽出されたサブパス用の出力ディレクトリを作成してください。
1. 抽出された [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) オブジェクトを反復処理し、各要素に対して `saveToSvg(...)` を呼び出してください。
1. 抽出されたすべての要素を個別の SVG ファイルに保存してください。

```java
public static void extractSubpathsToSvgs(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));
        Path subpathsDir = outputDir.resolve("subpaths");
        Files.createDirectories(subpathsDir);

        int index = 1;
        for (GraphicElement element : absorber.getElements()) {
            element.saveToSvg(subpathsDir.resolve("subpath_" + index + ".svg").toString());
            index++;
        }
    }
}
```

## 抽出した要素の1つのSVGへの結合

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) を作成し、対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を訪問してください。
1. 結合されたベクトルフラグメントを含む SVG ラッパーのマークアップを作成してください。
1. 抽出された [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) オブジェクトを反復処理し、生成された各 SVG フラグメントを追加してください。
1. 結合された SVG 出力をターゲットファイルに書き込んでください。

```java
public static void extractListOfElementsToSingleImage(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber absorber = new GraphicsAbsorber();
        absorber.visit(document.getPages().get_Item(1));

        StringBuilder svg = new StringBuilder();
        svg.append("<svg xmlns=\"http://www.w3.org/2000/svg\">\n");
        for (GraphicElement element : absorber.getElements()) {
            svg.append(element.saveToSvg()).append("\n");
        }
        svg.append("</svg>\n");
        Files.writeString(outputFile, svg.toString());
    }
}
```

## 単一のベクトル要素の抽出

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) を作成し、対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を訪問してください。
1. 必要な [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) を抽出された要素コレクションから取得してください。
1. 選択された要素が [XFormPlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/) であるかどうかを確認し、必要に応じてその入れ子要素に降りてください。
1. 選択したベクトル要素を出力 SVG ファイルに保存してください。

```java
public static void extractSingleVectorElement(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        GraphicsAbsorber graphicsAbsorber = new GraphicsAbsorber();
        Page page = document.getPages().get_Item(1);
        graphicsAbsorber.visit(page);
        if (graphicsAbsorber.getElements().size() > 1) {
            GraphicElement xformPlacement = graphicsAbsorber.getElements().get_Item(1);
            if (xformPlacement instanceof XFormPlacement) {
                XFormPlacement placement = (XFormPlacement) xformPlacement;
                if (placement.getElements().size() > 2) {
                    placement.getElements().get_Item(2).saveToSvg(outputFile.toString());
                }
            } else {
                xformPlacement.saveToSvg(outputFile.toString());
            }
        }
    }
}
```
