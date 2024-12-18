---
title: 기존 PDF 파일에 텍스트 추가하기 (Python)
type: docs
weight: 20
url: /ko/python-java/add-text-to-an-existing-pdf-file-in-python/
---

**Aspose.PDF Java for Python**을 사용하여 Pdf 문서에 텍스트 문자열을 추가하려면, **AddText** 모듈을 호출하세요.

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

**실행 코드 다운로드**

아래에 언급된 소셜 코딩 사이트 중 하나에서 **Add Text (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)