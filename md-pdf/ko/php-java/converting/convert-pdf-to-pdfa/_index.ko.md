---
title: PDF를 PDF/A 형식으로 변환하기
linktitle: PDF를 PDF/A 형식으로 변환하기
type: docs
weight: 100
url: /php-java/convert-pdf-to-pdfa/
lastmod: "2024-05-20"
description: 이 주제는 Aspose.PDF가 PDF 파일을 PDF/A 호환 PDF 파일로 변환하는 방법을 보여줍니다.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF for PHP**를 사용하면 PDF 파일을 PDF/A 호환 PDF 파일로 변환할 수 있습니다. 이를 수행하기 전에 파일을 검증해야 합니다. 이 문서에서는 그 방법을 설명합니다.

PDF/A 적합성을 검증하기 위해 Adobe Preflight를 따릅니다. 시장의 모든 도구는 PDF/A 적합성에 대한 자신만의 "표현"을 가지고 있습니다. 참조를 위해 [PDF/A 검증 도구](http://wiki.opf-labs.org/display/SPR/PDFA+Validation+tools+give+different+results)에 대한 이 기사를 확인하십시오. Aspose.PDF가 PDF 파일을 생성하는 방식을 확인하기 위해 Adobe 제품을 선택한 이유는 Adobe가 PDF와 관련된 모든 것의 중심에 있기 때문입니다.

PDF를 PDF/A 호환 파일로 변환하기 전에 validate 메소드를 사용하여 PDF를 검증하십시오.
 유효성 검사 결과는 XML 파일에 저장된 후 이 결과가 convert 메서드로 전달됩니다. [ConvertErrorAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/converterroraction) 열거형을 사용하여 변환할 수 없는 요소에 대한 작업을 지정할 수도 있습니다.

## PDF를 PDF/A로 변환

다음 코드 스니펫은 PDF 파일을 PDF/A-1b 규격의 PDF로 변환하는 방법을 보여줍니다.

```php
// 새 Document 객체를 생성하고 입력 PDF 파일을 로드합니다.
$document = new Document($inputFile);

// 문서를 PDF/A-1a 형식으로 변환하고 로그 파일 및 오류 작업을 지정합니다.
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// 변환된 문서를 출력 파일로 저장합니다.
$document->save($outputFile);
```

유효성 검사만 수행하려면 다음 코드를 사용하십시오:

```php
// 새 Document 객체를 생성하고 입력 PDF 파일을 로드합니다.
$document = new Document($inputFile);

// 문서를 PDF/A-1a 형식으로 변환하고 로그 파일 및 오류 작업을 지정합니다.
$res = $document->convert($logFile, PdfFormat::$PDF_A_1A, ConvertErrorAction::$Delete);

// PDF/A-1a에 대해 PDF를 검증합니다.
if ($document->validate("validation-result-A1A.xml", PdfFormat.PDF_A_1A))
{
    echo "유효함";
}
else
{
    echo "유효하지 않음";
}
```

{{% alert color="primary" %}}
**PDF를 PDF/A로 온라인 변환 시도하기**

Aspose.PDF for PHP는 온라인 무료 애플리케이션 ["PDF to PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)을 제공합니다. 여기서 기능과 품질을 확인해 볼 수 있습니다.

[![Aspose.PDF 무료 앱으로 PDF를 PDF/A로 변환하기](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}