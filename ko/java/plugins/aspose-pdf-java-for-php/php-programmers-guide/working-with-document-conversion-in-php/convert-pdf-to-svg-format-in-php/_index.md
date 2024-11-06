---
title: PHP에서 PDF를 SVG 형식으로 변환
type: docs
weight: 30
url: ko/java/convert-pdf-to-svg-format-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF를 SVG로 변환

**Aspose.PDF Java for PHP**를 사용하여 PDF를 SVG 형식으로 변환하려면, **PdfToSvg** 모듈을 호출하십시오.

PHP 코드

```php

# 대상 문서 열기
$pdf = new Document($dataDir . 'input1.pdf');

# SvgSaveOptions 객체 인스턴스화
$save_options = new SvgSaveOptions();

# SVG 이미지를 Zip 아카이브로 압축하지 않음
$save_options->CompressOutputToZipArchive = false;

# 출력을 XLS 형식으로 저장
$pdf->save($dataDir . "Output.svg", $save_options);

print "문서가 성공적으로 변환되었습니다" . PHP_EOL;

```

**실행 코드 다운로드**

다음에 언급된 소셜 코딩 사이트 중 하나에서 **Convert PDF to SVG Format (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithDocumentConversion/PdfToSvg.php)