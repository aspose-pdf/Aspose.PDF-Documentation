---
title: PHP에서 PDF 파일 연결
type: docs
weight: 10
url: ko/java/concatenate-pdf-files-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF 파일 연결

**Aspose.PDF Java for PHP**를 사용하여 PDF 파일을 연결하려면, **ConcatenatePdfFiles** 클래스를 호출하십시오.

PHP 코드

```php

# 대상 문서 열기
$pdf1 = new Document($dataDir . 'input1.pdf');

# 소스 문서 열기
$pdf2 = new Document($dataDir . 'input2.pdf');

# 소스 문서의 페이지를 대상 문서에 추가
$pdf1->getPages()->add($pdf2->getPages());

# 연결된 출력 파일 저장 (대상 문서)
$pdf1->save($dataDir . "Concatenate_output.pdf");

print "새 문서가 저장되었습니다. 출력 파일을 확인하십시오." . PHP_EOL;

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Concatenate PDF Files (Aspose.PDF)** 를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/ConcatenatePdfFiles.php)