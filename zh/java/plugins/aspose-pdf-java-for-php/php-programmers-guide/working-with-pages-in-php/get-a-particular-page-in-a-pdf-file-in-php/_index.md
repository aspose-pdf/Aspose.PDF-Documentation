---
title: 在 PHP 中获取 PDF 文件中的特定页面
type: docs
weight: 30
url: zh/java/get-a-particular-page-in-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 获取页面

要使用 **Aspose.PDF Java for Ruby** 获取 PDF 文档中的特定页面，只需调用 **GetPage** 类。

Ruby 代码

```php

# 打开目标文档
$pdf = new Document($dataDir . 'input1.pdf');

# 获取页面集合中特定索引处的页面
$pdf_page = $pdf->getPages()->get_Item(1);

# 创建一个新的 Document 对象
$new_document = new Document();

# 将页面添加到新文档对象的页面集合中
$new_document->getPages()->add($pdf_page);

# 保存新生成的 PDF 文件
$new_document->save($dataDir . "output.pdf");

print "Process completed successfully!";

```

## 下载运行代码

从以下任一社交编码网站下载 **获取页面 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)