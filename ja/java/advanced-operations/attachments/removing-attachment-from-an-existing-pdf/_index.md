---
title: "Java での PDF から添付ファイルの削除"
linktitle: "既存の PDF から添付ファイルの削除"
type: docs
weight: 30
url: /ja/java/removing-attachment-from-an-existing-pdf/
description: "Aspose.PDF を使用して Java で PDF ドキュメントから 1 つまたはすべての埋め込み添付ファイルを削除する方法を学習します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での プログラム的に PDF 添付ファイルの削除"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルから添付ファイルを削除する方法を示します。サンプルでは、キーで指定した単一の埋め込みファイルの削除と、更新されたドキュメントを保存する前に EmbeddedFiles コレクション全体をクリアする方法を実演しています。
---
PDF ドキュメントに保存された添付ファイルは、個別に、あるいは一括で `EmbeddedFiles` コレクションから削除できます。

## 単一の添付ファイルの削除

PDF から削除すべき名前付き埋め込みファイルが 1 つある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 埋め込みファイルコレクションからキーで添付ファイルを削除してください。
1. 更新された出力ドキュメントを保存してください。

```java
public static void removeAttachment(Path inputFile, String attachmentName, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().deleteByKey(attachmentName);
        document.save(outputFile.toString());
    }
}
```

## すべての添付ファイルの削除

埋め込みファイルコレクション全体をクリアする必要がある場合は、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 埋め込みファイルコレクションからすべての項目を削除してください。
1. クリーンアップされた出力ドキュメントを保存してください。

```java
public static void removeAllAttachments(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getEmbeddedFiles().delete();
        document.save(outputFile.toString());
    }
}
```
