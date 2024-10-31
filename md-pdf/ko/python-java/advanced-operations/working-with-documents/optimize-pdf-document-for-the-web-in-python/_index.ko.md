---
title: 웹을 위한 PDF 문서 최적화 in Python
type: docs
weight: 60
url: /python-java/optimize-pdf-document-for-the-web-in-python/
---

<ins>**Aspose.PDF Java for Python**을 사용하여 웹을 위한 PDF 문서를 최적화하려면, **Optimize** 클래스의 **optimize_web** 메서드를 호출하세요.

**Python 코드**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 웹을 위해 최적화
doc.optimize();

# 출력 문서 저장
doc.save(self.dataDir + "Optimized_Web.pdf")

print "웹을 위한 PDF가 최적화되었습니다. 출력 파일을 확인하세요."
```


**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **웹을 위한 PDF 최적화 (Aspose.PDF)**를 다운로드하십시오:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/Optimize/Optimize.py)