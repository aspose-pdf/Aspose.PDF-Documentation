---
title: "Java での 画像フォーマットの PDF への変換"
linktitle: "画像の PDF への変換"
type: docs
weight: 60
url: /ja/java/convert-images-format-to-pdf/
lastmod: "2026-10-06"
description: Java と Aspose.PDF を使用して、BMP、CGM、DICOM、PNG、TIFF、EMF、SVG、CDR などの画像フォーマットを PDF に変換する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Java で画像を PDF に変換する方法
Abstract: この記事では、Aspose.PDF for Java を使用して複数の画像フォーマットを PDF に変換する方法を解説します。CGM、SVG、CDR 入力に対するファイルタイプ固有のロードオプションと、新しい PDF ページへの画像の直接配置の両方をカバーしています。
---
Aspose.PDF for Java は、多くのラスターおよびベクトル画像フォーマットを PDF ドキュメントに変換できます。

## BMP を PDF に変換

BMP 画像を PDF ドキュメントに配置する必要がある場合は、この例を使用してください。

1. 空の [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトを作成し、出力 PDF を保持してください。
1. [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) オブジェクトを追加し、`page.addImage(...)` を使用して BMP を配置してください。
1. 対象画像矩形を [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) クラスで定義し、ラスター コンテンツが PDF ページ領域全体を埋めるようにしてください。
1. 出力 PDF ファイルを保存してください。

```java
public static void convertBmpToPdf(Path inputFile, Path outputFile) {
        try (Document document = new Document()) {
            try (Page page = document.getPages().add()) {
                page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
            }
            document.save(outputFile.toString());
        }
        System.out.println(inputFile + " converted into " + outputFile);
    }
```

## CGM を PDF に変換

CGM グラフィック ファイルを PDF に変換する必要がある場合は、この例を使用してください。

1. ファイルパスと [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) のコンストラクタに渡して、CGM ソースを開いてください。
1. ドキュメントの読み込み時に、Aspose.PDF に CGM グラフィックスストリームを解釈させてください。
1. 変換された PDF をターゲット出力パスに保存してください。

```java
public static void convertCgmToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CgmLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## DICOM を PDF に変換

医療用 DICOM 画像を PDF ドキュメントにラップする必要がある場合は、この例を使用してください。

1. 空の [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトを PDF 出力用に作成してください。
1. [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) オブジェクトを作成し、その [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) を `Dicom` に設定したうえで、ソースファイルのパスを割り当ててください。
1. [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加し、DICOM 画像をそのページの段落コレクションに追加してください。
1. 結果を PDF として保存してください。

```java
public static void convertDicomToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        Image image = new Image();
        image.setFileType(ImageFileType.Dicom);
        image.setFile(inputFile.toString());

        try (Page page = document.getPages().add()) {
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 直接文書をロードして EMF を PDF に変換

EMF ファイルを主要な EMF ロードパスを介して PDF に変換する必要がある場合は、この例を使用してください。

1. 空の [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、EMF ソースをバイナリストリームとして開いてください。
1. [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加し、余白をクリアして EMF アートワークがページ全体を占められるようにしてください。
1. [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) を作成し、EMF ストリームをそれにバインドして、ページの段落コレクションに追加してください。
1. 出力 PDF ファイルを保存してください。

```java
public static void convertEmfToPdf01(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         FileInputStream imageStream = new FileInputStream(inputFile.toFile())) {
        try (Page page = document.getPages().add()) {
            page.getPageInfo().getMargin().setBottom(0);
            page.getPageInfo().getMargin().setTop(0);
            page.getPageInfo().getMargin().setLeft(0);
            page.getPageInfo().getMargin().setRight(0);

            Image image = new Image();
            image.setFileType(ImageFileType.Unknown);
            image.setImageStream(imageStream);
            page.getParagraphs().add(image);
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 代替ワークフローで EMF を PDF に変換

代替の設定またはページ構成フローを使用して EMF コンテンツを変換する必要がある場合は、この例を使用してください。

1. Aspose.Imaging を使用して EMF ソースをロードし、PDF 配置の前にメモリ内 PNG ストリームにレンダリングしてください。
1. 空の [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、[`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加してください。
1. 中間バイトストリームから [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) を作成し、ページに追加してください。
1. 変換された PDF を保存してください。

```java
public static void convertEmfToPdf02(Path inputFile, Path outputFile) throws IOException {
    try (Document document = new Document();
         com.aspose.imaging.Image emfImage = com.aspose.imaging.Image.load(inputFile.toString());
         ByteArrayOutputStream byteArrayOutputStream = new ByteArrayOutputStream()) {
        emfImage.save(byteArrayOutputStream, new PngOptions());

        try (Page page = document.getPages().add()) {
            Image image = new Image();
            image.setImageStream(new ByteArrayInputStream(byteArrayOutputStream.toByteArray()));
            page.getParagraphs().add(image);
        }

        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## GIF を PDF に変換

GIF 画像を PDF ページに追加する必要がある場合は、この例を使用してください。

1. 空の [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトを PDF 出力用に作成してください。
1. [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加し、`page.addImage(...)` を使用して GIF を配置してください。
1. 配置境界を [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) で定義し、画像がページ領域全体を埋めるようにしてください。
1. 出力 PDF を保存してください。

```java
public static void convertGifToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## JPEG から PDF への変換

JPEG 画像を 1 ページの PDF に変換する必要がある場合は、この例を使用してください。

1. 空の [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を出力 PDF 用に作成してください。
1. [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加し、JPEG 画像を `page.addImage(...)` で挿入してください。
1. ラスター画像がページ座標にどのようにマッピングされるかを制御するために、[`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) を使用してください。
1. 生成された PDF ファイルを保存してください。

```java
public static void convertJpegToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PNG から PDF への変換

PNG 画像を PDF ドキュメントにラップする必要がある場合は、この例を使用してください。

1. 変換出力用に空の [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成してください。
1. [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加し、PNG 画像を `page.addImage(...)` で配置してください。
1. [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) を使用して、ページキャンバスに対して画像のサイズを調整してください。
1. 出力ファイルを保存してください。

```java
public static void convertPngToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## SVG から PDF への変換

SVG アートワークを PDF ドキュメント内にレンダリングする必要がある場合は、この例を使用してください。

1. ファイルパスと [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) のコンストラクタに渡して、SVG ソースを開いてください。
1. Aspose.PDF に SVG マークアップを解析させ、ロード中に対応する PDF グラフィックスモデルを作成させてください。
1. PDF の出力を対象のファイルパスに保存してください。

```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## TIFF から PDF への変換

TIFF 画像を PDF に変換する必要がある場合は、この例を使用してください。

1. 空の [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) オブジェクトを PDF 出力用に作成してください。
1. [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を追加し、`page.addImage(...)` を使用して TIFF 画像を配置してください。
1. 配置領域を [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) で定義し、TIFF コンテンツがページ座標にマッピングされるようにしてください。
1. 結果を PDF として保存してください。

```java
public static void convertTiffToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        try (Page page = document.getPages().add()) {
            page.addImage(inputFile.toString(), new Rectangle(0, 0, 595, 842, true));
        }
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## CDR から PDF への変換

CorelDRAW CDR ファイルを PDF に変換する必要がある場合は、この例を使用してください。

1. ファイルパスと [`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) のコンストラクタに渡して、CDR ソースを開いてください。
1. Aspose.PDF に CorelDRAW コンテンツを PDF ドキュメントモデルにロードさせてください。
1. 変換された PDF ファイルを指定された出力パスに保存してください。

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
