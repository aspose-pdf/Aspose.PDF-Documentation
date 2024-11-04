---
title: Ruby에서 PDF를 SVG 형식으로 변환
type: docs
weight: 50
url: /java/convert-pdf-to-svg-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - PDF를 SVG로 변환

**Aspose.PDF Java for Ruby**를 사용하여 PDF를 SVG 형식으로 변환하려면, **PdfToSvg** 모듈을 호출하십시오.

Ruby 코드

```java

# 문서 디렉토리의 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# 대상 문서를 엽니다

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# SvgSaveOptions 객체의 인스턴스화

save_options = Rjb::import('com.aspose.pdf.SvgSaveOptions').new

# SVG 이미지를 Zip 아카이브로 압축하지 않음

save_options.CompressOutputToZipArchive = false

# 출력을 XLS 형식으로 저장

pdf.save(data_dir + "Output.svg", save_options)

puts "문서가 성공적으로 변환되었습니다"
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **Convert PDF to SVG Format (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/pdftosvg.rb)