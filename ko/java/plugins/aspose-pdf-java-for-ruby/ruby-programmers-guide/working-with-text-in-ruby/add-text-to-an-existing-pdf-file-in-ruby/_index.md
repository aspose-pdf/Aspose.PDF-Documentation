---
title: Ruby의 기존 PDF 파일에 텍스트 추가
linktitle: Ruby의 기존 PDF 파일에 텍스트 추가
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-ruby/
description: Aspose.PDF를 사용하여 Ruby의 기존 PDF 문서에 텍스트를 추가하여 PDF 콘텐츠를 향상하거나 업데이트하는 방법을 알아보세요.
lastmod: "2026-06-09"
---
## 
Aspose.PDF - 텍스트 추가



**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서에 텍스트 문자열을 추가하려면 **AddText** 모듈을 호출하기만 하면 됩니다.



루비 코드


```java
# The path to the documents directory.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Instantiate Document object

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# get particular page

pdf_page = doc.getPages().get_Item(1)

# create text fragment

text_fragment = Rjb::import('com.aspose.pdf.TextFragment').new("main text")

text_fragment.setPosition(Rjb::import('com.aspose.pdf.Position').new(100, 600))

font_repository = Rjb::import('com.aspose.pdf.FontRepository')

color = Rjb::import('com.aspose.pdf.Color')

# set text properties

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))

text_fragment.getTextState().setFontSize(14)

#text_fragment.getTextState().setForegroundColor(color.BLUE)

#text_fragment.getTextState().setBackgroundColor(color.GRAY)

# create TextBuilder object

text_builder = Rjb::import('com.aspose.pdf.TextBuilder').new(pdf_page)

# append the text fragment to the PDF page

text_builder.appendText(text_fragment)

# Save PDF file

doc.save(data_dir + "Text_Added.pdf")

puts "Text added successfully"
```

## 
실행 코드 다운로드



아래에 언급된 소셜 코딩 사이트에서 В **텍스트 추가(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addtext.rb)
