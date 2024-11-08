---
title: AcroFormsの変更
linktitle: AcroFormsの変更
type: docs
weight: 40
url: /ja/java/modifing-form/
description: このセクションでは、Aspose.PDF for PHP via Javaを使用してPDFドキュメント内のフォームを変更する方法を説明します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## カスタムフォームフィールドフォントの設定

Adobe PDFファイルのフォームフィールドは、特定のデフォルトフォントを使用するように設定できます。Aspose.PDFを使用すると、開発者は14のコアフォントの1つまたはカスタムフォントをフィールドのデフォルトフォントとして適用できます。
フォームフィールドに使用されるデフォルトフォントを設定および更新するには、Aspose.PDFのDefaultAppearance (Font font, double size, Color color) クラスを使用します。このクラスはcom.aspose.pdf.DefaultAppearanceを使用してアクセスできます。このオブジェクトを使用するには、FieldクラスのsetDefaultAppearance(..)メソッドを使用します。

次のコードスニペットは、PDFフォームフィールドのデフォルトフォントを設定する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ドキュメントから特定のフォームフィールドを取得
    $field = $document->getForm()->get("textbox1");

    // フォントオブジェクトを作成
    $fontRepository = new FontRepository();
    $font = $fontRepository->findFont("ComicSansMS");

    $colors = new Color();
    $blackColor = $colors->getBlack();

    // フォームフィールドのフォント情報を設定
    $field->setDefaultAppearance(new DefaultAppearance($font, 10, $blackColor));

    // 更新されたドキュメントを保存
    $document->save($outputFile);
    $document->close();        

    $document->close();
```


## Get/Set FieldLimit

このコードは、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスを使用して、ドキュメントを開き、フォームフィールドを取得し、その最大長を設定し、'setMaxLen' と 'getMaxLen' メソッドで最大長を取得する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ドキュメントから特定のフォームフィールドを取得
    $field = $document->getForm()->get("textbox1");
    
    $field->setMaxLen(10);

    // DOMを使用して最大フィールド制限を取得
    $responseData = "Limit: " . $field->getMaxLen();          

    $document->close();
```

以下のコードスニペットを使用して、Aspose.PDF.Facades 名前空間を使用して同じ値を取得することもできます。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ドキュメントから特定のフォームフィールドを取得
    $field = $document->getForm()->get("textbox1");

    // DOMを使用して最大フィールド制限を取得
    $responseData = "Limit: " . $field->getMaxLen();          

    $document->close();
```


同様に、Aspose.PDF には DOM アプローチを使用してフィールドの制限を取得するメソッドがあります。次のコードスニペットは、その手順を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ドキュメントから特定のフォームフィールドを取得
    $field = $document->getForm()->get("textbox1");

    // フィールドを削除
    $field->delete();
    
    $document->close();
```
## PDFドキュメントから特定のフォームフィールドを削除する

すべてのフォームフィールドは、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトのフォームコレクションに含まれています。このコレクションは、削除メソッドを含むフォームフィールドを管理するためのさまざまなメソッドを提供します。特定のフィールドを削除したい場合、削除メソッドのパラメータとしてフィールド名を渡し、その後、更新されたPDFドキュメントを保存します。

次のコードスニペットは、PDFドキュメントから名前付きフィールドを削除する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ドキュメントから特定のフォームフィールドを取得
    $field = $document->getForm()->get("textbox1");

    // フィールドを削除
    $field->delete();
    
    $document->close();
```


## PDFドキュメントのフォームフィールドを修正する

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトのフォームコレクションを使用して、PDFドキュメントのフォームフィールドを管理できます。

フォームフィールドを修正するには、フォームコレクションからフィールドを取得し、そのプロパティを設定します。その後、更新したPDFドキュメントを保存します。

次のコードスニペットは、PDFドキュメント内の既存のフォームフィールドを修正する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ドキュメントから特定のフォームフィールドを取得
    $field = $document->getForm()->get("textbox1");

    // フィールドの値を修正
    $field->setValue("更新された値");

    // フィールドを読み取り専用に設定
    $field->setReadOnly(true);

    // 更新されたドキュメントを保存
    $document->save($outputFile);        
    $document->close();
```

### PDFファイル内でフォームフィールドを新しい場所に移動する

PDFページ上でフォームフィールドを新しい場所に移動したい場合は、まずフィールドオブジェクトを取得し、そのsetRectメソッドに新しい値を指定します。
 A [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) オブジェクトに新しい座標を設定して setRect(..) メソッドに割り当てます。その後、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトの save メソッドを使用して更新された PDF を保存します。

次のコードスニペットは、フォームフィールドを新しい場所に移動する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ドキュメントから特定のフォームフィールドを取得
    $field = $document->getForm()->get("textbox1");

    // フィールドの位置を変更
    $field->setRect(new Rectangle(300, 400, 600, 500));

    // 更新されたドキュメントを保存
    $document->save($outputFile);        
    $document->close();
```