---
title: Ruby에서 PDF 페이지를 이미지로 변환
linktitle: Ruby에서 PDF 페이지를 이미지로 변환
type: docs
weight: 20
url: /java/convert-pdf-pages-to-images-in-ruby/
description: Aspose.PDF와 함께 Ruby를 사용하여 PDF 페이지를 이미지로 변환하여 PDF에서 시각적 콘텐츠를 쉽게 추출하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - PDF 페이지를 이미지로 변환



**Aspose.PDF Java for Ruby**를 사용하여 모든 페이지를 PDF 문서의 이미지로 변환하려면 **ConvertPagesToImages** 모듈을 호출하기만 하면 됩니다.

루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

В В В  converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

В В В  image_count +=1

end

puts "PDF pages are converted to individual images successfully!"
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 **PDF 페이지를 이미지로 변환(Aspose.PDF)**В을 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)
