---
title: 在 PHP 中在 PDF 文件末尾插入空白页
type: docs
weight: 60
url: /zh/java/insert-an-empty-page-at-end-of-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 在 PDF 文件末尾插入空白页

要使用 **Aspose.PDF Java for PHP** 在 PDF 文档末尾插入空白页，只需调用 **InsertEmptyPageAtEndOfFile** 类。

PHP 代码

```php

# 打开目标文档
$pdf = new Document($dataDir . 'input1.pdf');

# 在 PDF 中插入空白页
$pdf->getPages()->add();

# 保存合并后的输出文件（目标文档）
$pdf->save($dataDir . "output.pdf");

print "空白页添加成功！" . PHP_EOL;

```

## 下载运行代码

从以下任一社交编码网站下载 **Insert an Empty Page at End of PDF File (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)