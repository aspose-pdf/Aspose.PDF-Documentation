---
title: 在 PHP 中使用 DOM 添加 HTML 字符串
linktitle: 在 PHP 中使用 DOM 添加 HTML 字符串
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-php/
description: 探索如何使用 PHP 中的 DOM 和 Aspose.PDF 将 HTML 内容添加到 PDF 文档中，以创建丰富的文档。
lastmod: "2026-06-09"
---
## Aspose.PDF - 添加 HTML

要使用 **Aspose.PDF Java for PHP** 在 Pdf 文档中添加 HTML 字符串，只需调用 **AddHtml** 模块即可。

PHP代码

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

从以下任何一个社交编码网站下载**添加 HTML (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)
