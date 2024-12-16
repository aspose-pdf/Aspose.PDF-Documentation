---
title: Ruby에서 페이지 속성 가져오기
type: docs
weight: 50
url: /ko/java/get-page-properties-in-ruby/
lastmod: "2021-06-05"
---

## Aspose.PDF - 페이지 속성 가져오기

**Aspose.PDF Java for Ruby**를 사용하여 PDF 문서의 페이지 속성을 가져오려면, **GetPageProperties** 모듈을 호출하십시오.

Ruby 코드

```java
# 문서 디렉터리의 경로입니다.

data_dir = File.dirname(File.dirname(File.dirname(File.dirname(__FILE__)))) + '/data/'

# PDF 문서 생성

pdf_document = Rjb::import('com.aspose.pdf.Document').new(data_dir + 'input1.pdf')

# 페이지 컬렉션 가져오기

page_collection = pdf_document.getPages()

# 특정 페이지 가져오기

pdf_page = page_collection.get_Item(1)

# 페이지 속성 가져오기

puts "ArtBox : Height = " + pdf_page.getArtBox().getHeight().to_s + ", Width = " + pdf_page.getArtBox().getWidth().to_s + ", LLX = " + pdf_page.getArtBox().getLLX().to_s + ", LLY = " + pdf_page.getArtBox().getLLY().to_s + ", URX = " + pdf_page.getArtBox().getURX().to_s + ", URY = " + pdf_page.getArtBox().getURY().to_s

puts "BleedBox : Height = " + pdf_page.getBleedBox().getHeight().to_s + ", Width = " + pdf_page.getBleedBox().getWidth().to_s + ", LLX = " + pdf_page.getBleedBox().getLLX().to_s + ", LLY = " + pdf_page.getBleedBox().getLLY().to_s + ", URX = " + pdf_page.getBleedBox().getURX().to_s + ", URY = " + pdf_page.getBleedBox().getURY().to_s

puts "CropBox : Height = " + pdf_page.getCropBox().getHeight().to_s + ", Width = " + pdf_page.getCropBox().getWidth().to_s + ", LLX = " + pdf_page.getCropBox().getLLX().to_s + ", LLY = " + pdf_page.getCropBox().getLLY().to_s + ", URX = " + pdf_page.getCropBox().getURX().to_s + ", URY = " + pdf_page.getCropBox().getURY().to_s

puts "MediaBox : Height = " + pdf_page.getMediaBox().getHeight().to_s + ", Width = " + pdf_page.getMediaBox().getWidth().to_s + ", LLX = " + pdf_page.getMediaBox().getLLX().to_s + ", LLY = " + pdf_page.getMediaBox().getLLY().to_s + ", URX = " + pdf_page.getMediaBox().getURX().to_s + ", URY = " + pdf_page.getMediaBox().getURY().to_s

puts "TrimBox : Height = " + pdf_page.getTrimBox().getHeight().to_s + ", Width = " + pdf_page.getTrimBox().getWidth().to_s + ", LLX = " + pdf_page.getTrimBox().getLLX().to_s + ", LLY = " + pdf_page.getTrimBox().getLLY().to_s + ", URX = " + pdf_page.getTrimBox().getURX().to_s + ", URY = " + pdf_page.getTrimBox().getURY().to_s

puts "Rect : Height = " + pdf_page.getRect().getHeight().to_s + ", Width = " + pdf_page.getRect().getWidth().to_s + ", LLX = " + pdf_page.getRect().getLLX().to_s + ", LLY = " + pdf_page.getRect().getLLY().to_s + ", URX = " + pdf_page.getRect().getURX().to_s + ", URY = " + pdf_page.getRect().getURY().to_s

puts "Page Number :- " + pdf_page.getNumber().to_s

puts "Rotate :-" + pdf_page.getRotate().to_s
```


## 실행 코드 다운로드

**Get Page Properties (Aspose.PDF)**를 아래 언급된 소셜 코딩 사이트 중 하나에서 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Ruby/lib/asposepdfjava/Pages/getpageproperties.rb)