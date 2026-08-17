---
title: Ruby에서 PDF를 Excel 통합 문서로 변환
linktitle: Ruby에서 PDF를 Excel 통합 문서로 변환
type: docs
weight: 40
url: /java/convert-pdf-to-excel-workbook-in-ruby/
description: Aspose.PDF와 함께 Ruby를 사용하여 PDF 데이터를 Excel 통합 문서로 변환하고 데이터 추출 및 분석을 단순화하는 방법을 이해합니다.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF를 Excel 통합 문서로 변환



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서를 Excel 통합 문서로 변환하려면 **PdfToExcel** 모듈을 호출하기만 하면 됩니다.



루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Instantiate ExcelSave Option object

excelsave = Rjb::import('com.aspose.pdf.ExcelSaveOptions').new

# Save the output to XLS format

pdf.save(data_dir + "Converted_Excel.xls", excelsave)

puts "Document has been converted successfully"
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF를 DOC 또는 DOCX로 변환(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftoexcel.rb)
