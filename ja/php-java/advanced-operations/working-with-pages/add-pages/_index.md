---
title: PDFにページを追加する
linktitle: ページを追加
type: docs
weight: 10
url: ja/php-java/add-pages/
description: この記事では、PDFファイルの希望する位置にページを挿入（追加）する方法を学びます。PHPを使用してPDFファイルからページを移動、削除（削除）する方法を学びます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFファイルにページを追加または挿入する

Aspose.PDF for PHP via Javaを使用すると、PDFドキュメントに任意の位置でページを挿入することができ、PDFファイルの最後にページを追加することもできます。挿入メソッドに空白ページを挿入したい位置を渡す必要があります。このセクションでは、Aspose.PDF for PHP via Javaを使用してPDFにページを追加する方法を示します。

### 希望の位置にPDFファイルに空のページを挿入する

以下のコードスニペットは、PDFファイルに空のページを挿入する方法を示しています：

1. 入力PDFファイルで[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスオブジェクトを作成します。
1. ページを追加し、PDFに挿入します。

1. 出力PDFをSaveメソッドを使って保存します。

以下のコードスニペットは、PDFファイルにページを挿入する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ページを追加
    $document->getPages()->add();

    // PDFに空のページを挿入
    $document->getPages()->insert(2);

    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```

上記の例では、デフォルトのパラメータで空のページを追加しました。ドキュメント内の別のページと同じページサイズにする必要がある場合は、いくつかのコード行を追加する必要があります：

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ページを追加
    $page1 = $document->getPages()->add();

    // PDFに空のページを挿入
    $page2 = $document->getPages()->insert(2);

    // ページ1からページパラメータをコピー
    $page2->setCropBox($page1->getCropBox());
    $page2->setMediaBox($page1->getMediaBox());
    $page2->setTrimBox($page1->getTrimBox());
    $page2->setArtBox($page1->getArtBox());
    $page2->setBleedBox($page1->getBleedBox());
    
    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```


### PDFファイルの最後に空白ページを追加する

時々、ドキュメントが空白ページで終わるようにしたいことがあります。このトピックでは、PDFドキュメントの最後に空白ページを挿入する方法を説明します。

PDFファイルの最後に空白ページを挿入するには：

1. 入力PDFファイルで[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスオブジェクトを作成します。
1. ページを追加し、PDFに挿入します。
1. saveメソッドを使用して出力PDFを保存します。

次のコードスニペットは、PDFファイルの最後に空白ページを挿入する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);

    // ページを追加
    $document->getPages()->add();

    // PDFに空白ページを挿入
    $document->getPages()->insert(2);

    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```