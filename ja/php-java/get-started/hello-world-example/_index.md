---
title: Hello World PHP via Java Example
linktitle: Hello World Example
type: docs
weight: 40
url: /ja/php-java/hello-world-example/
description: このページは、Aspose.PDF for PHP via Javaを使用して、テキスト - Hello Worldを含むPDFドキュメントを作成するためのシンプルなプログラミングを使用する方法を示します。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Hello World Example

「Hello World」例は、通常、プログラミング言語やソフトウェアの基本機能を簡単な使用例で示すために使用されます。

Aspose.PDF for PHP via Java APIを使用すると、開発者はJavaアプリケーション内でPDFファイルを作成、読み取り、編集、および操作することができます。さまざまなファイルタイプをPDFフォーマットに変換したり、逆にPDFフォーマットから変換したりすることをサポートしています。このHello World記事では、Aspose.PDF for PHP via Java APIを使用してPDFファイルを作成する方法を示します。[Aspose.PDF for PHP via Javaをインストールした後](/pdf/ja/php-java/installation/)、以下のコードサンプルを実行して、Aspose.PDF APIがどのように機能するかを確認できます。

以下のコードスニペットは、次のステップに従います:

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) オブジェクトをインスタンス化する
1. ドキュメントオブジェクトに[Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) を追加する
1. [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) オブジェクトを作成する
1. ページの[Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) コレクションにTextFragmentを追加する
1. 結果のPDFドキュメントを保存する

以下のコードスニペットは、Java API を介した Aspose.PDF for PHP の動作を示す Hello World プログラムです。

```php
    $document = new Document();    
    $page = $document->getPages()->add();
    $textFragment = new TextFragment("Hello World!");    
    $page->getParagraphs()->add($textFragment);
    $document->save($outputFile);
```