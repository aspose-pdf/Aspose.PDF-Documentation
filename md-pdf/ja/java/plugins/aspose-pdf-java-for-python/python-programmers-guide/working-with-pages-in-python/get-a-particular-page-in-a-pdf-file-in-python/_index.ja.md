---
title: PythonでPDFファイルの特定のページを取得する
type: docs
weight: 30
url: /java/get-a-particular-page-in-a-pdf-file-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**を使用してPDFドキュメントの特定のページを取得するには、**GetPage**クラスを呼び出します。

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# ページコレクションの特定のインデックスのページを取得
pdf_page = pdf.getPages().get_Item(1)

# 新しいDocumentオブジェクトを作成
new_document = self.Document()

# 新しいDocumentオブジェクトのページコレクションにページを追加
new_document.getPages().add(pdf_page)

# 新しく生成されたPDFファイルを保存
new_document.save(self.dataDir + "output.pdf")

print "プロセスが正常に完了しました！
```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Get Page (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose.PDF-for-Java_for_Python/test/WorkingWithPages/GetPage/GetPage.py)