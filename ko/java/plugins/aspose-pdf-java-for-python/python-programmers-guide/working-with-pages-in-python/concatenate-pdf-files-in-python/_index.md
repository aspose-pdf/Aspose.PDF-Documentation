---
title: 파이썬에서 PDF 파일 연결하기
type: docs
weight: 10
url: /ko/java/concatenate-pdf-files-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 파일을 연결하려면, **ConcatenatePdfFiles** 클래스를 호출하세요.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 소스 문서 열기
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# 소스 문서의 페이지를 대상 문서에 추가
pdf1.getPages().add(pdf1.getPages())

# 연결된 출력 파일(대상 문서) 저장
doc.save(self.dataDir + "Concatenate_output.pdf")

print "새 문서가 저장되었습니다. 출력 파일을 확인하세요."
```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Concatenate PDF Files (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)