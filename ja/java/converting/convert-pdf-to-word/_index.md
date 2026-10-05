---
title: JavaでPDFをWordに変換
linktitle: PDFをWordに変換
type: docs
weight: 10
url: /ja/java/convert-pdf-to-word/
lastmod: "2026-10-05"
description: Aspose.PDF を使用して、Java で PDF ファイルを DOC および DOCX に変換する方法を学び、文書の編集と再利用を容易にします。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF を Word に変換する方法
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルを Microsoft Word 形式に変換する方法を説明します。DOC 出力、DOCX 出力、拡張フロー DOCX 変換、改行の保持、箇条書きの認識、および `DocSaveOptions` による画像解像度の制御について解説します。
---
Aspose.PDF for Java は、さまざまな認識およびレイアウトオプションで PDF ドキュメントを Microsoft Word 形式にエクスポートできます。 Use [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) PDFのテキスト、リスト、画像がWord出力にどのようにマッピングされるかを制御するために。

## PDF を DOC に変換する

PDF ドキュメントをレガシー DOC 形式にエクスポートする必要があるときは、この例を使用してください。コードは作成します `DocSaveOptions`, 形式を設定します `Doc`, そしてオプションを共有保存メソッドに渡します。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) そして形式を設定します `Doc`。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` その結果、PDFはMicrosoft Wordのバイナリ ドキュメント形式にエクスポートされます。
1. 変換された DOC ファイルを保存してください。

```java
public static void convertPdfToDoc(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.Doc);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF を DOCX に変換

PDF ドキュメントを DOCX ファイルとしてエクスポートする必要がある場合は、この例を使用してください。DOCX は、広くサポートされており、編集が容易であるため、ほとんどの新しいワードプロセッシングワークフローで推奨される形式です。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) そして形式を設定します `DocX`。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` したがって、PDF コンテンツは Office Open XML Word ドキュメントとしてエクスポートされます。
1. 結果の DOCX ファイルを保存してください。

```java
public static void convertPdfToDocx(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## 拡張フロー認識によるPDFからDOCXへの変換

Word のエクスポートで、固定された視覚レイアウトではなく、流れるような編集可能なコンテンツを優先すべき場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) ために `DocX` 出力。
1. 有効にする `setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` そのため、コンバータは DOCX 生成中に高度なフロー認識を使用してください。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` 変換されたDOCX出力を保存してください。

```java
public static void convertPdfToDocxAdvanced(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setMode(DocSaveOptions.RecognitionMode.EnhancedFlow);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDF を DOCX に変換し、改行を保持する

ソースPDFの改行をWord出力で保持する必要がある場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) ために `DocX` エクスポート。
1. 有効にする `setAddReturnToLineEnd(true)` そのため、変換時に明示的な改行が保持されます。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そして DOCX ファイルを保存してください。

```java
public static void convertPdfToDocxWithLineBreaks(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setAddReturnToLineEnd(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## PDFをDOCXに変換し、箇条書きの認識を行う

ソースPDFのリスト箇条書きが認識され、Wordでリスト構造として保持されるべき場合にこの例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) ために `DocX` エクスポート。
1. 有効にする `setRecognizeBullets(true)` そのため、リストのような PDF コンテンツは変換時に箇条書きリストとして認識されます。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そして DOCX ファイルを保存してください。

```java
public static void convertPdfToDocxWithBulletRecognition(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setRecognizeBullets(true);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```

## カスタム画像解像度でPDFをDOCXに変換する

生成された DOCX 内の画像の忠実度を変換中に制御したい場合は、この例を使用してください。

1. ソースPDFを開く [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) ために `DocX` エクスポート。
1. 設定 `setImageResolutionX(300)` そして `setImageResolutionY(300)` そのため、ラスタ コンテンツは要求された解像度で生成されます。
1. 呼び出す `document.save(outputFile.toString(), saveOptions)` そして DOCX 出力を保存してください。

```java
public static void convertPdfToDocxWithImageResolution(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocSaveOptions saveOptions = new DocSaveOptions();
        saveOptions.setFormat(DocSaveOptions.DocFormat.DocX);
        saveOptions.setImageResolutionX(300);
        saveOptions.setImageResolutionY(300);
        document.save(outputFile.toString(), saveOptions);
    }
    System.out.println(inputFile + " converted into " + outputFile);
}
```
