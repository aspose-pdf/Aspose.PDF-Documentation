---
title: 在 PHP 中更新页面尺寸
type: docs
weight: 90
url: /java/update-page-dimensions-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 更新页面尺寸

要使用 **Aspose.PDF Java for PHP** 更新页面尺寸，只需调用 **UpdatePageDimensions** 类。

PHP 代码

```php

# 打开目标文档
$pdf = new Document($dataDir . 'input1.pdf');

# 获取页面集合
$page_collection = $pdf->getPages();

# 获取特定页面
$pdf_page = $page_collection->get_Item(1);

# 将页面大小设置为 A4 (11.7 x 8.3 英寸)，在 Aspose.PDF 中，1 英寸 = 72 点
# 因此 A4 的尺寸以点为单位为 (842.4, 597.6)
$pdf_page->setPageSize(597.6,842.4);

# 保存新生成的 PDF 文件
$pdf->save($dataDir . "output.pdf");

print "尺寸更新成功！" . PHP_EOL;

```

**下载运行代码**

从以下任一社交编码网站下载 **更新页面尺寸 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/UpdatePageDimensions.php)