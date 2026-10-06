---
title: 在 PHP 中向现有 PDF 文件添加文本
linktitle: 在 PHP 中向现有 PDF 文件添加文本
type: docs
weight: 20
url: /zh/java/add-text-to-an-existing-pdf-file-in-php/
description: 了解如何在 PHP 中使用 Aspose.PDF 向现有 PDF 文档添加新文本，以实现内容增强。
lastmod: "2026-10-06"
---
## Aspose.PDF - 添加文本

要在 Pdf 文档中使用 **Aspose.PDF Java for PHP** 添加文本字符串，只需调用 **AddText** 模块。

PHP 代码

```php

# Instantiate Document object
$doc = new Document($dataDir . 'input1.pdf');

# get particular page
$pdf_page = $doc->getPages()->get_Item(1);

# create text fragment
$text_fragment = new TextFragment("main text");
$text_fragment->setPosition(new Position(100, 600));

$font_repository = new FontRepository();
$color = new Color();

# set text properties
$text_fragment->getTextState()->setFont($font_repository->findFont("Verdana"));
$text_fragment->getTextState()->setFontSize(14);

# create TextBuilder object
$text_builder = new TextBuilder($pdf_page);

# append the text fragment to the PDF page
$text_builder->appendText($text_fragment);

# Save PDF file
$doc->save($dataDir . "Text_Added.pdf");

print "Text added successfully" . PHP_EOL;

```

**下载运行代码**

下载 **Add Text (Aspose.PDF)** 从 以下提到的社交编码站点：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)
