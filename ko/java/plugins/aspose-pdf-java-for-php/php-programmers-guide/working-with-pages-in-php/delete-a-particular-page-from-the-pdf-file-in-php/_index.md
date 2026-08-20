---
title: PHP의 PDF 파일에서 특정 페이지 삭제
linktitle: PHP의 PDF 파일에서 특정 페이지 삭제
type: docs
weight: 20
url: /java/delete-a-particular-page-from-the-pdf-file-in-php/
description: Aspose.PDF를 사용하여 PHP의 PDF 문서에서 특정 페이지를 삭제하여 문서 편집을 단순화하는 방법을 살펴보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 페이지 삭제



PHP용 **Aspose.PDF Java**를 사용하여 PDF 문서에서 특정 페이지를 삭제하려면 **DeletePage** 클래스를 호출하면 됩니다.

PHP 코드


```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# delete a particular page
$pdf->getPages()->delete(2);

# save the newly generated PDF file
$pdf->save($dataDir . "output.pdf");

print "Page deleted successfully!";

```


**러닝 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **페이지 삭제(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)
