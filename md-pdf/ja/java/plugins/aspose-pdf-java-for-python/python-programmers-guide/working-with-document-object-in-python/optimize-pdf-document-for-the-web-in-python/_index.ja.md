---
title: PythonでWeb用にPDFドキュメントを最適化する
type: docs
weight: 60
url: /java/optimize-pdf-document-for-the-web-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**を使用してWeb用にPDFドキュメントを最適化するには、**Optimize**クラスの**optimize_web**メソッドを呼び出します。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Web用に最適化
doc.optimize();

# 出力ドキュメントを保存
doc.save(self.dataDir + "Optimized_Web.pdf")

print "Web用に最適化されたPDFを出力しました。出力ファイルを確認してください。"
```

**実行可能なコードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Optimize PDF for Web (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)