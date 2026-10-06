---
title: "Java で PDF を Word に変換"
linktitle: "PDF を Word に変換"
type: docs
weight: 10
url: /ja/java/convert-pdf-to-word/
lastmod: "2026-10-06"
description: Aspose.PDF を使用して、Java で PDF ファイルを DOC および DOCX に変換する方法を学び、文書の編集と再利用を容易にします。
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF から Word への変換"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルを Microsoft Word 形式に変換する方法を説明します。DOC 出力、DOCX 出力、拡張フロー DOCX 変換、改行の保持、箇条書きの認識、および `DocSaveOptions` による画像解像度の制御について解説します。
---
Aspose.PDF for Java では、さまざまな認識およびレイアウトオプションを使用して、PDF ドキュメントを Microsoft Word 形式にエクスポートできます。[`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) を使用して、PDF のテキスト、リスト、画像が Word 出力にどのようにマッピングされるかを制御してください。

## PDF から DOC への変換

PDF ドキュメントをレガシー DOC 形式にエクスポートする必要がある場合は、この例を使用してください。コードでは、`DocSaveOptions` を作成し、形式を `Doc` に設定したうえで、オプションを共有の保存メソッドに渡します。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) を作成し、出力形式を `Doc` に設定してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。その結果、PDF は Microsoft Word のバイナリ ドキュメント形式にエクスポートされます。
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

## PDF から DOCX への変換

PDF ドキュメントを DOCX ファイルとしてエクスポートする必要がある場合は、この例を使用してください。DOCX は広くサポートされており、編集が容易であるため、ほとんどの新しいワードプロセッシングワークフローで推奨される形式です。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) を作成し、出力形式を `DocX` に設定してください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出してください。これにより、PDF コンテンツが Office Open XML Word ドキュメントとしてエクスポートされます。
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

## 拡張フロー認識による PDF から DOCX への変換

Word のエクスポートで、固定された視覚レイアウトではなく、流れるような編集可能なコンテンツを優先すべき場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. `DocX` 出力用に [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) を作成してください。
1. コンバータが DOCX 生成中に高度なフロー認識を使用するように、`setMode(DocSaveOptions.RecognitionMode.EnhancedFlow)` を有効にしてください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出して、変換された DOCX 出力を保存してください。

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

## 改行を保持した PDF から DOCX への変換

ソース PDF の改行を Word 出力で保持する必要がある場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. `DocX` エクスポート用に [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) を作成してください。
1. 変換時に明示的な改行が保持されるように、`setAddReturnToLineEnd(true)` を有効にしてください。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出して、DOCX ファイルを保存してください。

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

## PDF から DOCX への変換と箇条書きの認識

ソース PDF のリスト箇条書きを認識し、Word でリスト構造として保持する必要がある場合に、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. `DocX` エクスポート用に [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) を作成してください。
1. `setRecognizeBullets(true)` を有効にしてください。これにより、リストのような PDF コンテンツが変換時に箇条書きリストとして認識されます。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出して、DOCX ファイルを保存してください。

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

## カスタム画像解像度で PDF の DOCX への変換

生成された DOCX 内の画像の忠実度を変換中に制御したい場合は、この例を使用してください。

1. ソース PDF を [`Document`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. `DocX` エクスポート用に [`DocSaveOptions`](https://reference.aspose.com/pdf/java/com.aspose.pdf/docsaveoptions/) を作成してください。
1. `setImageResolutionX(300)` および `setImageResolutionY(300)` を設定してください。これにより、ラスタ コンテンツが指定された解像度で生成されます。
1. `document.save(outputFile.toString(), saveOptions)` を呼び出して、DOCX 出力を保存してください。

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
