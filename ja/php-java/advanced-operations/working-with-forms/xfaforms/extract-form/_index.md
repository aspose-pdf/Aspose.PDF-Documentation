---
title: XFAフォームの抽出
linktitle: XFAフォームの抽出
type: docs
weight: 30
url: /ja/php-java/extract-form/
description: このセクションでは、Aspose.PDF for PHP via Javaを使用してPDFドキュメントからフォームを抽出する方法について説明します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントのフォームフィールドから値を取得する

フォームフィールドの[getValue() メソッド](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)を使用すると、特定のフィールドの値を取得できます。

値を取得するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトのFormコレクションからフォームフィールドを取得します。

この例では、[TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField)を選択し、[getValue() メソッド](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)を使用してその値を取得します。

```php

    // XFAフォームを読み込む
    $document = new Document($inputFile);
    
    // XFAフォームフィールドの名前を取得
    $names = $document->getForm()->getXFA()->getFieldNames();
        
    // フィールド値を取得
    $document->getForm()->getXFA()->get_Item($names[0]);
    $document->getForm()->getXFA()->get_Item($names[1]);
    
    // 変更されたPDFを保存    
    $document->close();
```