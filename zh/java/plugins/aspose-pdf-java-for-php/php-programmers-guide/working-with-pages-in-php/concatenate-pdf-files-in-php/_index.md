---
title: 在 PHP 中合并 PDF 文件
type: docs
weight: 10
url: zh/java/concatenate-pdf-files-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 合并 PDF 文件

要使用 **Aspose.PDF Java for PHP** 合并 PDF 文件，只需调用 **ConcatenatePdfFiles** 类。

PHP 代码

```php

# 打开目标文档
$pdf1 = new Document($dataDir . 'input1.pdf');

# 打开源文档
$pdf2 = new Document($dataDir . 'input2.pdf');

# 将源文档的页面添加到目标文档
$pdf1->getPages()->add($pdf2->getPages());

# 保存合并后的输出文件（目标文档）
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "新文档已保存，请检查输出文件" . PHP_EOL;

```

**下载运行代码**

从以下任一社交编码网站下载 **Concatenate PDF Files (Aspose.PDF)**：


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)