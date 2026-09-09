---
title: Ruby에서 PDF의 페이지 수 얻기
linktitle: Ruby에서 PDF의 페이지 수 얻기
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-ruby/
description: Aspose.PDF와 함께 Ruby를 사용하여 프로그래밍 방식으로 PDF 문서의 총 페이지 수를 검색합니다.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 페이지 수 가져오기



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서의 페이지 수를 얻으려면 **GetNumberOfPages** 모듈을 호출하기만 하면 됩니다.

루비 코드


```java
data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Create PDF document

pdf = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

page_count = pdf.getPages().size()

puts "Page Count:" + page_count.to_s
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 다운로드**페이지 수 가져오기(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getnumberofpages.rb)
