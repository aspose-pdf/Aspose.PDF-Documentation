---
title: PythonでPDFドキュメントのすべてのページからテキストを抽出する
type: docs
weight: 30
url: /ja/python-java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
---

**Aspose.PDF Java for Python**を使用してPDFドキュメントのすべてのページからテキストを抽出するには、**ExtractTextFromAllPages**モジュールを呼び出します。

```python
# 目的のドキュメントを開く
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "テキストが正常に抽出されました。出力ファイルを確認してください。"

```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Extract Text From All the Pages (Aspose.PDF)**をダウンロードできます。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)