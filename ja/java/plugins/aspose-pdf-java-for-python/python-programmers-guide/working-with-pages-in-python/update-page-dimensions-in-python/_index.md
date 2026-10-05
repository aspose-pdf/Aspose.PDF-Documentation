---
title: "Python での ページ寸法の更新"
linktitle: "Python での ページ寸法の更新"
type: docs
weight: 90
url: /ja/java/update-page-dimensions-in-python/
description: Aspose.PDF を使用して Python で PDF ドキュメント内のページ寸法を更新する方法を理解し、文書レイアウトの制御を向上させます。
lastmod: "2026-10-05"
---
**Aspose.PDF Java for Python** を使用してページ寸法を更新するには、単に **UpdatePageDimensions** クラスを呼び出します。

```python
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# get page collection
page_collection = pdf.getPages()

# get particular page
pdf_page = page_collection.get_Item(1)

# set the page size as A4 (11.7 x 8.3 in) and in Aspose.PDF, 1 inch = 72 points
# so A4 dimensions in points will be (842.4, 597.6)
pdf_page.setPageSize(597.6,842.4)

# save the newly generated PDF file
pdf.save(self.dataDir + "output.pdf")

print "Dimensions updated successfully!"

```

**ランニングコードをダウンロード**

ダウンロードВ **ページ寸法の更新 (Aspose.PDF)**В からВ 以下に記載されたソーシャルコーディングサイトのいずれかから:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)
