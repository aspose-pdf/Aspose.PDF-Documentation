---
title: أضف سلسلة HTML باستخدام DOM في PHP
linktitle: أضف سلسلة HTML باستخدام DOM في PHP
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-php/
description: اكتشف كيفية إضافة محتوى HTML إلى مستند PDF باستخدام DOM في PHP باستخدام Aspose.PDF لإنشاء مستند غني.
lastmod: "2026-06-09"
---
## Aspose.PDF - إضافة HTML

لإضافة سلسلة HTML في مستند Pdf باستخدام **Aspose.PDF Java for PHP**، ما عليك سوى استدعاء وحدة **AddHtml**.

كود PHP

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

** تنزيل كود التشغيل **

تنزيلВ **إضافة HTML (Aspose.PDF)**В fromВ من أي من مواقع الترميز الاجتماعي المذكورة أدناه:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddHtml.php)
