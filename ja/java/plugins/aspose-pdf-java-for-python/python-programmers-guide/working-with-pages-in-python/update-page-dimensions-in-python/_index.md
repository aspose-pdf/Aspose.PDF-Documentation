---
title: Pythonでページの寸法を更新
type: docs
weight: 90
url: /ja/java/update-page-dimensions-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**を使用してページの寸法を更新するには、単に**UpdatePageDimensions**クラスを呼び出します。

```python
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# ページコレクションを取得
page_collection = pdf.getPages()

# 特定のページを取得
pdf_page = page_collection.get_Item(1)

# ページサイズをA4（11.7 x 8.3インチ）に設定し、Aspose.PDFでは1インチ=72ポイント
# したがって、A4の寸法はポイントで(842.4, 597.6)になります
pdf_page.setPageSize(597.6,842.4)

# 新しく生成されたPDFファイルを保存
pdf.save(self.dataDir + "output.pdf")

print "寸法が正常に更新されました！"

```

**実行コードのダウンロード**

以下のいずれかのソーシャルコーディングサイトから**Update Page Dimensions (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/UpdatePageDimensions/UpdatePageDimensions.py)