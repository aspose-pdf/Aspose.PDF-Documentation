---
title: 将SVG文件转换为PDF格式在PHP中
type: docs
weight: 40
url: /java/convert-svg-file-to-pdf-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 将SVG转换为PDF

要使用**Aspose.PDF Java for PHP**将SVG文件转换为PDF格式，只需调用**SvgToPdf**模块。

PHP代码

```php
# 使用SVG加载选项实例化LoadOption对象
$options = new SvgLoadOptions();

# 创建文档对象
$pdf = new Document($dataDir . 'Example.svg', $options);

# 将输出保存为XLS格式
$pdf->save($dataDir . "SVG.pdf");

print "文档已成功转换";

```

**下载运行代码**

从以下任一社交编码网站下载**Convert SVG to PDF (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)