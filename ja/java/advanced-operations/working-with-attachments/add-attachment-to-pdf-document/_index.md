---
title: PDFドキュメントへの添付ファイルの追加
linktitle: PDFドキュメントへの添付ファイルの追加
type: docs
weight: 10
url: /ja/java/add-attachment-to-pdf-document/
description: このページでは、Javaを使用してPDFファイルに添付ファイルを追加する方法について説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

添付ファイルにはさまざまな情報を含めることができ、さまざまなファイルタイプが存在します。この記事では、PDFファイルに添付ファイルを追加する方法を説明します。

1. 添付したいファイルとファイルの説明を含む[FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification)オブジェクトを作成します。

1. [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) オブジェクトを、[add(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) メソッドを使用して、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) コレクションに追加します。[EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) コレクションには、PDF ファイルに追加されたすべての添付ファイルが含まれています。

以下のコードスニペットは、PDF ドキュメントに添付ファイルを追加する方法を示しています。

```java
public class ExampleAttachments {
    
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Attachments/";

    public static void AddingAttachment() {
        // ドキュメントを開く
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // 添付ファイルとして追加する新しいファイルを設定する
  FileSpecification fileSpecification = new FileSpecification("sample.txt", "サンプルテキストファイル");
  // ドキュメントの添付ファイルコレクションに添付ファイルを追加する
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // 更新されたドキュメントを保存する
  pdfDocument.save("output.pdf");
    }
}
```