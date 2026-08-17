---
title: PHP에서 PDF 파일에 빈 페이지 삽입
linktitle: PHP에서 PDF 파일에 빈 페이지 삽입
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-php/
description: 유연한 문서 구조화를 위해 Aspose.PDF를 사용하여 PHP에서 PDF 파일 내 임의 위치에 빈 페이지를 삽입하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 빈 페이지 삽입



**Aspose.PDF Java for PHP**를 사용하여 PDF 문서에 빈 페이지를 삽입하려면 **InsertEmptyPage** 클래스를 호출하기만 하면 됩니다.



PHP 코드


```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->insert(1);

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!";

```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **빈 페이지 삽입(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)
