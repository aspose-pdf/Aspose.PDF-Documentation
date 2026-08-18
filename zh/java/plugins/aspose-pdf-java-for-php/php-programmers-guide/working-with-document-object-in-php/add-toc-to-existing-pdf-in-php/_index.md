---
title: 使用 PHP 将目录添加到现有 PDF
linktitle: 使用 PHP 将目录添加到现有 PDF
type: docs
weight: 20
url: /java/add-toc-to-existing-pdf-in-php/
description: 探索如何使用 Aspose.PDF 将目录 (TOC) 添加到 PHP 中的现有 PDF 文档中，以改进导航。
lastmod: "2026-06-09"
---
## Aspose.PDF - 添加目录

要使用 **Aspose.PDF Java for PHP** 在 Pdf 文档中添加 TOC，只需调用 **AddToc** 类即可。

PHP代码

```php

# Open a pdf document.
$doc = new Document($dataDir . "input1.pdf");

# Get access to first page of PDF file
$toc_page = $doc->getPages()->insert(1);

# Create object to represent TOC information
$toc_info = new TocInfo();
$title = new TextFragment("Table Of Contents");
$title->getTextState()->setFontSize(20);
#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Set the title for TOC
$toc_info->setTitle($title);
$toc_page->setTocInfo($toc_info);

# Create string objects which will be used as TOC elements
$titles = array("First page", "Second page");

$i = 0;
while ($i < 2){

    # Create Heading object
    $heading2 = new Heading(1);

    $segment2 = new TextSegment();
    $heading2->setTocPage($toc_page);
    $heading2->getSegments()->add($segment2);

    # Specify the destination page for heading object
    $heading2->setDestinationPage($doc->getPages()->get_Item($i + 2));

    # Destination page
    $heading2->setTop($doc->getPages()->get_Item($i + 2)->getRect()->getHeight());

    # Destination coordinate
    $segment2->setText($titles[$i]);

    # Add heading to page containing TOC
    $toc_page->getParagraphs()->add($heading2);

    $i +=1;

}

# Save PDF Document
$doc->save($dataDir . "TOC.pdf");

print "Added TOC Successfully, please check the output file.";

```

**下载运行代码**

从以下任何一个社交编码网站下载**添加目录 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/AddToc.php)
