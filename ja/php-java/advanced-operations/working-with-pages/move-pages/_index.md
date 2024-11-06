---
title: PDFページの移動 
linktitle: PDFページの移動
type: docs
weight: 20
url: ja/php-java/move-pages/
description: Aspose.PDF for PHP via Javaを使用して、任意の位置またはPDFファイルの末尾にページを移動してみてください。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## あるPDFドキュメントから別のPDFドキュメントにページを移動する

このトピックでは、PHPを使用してあるPDFドキュメントから別のドキュメントの末尾にページを移動する方法を説明します。
ページを移動するには、次の手順を実行します：

1. ソースPDFファイルで[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスオブジェクトを作成します
1. 目的のPDFファイルで[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスオブジェクトを作成します
1. ページを出力ドキュメントに追加します。出力ファイルを保存します
1. 入力ドキュメントからページを削除します。変更された入力ドキュメントを保存します
1. ドキュメントを閉じます
1. 出力ドキュメントを保存し、閉じます

次のコードスニペットは、1ページを移動する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $page = $document->getPages()->get_Item(2);
    $dstDocument->getPages()->add($page);

    // 出力ファイルを保存
    $dstDocument->save($srcFileName);
    $document->getPages()->delete(2);
    $document->save($dstFileName);
    $document->close();
    $dstDocument->close();
  
    // 出力ドキュメントを保存
    $document->save($outputFile);
    $document->close();
```


## PDFドキュメントから別のPDFドキュメントに複数のページを移動する

1. ソースPDFファイルで[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスのオブジェクトを作成します。
1. 目的のPDFファイルで[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスのオブジェクトを作成します。
1. 入力ドキュメントから出力ドキュメントにコピーするページを定義します。
1. 配列をループします：
    1. 入力ドキュメントから指定されたインデックスのページを取得します。
    1. ページを目的のドキュメントに追加します。
1. Saveメソッドを使用して出力PDFを保存します。
1. 配列を使用してソースドキュメントのページを削除します。
1. Saveメソッドを使用してソースPDFを保存します。

次のコードスニペットは、PDFファイルの最後に空のページを挿入する方法を示しています。

```php

    // ドキュメントを開く
    $document = new Document($inputFile1);
    $dstDocument = new Document($outputFile);
    
    $pages = [1, 3 ];
    foreach ($pages as $pageIndex) {
      $page = $document->getPages()->get_Item($pageIndex);
      $dstDocument->getPages()->add(page);
    }
    // 出力ファイルを保存
    $dstDocument->save($srcFileName);
    $document->getPages()->delete($pages);

    $document->save(dstFileName);

    $document->close();
    $dstDocument->close();  
```


## 現在のPDFドキュメント内でページを新しい場所に移動する

1. ソースPDFファイルで[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)クラスオブジェクトを作成します。
1. [pageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/PageCollection)コレクションからページを取得します。
1. 新しい場所にページを追加します。
1. インデックス2のページを削除します。
1. saveメソッドを使用して出力PDFを保存します。

```php

    // ドキュメントを開く
    $document = new Document($inputFile);
        
    $pageCollection = $document->getPages();
    
    $page = $pageCollection->get_Item(2);
    $pageCollection->add(page);
    $pageCollection->delete(2);

    // 出力ファイルを保存
    $document->save($outputFile);
    $document->close();      
```