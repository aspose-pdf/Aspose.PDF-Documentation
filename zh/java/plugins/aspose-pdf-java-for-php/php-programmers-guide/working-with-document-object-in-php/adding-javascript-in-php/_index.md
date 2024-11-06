---
title: 在 PHP 中添加 JavaScript
type: docs
weight: 10
url: zh/java/adding-javascript-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 添加 JavaScript

要在 Pdf 文档中使用 **Aspose.PDF Java for PHP** 添加 JavaScript，只需调用 **AddJavaScript** 类。

PHP 代码

```php
# 打开一个 pdf 文档。
$doc = new Document($dataDir . "input1.pdf");

# 在文档级别添加 JavaScript
# 使用所需的 JavaScript 语句实例化 JavascriptAction
$javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

# 将 JavascriptAction 对象分配给文档的所需动作
$doc->setOpenAction($javaScript);

# 在页面级别添加 JavaScript
$doc->getPages()->get_Item(2)->getActions()->setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));
$doc->getPages()->get_Item(2)->getActions()->setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

# 保存 PDF 文档
$doc->save($dataDir . "JavaScript-Added.pdf");

print "成功添加 JavaScript，请检查输出文件。";
```


**下载运行代码**

从以下任一社交编码网站下载**添加 JavaScript (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddJavascript.php)