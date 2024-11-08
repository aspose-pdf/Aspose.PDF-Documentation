---
title: PDFにデジタル署名をする方法
linktitle: PDFにデジタル署名
type: docs
weight: 10
url: /ja/cpp/digitally-sign-pdf-file/
description: C++を使用してPDFドキュメントにデジタル署名をします。C++を使用してデジタル署名されたPDFを確認または検証します。
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## デジタル署名でPDFに署名する

PDFドキュメントに署名してその内容を確認したり、Aspose.PDFでドキュメントを承認したりできます。

Aspose.PDF for C++は、SignatureFieldクラスを使用してPDFファイルにデジタル署名をする機能をサポートしています。PKCS12証明書を使用してPDFファイルを認証することもできます。これは[Adobe Acrobatでの署名とセキュリティの追加](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6)に似ています。

PDFに署名するには、[PdfFileSignature](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_signature)クラスを使用します。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SecuringAndSigning::SignDocument() {

// パス名の文字列。

String _dataDir("C:\\Samples\\");


String inFile = _dataDir + u"DigitallySign.pdf";

String outFile = _dataDir + u"DigitallySign_out.pdf";


auto document = MakeObject<Document>(inFile);


auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020"); // PKCS7/PKCS7Detachedを使用
























// オブジェクト

System::Drawing::Rectangle rect(300, 100, 400, 200);

signature->Sign(1, true, rect, pkcs);

// 出力PDFファイルを保存

signature->Save(outFile);
}
```

## デジタル署名にタイムスタンプを追加する

### タイムスタンプ付きでPDFにデジタル署名する方法

Aspose.PDF for C++は、タイムスタンプサーバーまたはWebサービスを使用してPDFにデジタル署名することをサポートしています。

タイムスタンプは、ドキュメントに署名した日時を示すために使用されます。信頼性のあるタイムスタンプは、PDFの内容が特定の時点で存在しており、それ以降変更されていないことを証明します。

デジタル署名またはドキュメントに信頼できるタイムスタンプを追加するには、[TimestampSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.timestamp_settings)クラスを使用します。

以下のコードスニペットは、タイムスタンプを取得してPDFドキュメントに追加する方法を示しています。

```cpp
void SecuringAndSigning::SignWithTimeStampServer() {


// パス名の文字列。

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"SimpleResume.pdf");

auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020");


auto timestampSettings = MakeObject<TimestampSettings>(u"https://freetsa.org/tsr", String::Empty); // ユーザー名/パスワードは省略可能
























pkcs->set_TimestampSettings(timestampSettings);


System::Drawing::Rectangle rect(100, 100, 200, 100);

// 3つの署名タイプのいずれかを作成

signature->Sign(1, u"Signature Reason", u"Contact", u"Location", true, rect, pkcs);

// 出力PDFファイルを保存

signature->Save(_dataDir + u"DigitallySignWithTimeStamp_out.pdf");
}
```