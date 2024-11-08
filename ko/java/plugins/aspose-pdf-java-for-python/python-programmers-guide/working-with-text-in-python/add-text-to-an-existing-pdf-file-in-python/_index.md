---
title: 파이썬을 사용하여 기존 PDF에 텍스트 추가
type: docs
weight: 20
url: /ko/java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2021-06-05"
keywords: 파이썬 pdf 텍스트 추가, 파이썬 pdf 텍스트 쓰기
description: PDF 라이브러리를 사용하여 Pdf 문서에 텍스트를 추가하거나 쓰는 방법에 대한 코드 예제입니다.
---

## 파이썬을 사용하여 PDF에 텍스트 쓰기 또는 추가

**Aspose.PDF Java for Python**을 사용하여 Pdf 문서에 텍스트 문자열을 추가하려면, **AddText** 모듈을 호출합니다.

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("main text")
position=self.Position()
text_fragment.setPosition(position(100,600))

font_repository=self.FontRepository()
color=self.Color()

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))
text_fragment.getTextState().setFontSize(14)

text_builder=self.TextBuilder(pdf_page)
text_builder.appendText(text_fragment)

# PDF 파일 저장
doc.save(self.dataDir + "Text_Added.pdf")
print "텍스트가 성공적으로 추가되었습니다"
```


**코드 실행 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **텍스트 추가 (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)