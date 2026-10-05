---
title: "Java を使用した PDF ファイルからベクトル データの抽出"
linktitle: "PDF からベクトル データの抽出"
type: docs
weight: 80
url: /ja/java/extract-vector-data-from-pdf/
description: Aspose.PDF は、PDF ファイルからベクトル データを簡単に抽出できるようにします。位置や矩形の境界、SVG 出力などのベクトル データを取得できます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
## PDF ドキュメントからベクトル データにアクセスする

使用 `GraphicsAbsorber` ページ上のベクタ画像要素を検査し、その基本的な形状情報をテキストファイルに書き出す。

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) を作成し、対象に訪問する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ベクトルグラフィック操作を収集するために。
1. 抽出されたものを反復処理する [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) オブジェクトを取得し、矩形、位置、および演算子コレクションを読み取ります。
1. 各要素について、ジオメトリとオペレーター カウントの詳細を含む出力テキストを作成してください。
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

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. ターゲットを取得 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ドキュメントから。
1. 呼び出し `page.trySaveVectorGraphics(outputFile.toString())` そのページのベクトルグラフィックコンテンツを直接 SVG にエクスポートしてください。

```java
public static void saveVectorGraphicsToSvg(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);
        page.trySaveVectorGraphics(outputFile.toString());
    }
}
```

## 抽出された各要素を個別の SVG に保存する

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) を作成し、対象に訪問する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. ファイルを書き込む前に、抽出されたサブパス用の出力ディレクトリを作成してください。
1. 抽出されたものを反復処理する [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) オブジェクトと呼び出し `saveToSvg(...)` 各要素について。
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

## 抽出した要素を1つのSVGに結合する

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) を作成し、対象に訪問する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 結合されたベクトルフラグメントを含むSVGラッパーのマークアップを作成してください。
1. 抽出されたものを反復処理する [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) オブジェクトを取得し、生成された各SVGフラグメントを追加してください。
1. 結合されたSVG出力をターゲットファイルに書き込む。

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

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. [GraphicsAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicsabsorber/) を作成し、対象に訪問する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 必要なものを取得する [GraphicElement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/graphicelement/) 抽出された要素コレクションから。
1. 選択された要素が...かどうか確認します。 [XFormPlacement](https://reference.aspose.com/pdf/java/com.aspose.pdf.vector/xformplacement/) 必要に応じてその入れ子要素に降りていきます。
1. 選択したベクトル要素を出力SVGファイルに保存してください。

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
