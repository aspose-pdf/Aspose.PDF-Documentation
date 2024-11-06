---
title: PHP에서 PDF를 DOC 또는 DOCX 형식으로 변환
type: docs
weight: 10
url: ko/java/convert-pdf-to-doc-or-docx-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF를 DOC 또는 DOCX로 변환

**Aspose.PDF Java for PHP**를 사용하여 PDF 문서를 DOC 또는 DOCX 형식으로 변환하려면, **PdfToDoc** 모듈을 호출하세요.

PHP 코드

```php

# 대상 문서 열기
$pdf = new Document($dataDir . 'input1.pdf');

# 연결된 출력 파일 저장 (대상 문서)
$pdf->save($dataDir . "output.doc");

print "문서가 성공적으로 변환되었습니다";

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Convert PDF to DOC or DOCX (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToDoc.php)