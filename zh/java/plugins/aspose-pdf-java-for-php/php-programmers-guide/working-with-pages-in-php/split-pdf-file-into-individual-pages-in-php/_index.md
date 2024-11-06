---
title: 将 PDF 文件拆分为单独页面在 PHP 中
type: docs
weight: 80
url: zh/java/split-pdf-file-into-individual-pages-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 拆分页面

要使用 **Aspose.PDF Java for PHP** 将 PDF 文档拆分为单独页面，只需调用 **SplitAllPages** 类。

PHP 代码

```php

# 打开目标文档
$pdf = new Document($dataDir . 'input1.pdf');

# 遍历所有页面
$pdf_page = 1;
$total_size = $pdf->getPages()->size();
#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)
while ($pdf_page <= $total_size)

{

    # 创建一个新的 Document 对象
    $new_document = new Document();

    # 获取页面集合中特定索引的页面
    $new_document->getPages()->add($pdf->getPages()->get_Item($pdf_page));

    # 保存新生成的 PDF 文件
    $new_document->save($dataDir . "page_#{$pdf_page}.pdf");

    $pdf_page++;

}

print "拆分过程成功完成！";

```

**下载运行代码**

从以下任何一个社交编码网站下载 **Split Pages (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)