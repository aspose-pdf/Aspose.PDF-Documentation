---
title: 既存のPDFのXMPメタデータを設定する - ファサード
type: docs
weight: 20
url: ja/java/set-xmp-metadata/
description: このセクションでは、PdfXmpMetadataクラスを使用してAspose.PDFファサードでXMPメタデータを設定する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDFファイルにXMPメタデータを設定するためには、[PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata)オブジェクトを作成し、[bindPdf(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Facade#bindPdf-com.aspose.pdf.IDocument-)メソッドを使用してPDFファイルをバインドする必要があります。
 You can use setByDefaultMetadataProperties(..) メソッドを [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) クラスで使用して、さまざまなプロパティを追加できます。最後に、[save(...)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/SaveableFacade#save-java.io.OutputStream-) メソッドを [PdfXmpMetadata](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfXmpMetadata) クラスで呼び出します。

次のコードスニペットは、PDFファイルにXMPメタデータを追加する方法を示しています。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Document-SetXMPMetadataOfAnExistingPDF-.java" >}}