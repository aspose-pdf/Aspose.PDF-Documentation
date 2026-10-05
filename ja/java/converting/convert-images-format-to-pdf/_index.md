---
title: Javaで画像フォーマットをPDFに変換する
linktitle: 画像をPDFに変換する
type: docs
weight: 60
url: /ja/java/convert-images-format-to-pdf/
lastmod: "2026-10-05"
description: Java と Aspose.PDF を使用して、BMP、CGM、DICOM、PNG、TIFF、EMF、SVG、CDR などの画像フォーマットを PDF に変換する方法を学びましょう。
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Java で画像を PDF に変換する方法
Abstract: この記事では、Aspose.PDF for Java を使用して複数の画像フォーマットを PDF に変換する方法を解説します。CGM、SVG、CDR 入力に対するファイルタイプ固有のロードオプションと、新しい PDF ページへの画像の直接配置の両方をカバーしています。
---
Aspose.PDF for Java は多くのラスターおよびベクトル画像フォーマットを PDF ドキュメントに変換できます。

## BMP を PDF に変換

BMP 画像を PDF ドキュメントに配置する必要がある場合は、この例を使用してください。

1. 空のものを作成 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 出力PDFを保持してください。
1. 追加する [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) そして BMP を配置する `page.addImage(...)`。
1. 対象画像矩形を定義する [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) そのため、ラスター コンテンツが PDF ページ領域を埋めます。
1. 出力PDFファイルを保存してください。

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

1. ファイルパスを渡して CGM ソースを開く [`CgmLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cgmloadoptions/) ～へ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. ドキュメントの読み込み時に Aspose.PDF に CGM グラフィックスストリームを解釈させる。
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

1. 空のものを作成 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) PDF出力用に。
1. 作成する [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) オブジェクト、それを設定 [`ImageFileType`](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagefiletype/) へ `Dicom`、そしてソースファイルのパスを割り当てます。
1. 追加する [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) そして DICOM 画像をページの段落コレクションに追加してください。
1. 結果をPDFとして保存してください。

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

EMFファイルを主要なEMFロードパスを介してPDFに変換する必要がある場合は、この例を使用してください。

1. 空のものを作成 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) そして EMF ソースをバイナリストリームとして開いてください。
1. 追加する [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) そして余白をクリアして、EMF アートワークがページ全体を占められるようにしてください。
1. 作成する [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/), EMF ストリームをそれにバインドし、ページの段落コレクションに追加してください。
1. 出力PDFファイルを保存してください。

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

## 代替ワークフローでEMFをPDFに変換

代替の設定またはページ構成フローを使用して EMF コンテンツを変換する必要がある場合は、この例を使用してください。

1. Aspose.Imaging を使用して EMF ソースをロードし、PDF 配置の前にメモリ内 PNG ストリームにレンダリングしてください。
1. 空のものを作成 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) そして追加する [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 作成する [`Image`](https://reference.aspose.com/pdf/java/com.aspose.pdf/image/) 中間バイトストリームから取得し、ページに追加してください。
1. 変換されたPDFを保存してください。

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

GIF画像をPDFページに追加する必要がある場合は、この例を使用してください。

1. 空のものを作成 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) PDF出力用に。
1. 追加する [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) そして GIF を配置する `page.addImage(...)`。
1. 配置境界を定義します [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) 画像がページ領域全体を埋めます。
1. 出力PDFを保存してください。

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

## JPEGをPDFに変換

JPEG画像を1ページのPDFに変換する必要がある場合は、この例を使用してください。

1. 空のものを作成 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 出力 PDF 用に。
1. 追加する [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) JPEG画像を挿入して `page.addImage(...)`。
1. 使用 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) ラスター画像がページ座標にどのようにマッピングされるかを制御するために。
1. 生成されたPDFファイルを保存してください。

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

## PNG を PDF に変換

PNG画像をPDFドキュメントにラップする必要がある場合は、この例を使用してください。

1. 空のものを作成 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 変換出力用に。
1. 追加する [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) そしてPNG画像をそれに配置します `page.addImage(...)`。
1. 使用 [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) ページキャンバスに対して画像のサイズを調整してください。
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

## SVG を PDF に変換

SVG アートワークを PDF ドキュメント内にレンダリングする必要がある場合は、この例を使用してください。

1. ファイルパスを渡して SVG ソースを開く [`SvgLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/svgloadoptions/) ～へ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. Aspose.PDFにSVGマークアップを解析させ、ロード中に対応するPDFグラフィックスモデルを作成させます。
1. PDFの出力を対象のファイルパスに保存してください。

```java
public static void convertSvgToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new SvgLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## TIFF を PDF に変換

TIFF画像をPDFに変換する必要がある場合は、この例を使用してください。

1. 空のものを作成 [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) PDF出力用に。
1. 追加する [`Page`](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) そして TIFF 画像を配置する `page.addImage(...)`。
1. 配置領域を定義する [`Rectangle`](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) したがって、TIFF コンテンツはページ座標にマッピングされます。
1. 結果をPDFとして保存してください。

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

## CDR を PDF に変換

CorelDRAW CDR ファイルを PDF に変換する必要がある場合は、この例を使用してください。

1. ファイルパスを渡して CDR ソースを開き、 [`CdrLoadOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/cdrloadoptions/) ～へ [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. Aspose.PDF に CorelDRAW コンテンツを PDF ドキュメントモデルにロードさせます。
1. 変換された PDF ファイルを指定された出力パスに保存してください。

```java
public static void convertCdrToPdf(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString(), new CdrLoadOptions())) {
        document.save(outputFile.toString());
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
