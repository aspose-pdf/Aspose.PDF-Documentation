---
title: PHPでDOMを使用してHTML文字列を追加する
type: docs
weight: 10
url: ja/java/add-html-string-using-dom-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - HTMLを追加

**Aspose.PDF Java for PHP**を使用してPDFドキュメントにHTML文字列を追加するには、単に**AddHtml**モジュールを呼び出します。

PHPコード

```php
# Documentオブジェクトをインスタンス化
$doc = new Document();

# PDFファイルのページコレクションにページを追加
$page = $doc->getPages()->add();

# HTML内容でHtmlFragmentをインスタンス化
$title = new HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>");

# marginの詳細のためにMarginInfoを設定
$margin = new MarginInfo();
$margin->setBottom(10);
$margin->setTop(200);

# margin情報を設定
$title->setMargin($margin);

# ページの段落コレクションにHTMLフラグメントを追加
$page->getParagraphs()->add($title);

# PDFファイルを保存
$doc->save($dataDir . "html.output.pdf");

print "HTMLが正常に追加されました" . PHP_EOL;

```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Add HTML (Aspose.PDF)**をダウンロードします：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)