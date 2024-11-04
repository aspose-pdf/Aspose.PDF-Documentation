---
title: PythonでPDFファイルに空のページを挿入する
type: docs
weight: 70
url: /java/insert-an-empty-page-into-a-pdf-file-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**を使用してPDFドキュメントに空のページを挿入するには、**InsertEmptyPage**クラスを呼び出します。

```Python

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# PDFに空のページを挿入する
pdf_document.getPages().insert(1)

# 連結された出力ファイル（ターゲットドキュメント）を保存する
pdf_document.save(self.dataDir + "output.pdf")

print "空のページが正常に追加されました！"

```

**実行コードのダウンロード**

以下のソーシャルコーディングサイトから**Insert an Empty Page (Aspose.PDF)**をダウンロードできます:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)