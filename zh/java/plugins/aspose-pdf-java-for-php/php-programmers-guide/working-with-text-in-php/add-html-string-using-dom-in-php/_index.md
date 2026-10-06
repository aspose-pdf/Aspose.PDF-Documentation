---
title: 在 PHP 中使用 DOM 添加 HTML 字符串
linktitle: 在 PHP 中使用 DOM 添加 HTML 字符串
type: docs
weight: 10
url: /zh/java/add-html-string-using-dom-in-php/
description: 了解如何在 PHP 中使用 DOM 将 HTML 内容添加到 PDF 文档中，结合 Aspose.PDF 实现丰富的文档创建。
lastmod: "2026-10-06"
---
## Aspose.PDF - 添加 HTML

要在 PDF 文档中使用 **Aspose.PDF Java for PHP** 添加 HTML 字符串，只需调用 **AddHtml** 模块。

PHP 代码

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

**下载运行代码**

下载В **Add HTML (Aspose.PDF)**В 来自В 以下提到的任何社交代码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)
