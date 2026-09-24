---
title: Ruby에서 SVG 파일을 PDF 형식으로 변환
linktitle: Ruby에서 SVG 파일을 PDF 형식으로 변환
type: docs
weight: 60
url: /java/convert-svg-file-to-pdf-format-in-ruby/
description: 정확하고 확장 가능한 문서 변환을 위해 Aspose.PDF를 사용하여 Ruby에서 SVG 파일을 PDF 형식으로 변환하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - SVG를 PDF로 변환



**Aspose.PDF Java for Ruby**를 사용하여 SVG 파일을 PDF 형식으로 변환하려면 **SvgToPdf** 모듈을 호출하기만 하면 됩니다.

루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate LoadOption object using SVG load option

options = Rjb::import('com.aspose.pdf.SvgLoadOptions').new

# Create document object

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'Example.svg', options)

# Save the output to XLS format

pdf.save(data_dir + "SVG.pdf")

puts "Document has been converted successfully"
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **SVG를 PDF로 변환(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/svgtopdf.rb)
