---
title: PHP에서 웹용 PDF 문서 최적화
linktitle: PHP에서 웹용 PDF 문서 최적화
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-php/
description: Aspose.PDF를 사용하여 PHP에서 더 빠른 웹 성능과 파일 크기 감소를 위해 PDF 문서를 최적화하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 웹용 PDF 최적화



**Aspose.PDF Java for PHP**를 사용하여 웹용 PDF 문서를 최적화하려면 **Optimize** 클래스의 **optimize_web** 메소드를 호출하기만 하면 됩니다.



PHP 코드


```php

 public static function optimize_web($dataDir=null)

{

    # Open a pdf document.

    $doc = new Document($dataDir . "input1.pdf");

    # Optimize for web

    $doc->optimize();

    #Save output document

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "Optimized PDF for the Web, please check output file." . PHP_EOL;

}В В В
```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서**웹용 PDF 최적화(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)
