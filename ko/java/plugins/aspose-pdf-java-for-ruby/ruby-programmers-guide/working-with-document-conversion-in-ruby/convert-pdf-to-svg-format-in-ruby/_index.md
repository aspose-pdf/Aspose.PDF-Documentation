---
title: Ruby에서 PDF를 SVG 형식으로 변환
linktitle: Ruby에서 PDF를 SVG 형식으로 변환
type: docs
weight: 50
url: /java/convert-pdf-to-svg-format-in-ruby/
description: Ruby 및 Aspose.PDF를 사용하여 PDF 파일을 SVG 형식으로 변환하여 확장 가능하고 편집 가능한 벡터 그래픽을 활성화하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF를 SVG로 변환



**Aspose.PDF Java for Ruby**를 사용하여 PDF를 SVG 형식으로 변환하려면 **PdfToSvg** 모듈을 호출하기만 하면 됩니다.

루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open the target document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# instantiate an object of SvgSaveOptions

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# do not compress SVG image to Zip archive

save_options.CompressOutputToZipArchive = false

# Save the output to XLS format

pdf.save(data_dir + "Output.svg", save_options)

puts "Document has been converted successfully"
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF를 SVG 형식으로 변환(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)
