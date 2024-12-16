---
title: PDFから添付ファイルを削除する
linktitle: 既存のPDFから添付ファイルを削除する
type: docs
weight: 30
url: /ja/cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF for C++はPDFドキュメントから添付ファイルを削除できます。C++ PDF APIを使用してPDFファイルから添付ファイルを削除するには、Aspose.PDFライブラリを使用します。
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDFはPDFファイルから添付ファイルを削除できます。PDFドキュメントの添付ファイルは、DocumentオブジェクトのEmbeddedFilesコレクションに保持されています。

PDFファイルに関連付けられたすべての添付ファイルを削除するには:

1. [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection)コレクションの[Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection#afff8b235b554a66c203464b61204b843)メソッドを呼び出します。
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトのSaveメソッドを使用して更新されたファイルを保存します。

以下のコードスニペットは、PDFドキュメントから添付ファイルを削除する方法を示しています。

```cpp
void WorkingWithAttachments::RemovingAttachment() {

 String _dataDir("C:\\Samples\\");

 // ドキュメントを開く
 auto pdfDocument = new Document(_dataDir + u"DeleteAllAttachments.pdf");

 // すべての添付ファイルを削除
 pdfDocument->get_EmbeddedFiles()->Delete();

 // 更新されたファイルを保存
 pdfDocument->Save(_dataDir + u"DeleteAllAttachments_out.pdf");
}
```