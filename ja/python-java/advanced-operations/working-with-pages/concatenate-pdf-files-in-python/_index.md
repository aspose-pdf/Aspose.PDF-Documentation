---
title: PythonでPDFファイルを連結
type: docs
weight: 10
url: /ja/python-java/concatenate-pdf-files-in-python/
---

**Aspose.PDF Java for Python**を使用してPDFファイルを連結するには、単に**ConcatenatePdfFiles**クラスを呼び出します。

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# ソースドキュメントを開く
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# ソースドキュメントのページをターゲットドキュメントに追加する
pdf1.getPages().add(pdf1.getPages())

# 連結された出力ファイルを保存する（ターゲットドキュメント）
doc.save(self.dataDir + "Concatenate_output.pdf")

print "新しいドキュメントが保存されました。出力ファイルを確認してください"
```

**実行コードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから、**Concatenate PDF Files (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)