---
title: 使用 PHP 将文本添加到现有 PDF 文件
linktitle: 使用 PHP 将文本添加到现有 PDF 文件
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-php/
description: 了解如何使用 Aspose.PDF 在 PHP 中向现有 PDF 文档添加新文本以增强内容。
lastmod: "2026-06-09"
---
## Aspose.PDF - 添加文本

要使用 **Aspose.PDF Java for PHP** 在 Pdf 文档中添加文本字符串，只需调用 **AddText** 模块即可。

PHP代码

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

从以下任何一个社交编码网站下载**添加文本 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/AddText.php)
