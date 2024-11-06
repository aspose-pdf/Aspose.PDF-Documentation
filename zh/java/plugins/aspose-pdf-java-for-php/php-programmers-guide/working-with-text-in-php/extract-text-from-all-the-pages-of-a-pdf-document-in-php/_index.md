---
title: 从PDF文档的所有页面提取文本在PHP中
type: docs
weight: 30
url: zh/java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 从所有页面提取文本

要使用**Aspose.PDF Java for PHP**从PDF文档的所有页面提取文本，只需调用**ExtractTextFromAllPages**模块。
PHP代码

```php

# 打开目标文档
$pdf = new Document($dataDir . 'input1.pdf');

# 创建TextAbsorber对象以提取文本
$text_absorber = new TextAbsorber();

# 接受所有页面的吸收器
$pdf->getPages()->accept($text_absorber);

# 为了从文档的特定页面提取文本，我们需要使用其索引指定特定页面以对accept(..)方法进行操作。
# 接受特定PDF页面的吸收器
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# 获取提取的文本
$extracted_text = $text_absorber->getText();

# 创建一个写入器并打开文件
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# 将一行文本写入文件
# tw.WriteLine(extractedText);
# 关闭流
$writer->close();

print "文本提取成功。检查输出文件。" . PHP_EOL;

```


**下载运行代码**

从以下任意一个社交编码网站下载**从所有页面提取文本 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)