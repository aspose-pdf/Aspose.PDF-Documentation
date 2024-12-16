---
title: Python에서 페이지 속성 가져오기
type: docs
weight: 50
url: /ko/java/get-page-properties-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**을 사용하여 Pdf 문서의 페이지 속성을 가져오려면, **GetPageProperties** 클래스를 호출하세요.

```Python
doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# 페이지 컬렉션 가져오기
page_collection = pdf_document.getPages();

# 특정 페이지 가져오기
pdf_page = page_collection.get_Item(1);

# 페이지 속성 가져오기
print "ArtBox : Height = " + pdf_page.getArtBox().getHeight() + ", Width = " + pdf_page.getArtBox().getWidth() + ", LLX = " + pdf_page.getArtBox().getLLX() + ", LLY = " + pdf_page.getArtBox().getLLY() + ", URX = " + pdf_page.getArtBox().getURX() + ", URY = " + pdf_page.getArtBox().getURY()
print "BleedBox : Height = " + pdf_page.getBleedBox().getHeight() + ", Width = " + pdf_page.getBleedBox().getWidth() + ", LLX = " + pdf_page.getBleedBox().getLLX() + ", LLY = " + pdf_page.getBleedBox().getLLY() + ", URX = " + pdf_page.getBleedBox().getURX() + ", URY = " + pdf_page.getBleedBox().getURY()
print "CropBox : Height = " + pdf_page.getCropBox().getHeight() + ", Width = " + pdf_page.getCropBox().getWidth() + ", LLX = " + pdf_page.getCropBox().getLLX() + ", LLY = " + pdf_page.getCropBox().getLLY() + ", URX = " + pdf_page.getCropBox().getURX() + ", URY = " + pdf_page.getCropBox().getURY()
print "MediaBox : Height = " + pdf_page.getMediaBox().getHeight() + ", Width = " + pdf_page.getMediaBox().getWidth() + ", LLX = " + pdf_page.getMediaBox().getLLX() + ", LLY = " + pdf_page.getMediaBox().getLLY() + ", URX = " + pdf_page.getMediaBox().getURX() + ", URY = " + pdf_page.getMediaBox().getURY()
print "TrimBox : Height = " + pdf_page.getTrimBox().getHeight() + ", Width = " + pdf_page.getTrimBox().getWidth() + ", LLX = " + pdf_page.getTrimBox().getLLX() + ", LLY = " + pdf_page.getTrimBox().getLLY() + ", URX = " + pdf_page.getTrimBox().getURX() + ", URY = " + pdf_page.getTrimBox().getURY()
print "Rect : Height = " + pdf_page.getRect().getHeight() + ", Width = " + pdf_page.getRect().getWidth() + ", LLX = " + pdf_page.getRect().getLLX() + ", LLY = " + pdf_page.getRect().getLLY() + ", URX = " + pdf_page.getRect().getURX() + ", URY = " + pdf_page.getRect().getURY()
print "Page Number :- " + pdf_page.getNumber()
print "Rotate :-" + pdf_page.getRotate()

```


**코드 실행 다운로드**

다음 소셜 코딩 사이트 중 하나에서 **페이지 속성 가져오기 (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/GetPageProperties/GetPageProperties.py)