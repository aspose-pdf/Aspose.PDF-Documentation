---
title: Python에서 PDF 만료 설정
type: docs
weight: 80
url: /java/set-pdf-expiration-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**을 사용하여 PDF 문서의 만료를 설정하려면 **SetExpiration** 클래스를 호출하십시오.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2021; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# 새 정보를 포함하여 업데이트된 문서 저장
doc.save(self.dataDir + "set_expiration.pdf");

print "문서 정보가 업데이트되었습니다. 출력 파일을 확인하십시오."
```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **PDF 만료 설정 (Aspose.PDF)**을 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)