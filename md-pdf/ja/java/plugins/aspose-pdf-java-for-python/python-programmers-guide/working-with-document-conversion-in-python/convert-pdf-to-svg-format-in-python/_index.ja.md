---
title: PythonでPDFをSVG形式に変換
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-python/
lastmod: "2021-06-05"
---

**Aspose.PDF Java for Python**を使用してPDFをSVG形式に変換するには、**PdfToSvg**モジュールを呼び出すだけです。

```python

# 対象のドキュメントを開く
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# SvgSaveOptionsのオブジェクトをインスタンス化
save_options = self.SvgSaveOptions()

# SVG画像をZipアーカイブに圧縮しない
save_options.CompressOutputToZipArchive = False;

# 出力をXLS形式で保存
doc.save(self.dataDir + "Output1.svg", save_options)

print "ドキュメントが正常に変換されました"
```

**実行コードをダウンロード**

以下のいずれかのソーシャルコーディングサイトから、**Convert PDF to SVG Format (Aspose.PDF)**をダウンロードしてください：

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)