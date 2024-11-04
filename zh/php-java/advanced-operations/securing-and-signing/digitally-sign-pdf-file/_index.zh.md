---
title: 如何数字签名PDF
linktitle: 数字签名PDF
type: docs
weight: 10
url: /php-java/digitally-sign-pdf-file/
description: 使用Java对PDF文档进行数字签名。通过PDF库与基于Java的应用程序验证或验证数字签名的PDF。您可以使用PKCS1证书对PDF文件进行认证。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

当使用签名对PDF文档进行签署时，您基本上是确认其内容应保持“不变”。因此，之后所做的任何更改都会使签名失效，从而您可以知道文档是否已被更改。首先对文档进行认证，允许您指定用户可以对文档进行哪些更改而不会使认证失效。

换句话说，文档仍然被认为保持其完整性，接收者仍然可以信任该文档。有关更多详细信息，请访问认证和签署PDF。

## 使用数字签名签署PDF

```php

    // 打开文档
    $document = new Document($inputFile);    
    $signature = new facades_PdfFileSignature($document);
    $pkcs = new PKCS7($inputPKCS7, 'Pa$$w0rd2020'); // 使用PKCS7/PKCS7Detached
    $rectangle = new Rectangle(300,100,420,160);
    $signature->sign(1, true, $rectangle->toRect(), $pkcs);
    // 保存输出PDF文件
    $signature->save($outputFile);    
    $document->close();
```