---
title: PDFファイルメタデータの操作
linktitle: PDFファイルメタデータ
type: docs
weight: 140
url: /php-java/pdf-file-metadata/
description: このセクションでは、PDFファイル情報の取得方法、PDFファイルからXMPメタデータを取得する方法、PDFファイル情報の設定方法について説明します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイル情報の取得

PDFファイルに関するファイル固有の情報を取得するには、まず[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスの[getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--)を使用して'docInfo'オブジェクトを取得します。'docInfo'オブジェクトが取得されると、個々のプロパティの値を取得できます。

次のコードスニペットは、PDFファイル情報を設定する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    
    // ドキュメント情報を取得
    $docInfo = $document->getInfo();

    // ドキュメント情報を表示
    $responseData1 = "著者: " . $docInfo->getAuthor() . ", ";
    $responseData2 = "作成日: " . $docInfo->getCreationDate() . ", ";
    $responseData3 = "キーワード: " . $docInfo->getKeywords() . ", ";
    $responseData4 = "変更日: " . $docInfo->getModDate() . ", ";
    $responseData5 = "件名: " . $docInfo->getSubject() . ", ";
    $responseData6 = "タイトル: " . $docInfo->getTitle() . "";

    $document->close();
```