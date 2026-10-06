---
title: 在 PHP 中提取 PDF 文档所有页面的文本
linktitle: 在 PHP 中提取 PDF 文档所有页面的文本
type: docs
weight: 30
url: /zh/java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
description: 了解如何使用 Aspose.PDF 在 PHP 中提取 PDF 文档所有页面的文本进行文本分析。
lastmod: "2026-10-06"
---
## Aspose.PDF - 从所有页面提取文本

要使用 **Aspose.PDF Java for PHP** 从 PDF 文档的所有页面提取 TextrFrom，只需调用 **ExtractTextFromAllPages** 模块。
PHP 代码

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

下载В **提取所有页面的文本 (Aspose.PDF)**В 来自В 以下任意提及的社交编码站点:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)
