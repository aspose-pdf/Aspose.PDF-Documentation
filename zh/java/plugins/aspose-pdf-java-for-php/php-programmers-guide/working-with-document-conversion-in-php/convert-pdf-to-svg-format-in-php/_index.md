---
title: 将PDF转换为SVG格式在PHP中
type: docs
weight: 30
url: zh/java/convert-pdf-to-svg-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 将PDF转换为SVG

要使用**Aspose.PDF Java for PHP**将PDF转换为SVG格式，只需调用**PdfToSvg**模块。

PHP代码

```php

# 打开目标文档
$pdf = new Document($dataDir . 'input1.pdf');

# 实例化一个SvgSaveOptions对象
$save_options = new SvgSaveOptions();

# 不将SVG图像压缩到Zip档案
$save_options->CompressOutputToZipArchive = false;

# 将输出保存为XLS格式
$pdf->save($dataDir . "Output.svg", $save_options);

print "文档已成功转换" . PHP_EOL;

```

**下载运行代码**

从以下任一社交编码网站下载**将PDF转换为SVG格式 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)