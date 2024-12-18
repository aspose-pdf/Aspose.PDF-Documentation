---
title: 既存のPDFファイルにテキストを追加する方法 (PHP)
type: docs
weight: 20
url: /ja/java/add-text-to-an-existing-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - テキストを追加

**Aspose.PDF Java for PHP** を使用してPDFドキュメントにテキスト文字列を追加するには、単に **AddText** モジュールを呼び出します。

PHPコード

```php

# Documentオブジェクトをインスタンス化
$doc = new Document($dataDir . 'input1.pdf');

# 特定のページを取得
$pdf_page = $doc->getPages()->get_Item(1);

# テキストフラグメントを作成
$text_fragment = new TextFragment("メインテキスト");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# テキストのプロパティを設定
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# TextBuilderオブジェクトを作成
$text_builder = new TextBuilder($pdf_page);

# テキストフラグメントをPDFページに追加
$text_builder->appendText($text_fragment);

# PDFファイルを保存
$doc->save($dataDir . "Text_Added.pdf");

print "テキストが正常に追加されました" . PHP_EOL;

```


**コードを実行してダウンロード**

以下のいずれかのソーシャルコーディングサイトから**テキストを追加 (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)