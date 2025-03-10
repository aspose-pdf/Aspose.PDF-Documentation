---
title: Python에서 PDF 문서의 모든 페이지에서 텍스트 추출
type: docs
weight: 30
url: /ko/python-java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서의 모든 페이지에서 텍스트를 추출하려면, **ExtractTextFromAllPages** 모듈을 호출합니다.

```python
# 대상 문서 열기
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "텍스트가 성공적으로 추출되었습니다. 출력 파일을 확인하세요."

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Extract Text From All the Pages (Aspose.PDF)** 를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)