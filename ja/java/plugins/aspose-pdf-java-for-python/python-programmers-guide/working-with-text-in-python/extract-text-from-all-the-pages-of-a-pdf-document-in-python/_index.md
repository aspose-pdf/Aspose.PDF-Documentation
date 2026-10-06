---
title: "Python での PDF ドキュメントの全ページからのテキスト抽出"
linktitle: "Python での PDF ドキュメントの全ページからのテキスト抽出"
type: docs
weight: 30
url: /ja/java/extract-text-from-all-the-pages-of-a-pdf-document-in-python/
lastmod: "2026-10-06"
description: "PDF ファイル形式 API を使用して、Python で PDF ページからテキストを抽出する方法を説明します。"
---
## Python を使用した PDF からテキストの抽出

**Aspose.PDF Java for Python** を使用して PDF ドキュメントのすべてのページから TextrFrom を抽出するには、単に **ExtractTextFromAllPages** モジュールを呼び出すだけです。

```python

# Open the target document
pdf=self.Document()
pdf=self.dataDir + 'input1.pdf'

text_absorber=self.TextAbsorber()

pdf.getPages().accept(text_absorber)

extracted_text=text_absorber.getText()

writer=self.FileWriter(self.File(self.dataDir + 'extracted_text.out.txt'))
writer.write(extracted_text)
writer.close()

print "Text extracted successfully. Check output file."

```

**実行コードをダウンロード**

以下に示すソーシャルコーディングサイトのいずれかから、**すべてのページからテキストを抽出 (Aspose.PDF)** をダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithText/ExtractTextFromAllPages/ExtractTextFromAllPages.py)
