---
title: AcroFormsを埋める
linktitle: AcroFormsを埋める
type: docs
weight: 20
url: /php-java/fill-form/
description: このセクションでは、Aspose.PDF for PHP via Javaを使用してPDFドキュメントのフォームフィールドに記入する方法を説明します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDFドキュメントは素晴らしく、フォームを作成するための好ましいファイルタイプです。

Aspose.PDF for PHP via Javaを使用すると、フォームフィールドに記入し、DocumentオブジェクトのFormコレクションからフィールドを取得できます。

このタスクを解決するための次の例を見てみましょう：

```php

    // XFAフォームを読み込む
    $document = new Document($inputFile);
    
    // XFAフォームフィールドの名前を取得
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // フィールド値を設定        
    $document->getForm()->getXFA()->set_Item($names[0],"フィールド 0");
    $document->getForm()->getXFA()->set_Item($names[1],"フィールド 1");
        
    // 更新されたドキュメントを保存
    $document->save($outputFile);
    
    // 修正されたPDFを保存    
    $document->close();
```