---
title: PythonでWeb用にPDFドキュメントを最適化する
type: docs
weight: 60
url: ja/python-java/optimize-pdf-document-for-the-web-in-python/
---

<ins>**Aspose.PDF Java for Python**を使用してWeb用にPDFドキュメントを最適化するには、**Optimize**クラスの**optimize_web**メソッドを呼び出します。

**Pythonコード**
```

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# Web用に最適化
doc.optimize();

# 出力ドキュメントを保存
doc.save(self.dataDir + "Optimized_Web.pdf")

print "Web用に最適化されたPDF、出力ファイルを確認してください。"
```


**実行コードのダウンロード**

次の任意のソーシャルコーディングサイトから**Web用にPDFを最適化 (Aspose.PDF)**をダウンロードできます:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentObject/Optimize/Optimize.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithDocumentObject/Optimize/Optimize.py)