---
title: PHP에서 PDF 문서의 모든 페이지에서 텍스트 추출
linktitle: PHP에서 PDF 문서의 모든 페이지에서 텍스트 추출
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-php/
description: 텍스트 분석을 위해 Aspose.PDF를 사용하여 PHP에서 PDF 문서의 모든 페이지에서 텍스트를 추출하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 모든 페이지에서 텍스트 추출



**Aspose.PDF Java for PHP**를 사용하여 TextrFrom 모든 페이지 PDF 문서를 추출하려면 **ExtractTextFromAllPages** 모듈을 호출하기만 하면 됩니다.
PHP 코드


```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# create TextAbsorber object to extract text
$text_absorber = new TextAbsorber();

# accept the absorber for all the pages
$pdf->getPages()->accept($text_absorber);

# In order to extract text from specific page of document, we need to specify the particular page using its index against accept(..) method.
# accept the absorber for particular PDF page
# pdfDocument.getPages().get_Item(1).accept(textAbsorber);

#get the extracted text
$extracted_text = $text_absorber->getText();

# create a writer and open the file
$writer = new FileWriter(new File($dataDir . "extracted_text.out.txt"));
$writer->write($extracted_text);
# write a line of text to the file
# tw.WriteLine(extractedText);
# close the stream
$writer->close();

print "Text extracted successfully. Check output file." . PHP_EOL;

```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트 중 하나에서 **모든 페이지에서 텍스트 추출(Aspose.PDF)**을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithText/ExtractTextFromAllPages.php)
