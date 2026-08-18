---
title: 在 PHP 中添加 JavaScript
linktitle: 在 PHP 中添加 JavaScript
type: docs
weight: 10
url: /java/adding-javascript-in-php/
description: 了解如何使用 PHP 和 Aspose.PDF 将 JavaScript 添加到 PDF 文件以增强文档交互性。
lastmod: "2026-06-09"
---
## Aspose.PDF - 添加 JavaScript

要使用 **Aspose.PDF Java for PHP** 在 Pdf 文档中添加 JavaScript，只需调用 **AddJavaScript** 类即可。

PHP代码

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

**下载运行代码**

从以下任何一个社交编码网站下载**添加 JavaScript (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)
