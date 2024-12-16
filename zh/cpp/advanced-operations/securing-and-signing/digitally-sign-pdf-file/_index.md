---
title: 如何为 PDF 进行数字签名
linktitle: 为 PDF 进行数字签名
type: docs
weight: 10
url: /zh/cpp/digitally-sign-pdf-file/
description: 使用 C++ 为 PDF 文档进行数字签名。使用 C++ 验证或验证数字签名的 PDF。
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 使用数字签名签署 PDF

您可以签署 PDF 文档以确认其内容，或者您可以使用 Aspose.PDF 批准文档。

Aspose.PDF for C++ 支持使用 SignatureField 类对 PDF 文件进行数字签名的功能。您还可以使用 PKCS12 证书认证 PDF 文件。类似于 [在 Adobe Acrobat 中添加签名和安全性](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6)。

使用 [PdfFileSignature](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_signature) 类来签署您的 PDF。

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SecuringAndSigning::SignDocument() {

// 用于路径名称的字符串。

String _dataDir("C:\\Samples\\");


String inFile = _dataDir + u"DigitallySign.pdf";

String outFile = _dataDir + u"DigitallySign_out.pdf";


auto document = MakeObject<Document>(inFile);


auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020"); // 使用 PKCS7/PKCS7Detached

// 对象

System::Drawing::Rectangle rect(300, 100, 400, 200);

signature->Sign(1, true, rect, pkcs);

// 保存输出 PDF 文件

signature->Save(outFile);
}
```

## 为数字签名添加时间戳

### 如何为带有时间戳的 PDF 进行数字签名

Aspose.PDF for C++ 支持通过时间戳服务器或 Web 服务对 PDF 进行数字签名。

时间戳用于指示您签署文档的日期和时间。可靠的时间戳证明您的 PDF 内容在特定时间点存在，并且自那时以来没有更改。

使用 [TimestampSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.timestamp_settings) 类为数字签名或文档添加可信时间戳。

请查看以下代码片段，该代码片段获取时间戳并将其添加到 PDF 文档中：

```cpp
void SecuringAndSigning::SignWithTimeStampServer() {


// 路径名称的字符串。

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"SimpleResume.pdf");

auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020");


auto timestampSettings = MakeObject<TimestampSettings>(u"https://freetsa.org/tsr", String::Empty); // 用户名/密码可以
























// 省略

pkcs->set_TimestampSettings(timestampSettings);


System::Drawing::Rectangle rect(100, 100, 200, 100);

// 创建三种签名类型中的任意一种

signature->Sign(1, u"签名原因", u"联系方式", u"位置", true, rect, pkcs);

// 保存输出 PDF 文件

signature->Save(_dataDir + u"DigitallySignWithTimeStamp_out.pdf");
}
```