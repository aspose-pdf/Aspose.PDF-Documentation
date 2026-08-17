---
title: Ruby에서 PDF를 DOC 또는 DOCX 형식으로 변환
linktitle: Ruby에서 PDF를 DOC 또는 DOCX 형식으로 변환
type: docs
weight: 30
url: /java/convert-pdf-to-doc-or-docx-format-in-ruby/
description: Aspose.PDF를 사용하여 Ruby에서 PDF 문서를 DOC 또는 DOCX 형식으로 변환하여 더 쉽게 편집하고 처리하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF를 DOC 또는 DOCX로 변환



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서를 DOC 또는 DOCX 형식으로 변환하려면 **PdfToDoc** 모듈을 호출하기만 하면 됩니다.



루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Save the concatenated output file (the target document)

pdf.save(data_dir + "output.doc")

puts "Document has been converted successfully"
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF를 DOC 또는 DOCX로 변환(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftodoc.rb)
