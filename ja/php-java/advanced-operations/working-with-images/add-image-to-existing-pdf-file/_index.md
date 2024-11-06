---
title: 既存のPDFファイルに画像を追加する
linktitle: 画像を追加
type: docs
weight: 10
url: ja/php-java/add-image-to-existing-pdf-file/
description: このセクションでは、PHPを使用して既存のPDFファイルに画像を追加する方法について説明します。
lastmod: "2024-06-05"
---

すべてのPDFページにはリソースとコンテンツのプロパティがあります。リソースには画像やフォームが含まれることがあり、コンテンツは一連のPDFオペレーターによって表されます。各オペレーターには名前と引数があります。この例では、オペレーターを使用してPDFファイルに画像を追加します。

既存のPDFファイルに画像を追加するには：

- [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) オブジェクトを作成し、入力PDFドキュメントを開きます。
- 画像を追加したいページを取得します。
- ドキュメントに新しいページを追加します。
- ページのサイズを1190.7 x 841.995に設定します。
- 指定された画像ファイルとページのクロップボックスを使用して、ページに画像を追加します。
- ファイルを保存します。

次のコードスニペットは、PDFドキュメントに画像を追加する方法を示しています。

```php

    // 指定された入力ファイルを使用してドキュメントを開きます。
    $document = new Document($inputFile);
    
    // ドキュメントに新しいページを追加します。
    $page = $document->getPages()->add();
    
    // ページのサイズを1190.7 x 841.995に設定します。
    $page->setPageSize(1190.7, 841.995);
    
    // 指定された画像ファイルとページのクロップボックスを使用して、ページに画像を追加します。
    $page->addImage($imageFileName, $page->getCropBox());
    
    // 修正されたドキュメントを指定された出力ファイルに保存します。
    $document->save($outputFile);
    
    // ドキュメントを閉じます。
    $document->close();
```