---
title: PythonでPDFファイルに空のページを挿入する
type: docs
weight: 70
url: ja/python-java/insert-an-empty-page-into-a-pdf-file-in-python/
---

<ins>**Aspose.PDF Java for Python**を使用してPDFドキュメントに空のページを挿入するには、**InsertEmptyPage**クラスを呼び出します。

**Python コード**
```

doc= self.Document()
pdf_document = self.Document()
pdf_document=self.dataDir + 'input1.pdf'

# PDFに空のページを挿入
pdf_document.getPages().insert(1)

# 結合された出力ファイルを保存（ターゲットドキュメント）
pdf_document.save(self.dataDir + "output.pdf")

print "空のページが正常に追加されました！"

```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから、**Insert an Empty Page (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)

- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/InsertEmptyPage/InsertEmptyPage.py)