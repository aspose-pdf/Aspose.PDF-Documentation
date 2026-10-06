---
title: Python で PDF を SVG 形式に変換
linktitle: Python で PDF を SVG 形式に変換
type: docs
weight: 30
url: /ja/java/convert-pdf-to-svg-format-in-python/
description: "Python を使用して Aspose.PDF により PDF ドキュメントを SVG 形式に変換し、スケーラブルなベクター出力を実現する方法を学びます。"
lastmod: "2026-10-06"
---
**Aspose.PDF Java for Python** を使用して PDF を SVG 形式に変換するには、単に **PdfToSvg** モジュールを呼び出してください。

```python

# Open the target document
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# instantiate an object of SvgSaveOptions
save_options = self.SvgSaveOptions()

# do not compress SVG image to Zip archive
save_options.CompressOutputToZipArchive = False;

# Save the output to XLS format
doc.save(self.dataDir + "Output1.svg", save_options)

print "Document has been converted successfully"
```

**実行コードのダウンロード**

ダウンロード **Convert PDF to SVG Format (Aspose.PDF)** は、以下に記載されたソーシャルコーディングサイトのいずれかから行ってください。

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)
