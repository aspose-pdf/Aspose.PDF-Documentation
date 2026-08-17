---
title: Ruby에서 HTML을 PDF 형식으로 변환
linktitle: Ruby에서 HTML을 PDF 형식으로 변환
type: docs
weight: 10
url: /java/convert-html-to-pdf-format-in-ruby/
description: 안정적이고 정확한 문서 생성을 위해 Aspose.PDF를 사용하여 Ruby에서 HTML 콘텐츠를 PDF 형식으로 변환하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - HTML을 PDF 형식으로 변환



**Aspose.PDF Java for Ruby**를 사용하여 HTML을 PDF 형식으로 변환하려면 **HtmlToPdf** 모듈을 호출하기만 하면 됩니다.



루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# Load HTML file

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# Save the concatenated output file (the target document)

pdf.save(data_dir + "html.pdf")

puts "Document has been converted successfully"
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **HTML을 PDF 형식으로 변환(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)
