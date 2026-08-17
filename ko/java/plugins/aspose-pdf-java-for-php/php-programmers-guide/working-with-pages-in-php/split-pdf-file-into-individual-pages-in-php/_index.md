---
title: PHP에서 PDF 파일을 개별 페이지로 분할
linktitle: PHP에서 PDF 파일을 개별 페이지로 분할
type: docs
weight: 80
url: /java/split-pdf-file-into-individual-pages-in-php/
description: 효율적인 페이지 추출을 위해 PHP 및 Aspose.PDF를 사용하여 PDF 문서를 개별 페이지로 분할하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 분할 페이지



**Aspose.PDF Java for PHP**를 사용하여 PDF 문서를 개별 페이지로 분할하려면 **SplitAllPages** 클래스를 호출하기만 하면 됩니다.



PHP 코드


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


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **Split Pages(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)
