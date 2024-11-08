---
title: PHP에서 PDF 문서의 모든 페이지에서 텍스트 추출하기
type: docs
weight: 30
url: /ko/java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - 모든 페이지에서 텍스트 추출

**Aspose.PDF Java for PHP**를 사용하여 Pdf 문서의 모든 페이지에서 텍스트를 추출하려면, 간단히 **ExtractTextFromAllPages** 모듈을 호출하십시오.
PHP 코드

```php

# 대상 문서를 엽니다
$pdf = new Document($dataDir . 'input1.pdf');

# 텍스트를 추출하기 위한 TextAbsorber 객체 생성
$text_absorber = new TextAbsorber();

# 모든 페이지에 대해 absorber를 허용
$pdf->getPages()->accept($text_absorber);

# 문서의 특정 페이지에서 텍스트를 추출하려면, accept(..) 메서드에 대한 인덱스를 사용하여 특정 페이지를 지정해야 합니다.
# 특정 PDF 페이지에 대해 absorber를 허용
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

# 추출된 텍스트를 가져옵니다
$extracted_text = $text_absorber->getText();

# 작성자를 생성하고 파일을 엽니다
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# 파일에 텍스트 라인을 씁니다
# tw.WriteLine(extractedText);
# 스트림을 닫습니다
$writer->close();

print "텍스트가 성공적으로 추출되었습니다. 출력 파일을 확인하세요." . PHP_EOL;

```


**코드 실행 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **모든 페이지에서 텍스트 추출 (Aspose.PDF)** 를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)