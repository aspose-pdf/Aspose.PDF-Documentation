---
title: PDFドキュメントへの添付ファイルの追加
linktitle: PDFドキュメントへの添付ファイルの追加
type: docs
weight: 10
url: ja/cpp/add-attachment-to-pdf-document/
description: このページでは、Aspose.PDF for C++ライブラリを使用してPDFファイルに添付ファイルを追加する方法について説明します
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

添付ファイルにはさまざまな情報を含めることができ、さまざまなファイルタイプが可能です。この記事では、PDFファイルに添付ファイルを追加する方法を説明します。

1. 新しいC++プロジェクトを作成します。
1. Aspose.PDF DLLへの参照を追加します。
1. [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)オブジェクトを作成します。
1. 追加するファイルとファイルの説明を含む[FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification)オブジェクトを作成します。
1. [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) オブジェクトを [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) オブジェクトの [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) コレクションに、コレクションの Add メソッドを使って追加します。

[EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) コレクションには、PDF ファイル内のすべての添付ファイルが含まれています。次のコードスニペットは、PDF ドキュメントに添付ファイルを追加する方法を示しています。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithAttachments::AddingAttachment()
{

String _dataDir("C:\\Samples\\");


// ドキュメントを開く

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddAttachment.pdf");


// 添付ファイルとして追加する新しいファイルをセットアップ

auto fileSpecification = MakeObject<FileSpecification>(_dataDir + u"test.txt", u"サンプル テキスト ファイル");


// ドキュメントの添付ファイルコレクションに添付ファイルを追加

pdfDocument->get_EmbeddedFiles()->Add(fileSpecification);


// 新しい出力を保存

pdfDocument->Save(_dataDir + u"AddAttachment_out.pdf");
}
```