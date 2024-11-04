---
title: HTMLをPDFに変換
linktitle: HTMLをPDFに変換
type: docs
weight: 40
url: /php-java/convert-html-to-pdf/
lastmod: "2024-05-20"
description: このトピックでは、Aspose.PDFがHTMLおよびMHTML形式をPDFファイルに変換する方法を示します。
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## 概要

この記事では、PHPを使用してHTMLをPDFに変換する方法を説明します。コードは非常にシンプルで、HTMLをDocumentクラスにロードして出力PDFとして保存するだけです。JavaでMHTMLをPDFに変換するのも同様です。以下のトピックをカバーします。

## Java HTMLからPDFへの変換ライブラリ

**Aspose.PDF for PHP via Java** は、既存のHTMLドキュメントをシームレスにPDFに変換できるPDF操作APIです。HTMLからPDFへの変換プロセスは柔軟にカスタマイズできます。

## HTMLをPDFに変換

次のJavaコードサンプルは、HTMLドキュメントをPDFに変換する方法を示しています。

1. [HtmlLoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions)クラスのインスタンスを作成します。

1. [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)オブジェクトを初期化します。
1. [Document.save(String)](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/#save-java.lang.String-)メソッドを呼び出して、出力PDFドキュメントを保存します。

```php
    // HTMLファイルの読み込みオプションを指定するためのHtmlLoadOptionsのインスタンスを作成します
    $loadOption = new HtmlLoadOptions();

    // 新しいDocumentオブジェクトを作成し、HTMLファイルを読み込みます
    $document = new Document($inputFile, $loadOption);

    // ドキュメントをPDFファイルとして保存します
    $document->save($outputFile);
```

## HTMLからPDFへの高度な変換

HTML変換エンジンには、変換プロセスを制御するためのいくつかのオプションがあります。

### メディアクエリサポート

1. HTML [LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions)を作成します。
1. [印刷またはスクリーン](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setHtmlMediaType-int-)モードを設定します。

1. [Documentオブジェクト](https://reference.aspose.com/page/java/com.aspose.page/document)を初期化する。
1. 出力PDFドキュメントを保存する。

メディアクエリは、異なるデバイスに合わせたスタイルシートを提供するための一般的な手法です。デバイスタイプは、[HtmlMediaType](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlMediaType)クラスを使用して設定できます。

```php

    // HTMLファイルのロードオプションを指定するためにHtmlLoadOptionsのインスタンスを作成
    $htmlMediaType = new HtmlMediaType();

    // プリントモードまたはスクリーンモードを設定
    $loadOption->setHtmlMediaType($htmlMediaType->Print);

    // 新しいDocumentオブジェクトを作成し、HTMLファイルをロード
    $document = new Document($inputFile, $loadOption);

    // ドキュメントをPDFファイルとして保存
    $document->save($outputFile);
```

### フォント埋め込みの有効化（無効化）

1. 新しいHtml[LoadOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/HtmlLoadOptions)を追加する。
1. フォント埋め込みを無効にする。
1. 新しいドキュメントを保存する。

HTMLページはしばしばフォントを使用します（例：
 ローカルフォルダ、Google Fontsなどからフォントを取得します。また、[setEmbedFonts](https://reference.aspose.com/pdf/java/com.aspose.pdf/htmlloadoptions/#setEmbedFonts-boolean-)プロパティを使用して、ドキュメント内のフォントの埋め込みを制御することもできます。

```php

    // HTMLファイルの読み込みオプションを指定するためのHtmlLoadOptionsのインスタンスを作成します
    $loadOption = new HtmlLoadOptions();

    // フォントの埋め込みを無効にします
    $loadOption->setEmbedFonts(true);

    // 新しいDocumentオブジェクトを作成し、HTMLファイルを読み込みます
    $document = new Document($inputFile, $loadOption);

    // ドキュメントをPDFファイルとして保存します
    $document->save($outputFile);
```

## MHTMLをPDFに変換

<abbr title="MIME encapsulation of aggregate HTML documents">MHTML</abbr>、MIME HTMLの略で、通常は外部リンクで表されるリソース（画像、Flashアニメーション、Javaアプレット、音声ファイルなど）をHTMLコードと共に1つのファイルに結合するために使用されるWebページアーカイブ形式です。 The content of an MHTML file is encoded as if it were an HTML email message, using the MIME type multipart/related.

MHTMLファイルの内容は、MIMEタイプmultipart/relatedを使用してHTMLメールメッセージとしてエンコードされます。

Next code snippet show how to covert MHTML files to PDF format with Java:

次のコードスニペットは、MHTMLファイルをJavaでPDF形式に変換する方法を示しています。

```php

    // MhtLoadOptionsクラスの新しいインスタンスを作成します。
    $loadOption = new MhtLoadOptions();

    // Documentクラスの新しいインスタンスを作成し、MHTMLファイルをロードします。
    $document = new Document($inputFile, $loadOption);

    // ドキュメントをPDFファイルとして保存します。
    $document->save($outputFile);
```