---
title: 既存のPDFファイルにテキストを追加する方法（Python）
type: docs
weight: 20
url: /python-java/add-text-to-an-existing-pdf-file-in-python/
---

**Aspose.PDF Java for Python**を使用してPDFドキュメントにテキスト文字列を追加するには、**AddText**モジュールを呼び出します。

```python
doc=self.Document()
doc=self.dataDir + 'input1.pdf'

pdf_page=self.Document()
pdf_page.getPages().get_Item(1)

text_fragment=self.TextFragment("メインテキスト")
position=self.Position()
text_fragment.setPosition(position(100,600))

font_repository=self.FontRepository()
color=self.Color()

text_fragment.getTextState().setFont(font_repository.findFont("Verdana"))
text_fragment.getTextState().setFontSize(14)

text_builder=self.TextBuilder(pdf_page)
text_builder.appendText(text_fragment)

# PDFファイルを保存

doc.save(self.dataDir + "Text_Added.pdf")

print "テキストが正常に追加されました"

```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Add Text (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)