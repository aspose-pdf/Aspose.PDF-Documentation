---
title: PythonでPDFのページ数を取得
type: docs
weight: 40
url: /python-java/get-page-count-of-pdf-in-python/
---

<ins>**Aspose.PDF Java for Python**を使用してPDFドキュメントのページ数を取得するには、**GetNumberOfPages**クラスを呼び出します。

**Pythonコード**
```
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'
page_count = pdf.getPages().size()
print "Page Count:" . page_count

```

**実行コードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Get Page Count (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/GetNumberOfPages/GetNumberOfPages.py)
- [CodePlex](http://asposepdfjavapython.codeplex.com/SourceControl/latest#test/WorkingWithPages/GetNumberOfPages/GetNumberOfPages.py)