---
title: 파이썬에서 페이지 크기 업데이트
type: docs
weight: 90
url: ko/java/update-page-dimensions-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**을 사용하여 페이지 크기를 업데이트하려면, **UpdatePageDimensions** 클래스를 호출하십시오.

```python
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 페이지 컬렉션 가져오기
page_collection = pdf.getPages()

# 특정 페이지 가져오기
pdf_page = page_collection.get_Item(1)

# 페이지 크기를 A4 (11.7 x 8.3 인치)로 설정하고 Aspose.PDF에서는 1 인치 = 72 포인트이므로
# A4 크기는 포인트로 (842.4, 597.6)이 됩니다.
pdf_page.setPageSize(597.6,842.4)

# 새로 생성된 PDF 파일 저장
pdf.save(self.dataDir + "output.pdf")

print "크기가 성공적으로 업데이트되었습니다!"

```

**실행 코드 다운로드**

다음에 언급된 소셜 코딩 사이트 중 하나에서 **Update Page Dimensions (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)