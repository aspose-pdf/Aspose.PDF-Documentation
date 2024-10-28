---
title: PHPにJavaScriptを追加
type: docs
weight: 10
url: /java/adding-javascript-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - JavaScriptの追加

**Aspose.PDF Java for PHP**を使用してPdfドキュメントにJavaScriptを追加するには、単に**AddJavaScript**クラスを呼び出します。

PHPコード

```php
# PDFドキュメントを開く。
$doc = new Document($dataDir . "input1.pdf");

# ドキュメントレベルでJavaScriptを追加
# 望むJavaScript文でJavascriptActionをインスタンス化
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# Documentの望むアクションにJavascriptActionオブジェクトを割り当てる
$doc->setOpenAction($javaScript);

# ページレベルでJavaScriptを追加
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

# PDFドキュメントを保存
$doc->save($dataDir . "JavaScript-Added.pdf");

print "JavaScriptが正常に追加されました。出力ファイルを確認してください。";
```


**コードの実行をダウンロード**

以下のいずれかのソーシャルコーディングサイトから**JavaScriptの追加 (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)