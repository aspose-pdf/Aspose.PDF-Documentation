---
title: PythonでPDFドキュメントのすべてのページからテキストを抽出
type: docs
weight: 30
url: /java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2021-06-05"
keywords: extract pdf text python
description: PDFファイルフォーマットAPIを使用して、PythonでPDFページからテキストを抽出する方法を説明します。
---

## Pythonを使用してPDFからテキストを抽出

**Aspose.PDF Java for Python**を使用して、PDFドキュメントのすべてのページからテキストを抽出するには、単に**ExtractTextFromAllPages**モジュールを呼び出します。

```python

# 対象のドキュメントを開く
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

**実行コードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから、**Extract Text From All the Pages (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)