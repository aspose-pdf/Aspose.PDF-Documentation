---
title: PDFドキュメントの作成
linktitle: 作成
type: docs
weight: 10
url: /ja/php-java/create-document/
description: Aspose.PDF for PHP via JavaでPDFファイルを作成する方法を学びます。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for PHP via Java** APIは、アプリケーション開発者がアプリケーションにPDFドキュメント処理機能を埋め込むことを可能にします。他のソフトウェアを基盤となるマシンにインストールすることなく、PDFファイルの作成と読み取りに使用できます。Aspose.PDF for PHP via Javaは、デスクトップアプリケーション、JSP、JSFアプリケーションなど、さまざまなタイプのアプリケーションで使用できます。

## PHP via Javaを使用してPDFファイルを作成する方法

PHP via Javaを使用してPDFファイルを作成するには、次の手順を使用します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)オブジェクトをインスタンス化する
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)を追加する

1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) オブジェクトを作成する
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) をページの [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) コレクションに追加する
1. 結果として得られるPDFドキュメントを保存する

```php

    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```