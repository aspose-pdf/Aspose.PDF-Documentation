---
title: Python에 JavaScript 추가하기
linktitle: Python에 JavaScript 추가하기
type: docs
weight: 10
url: /java/adding-javascript-in-python/
description: Python 및 Aspose.PDF를 사용하여 PDF 문서에 JavaScript 코드를 삽입하여 대화형 기능을 향상시키는 방법을 알아보세요.
lastmod: "2026-06-09"
---

Python에서 Aspose.PDF Java를 사용하여 Add Javascript를 추가하려면 Document 클래스의 AddJavascript() 메서드를 호출하기만 하면 됩니다.


```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('page 2 is opened')")

# Adding JavaScript at Page Level
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# Save PDF Document
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "Added JavaScript Successfully, please check the output file."

```


**실행 코드 다운로드**



아래 언급된 소셜 코딩 사이트 중 하나에서 **Javascript 추가(Aspose.PDF)**를 다운로드하세요.


- 
[GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)
