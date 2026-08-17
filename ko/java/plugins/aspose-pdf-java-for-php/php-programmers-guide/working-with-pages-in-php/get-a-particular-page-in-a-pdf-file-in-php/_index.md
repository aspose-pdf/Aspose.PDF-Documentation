---
title: PHP에서 PDF 파일의 특정 페이지 가져오기
linktitle: PHP에서 PDF 파일의 특정 페이지 가져오기
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-php/
description: 대상 페이지 처리를 위해 Aspose.PDF를 사용하여 PHP의 PDF 파일에서 특정 페이지를 검색하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 페이지 가져오기



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서의 특정 페이지를 얻으려면 **GetPage** 클래스를 호출하기만 하면 됩니다.



루비 코드


```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# get the page at particular index of Page Collection
$pdf_page = $pdf->getPages()->get_Item(1);

# create a new Document object
$new_document = new Document();

# add page to pages collection of new document object
$new_document->getPages()->add($pdf_page);

# save the newly generated PDF file
$new_document->save($dataDir . "output.pdf");

print "Process completed successfully!";

```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **Get Page(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetPage.php)
