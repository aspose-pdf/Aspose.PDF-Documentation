---
title: "PHP での DOM を使用した HTML 文字列の追加"
linktitle: "PHP での DOM を使用した HTML 文字列の追加"
type: docs
weight: 10
url: /ja/java/add-html-string-using-dom-in-php/
description: "Aspose.PDF を使用したリッチな文書作成において、PHP の DOM を使って PDF ドキュメントに HTML コンテンツを追加する方法を探ります。"
lastmod: "2026-10-06"
---
## Aspose.PDF - HTML の追加

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントに HTML 文字列を追加するには、単に **AddHtml** モジュールを呼び出すだけです。

PHP コード

```php
# Instantiate Document object
$doc = new Document();

# Add a page to pages collection of PDF file
$page = $doc->getPages()->add();

# Instantiate HtmlFragment with HTML contents
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# set MarginInfo for margin details
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# Set margin information
$title->setMargin($margin);

# Add HTML Fragment to paragraphs collection of page
$page->getParagraphs()->add($title);

# Save PDF file
$doc->save($dataDir . "html.output.pdf");

print "HTML added successfully" . PHP_EOL;

```

**実行中のコードをダウンロード**

ダウンロード **Add HTML (Aspose.PDF)** から、以下に記載されたソーシャルコーディングサイトのいずれかから取得してください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)
