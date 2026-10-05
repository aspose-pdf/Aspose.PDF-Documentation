---
title: PythonでPDFファイルを個別ページに分割する
linktitle: PythonでPDFファイルを個別ページに分割する
type: docs
weight: 80
url: /ja/java/split-pdf-file-into-individual-pages-in-python/
description: Aspose.PDF を使用して Python で PDF を個別ページに分割する方法を調査し、ページ抽出と管理を容易にします。
lastmod: "2026-10-05"
---
**Aspose.PDF Java for PHP** を使用して PDF ドキュメントを個別ページに分割するには、単に **SplitAllPages** クラスを呼び出すだけです。

```python

pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# loop through all the pages
pdf_page = 1
total_size = pdf.getPages().size()
while (pdf_page <= total_size):

# create a new Document object
new_document = self.Document();

# get the page at particular index of Page Collection
new_document.getPages().add(pdf.getPages().get_Item(pdf_page))

# save the newly generated PDF file
new_document.save(self.dataDir + "page_#{$pdf_page}.pdf")

pdf_page+=1

print "Split process completed successfully!";
```

**コードの実行をダウンロード**

Download **Split Pages (Aspose.PDF)**В from В 以下に記載されたソーシャルコーディングサイトのいずれかからダウンロード:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/SplitAllPages/SplitAllPages.py)
