---
title: PHP 파일에서 특정 페이지 삭제
type: docs
weight: 20
url: /ko/java/delete-a-particular-page-from-the-pdf-file-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 페이지 삭제

**Aspose.PDF Java for PHP**를 사용하여 PDF 문서에서 특정 페이지를 삭제하려면, **DeletePage** 클래스를 호출하세요.

PHP 코드

```php

# 대상 문서 열기
$pdf = new Document($dataDir . 'input1.pdf');

# 특정 페이지 삭제
$pdf->getPages()->delete(2);

# 새로 생성된 PDF 파일 저장
$pdf->save($dataDir . "output.pdf");

print "페이지가 성공적으로 삭제되었습니다!";

```

**실행 파일 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **삭제 페이지 (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/DeletePage.php)