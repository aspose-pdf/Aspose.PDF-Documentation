---
title: "Java での PDF ファイルの結合"
linktitle: "PDF ファイルの結合"
type: docs
weight: 50
url: /ja/java/merge-pdf/
description: "Aspose.PDF を使用して、Java で複数の PDF ファイルを 1 つのドキュメントに結合する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用して PDF ページを結合"
Abstract: "この記事では、Aspose.PDF を使用して Java で 2 つの PDF ドキュメントを結合する方法を説明します。例では、2 つのソースドキュメントを開き、2 番目のドキュメントのページを最初のドキュメントに追加し、結合された結果を新しい PDF ファイルとして保存します。"
---
PDF ファイルを結合することは、配布、アーカイブ、または処理のために関連するドキュメントを 1 つのファイルにまとめる必要がある場合に便利です。

## ライブ例

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) は、ブラウザで PDF 結合をテストするための無料オンラインアプリケーションです。

このトピックでは、Java で複数の PDF ファイルを単一のドキュメントに結合する方法を示します。

1. 両方のソースドキュメントを [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタで開いてください。
1. 2 番目の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) から [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) コレクションを取得し、`document1.getPages().add(document2.getPages())` を使用して最初のドキュメントに追加してください。
1. マージした [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を出力パスに保存してください。

## 2 つの PDF ドキュメントの結合

次の Java の例は `MergeDocumentExamples.java` に基づいています。

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
