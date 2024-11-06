---
title: PHP에서 PDF의 페이지 수 가져오기
type: docs
weight: 40
url: ko/java/get-page-count-of-pdf-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 페이지 수 가져오기

**Aspose.PDF Java for PHP**를 사용하여 Pdf 문서의 페이지 수를 가져오려면 **GetNumberOfPages** 클래스를 호출하십시오.

PHP 코드

```php

# PDF 문서 생성

$pdf = new Document($dataDir . 'input1.pdf');

$page_count = $pdf->getPages()->size();

print "페이지 수:" . $page_count . PHP_EOL;

```

**실행 코드 다운로드**

다음 소셜 코딩 사이트 중 하나에서 **Get Page Count (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/GetNumberOfPages.php)