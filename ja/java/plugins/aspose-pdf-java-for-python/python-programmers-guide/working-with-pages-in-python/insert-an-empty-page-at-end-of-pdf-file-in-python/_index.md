---
title: PDFファイルの末尾に空のページを挿入する方法（Python）
type: docs
weight: 60
url: /ja/java/insert-an-empty-page-at-end-of-pdf-file-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**を使用してPDFドキュメントの末尾に空のページを挿入するには、**InsertEmptyPageAtEndOfFile**クラスを呼び出します。

```python

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# PDFに空のページを挿入する
pdf_document.getPages().add();

# 連結された出力ファイル（ターゲットドキュメント）を保存する
pdf_document.save(self.dataDir + "output.pdf")

print "空のページが正常に追加されました！"

```

**サンプルコードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから、**PDFファイルの末尾に空のページを挿入する（Aspose.PDF）**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)