---
title: 向 PDF 文件中插入空白页在 PHP 中
type: docs
weight: 70
url: /zh/java/insert-an-empty-page-into-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 插入空白页

要在 PDF 文档中插入空白页，使用 **Aspose.PDF Java for PHP**，只需调用 **InsertEmptyPage** 类。

PHP 代码

```php

# 打开目标文档
$pdf = new Document($dataDir . 'input1.pdf');

# 在 PDF 中插入一个空白页
$pdf->getPages()->insert(1);

# 保存合并后的输出文件（目标文档）
$pdf->save($dataDir . "output.pdf");

print "空白页添加成功！";

```

**下载运行代码**

从以下任一社交编码网站下载 **插入空白页 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)