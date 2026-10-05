---
title: "PHP での JavaScript の追加"
linktitle: "PHP での JavaScript の追加"
type: docs
weight: 10
url: /ja/java/adding-javascript-in-php/
description: PHP と Aspose.PDF を使用して PDF ファイルに JavaScript を追加し、ドキュメントのインタラクティビティを向上させる方法を学びます。
lastmod: "2026-10-05"
---
## Aspose.PDF - JavaScript の追加

**Aspose.PDF Java for PHP** を使用して PDF ドキュメントに JavaScript を追加するには、単に **AddJavaScript** クラスを呼び出します。

PHP コード

```php
# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Adding JavaScript at Document Level
# Instantiate JavascriptAction with desried JavaScript statement
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Assign JavascriptAction object to desired action of Document
$doc->setOpenAction($javaScript);

# Adding JavaScript at Page Level
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

# Save PDF Document
$doc->save($dataDir . "JavaScript-Added.pdf");

print "Added JavaScript Successfully, please check the output file.";
```

**実行コードをダウンロード**

ダウンロードВ **JavaScript の追加 (Aspose.PDF)**В からВ 以下に記載されたソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)
