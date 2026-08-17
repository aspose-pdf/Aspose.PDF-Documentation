---
title: Python을 사용하여 기존 PDF에 텍스트 추가
linktitle: Python을 사용하여 기존 PDF에 텍스트 추가
type: docs
weight: 20
url: /java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2026-06-09"
description: PDF 라이브러리와 함께 Python을 사용하여 PDF 문서에 텍스트를 추가하거나 쓰는 방법의 코드 예제입니다.
---
## 
Python을 사용하여 PDF에 텍스트 쓰기 또는 추가



**Aspose.PDF Java for Python**을 사용하여 PDF 문서에 텍스트 문자열을 추가하려면 **AddText** 모듈을 호출하기만 하면 됩니다.


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

# Save PDF file
doc.save(self.dataDir + "Text_Added.pdf")
print "Text added successfully"
```


**실행 코드 다운로드**



아래에 언급된 소셜 코딩 사이트에서 В **텍스트 추가(Aspose.PDF)**В를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)
