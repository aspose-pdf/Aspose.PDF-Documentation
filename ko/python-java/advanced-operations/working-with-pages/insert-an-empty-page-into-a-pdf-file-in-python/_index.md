---
title: Python에서 PDF 파일에 빈 페이지 삽입
type: docs
weight: 70
url: /ko/python-java/insert-an-empty-page-into-a-pdf-file-in-python/
---

<ins>**Aspose.PDF Java for Python**을 사용하여 Pdf 문서에 빈 페이지를 삽입하려면 **InsertEmptyPage** 클래스를 호출하세요.

**Python 코드**
```

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# PDF에 빈 페이지 삽입
pdf_document.getPages().insert(1)

# 연결된 출력 파일 저장 (대상 문서)
pdf_document.save(self.dataDir + "output.pdf")

print "빈 페이지가 성공적으로 추가되었습니다!"

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **빈 페이지 삽입 (Aspose.PDF)**을 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)