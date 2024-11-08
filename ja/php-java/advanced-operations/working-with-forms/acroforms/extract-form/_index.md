---
title: データを抽出する AcroForms
linktitle: データを抽出する AcroForms
type: docs
weight: 30
url: /ja/php-java/extract-form/
description: このセクションでは、Aspose.PDF for PHP via Java を使用して PDF ドキュメントからフォームを抽出する方法を説明します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDF ドキュメントの個別のフィールドから値を取得する

フォームフィールドの[getValue() メソッド](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)は、特定のフィールドの値を取得することを可能にします。

値を取得するには、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトのFormコレクションからフォームフィールドを取得します。

この例では、[textBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField)を選択し、[getValue() メソッド](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextBoxField#getValue--)を使用してその値を取得します。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // フィールドを取得
    $textBoxField = $document->getForm()->get("textbox1");

    // フィールド名を取得
    $responseData = "PartialName: " . $textBoxField->getPartialName();

    // フィールド値を取得
    $responseData = $responseData . " Value: " . $textBoxField->getValue();
    $document->close();
```