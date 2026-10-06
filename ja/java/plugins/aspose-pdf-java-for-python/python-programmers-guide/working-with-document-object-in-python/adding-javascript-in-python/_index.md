---
title: "Python での JavaScript の追加"
linktitle: "Python での JavaScript の追加"
type: docs
weight: 10
url: /ja/java/adding-javascript-in-python/
description: "Python と Aspose.PDF を使用して、PDF ドキュメント内に JavaScript コードを埋め込み、インタラクティブ性を向上させる方法を確認してください。"
lastmod: "2026-10-06"
---
Python で Aspose.PDF Java を使用して JavaScript を追加するには、`Document` クラスの `AddJavascript()` メソッドを呼び出してください。

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

**実行中のコードをダウンロード**

以下に記載されたソーシャルコーディングサイトのいずれかから **Add Javascript (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/AddJavascript/AddJavascript.py)
