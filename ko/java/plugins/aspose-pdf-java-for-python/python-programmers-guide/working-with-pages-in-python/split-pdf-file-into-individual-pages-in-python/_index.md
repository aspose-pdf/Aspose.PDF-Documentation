---
title: Python에서 PDF 파일을 개별 페이지로 분할
type: docs
weight: 80
url: /ko/java/split-pdf-file-into-individual-pages-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for PHP**를 사용하여 PDF 문서를 개별 페이지로 분할하려면, **SplitAllPages** 클래스를 호출하십시오.

```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 모든 페이지를 순회
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# 새로운 Document 객체 생성
new_document = self.Document();

# 페이지 컬렉션의 특정 인덱스에서 페이지 가져오기
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# 새로 생성된 PDF 파일 저장
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "분할 프로세스가 성공적으로 완료되었습니다!";
```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Split Pages (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)