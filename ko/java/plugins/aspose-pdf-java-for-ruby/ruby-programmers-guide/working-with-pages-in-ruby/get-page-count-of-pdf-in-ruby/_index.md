---
title: Ruby에서 PDF의 페이지 수 얻기
type: docs
weight: 40
url: /ko/java/get-page-count-of-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 페이지 수 얻기

**Aspose.PDF Java for Ruby**를 사용하여 Pdf 문서의 페이지 수를 얻으려면, 간단히 **GetNumberOfPages** 모듈을 호출하십시오.

Ruby 코드

```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDF 문서 생성

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## 실행 코드 다운로드

아래 언급된 소셜 코딩 사이트 중 하나에서 **Get Page Count (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)