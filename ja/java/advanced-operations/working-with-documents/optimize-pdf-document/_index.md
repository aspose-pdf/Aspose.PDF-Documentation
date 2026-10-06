---
title: "Java での PDF ファイルの最適化"
linktitle: "PDF の最適化"
type: docs
weight: 30
url: /ja/java/optimize-pdf/
description: "Aspose.PDF を使用して、Java で PDF ファイルのサイズを最適化・圧縮・削減する方法を学習します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF リソースの圧縮とファイルサイズ削減"
Abstract: "この記事では、Aspose.PDF for Java を使用した PDF ファイルの最適化方法を説明します。内容には、ドキュメント全体の最適化、リソースの圧縮、画像品質の低減、未使用のオブジェクトおよびストリームの削除、重複ストリームのリンク、フォントのアンエンベッド、アノテーションおよびフォームのフラット化、グレースケール変換、および Flate 画像圧縮が含まれます。"
---
Aspose.PDF for Java では、`Document.optimize`、`optimizeResources`、および `OptimizationOptions` を通じて最適化機能を提供します。

## 一般的なドキュメント最適化による PDF の最適化

この例は、Aspose.PDF が組み込みの全体文書最適化ルーチンを適用したいときに使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. `optimize()` をドキュメントに対して呼び出してください。
1. 最適化されたファイルを保存し、元のサイズと出力サイズを比較してください。

```java
public static void optimizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimize();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## リソースの最適化による PDF サイズの削減

この例は、個々のオプションを手動で構成せずにリソースレベルの最適化に焦点を当てています。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. `optimizeResources()` を実行して内部リソースを最適化してください。
1. 結果を保存し、入力ファイルと出力ファイルのサイズを表示してください。

```java
public static void reduceSizePdf(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        document.optimizeResources();
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## PDF 内のすべての画像の圧縮

画像が多い文書で、ファイルサイズを小さくし、ある程度の画像品質低下が許容できる場合にこのアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) を作成し、必要な品質レベルで画像圧縮を有効にしてください。
1. それらの設定でドキュメント リソースを最適化してください。
1. 最適化されたファイルを保存し、ファイルサイズを比較してください。

```java
public static void shrinkingOrCompressingAllImages(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.getImageCompressionOptions().setCompressImages(true);
        optimizeOptions.getImageCompressionOptions().setImageQuality(50);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## PDF から未使用のオブジェクトの削除

この例は、編集やマージの後にドキュメント構造に残る可能性のある未使用オブジェクトを削除します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) オブジェクトを作成し、未使用オブジェクトの削除を有効にしてください。
1. リソースを最適化し、更新されたファイルを保存してください。
1. 元のファイルサイズと縮小されたファイルサイズを印刷してください。

```java
public static void removingUnusedObjects(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedObjects(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## PDF から未使用のストリームの削除

ドキュメントで参照されなくなったストリームデータを破棄したい場合に、このアプローチを使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) を設定し、未使用のストリームを削除するようにしてください。
1. リソースを最適化し、出力文書を保存して、ファイルサイズを比較してください。

```java
public static void removingUnusedStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setRemoveUnusedStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## PDF の重複ストリームのリンク

この例では、繰り返しのストリームを重複排除し、同一のコンテンツを一度だけ保存できるようにします。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) を作成し、重複ストリームリンクを有効にしてください。
1. リソースを最適化し、出力ドキュメントを保存し、ファイルサイズを表示してください。

```java
public static void linkingDuplicateStreams(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setLinkDuplicateStreams(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## PDF からフォントの埋め込みの解除

ファイルサイズの削減が、出力で埋め込みフォントデータを保持することよりも重要な場合にこのオプションを使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) を設定し、フォントの埋め込みを解除してください。
1. リソースを最適化し、ドキュメントを保存し、ファイルサイズを比較してください。

```java
public static void unembedFonts(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizeOptions = new OptimizationOptions();
        optimizeOptions.setUnembedFonts(true);
        document.optimizeResources(optimizeOptions);
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## PDF 注釈のフラット化

この例では、注釈を静的なページ コンテンツに変換し、インタラクティブなオブジェクトとして残らないようにします。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 各 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) オブジェクトとその [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) コレクションを繰り返し処理してください。
1. すべての注釈をフラット化し、更新されたドキュメントを保存してください。

```java
public static void flattenAnnotations(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            for (Annotation annotation : page.getAnnotations()) {
                annotation.flatten();
            }
        }
        document.save(outputFile.toString());
    }
}
```

## PDF フォーム フィールドのフラット化

配布やアーカイブの前に、入力可能なフォーム フィールドを固定コンテンツにする必要がある場合は、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ドキュメントにフォームウィジェットが含まれているか確認してください。
1. 各 [Field](https://reference.aspose.com/pdf/java/com.aspose.pdf/field/) オブジェクトを、[WidgetAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/widgetannotation/) で表されるものとしてフラット化してください。
1. 出力ファイルを保存し、ファイルサイズを表示してください。

```java
public static void flattenForms(Path inputFile, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getForm() != null && document.getForm().size() > 0) {
            for (WidgetAnnotation annotation : document.getForm()) {
                if (annotation instanceof Field field) {
                    field.flatten();
                }
            }
        }
        document.save(outputFile.toString());
    }
    printFileSizes(inputFile, outputFile);
}
```

## PDF のグレースケールへの変換

この例では、各ページをグレースケールに変更します。これにより、色の複雑さを減らし、アーカイブや印刷ワークフロー向けの出力を標準化するのに役立ちます。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 各 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) オブジェクトをドキュメント内で繰り返し処理してください。
1. すべてのページで `makeGrayscale()` を呼び出して、出力ファイルを保存してください。

```java
public static void convertPdfFromRgbColorspaceToGrayscale(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Page page : document.getPages()) {
            page.makeGrayscale();
        }
        document.save(outputFile.toString());
    }
}
```

## FlateDecode 画像圧縮の使用

PDF リソース最適化時に画像に Flate ベースの圧縮を適用したい場合は、このパターンを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/optimizationoptions/) を作成し、画像エンコーディングを [ImageEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/imageencoding/).`Flate` に設定してください。
1. ドキュメントのリソースを最適化し、出力ファイルを保存してください。

```java
public static void usingFlatedecodeCompression(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        OptimizationOptions optimizationOptions = new OptimizationOptions();
        optimizationOptions.getImageCompressionOptions().setEncoding(ImageEncoding.Flate);
        document.optimizeResources(optimizationOptions);
        document.save(outputFile.toString());
    }
}
```

## 元のファイルサイズと最適化されたファイルサイズの印刷

このヘルパーメソッドは、ソースファイルと最適化された出力ファイルのサイズ差を報告します。

1. 入力ファイルのサイズを読み取ってください。
1. 出力ファイルのサイズを読み取ってください。
1. 単一のステータスメッセージで両方の値を出力してください。

```java
private static void printFileSizes(Path inputFile, Path outputFile) throws Exception {
    System.out.println("Original file size: " + Files.size(inputFile)
            + ". Reduced file size: " + Files.size(outputFile));
}
```
