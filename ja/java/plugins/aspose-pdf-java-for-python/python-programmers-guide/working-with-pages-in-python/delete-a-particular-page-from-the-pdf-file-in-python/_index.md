---
title: PythonでPDFファイルから特定のページを削除する
type: docs
weight: 20
url: ja/java/delete-a-particular-page-from-the-pdf-file-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**を使用してPDFドキュメントから特定のページを削除するには、**DeletePage**クラスを呼び出します。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 特定のページを削除
pdf.getPages().delete(2)

# 新しく生成されたPDFファイルを保存
doc.save(self.dataDir + "output.pdf")

print "ページが正常に削除されました！"

```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Delete Page (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)