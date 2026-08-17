---
title: PHP에서 PDF 파일 끝에 빈 페이지 삽입
linktitle: PHP에서 PDF 파일 끝에 빈 페이지 삽입
type: docs
weight: 60
url: /java/insert-an-empty-page-at-end-of-pdf-file-in-php/
description: 문서 확장을 위해 Aspose.PDF를 사용하여 PHP에서 PDF 문서 끝에 빈 페이지를 삽입하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF 파일 끝에 빈 페이지 삽입



PHP용 **Aspose.PDF Java**를 사용하여 PDF 문서 끝에 빈 페이지를 삽입하려면 간단히 **InsertEmptyPageAtEndOfFile** 클래스를 호출하면 됩니다.



PHP 코드


```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# insert a empty page in a PDF
$pdf->getPages()->add();

# Save the concatenated output file (the target document)
$pdf->save($dataDir . "output.pdf");

print "Empty page added successfully!" . PHP_EOL;

```

## 
실행 코드 다운로드



**PDF 파일 끝에 빈 페이지 삽입(Aspose.PDF)**В을 아래에 언급된 소셜 코딩 사이트 중 하나에서 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPageAtEndOfFile.php)
