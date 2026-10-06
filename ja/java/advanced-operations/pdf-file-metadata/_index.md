---
title: "Java での PDF ファイル メタデータの操作"
linktitle: PDF ファイル メタデータ
type: docs
weight: 200
url: /ja/java/pdf-file-metadata/
description: "Aspose.PDF を使用して、Java で PDF ファイル メタデータ、ドキュメント情報、XMP プロパティの抽出、更新、および管理方法を学習してください。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF ドキュメント情報と XMP メタデータの取得および設定"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF メタデータを操作する方法を説明します。著者、タイトル、キーワードなどのドキュメント情報を読み取り、ファイル プロパティを更新し、PDF バージョンと権限を確認し、XMP メタデータ フィールドを設定し、DOM API およびファサード API の両方を通じてメタデータを保存する方法を学習します。"
---
Aspose.PDF for Java は、メタデータを操作するための主に 2 つの方法を提供します。

- DOM API を介して `Document`、`DocumentInfo`、および `document.getMetadata()` を使用します。
- ファサード API を通じて `PdfFileInfo` を使用します。

## PDF ファイル情報の取得

著者、タイトル、サブジェクト、キーワードなどの標準的なドキュメント情報フィールドを読み取る必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) オブジェクトにアクセスしてください。
1. 必要なメタデータフィールドを読み取り、その値を出力してください。

```java
public static void getPdfFileInformation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();

        System.out.println("Author: " + docInfo.getAuthor());
        System.out.println("Creation Date: " + docInfo.getCreationDate());
        System.out.println("Keywords: " + docInfo.getKeywords());
        System.out.println("Modify Date: " + docInfo.getModDate());
        System.out.println("Subject: " + docInfo.getSubject());
        System.out.println("Title: " + docInfo.getTitle());
    }
}
```

## 名前空間プレフィックスでメタデータの設定

登録された名前空間プレフィックスを使用して `XMP` プロパティを追加または更新する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要な XMP 名前空間を登録し、メタデータ項目を追加してください。
1. 更新された文書を保存してください。

```java
public static void setPrefixMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().registerNamespaceUri("xmp", "http://ns.adobe.com/xap/1.0/");
        document.getMetadata().addItem("xmp:ModifyDate", OffsetDateTime.now().toString());
        document.save(outputFile.toString());
    }
    System.out.println("Prefix metadata saved to " + outputFile);
}
```

## ドキュメント情報フィールドの更新

作者、タイトル、製作者、作成日などの標準的な PDF ファイルプロパティを書き込む場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/documentinfo/) にアクセスし、新しいメタデータ値を割り当ててください。
1. 更新されたファイル情報でドキュメントを保存してください。

```java
public static void setFileInformation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        DocumentInfo docInfo = document.getInfo();
        Date now = new Date();

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(now);
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(now);
        docInfo.setSubject("PDF Information");
        docInfo.setTitle("Setting PDF Document Information");
        docInfo.setProducer("Custom producer");
        docInfo.setCreator("Custom creator");

        document.save(outputFile.toString());
    }
    System.out.println("File information saved to " + outputFile);
}
```

## XMP メタデータ プロパティの設定

追加の XMP エントリやカスタムメタデータ値を保存する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要な XMP メタデータ項目を `document.getMetadata()` に追加してください。
1. 出力ファイルを保存してください。

```java
public static void setXmpMetadata(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getMetadata().addItem("xmp:CreateDate", OffsetDateTime.now().toString());
        document.getMetadata().addItem("xmp:Nickname", "Nickname");
        document.getMetadata().addItem("xmp:CustomProperty", "Custom Value");
        document.save(outputFile.toString());
    }
    System.out.println("XMP metadata saved to " + outputFile);
}
```
