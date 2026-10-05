---
title: "PHP での 既存のPDFファイルへのテキストの追加"
linktitle: "PHP での 既存のPDFファイルへのテキストの追加"
type: docs
weight: 20
url: /ja/java/add-text-to-an-existing-pdf-file-in-php/
description: Aspose.PDF を使用して、PHPで既存のPDFドキュメントに新しいテキストを追加する方法を学びます。
lastmod: "2026-10-05"
---
## Aspose.PDF - テキストの追加

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントにテキスト文字列を追加するには、単に **AddText** モジュールを呼び出します。

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

ダウンロードВ **Add Text (Aspose.PDF)**В からВ 以下に記載されたソーシャルコーディングサイトのいずれか：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)
