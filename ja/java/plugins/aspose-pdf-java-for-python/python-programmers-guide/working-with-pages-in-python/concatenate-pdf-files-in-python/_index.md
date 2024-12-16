---
title: PythonでPDFファイルを連結する
type: docs
weight: 10
url: /ja/java/concatenate-pdf-files-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python** を使用してPDFファイルを連結するには、**ConcatenatePdfFiles** クラスを呼び出すだけです。

```python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# ソースドキュメントを開く
pdf1 = self.Document()
pdf1=self.dataDir + 'input2.pdf'

# ソースドキュメントのページをターゲットドキュメントに追加する
pdf1.getPages().add(pdf1.getPages())

# 連結した出力ファイル（ターゲットドキュメント）を保存する
doc.save(self.dataDir + "Concatenate_output.pdf")

print "新しいドキュメントが保存されました。出力ファイルを確認してください"
```

**コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから **Concatenate PDF Files (Aspose.PDF)** をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/ConcatenatePdfFiles/ConcatenatePdfFiles.py)