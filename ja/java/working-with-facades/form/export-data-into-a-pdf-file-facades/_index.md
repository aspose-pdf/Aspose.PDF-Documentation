---
title: PDFファイルからXMLへのデータエクスポート（ファサード）
type: docs
weight: 20
url: /ja/java/export-data-into-a-pdf-file-facades/
description: このセクションでは、Aspose.PDFファサードを使用して、PDFファイルからデータをXMLにエクスポートする方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) クラスを使用すると、exportXmlメソッドを使用してPDFファイルからXMLファイルにデータをエクスポートできます。データをXMLにエクスポートするには、まず [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Form) クラスのオブジェクトを作成し、bindPDFメソッドでソースPDFフォームを開き、OutputStreamオブジェクトを使用してexportXmlメソッドを呼び出します。最後に、OutputStreamオブジェクトを閉じてFormオブジェクトを破棄できます。以下のコードスニペットは、データをXMLファイルにエクスポートする方法を示しています。

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "Examples-src-main-java-com-aspose-pdf-examples-facades-Forms-ExportDataToXMLFromAPDFFile-.java" >}}