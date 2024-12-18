---
title: 기존 PDF에 목차 추가하기 - Ruby
type: docs
weight: 30
url: /ko/java/add-toc-to-existing-pdf-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 목차 추가

<ins>**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서에 목차를 추가하려면, **AddToc** 모듈을 호출하세요.

Ruby 코드

```java
# 문서 디렉토리의 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDF 문서를 엽니다.

doc = Rjb::import('com.aspose.pdf.Document').new(data_dir + "input1.pdf")

# PDF 파일의 첫 번째 페이지에 접근합니다.

toc_page = doc.getPages().insert(1)

# 목차 정보를 나타내는 객체를 생성합니다.

toc_info = Rjb::import('com.aspose.pdf.TocInfo').new

title = Rjb::import('com.aspose.pdf.TextFragment').new("목차")

title.getTextState().setFontSize(20)

#title.getTextState().setFontStyle(Rjb::import('com.aspose.pdf.FontStyles.Bold'))

# 목차의 제목을 설정합니다.

toc_info.setTitle(title)

toc_page.setTocInfo(toc_info)

# 목차 요소로 사용할 문자열 객체를 생성합니다.

titles = Array["첫 번째 페이지", "두 번째 페이지"]

i = 0

while i < 2

    # Heading 객체를 생성합니다.

    heading2 = Rjb::import('com.aspose.pdf.Heading').new(1)

    segment2 = Rjb::import('com.aspose.pdf.TextSegment').new

    heading2.setTocPage(toc_page)

    heading2.getSegments().add(segment2)

    # Heading 객체의 대상 페이지를 지정합니다.

    heading2.setDestinationPage(doc.getPages().get_Item(i + 2))

    # 대상 페이지

    heading2.setTop(doc.getPages().get_Item(i + 2).getRect().getHeight())

    # 대상 좌표

    segment2.setText(titles[i])

    # 목차를 포함하는 페이지에 Heading을 추가합니다.

    toc_page.getParagraphs().add(heading2)

    i +=1

end

# PDF 문서를 저장합니다.

doc.save(data_dir + "TOC.pdf")

puts "목차를 성공적으로 추가했습니다. 출력 파일을 확인하세요."
```


## <ins> **실행 코드 다운로드

**Add TOC (Aspose.PDF)**를 아래 언급된 소셜 코딩 사이트 중 하나에서 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Document/addtoc.rb)