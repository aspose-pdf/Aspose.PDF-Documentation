---
title: "Python での PDF ファイルから特定のページの削除"
linktitle: "Python での PDF ファイルから特定のページの削除"
type: docs
weight: 20
url: /ja/java/delete-a-particular-page-from-the-pdf-file-in-python/
description: Aspose.PDF を使用して Python で PDF ドキュメントから特定のページを削除する方法を学び、効率的な文書編集を実現します。
lastmod: "2026-10-06"
---
**Aspose.PDF Java for Python** を使用して PDF ドキュメントから特定のページを削除するには、単に **DeletePage** クラスを呼び出すだけです。

```python

doc= self.Document()
pdf = self.Document()
pdf=self.dataDir + 'input1.pdf'

# delete a particular page
pdf.getPages().delete(2)

# save the newly generated PDF file
doc.save(self.dataDir + "output.pdf")

print "Page deleted successfully!"

```

**実行コードのダウンロード**

**Delete Page (Aspose.PDF)** を、以下に記載されたソーシャルコーディングサイトのいずれかからダウンロードしてください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithPages/DeletePage/DeletePage.py)
