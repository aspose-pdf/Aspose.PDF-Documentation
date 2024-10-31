---
title: PythonでPDFファイルから特定のページを削除する
type: docs
weight: 20
url: /python-java/delete-a-particular-page-from-the-pdf-file-in-python/
---

**Aspose.PDF Java for Python** を使用してPDFドキュメントから特定のページを削除するには、**DeletePage** クラスを呼び出します。

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# 特定のページを削除する
pdf.getPages().delete(2)

# 新しく生成されたPDFファイルを保存する
doc.save(self.dataDir + "output.pdf")

print "ページが正常に削除されました！"

```

**実行コードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから **Delete Page (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)