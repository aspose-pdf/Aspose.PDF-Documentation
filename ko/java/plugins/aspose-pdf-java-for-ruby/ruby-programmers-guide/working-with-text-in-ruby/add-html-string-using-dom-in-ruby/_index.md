---
title: Ruby에서 DOM을 사용하여 HTML 문자열 추가
linktitle: Ruby에서 DOM을 사용하여 HTML 문자열 추가
type: docs
weight: 10
url: /java/add-html-string-using-dom-in-ruby/
description: 동적 콘텐츠 생성을 위해 Aspose.PDF와 함께 Ruby의 DOM API를 사용하여 PDF 문서에 HTML 문자열을 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - HTML 추가



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서에 HTML 문자열을 추가하려면 **AddHtml** 모듈을 호출하기만 하면 됩니다.



루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate Document object

doc = Rjb::import('com.aspose.pdf.Document').new

# Add a page to pages collection of PDF file

page = doc.getPages().add()

# Instantiate HtmlFragment with HTML contents

title = Rjb::import('com.aspose.pdf.HtmlFragment').new("<fontsize=10><b><i>Table</i></b></fontsize>")

# set MarginInfo for margin details

margin = Rjb::import('com.aspose.pdf.MarginInfo').new

margin.setBottom(10)

margin.setTop(200)

# Set margin information

title.setMargin(margin)

# Add HTML Fragment to paragraphs collection of page

page.getParagraphs().add(title)

# Save PDF file

doc.save(data_dir + "html.output.pdf")

puts "HTML added successfully"
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 HTML(Aspose.PDF) 추가**를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addhtml.rb)
