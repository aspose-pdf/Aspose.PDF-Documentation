---
title: "Python を使用した既存の PDF へのテキストの追加"
linktitle: "Python を使用した既存の PDF へのテキストの追加"
type: docs
weight: 20
url: /ja/java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2026-10-06"
description: "Python と PDF ライブラリを使用して、PDF 文書にテキストを追加または書き込むコード例を示します。"
---
## Python を使用した PDF へのテキストの書き込みおよび追加

**Aspose.PDF Java for Python** を使用して PDF ドキュメントにテキスト文字列を追加するには、**AddText** モジュールを呼び出してください。

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("main text")
position=self.Position()
text_fragment.setPosition(position(100,600))

font_repository=self.FontRepository()
color=self.Color()

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))
text_fragment.getTextState().setFontSize(14)

text_builder=self.TextBuilder(pdf_page)
text_builder.appendText(text_fragment)

# Save PDF file
doc.save(self.dataDir + "Text_Added.pdf")
print "Text added successfully"
```

**実行コードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから **Add Text (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)
