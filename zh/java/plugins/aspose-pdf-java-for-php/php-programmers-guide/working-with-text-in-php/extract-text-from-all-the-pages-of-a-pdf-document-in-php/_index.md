---
title: 使用 PHP 从 PDF 文档的所有页面中提取文本
linktitle: 使用 PHP 从 PDF 文档的所有页面中提取文本
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
description: 了解如何使用 Aspose.PDF 从 PHP 中的 PDF 文档的所有页面中提取文本进行文本分析。
lastmod: "2026-06-09"
---
## Aspose.PDF - 从所有页面中提取文本

要使用 **Aspose.PDF Java for PHP** 提取 TextrFrom All Pages Pdf 文档，只需调用 **ExtractTextFromAllPages** 模块即可。
PHP代码

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# create TextAbsorber object to extract text
$text_absorber = new TextAbsorber();

# accept the absorber for all the pages
$pdf->getPages()->accept($text_absorber);

# In order to extract text from specific page of document, we need to specify the particular page using its index against accept(..) method.
# accept the absorber for particular PDF page
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

#get the extracted text
$extracted_text = $text_absorber->getText();

# create a writer and open the file
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# write a line of text to the file
# tw.WriteLine(extractedText);
# close the stream
$writer->close();

print "Text extracted successfully. Check output file." . PHP_EOL;

```

**下载运行代码**

从以下任何一个社交编码网站下载**从所有页面提取文本 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)
