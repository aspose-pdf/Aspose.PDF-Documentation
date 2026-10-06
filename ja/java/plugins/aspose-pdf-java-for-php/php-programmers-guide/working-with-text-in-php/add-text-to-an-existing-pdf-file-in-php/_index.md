---
title: "PHP での既存の PDF ファイルへのテキストの追加"
linktitle: "PHP での既存の PDF ファイルへのテキストの追加"
type: docs
weight: 20
url: /ja/java/add-text-to-an-existing-pdf-file-in-php/
description: "Aspose.PDF を使用して、PHP で既存の PDF ドキュメントに新しいテキストを追加する方法を学びます。"
lastmod: "2026-10-06"
---
## Aspose.PDF - テキストの追加

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントにテキスト文字列を追加するには、**AddText** モジュールを呼び出してください。

PHP コード

```php

# Instantiate Document object
$doc = new Document($dataDir . 'input1.pdf');

# get particular page
$pdf_page = $doc->getPages()->get_Item(1);

# create text fragment
$text_fragment = new TextFragment("main text");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# set text properties
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# create TextBuilder object
$text_builder = new TextBuilder($pdf_page);

# append the text fragment to the PDF page
$text_builder->appendText($text_fragment);

# Save PDF file
$doc->save($dataDir . "Text_Added.pdf");

print "Text added successfully" . PHP_EOL;

```

**実行コードをダウンロード**

**Add Text (Aspose.PDF)** を以下のいずれかのソーシャルコーディングサイトからダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)
