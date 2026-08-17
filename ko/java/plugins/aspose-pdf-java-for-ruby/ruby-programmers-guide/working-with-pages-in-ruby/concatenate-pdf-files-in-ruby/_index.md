---
title: Ruby에서 PDF 파일 연결
linktitle: Ruby에서 PDF 파일 연결
type: docs
weight: 10
url: /java/concatenate-pdf-files-in-ruby/
description: Ruby 및 Aspose.PDF를 효율적으로 사용하여 여러 PDF를 단일 문서로 결합합니다.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF 파일 연결



**Aspose.PDF Java for Ruby**를 사용하여 PDF 파일을 연결하려면 **ConcatenatePdfFiles** 모듈을 호출하기만 하면 됩니다.



루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf1 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# Open the source document

pdf2 = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input2.pdf')

# Add the pages of the source document to the target document

pdf1.getPages().add(pdf2.getPages())

# Save the concatenated output file (the target document)

pdf1.save(data_dir+ "Concatenate_output.pdf")

puts "New document has been saved, please check the output file"
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF 파일 연결(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/concatenatepdffiles.rb)
