---
title: Python에서 PDF 파일 정보 설정
type: docs
weight: 90
url: /java/set-pdf-file-information-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서 정보를 업데이트하려면, **SetPdfFileInfo** 클래스를 호출하십시오.

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 문서 정보 가져오기
doc_info = doc.getInfo();

doc_info.setAuthor("Aspose.PDF for java");
doc_info.setCreationDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setKeywords("Aspose.PDF, DOM, API");
doc_info.setModDate(datetime.today.strftime("%m/%d/%Y"));
doc_info.setSubject("PDF 정보");
doc_info.setTitle("PDF 문서 정보 설정");

# 새 정보로 문서 저장

doc.save(self.dataDir + "Updated_Information.pdf")
print "문서 정보 업데이트 완료, 출력 파일을 확인하십시오."
```

**실행 코드 다운로드**

아래에 언급된 소셜 코딩 사이트 중 하나에서 **Set PDF File Information (Aspose.PDF)**를 다운로드하십시오:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetPdfFileInfo/SetPdfFileInfo.py)