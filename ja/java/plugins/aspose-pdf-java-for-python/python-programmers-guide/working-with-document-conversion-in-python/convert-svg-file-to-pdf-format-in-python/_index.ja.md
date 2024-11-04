---
title: PythonでSVGファイルをPDF形式に変換する
type: docs
weight: 40
url: /java/convert-svg-file-to-pdf-format-in-python/
lastmod: "2021-06-05"
---

## PythonでSVGファイルをPDF形式に変換する方法

**Aspose.PDF Java for Python**を使用してSVGファイルをPDF形式に変換するには、**SvgToPdf**モジュールを呼び出します。

Pythonコード:

```python
options = self.SvgLoadOptions();
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'
出力をXLS形式で保存
doc.save(self.dataDir + "SVG1.pdf");
print "ドキュメントが正常に変換されました"
```

## 実行コードのダウンロード

以下のいずれかのソーシャルコーディングサイトから**Convert SVG to PDF (Aspose.PDF)**をダウンロードしてください:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/SvgToPdf/SvgToPdf.py)