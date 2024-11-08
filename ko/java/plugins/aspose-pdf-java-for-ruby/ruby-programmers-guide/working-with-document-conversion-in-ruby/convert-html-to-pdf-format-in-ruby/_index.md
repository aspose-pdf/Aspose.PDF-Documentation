---
title: HTML을 PDF 형식으로 변환하기 - Ruby
type: docs
weight: 10
url: /ko/java/convert-html-to-pdf-format-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - HTML을 PDF 형식으로 변환하기

**Aspose.PDF Java for Ruby**를 사용하여 HTML을 PDF 형식으로 변환하려면, **HtmlToPdf** 모듈을 호출하세요.

Ruby 코드

```java

# 문서 디렉토리 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

htmloptions = Rjb::import('com.aspose.pdf.HtmlLoadOptions').new(data_dir)

# HTML 파일 로드

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + "index.html", htmloptions)

# 연결된 출력 파일 저장 (대상 문서)

pdf.save(data_dir + "html.pdf")

puts "문서가 성공적으로 변환되었습니다"
```

## 실행 코드 다운로드

**Convert HTML to PDF Format (Aspose.PDF)**를 아래 언급된 소셜 코딩 사이트 중 하나에서 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Converter/htmltopdf.rb)