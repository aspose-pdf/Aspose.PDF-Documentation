---
title: PHP에서 웹을 위한 PDF 문서 최적화
type: docs
weight: 60
url: ko/java/optimize-pdf-document-for-the-web-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 웹을 위한 PDF 최적화

**Aspose.PDF Java for PHP**를 사용하여 웹을 위한 PDF 문서를 최적화하려면, **Optimize** 클래스의 **optimize_web** 메서드를 호출하세요.

PHP 코드

```php

 public static function optimize_web($dataDir=null)

{

    # PDF 문서를 엽니다.

    $doc = new Document($dataDir . "input1.pdf");

    # 웹을 위해 최적화합니다.

    $doc->optimize();

    # 출력 문서를 저장합니다.

    $doc->save($dataDir . "Optimized_Web.pdf");

    print "웹을 위한 PDF 최적화가 완료되었습니다. 출력 파일을 확인하세요." . PHP_EOL;

}   
```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Optimize PDF for Web (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentObject/Optimize.php)