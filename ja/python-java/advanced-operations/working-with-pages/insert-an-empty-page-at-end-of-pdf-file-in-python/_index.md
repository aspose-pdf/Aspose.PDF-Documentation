---
title: PDFファイルの末尾に空白ページを挿入する方法（Python）
type: docs
weight: 60
url: ja/python-java/insert-an-empty-page-at-end-of-pdf-file-in-python/
---

<ins>PDFドキュメントの末尾に空白ページを挿入するには、**Aspose.PDF Java for Python**を使用し、**InsertEmptyPageAtEndOfFile**クラスを呼び出します。

**Pythonコード**
```

pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# PDFに空白ページを挿入する
pdf_document.getPages().add();

# 連結された出力ファイル（ターゲットドキュメント）を保存する
pdf_document.save(self.dataDir + "output.pdf")

print "空白ページが正常に追加されました！"

```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**PDFファイルの末尾に空白ページを挿入する（Aspose.PDF）**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPageAtEndOfFile/InsertEmptyPageAtEndOfFile.py)