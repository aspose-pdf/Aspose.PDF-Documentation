---
title: 기존 PDF 파일에 텍스트 추가하기 - 루비
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 텍스트 추가

**Aspose.PDF Java for Ruby**를 사용하여 Pdf 문서에 텍스트 문자열을 추가하려면, **AddText** 모듈을 호출하세요.

Ruby 코드

```java

# 문서 디렉토리의 경로.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# Document 객체 인스턴스화

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 특정 페이지 가져오기

pdf_page = doc.getPages().get_Item(1)

# 텍스트 조각 생성

text_fragment = Rjb::import('com.aspose.pdf.TextFragment').new("main text")

text_fragment.setPosition(Rjb::import('com.aspose.pdf.Position').new(100, 600))

font_repository = Rjb::import('com.aspose.pdf.FontRepository')

color = Rjb::import('com.aspose.pdf.Color')

# 텍스트 속성 설정

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))

text_fragment.getTextState().setFontSize(14)

#text_fragment.getTextState().setForegroundColor(color.BLUE)

#text_fragment.getTextState().setBackgroundColor(color.GRAY)

# TextBuilder 객체 생성

text_builder = Rjb::import('com.aspose.pdf.TextBuilder').new(pdf_page)

# PDF 페이지에 텍스트 조각 추가

text_builder.appendText(text_fragment)

# PDF 파일 저장

doc.save(data_dir + "Text_Added.pdf")

puts "텍스트가 성공적으로 추가되었습니다"
```


## Download Running Code

아래 언급된 소셜 코딩 사이트 중 하나에서 **Add Text (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Text/addtext.rb)