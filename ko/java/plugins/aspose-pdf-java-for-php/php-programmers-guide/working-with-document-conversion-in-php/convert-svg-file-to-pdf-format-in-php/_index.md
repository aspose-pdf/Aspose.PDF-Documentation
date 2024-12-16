---
title: PHP에서 SVG 파일을 PDF 형식으로 변환
type: docs
weight: 40
url: /ko/java/convert-svg-file-to-pdf-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - SVG를 PDF로 변환

**Aspose.PDF Java for PHP**를 사용하여 SVG 파일을 PDF 형식으로 변환하려면, **SvgToPdf** 모듈을 호출하십시오.

PHP 코드

```php
# SVG 로드 옵션을 사용하여 LoadOption 객체를 인스턴스화합니다.
$options = new SvgLoadOptions();

# 문서 객체를 생성합니다.
$pdf = new Document($dataDir . 'Example.svg', $options);

# 출력을 XLS 형식으로 저장합니다.
$pdf->save($dataDir . "SVG.pdf");

print "문서가 성공적으로 변환되었습니다";

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Convert SVG to PDF (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/SvgToPdf.php)