---
title: PythonでPDFのページ数を取得
type: docs
weight: 40
url: /java/get-page-count-of-pdf-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**を使用してPdfドキュメントのページ数を取得するには、**GetNumberOfPages**クラスを呼び出すだけです。

```Python
doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'
page_count = pdf.getPages().size()
print "ページ数:" . page_count

```

**実行可能コードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから **Get Page Count (Aspose.PDF)** をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/GetNumberOfPages/GetNumberOfPages.py)