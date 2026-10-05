---
title: "PDF 文書をプログラムで開く"
linktitle: "PDF を開く"
type: docs
weight: 20
url: /ja/java/open-pdf-document/
description: "ファイルパス、ストリーム、またはパスワードを使用して、Java で Aspose.PDF を利用して PDF ファイルを開く方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java で Aspose.PDF ライブラリを使用して PDF 文書を開く"
Abstract: この記事では、Aspose.PDF を使用して Java で既存の PDF ドキュメントを開く方法を示します。ファイルパスで PDF を開く方法、InputStream から PDF を開く方法、パスワードで保護されたドキュメントを開く方法について説明し、各例では読み込んだドキュメントのページ数を取得します。
---
Aspose.PDF for Java は、ソースデータの取得元に応じて既存の PDF ドキュメントを読み込む複数の方法をサポートしています。

## Java で PDF ドキュメントを開く

PDF ドキュメントを開くことができます。

1. ファイルパスから [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. `InputStream` から [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. パスワードを提供して暗号化された [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。

## ファイルからドキュメントを開く

```java
public static void openDocumentFromFile(Path inputFile) {
    Document document = new Document(inputFile.toString());
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```

## ストリームからドキュメントを開く

```java
public static void openDocumentFromStream(Path inputFile) throws Exception {
    try (InputStream stream = Files.newInputStream(inputFile)) {
        Document document = new Document(stream);
        System.out.println("Pages: " + document.getPages().size());
        document.close();
    }
}
```

## 暗号化されたドキュメントを開く

```java
public static void openDocumentEncrypted(Path inputFile) {
    Document document = new Document(inputFile.toString(), "P@ssw0rd");
    System.out.println("Pages: " + document.getPages().size());
    document.close();
}
```
