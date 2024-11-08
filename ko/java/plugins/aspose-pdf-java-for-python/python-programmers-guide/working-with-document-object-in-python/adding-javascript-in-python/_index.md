---
title: 파이썬에서 자바스크립트 추가하기
type: docs
weight: 10
url: /ko/java/adding-javascript-in-python/
lastmod: "2021-06-05"
---

Aspose.PDF Java를 사용하여 파이썬에서 자바스크립트를 추가하려면, Document 클래스의 AddJavascript() 메서드를 호출하면 됩니다.

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('page 2 is opened')")

# 페이지 레벨에서 자바스크립트 추가
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# PDF 문서 저장
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "자바스크립트가 성공적으로 추가되었습니다. 출력 파일을 확인하세요."

```

**실행 코드 다운로드**

아래 언급된 소셜 코딩 사이트 중 하나에서 **Add Javascript (Aspose.PDF)**를 다운로드하세요:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)