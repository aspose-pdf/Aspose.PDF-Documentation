---
title: DOM을 사용하여 Ruby에서 HTML 문자열 추가
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - HTML 추가

**Aspose.PDF Java for Ruby**를 사용하여 Pdf 문서에 HTML 문자열을 추가하려면, **AddHtml** 모듈을 호출하세요.

Ruby 코드

```java
# 문서 디렉토리 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Document 객체를 인스턴스화합니다.

doc = Rjb::import('com.aspose.pdf.Document').new

# PDF 파일의 페이지 컬렉션에 페이지를 추가합니다.

page = doc.getPages().add()

# HTML 내용을 가진 HtmlFragment를 인스턴스화합니다.

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# 여백 세부 정보를 위한 MarginInfo를 설정합니다.

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# 여백 정보를 설정합니다.

title.setMargin(margin)

# 페이지의 단락 컬렉션에 HTML 조각을 추가합니다.

page.getParagraphs().add(title)

# PDF 파일을 저장합니다.

doc.save(data_dir + "html.output.pdf")

puts "HTML이 성공적으로 추가되었습니다"
```


## Download Running Code

다음의 소셜 코딩 사이트 중 하나에서 **Add HTML (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)