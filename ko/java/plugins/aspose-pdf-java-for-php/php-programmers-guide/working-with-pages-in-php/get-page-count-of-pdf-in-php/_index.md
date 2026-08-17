---
title: PHP에서 PDF의 페이지 수 얻기
linktitle: PHP에서 PDF의 페이지 수 얻기
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-php/
description: 문서 분석을 위해 Aspose.PDF를 사용하여 PHP에서 PDF 문서의 총 페이지 수를 검색하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 페이지 수 가져오기



PHP용 **Aspose.PDF Java**를 사용하여 PDF 문서의 페이지 수를 얻으려면 **GetNumberOfPages** 클래스를 호출하기만 하면 됩니다.



PHP 코드


```php

# Create PDF document

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "Page Count:" . $page_count . PHP_EOL;

```


**실행 코드 다운로드**



아래 언급된 소셜 코딩 사이트 중 하나에서 다운로드**페이지 수 가져오기(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)
