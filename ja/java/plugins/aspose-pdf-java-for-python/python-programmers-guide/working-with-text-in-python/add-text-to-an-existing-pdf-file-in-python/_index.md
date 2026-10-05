---
title: "Python を使用した既存の PDF にテキストの追加"
linktitle: "Python を使用した既存の PDF にテキストの追加"
type: docs
weight: 20
url: /ja/java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2026-10-05"
description: Python と PDF ライブラリを使用して PDF 文書にテキストを追加または書き込むコード例。
---
## Python を使用して PDF にテキストを書き込むまたは追加する

**Aspose.PDF Java for Python** を使用して PDF 文書にテキスト文字列を追加するには、単に **AddText** モジュールを呼び出します。

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

以下に記載されたソーシャルコーディングサイトから **Add Text (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)
