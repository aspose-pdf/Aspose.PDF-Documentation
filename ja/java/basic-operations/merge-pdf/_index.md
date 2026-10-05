---
title: "Java での PDFファイルの結合"
linktitle: "PDFファイルの結合"
type: docs
weight: 50
url: /ja/java/merge-pdf/
description: Aspose.PDF を使用して、Javaで複数の PDF ファイルを 1 つの文書に結合する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Javaを使用して PDF ページを結合
Abstract: この記事では、Aspose.PDF を使用して Javaで 2 つの PDF ドキュメントを結合する方法を説明します。例では、2 つのソースドキュメントを開き、2 番目のドキュメントのページを最初のドキュメントに追加し、結合された結果を新しい PDF ファイルとして保存します。
---
PDF ファイルを結合することは、配布、アーカイブ、または処理のために関連する文書を 1 つのファイルにまとめる必要がある場合に便利です。

## ライブ例

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) ブラウザでPDF結合をテストするための無料オンラインアプリケーションです。

このトピックでは、Javaで複数のPDFファイルを単一のドキュメントに結合する方法を示します。

1. 次のもので両方のソースドキュメントを開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) コンストラクタ。
1. 追加 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 2番目のコレクションから [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 最初のものに `document1.getPages().add(document2.getPages())`。
1. マージしたものを保存 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 出力パスへ。

## 2つのPDFドキュメントの結合

次の Java の例は `MergeDocumentExamples.java`.

```java
public static void mergeTwoDocuments(Path inputFile1, Path inputFile2, Path outputFile) {
    try (Document document1 = new Document(inputFile1.toString());
         Document document2 = new Document(inputFile2.toString())) {
        document1.getPages().add(document2.getPages());
        document1.save(outputFile.toString());
    }
}
```
