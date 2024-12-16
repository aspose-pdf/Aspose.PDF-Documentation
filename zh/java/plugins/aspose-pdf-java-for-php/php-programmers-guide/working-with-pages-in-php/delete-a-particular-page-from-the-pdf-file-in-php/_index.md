---
title: 从 PDF 文件中删除特定页面在 PHP 中
type: docs
weight: 20
url: /zh/java/delete-a-particular-page-from-the-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 删除页面

要使用 **Aspose.PDF Java for PHP** 从 PDF 文档中删除特定页面，只需调用 **DeletePage** 类。

PHP 代码

```php

# 打开目标文档
$pdf = new Document($dataDir . 'input1.pdf');

# 删除特定页面
$pdf->getPages()->delete(2);

# 保存新生成的 PDF 文件
$pdf->save($dataDir . "output.pdf");

print "页面删除成功！";

```

**下载运行**

从以下任一提到的社交编码网站下载 **Delete Page (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)