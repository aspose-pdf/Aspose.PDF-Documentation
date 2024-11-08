---
title: 기존 PDF에 목차 추가하기
type: docs
weight: 20
url: /ko/java/add-toc-to-existing-pdf-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**을 사용하여 Pdf 문서에 목차를 추가하려면, **AddToc** 클래스를 호출하십시오.

```python

# PDF 문서를 엽니다.
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# PDF 파일의 첫 페이지에 접근합니다.
toc_page = doc.getPages().insert(1)

# 목차 정보를 나타내는 객체를 생성합니다.
toc_info = self.TocInfo()
title = self.TextFragment("목차")
title.getTextState().setFontSize(20)

# 목차의 제목을 설정합니다.
toc_info.setTitle(title)
toc_page.setTocInfo(toc_info)

# 목차 요소로 사용할 문자열 객체를 생성합니다.
titles = ["첫 번째 페이지", "두 번째 페이지"]

i = 0;
while (i < 2):

# Heading 객체를 생성합니다.
heading2 = self.Heading(1);

segment2 = self.TextSegment
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

i +=1;

# PDF 문서를 저장합니다.
doc.save(self.dataDir + "TOC.pdf")

print "목차가 성공적으로 추가되었습니다. 출력 파일을 확인하십시오."
```


**코드 실행 다운로드**

**Add TOC (Aspose.PDF)**를 아래 언급된 소셜 코딩 사이트 중 하나에서 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddToc/AddToc.py)