---
title: Python에서 DOM을 사용하여 HTML 문자열 추가
type: docs
weight: 10
url: /python-java/add-html-string-using-dom-in-python/
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서에 HTML 문자열을 추가하려면, **AddHtml** 모듈을 호출하십시오.

```python

# Document 객체 인스턴스화
doc=self.Document()
page=doc.getPages().add()

title=self.HtmlFragment("<fontsize=10><b><i>Table</i></b></fontsize>")

margin=self.MarginInfo()
#margin.setBottom(10)
#margin.setTop(200)

# 여백 정보 설정
title.setMargin(margin)

# 페이지의 단락 컬렉션에 HTML 조각 추가
page.getParagraphs().add(title)

# PDF 파일 저장
doc.save(self.dataDir + 'html.output.pdf')

print "HTML이 성공적으로 추가되었습니다."
```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Add HTML (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddHtml/AddHtml.py)