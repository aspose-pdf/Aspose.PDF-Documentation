---
title: "PDF から添付ファイルの抽出"
linktitle: "添付ファイルの抽出"
type: docs
weight: 50
url: /ja/java/extract-attachment/
description: Java と Aspose.PDF を使用して、PDF ドキュメントから埋め込みファイルおよびファイル添付注釈を抽出する方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用して PDF から単一またはすべての埋め込みファイルの抽出"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ドキュメントから添付ファイルを抽出する方法を説明します。単一の名前付き添付ファイルの抽出、すべての埋め込みファイルを出力フォルダーに保存、ファイルメタデータの読み取り、およびページ上の FileAttachment アノテーションからコンテンツをエクスポートする方法をカバーしています。
---
Aspose.PDF for Java は、添付ファイルがドキュメント内でどのように保存されているかに応じて、いくつかの抽出フローをサポートしています。

## 名前で単一の添付ファイルの抽出

PDF から特定の埋め込みファイルを 1 つ保存する必要がある場合にこの例を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要な添付ファイル名が見つかるまで、埋め込みファイルコレクションを反復処理してください。
1. 添付ストリームを出力ファイルにコピーし、抽出後に停止してください。

```java
public static void extractSingleAttachment(Path inputFile, String attachmentName, Path outputFile) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Extracting attachment: " + attachmentName);

        boolean attachmentFound = false;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            if (attachmentName.equals(fileSpecification.getName())) {
                try (InputStream inputStream = fileSpecification.getContents();
                     OutputStream outputStream = Files.newOutputStream(outputFile)) {
                    inputStream.transferTo(outputStream);
                }
                System.out.println("Attachment extracted successfully");
                attachmentFound = true;
                break;
            }
        }

        if (!attachmentFound) {
            throw new IllegalArgumentException("Attachment '" + attachmentName + "' not found in PDF");
        }
    }
}
```

## 埋め込みファイルのパラメータの印刷

このヘルパーメソッドは、格納されたメタデータを出力します [FileParams](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileparams/) オブジェクト。

1. ファイルパラメータオブジェクトが存在するかどうかを確認してください。
1. 利用可能なチェックサム、作成日、変更日、およびサイズの値を読み取ってください。
1. コンソールに値を出力してください。

```java
public static void printFileParams(FileParams params) {
    if (params != null) {
        try {
            System.out.println("CheckSum: " + params.getCheckSum());
        } catch (Exception ex) {
            System.out.println("CheckSum: null");
        }
        System.out.println("Creation Date: " + params.getCreationDate());
        System.out.println("Modification Date: " + params.getModDate());
        System.out.println("Size: " + params.getSize());
    }
}
```

## 埋め込み添付ファイルのすべてを抽出

この例は、PDF 内のすべての埋め込みファイルを出力ディレクトリに書き出す必要がある場合に使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 埋め込みファイルコレクションを反復処理し、各アイテムに対して安全な出力ファイル名を決定してください。
1. メタデータを出力し、各添付ストリームを保存し、すべてのファイルがエクスポートされるまで処理を続行してください。

```java
public static void extractAttachments(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        System.out.println("Total files: " + document.getEmbeddedFiles().size());

        int fileIndex = 1;
        for (FileSpecification fileSpecification : document.getEmbeddedFiles()) {
            String fileName = fileSpecification.getName();
            if (fileName == null || fileName.isBlank()) {
                fileName = fileSpecification.getUnicodeName();
            }
            if (fileName == null || fileName.isBlank()) {
                fileName = "attachment_" + fileIndex + ".bin";
            }

            System.out.println("Name: " + fileName);
            System.out.println("Description: " + fileSpecification.getDescription());
            System.out.println("Mime Type: " + fileSpecification.getMIMEType());
            printFileParams(fileSpecification.getParams());

            Path outputPath = outputDir.resolve(fileName);
            try (InputStream inputStream = fileSpecification.getContents();
                 OutputStream outputStream = Files.newOutputStream(outputPath)) {
                inputStream.transferTo(outputStream);
            }
            fileIndex++;
        }
    }
}
```

## ファイル添付注釈の抽出

埋め込みファイルコレクションだけでなく、ページ注釈を介してファイルが添付されている場合にこの例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページ上に最初の [FileAttachmentAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/fileattachmentannotation/) を検索してください。
1. そのファイル仕様を読み取り、内容をエクスポートし、宛先パスを出力してください。

```java
public static void extractFileAttachmentAnnotation(Path inputFile, Path outputDir) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        FileAttachmentAnnotation fileAttachment = null;
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.FileAttachment) {
                fileAttachment = (FileAttachmentAnnotation) annotation;
                break;
            }
        }

        if (fileAttachment == null) {
            System.out.println("File attachment annotation not found.");
            return;
        }

        FileSpecification fileSpecification = fileAttachment.getFile();
        System.out.println("File name: " + fileSpecification.getName());

        Path outputPath = outputDir.resolve("extracted-" + fileSpecification.getName());
        try (InputStream inputStream = fileSpecification.getContents();
             OutputStream outputStream = Files.newOutputStream(outputPath)) {
            inputStream.transferTo(outputStream);
        }

        System.out.println("Extracted to: " + outputPath);
    }
}
```
