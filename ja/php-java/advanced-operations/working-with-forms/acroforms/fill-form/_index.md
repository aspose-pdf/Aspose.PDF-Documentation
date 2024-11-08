---
title: AcroFormsを記入する
linktitle: AcroFormsを記入する
type: docs
weight: 20
url: /ja/php-java/fill-form/
description: このセクションでは、Aspose.PDF for PHP via Javaを使用してPDFドキュメントのフォームフィールドに入力する方法を説明します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFドキュメントは素晴らしく、フォームを作成するための好ましいファイルタイプです。

Aspose.PDF for PHP via Javaを使用すると、フォームフィールドを入力し、DocumentオブジェクトのFormコレクションからフィールドを取得できます。

次の例を見て、このタスクを解決する方法を見てみましょう。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);
    
    // フィールドを取得する    
    $textBoxField = $document->getForm()->get("textbox1");

    // フィールド値を変更する
    $textBoxField->setValue("フィールドに記入する値");
        
    // 更新されたドキュメントを保存する
    $document->save($outputFile);
    $document->close();
```