---
title: 在 PHP 中将 PDF 文件拆分为单独的页面
linktitle: 在 PHP 中将 PDF 文件拆分为单独的页面
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-php/
description: 了解如何使用 PHP 和 Aspose.PDF 将 PDF 文档拆分为单独的页面，以实现高效的页面提取。
lastmod: "2026-06-09"
---
## Aspose.PDF - 拆分页面

要使用 **Aspose.PDF Java for PHP** 将 PDF 文档拆分为单独的页面，只需调用 **SplitAllPages** 类即可。

PHP代码

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# loop through all the pages
$pdf_page = 1;
$total_size = $pdf->getPages()->size();
#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)
while ($pdf_page <= $total_size)

{

    # create a new Document object
    $new_document = new Document();

    # get the page at particular index of Page Collection
    $new_document->getPages()->add($pdf->getPages()->get_Item($pdf_page));

    # save the newly generated PDF file
    $new_document->save($dataDir . "page_#{$pdf_page}.pdf");

    $pdf_page++;

}

print "Split process completed successfully!";

```

**下载运行代码**

从以下任何一个社交编码网站下载 **拆分页面 (Aspose.PDF)**：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)
