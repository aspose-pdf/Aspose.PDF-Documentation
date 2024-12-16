---
title: 既存のPDFから添付ファイルを削除する
linktitle: 既存のPDFから添付ファイルを削除する
type: docs
weight: 30
url: /ja/java/removing-attachment-from-an-existing-pdf/
description: Aspose.PDFはPDFドキュメントから添付ファイルを削除できます。Aspose.PDFライブラリを使用して、Java PDF APIでPDFファイルの添付ファイルを削除します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDFはPDFファイルから添付ファイルを削除できます。PDFドキュメントの添付ファイルは、DocumentオブジェクトのEmbeddedFilesコレクションに保持されています。

PDFドキュメントの添付ファイルは、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトの[EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection)コレクションに保持されています。

PDFファイルに関連付けられたすべての添付ファイルを削除するには:

1. [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection)コレクションのdelete(..)メソッドを呼び出します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの save メソッドを使用して、更新されたファイルを保存します。

次のコードスニペットは、PDF ドキュメントからすべての添付ファイルを削除する方法を示しています。

```java
   public static void DeleteAllAttachmentsFromPDF(){
  // ドキュメントを開く
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // すべての添付ファイルを削除
  pdfDocument.getEmbeddedFiles().delete();
  // 更新されたファイルを保存
  pdfDocument.save("output.pdf");

    }
```