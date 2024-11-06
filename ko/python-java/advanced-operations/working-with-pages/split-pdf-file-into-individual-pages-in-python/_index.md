---
title: Python에서 PDF 파일을 개별 페이지로 분할하기
type: docs
weight: 80
url: ko/python-java/split-pdf-file-into-individual-pages-in-python/
---

<ins>**Aspose.PDF Java for PHP**를 사용하여 PDF 문서를 개별 페이지로 분할하려면 **SplitAllPages** 클래스를 호출하세요.

**Python Code**
```

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 모든 페이지를 반복합니다
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# 새로운 Document 객체를 생성합니다
new_document = self.Document();

# Page Collection의 특정 인덱스에서 페이지를 가져옵니다
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# 새로 생성된 PDF 파일을 저장합니다
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "분할 프로세스가 성공적으로 완료되었습니다!";
```


**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Split Pages (Aspose.PDF)**를 다운로드하세요:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/SplitAllPages/SplitAllPages.py)