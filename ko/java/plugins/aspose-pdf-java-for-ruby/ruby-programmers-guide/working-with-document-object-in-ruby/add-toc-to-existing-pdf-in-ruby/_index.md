---
title: Ruby의 기존 PDF에 TOC 추가
linktitle: Ruby의 기존 PDF에 TOC 추가
type: docs
weight: 30
url: /java/add-toc-to-existing-pdf-in-ruby/
description: 향상된 문서 탐색을 위해 Aspose.PDF를 사용하여 Ruby에서 기존 PDF에 목차를 추가하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 목차 추가



<ins> **Aspose.PDF Java for Ruby**를 사용하여 PDF 문서에 목차를 추가하려면 **AddToc** 모듈을 호출하기만 하면 됩니다.



루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Open a pdf document.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# Get access to first page of PDF file

toc_page = doc.getPages().insert(1)

# Create object to represent TOC information

toc_info = Rjb::import('com.aspose.pdf.TocInfo').new

title = Rjb::import('com.aspose.pdf.TextFragment').new("Table Of Contents")

title.getTextState().setFontSize(20)

#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# Set the title for TOC

toc_info.setTitle(title)

toc_page.setTocInfo(toc_info)

# Create string objects which will be used as TOC elements

titles = Array["First page", "Second page"]

i = 0

while i < 2

В В В  # Create Heading object

В В В  heading2 = Rjb::import('com.aspose.pdf.Heading').new(1)

В В В  segment2 = Rjb::import('com.aspose.pdf.TextSegment').new

В В В  heading2.setTocPage(toc_page)

В В В  heading2.getSegments().add(segment2)

В В В  # Specify the destination page for heading object

В В В  heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

В В В  # Destination page

В В В  heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

В В В  # Destination coordinate

В В В  segment2.setText(titles[i])

В В В  # Add heading to page containing TOC

В В В  toc_page.getParagraphs().add(heading2)

В В В  i +=1

end

# Save PDF Document

doc.save(data_dir + "TOC.pdf")

puts "Added TOC Successfully, please check the output file."
```

## 
<ins> **실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트 중 하나에서 В **TOC 추가(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addtoc.rb)
