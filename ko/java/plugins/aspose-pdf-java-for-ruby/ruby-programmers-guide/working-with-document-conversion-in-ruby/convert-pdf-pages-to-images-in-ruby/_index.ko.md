---
title: Ruby에서 PDF 페이지를 이미지로 변환
type: docs
weight: 20
url: /java/convert-pdf-pages-to-images-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF 페이지를 이미지로 변환

**Aspose.PDF Java for Ruby**를 사용하여 Pdf 문서의 모든 페이지를 이미지로 변환하려면, **ConvertPagesToImages** 모듈을 호출하세요.

Ruby 코드

```java

# 문서 디렉터리의 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

converter = Rjb::import('com.aspose.pdf.facades.PdfConverter').new

converter.bindPdf(data_dir + 'input1.pdf')

converter.doConvert()

suffix = ".jpg"

image_count = 1

image_format_internal = Rjb::import('com.aspose.pdf.ImageFormatInternal')

while converter.hasNextImage()

    converter.getNextImage(data_dir + "image#{image_count}#{suffix}", image_format_internal.getJpeg())

    image_count +=1

end

puts "PDF 페이지가 개별 이미지로 성공적으로 변환되었습니다!"
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **PDF 페이지를 이미지로 변환 (Aspose.PDF)**를 다운로드하세요.

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/convertpagestoimages.rb)