---
title: Python에서 PDF 만료 설정
type: docs
weight: 80
url: /python-java/set-pdf-expiration-in-python/
---

<ins>**Aspose.PDF Java for Python**을 사용하여 Pdf 문서의 만료를 설정하려면, **SetExpiration** 클래스를 호출하십시오.

**Python 코드**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

javascript = self.JavascriptAction(

"var year=2014; var month=4;today = new Date();today = new Date(today.getFullYear(), today.getMonth());expiry = new Date(year, month);if (today.getTime() > expiry.getTime())app.alert('The file is expired. You need a new one.');");

doc.setOpenAction(javascript);

# 새로운 정보로 업데이트된 문서 저장
doc.save(self.dataDir + "set_expiration.pdf");

print "문서 정보가 업데이트되었습니다. 출력 파일을 확인하십시오."
```

**실행 코드 다운로드**

아래에 언급된 소셜 코딩 사이트 중 하나에서 **Set PDF Expiration (Aspose.PDF)**를 다운로드하십시오:


- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/SetExpiration/SetExpiration.py)