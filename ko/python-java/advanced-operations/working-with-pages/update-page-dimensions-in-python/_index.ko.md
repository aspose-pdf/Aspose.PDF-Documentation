---
title: Python에서 페이지 크기 업데이트
type: docs
weight: 90
url: /python-java/update-page-dimensions-in-python/
---

<ins>**Aspose.PDF Java for Python**을 사용하여 페이지 크기를 업데이트하려면, **UpdatePageDimensions** 클래스를 호출하세요.

**Python 코드**
```s
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 페이지 컬렉션 가져오기
page_collection = pdf.getPages()

# 특정 페이지 가져오기
pdf_page = page_collection.get_Item(1)

# 페이지 크기를 A4로 설정 (11.7 x 8.3 인치) 및 Aspose.PDF에서는 1인치 = 72 포인트
# 따라서 A4 크기는 포인트로 (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# 새로 생성된 PDF 파일 저장
pdf.save(self.dataDir + "output.pdf")

print "크기가 성공적으로 업데이트되었습니다!"

```

**실행 코드 다운로드**

아래의 소셜 코딩 사이트 중 하나에서 **Update Page Dimensions (Aspose.PDF)** 를 다운로드하세요:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)