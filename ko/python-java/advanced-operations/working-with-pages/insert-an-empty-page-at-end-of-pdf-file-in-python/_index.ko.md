---
title: PDF 파일 끝에 빈 페이지 삽입하기 - Python
type: docs
weight: 60
url: /python-java/insert-an-empty-page-at-end-of-pdf-file-in-python/
---

<ins>**Aspose.PDF Java for Python**을 사용하여 PDF 문서의 끝에 빈 페이지를 삽입하려면, **InsertEmptyPageAtEndOfFile** 클래스를 호출하십시오.

**Python 코드**
```

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# PDF에 빈 페이지 삽입
pdf_document.getPages().add();

# 결합된 출력 파일 저장 (대상 문서)
pdf_document.save(self.dataDir + "output.pdf")

print "빈 페이지가 성공적으로 추가되었습니다!"

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Insert an Empty Page at End of PDF File (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)