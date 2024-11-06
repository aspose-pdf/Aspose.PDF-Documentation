---
title: 既存のPDFにテキストを追加するPython
type: docs
weight: 20
url: ja/java/add-text-to-an-existing-pdf-file-in-python/
lastmod: "2021-06-05"
keywords: add text pdf python, write text pdf python
description: PythonとPDFライブラリを使用して、Pdfドキュメントにテキストを追加または書き込む方法のコード例。
---

## Pythonを使用してPDFにテキストを書き込むまたは追加する

**Aspose.PDF Java for Python**を使用してPdfドキュメントにテキスト文字列を追加するには、**AddText**モジュールを呼び出します。

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

# PDFファイルを保存
doc.save(self.dataDir + "Text_Added.pdf")
print "テキストが正常に追加されました"
```


**コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから **Add Text (Aspose.PDF)** をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/AddText/AddText.py)