---
title: PythonにJavaScriptを追加する
type: docs
weight: 10
url: ja/python-java/adding-javascript-in-python/
---

Aspose.PDF Javaを使用してPythonにJavaScriptを追加するには、DocumentクラスのAddJavascript()メソッドを呼び出します。

**Pythonコード**

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'Template.pdf'

javaScript = self.JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

doc.setOpenAction(javaScript)
js=self.JavascriptAction("app.alert('page 2 is opened')")

# ページレベルでJavaScriptを追加
doc.getPages.get_Item(2)
doc.getActions().setOnOpen(js())
doc.getPages().get_Item(2).getActions().setOnClose(self.JavascriptAction("app.alert('page 2 is closed')"))

# PDFドキュメントを保存
doc.save(self.dataDir + "JavaScript-Added.pdf")

print "JavaScriptを正常に追加しました。出力ファイルを確認してください。"

```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Add Javascript (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)