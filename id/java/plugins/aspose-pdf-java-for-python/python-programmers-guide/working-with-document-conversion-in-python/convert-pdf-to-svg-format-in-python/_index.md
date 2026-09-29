---
title: Mengonversi PDF ke Format SVG di Python
linktitle: Mengonversi PDF ke Format SVG di Python
type: docs
weight: 30
url: /id/java/convert-pdf-to-svg-format-in-python/
description: Pelajari cara mengonversi dokumen PDF ke format SVG di Python menggunakan Aspose.PDF untuk output vektor skalabel.
lastmod: "2026-09-29"
---
Untuk mengonversi PDF ke format SVG menggunakan **Aspose.PDF Java for Python**, cukup panggil modul **PdfToSvg**.

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

**Unduh Kode yang Berjalan**

UnduhВ **Konversi PDF ke Format SVG (Aspose.PDF)**В dariВ salah satu situs coding sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)
