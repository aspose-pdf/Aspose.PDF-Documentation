---
title: PHP에서 PDF 파일에 빈 페이지 삽입
type: docs
weight: 70
url: /ko/java/insert-an-empty-page-into-a-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 빈 페이지 삽입

**Aspose.PDF Java for PHP**를 사용하여 Pdf 문서에 빈 페이지를 삽입하려면, **InsertEmptyPage** 클래스를 호출하십시오.

PHP 코드

```php

# 대상 문서를 엽니다
$pdf = new Document($dataDir . 'input1.pdf');

# PDF에 빈 페이지 삽입
$pdf->getPages()->insert(1);

# 결합된 출력 파일(대상 문서)을 저장합니다
$pdf->save($dataDir . "output.pdf");

print "빈 페이지가 성공적으로 추가되었습니다!";

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **빈 페이지 삽입 (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/InsertEmptyPage.php)