---
title: PDFにデジタル署名する方法
linktitle: PDFにデジタル署名
type: docs
weight: 10
url: /ja/php-java/digitally-sign-pdf-file/
description: Javaを使用してPDFドキュメントにデジタル署名します。JavaベースのアプリケーションとPDFライブラリでデジタル署名されたPDFを確認または検証します。PKCS1証明書でPDFファイルを認証できます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

署名を使用してPDFドキュメントに署名する場合、基本的にその内容が「そのまま」であるべきであることを確認します。したがって、後で行われた変更は署名を無効にし、ドキュメントが変更されたかどうかがわかります。ドキュメントを最初に認証することで、ユーザーが認証を無効にすることなくドキュメントに加えることができる変更を指定できます。

言い換えれば、ドキュメントは依然としてその完全性を保持していると見なされ、受信者はドキュメントを信頼することができます。詳細については、PDFの認証と署名をご覧ください。

## デジタル署名でPDFに署名する

```php

    // ドキュメントを開く
    $document = new Document($inputFile);    
    $signature = new facades_PdfFileSignature($document);
    $pkcs = new PKCS7($inputPKCS7, 'Pa$$w0rd2020'); // PKCS7/PKCS7Detachedを使用
    $rectangle = new Rectangle(300,100,420,160);
    $signature->sign(1, true, $rectangle->toRect(), $pkcs);
    // 出力PDFファイルを保存
    $signature->save($outputFile);    
    $document->close();
```