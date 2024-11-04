---
title: Konversi PDF ke Format SVG di Python
type: docs
weight: 30
url: /java/convert-pdf-to-svg-format-in-python/
lastmod: "2021-06-05"
---

Untuk mengonversi PDF ke format SVG menggunakan **Aspose.PDF Java for Python**, cukup panggil modul **PdfToSvg**.

```python

# Buka dokumen target
doc=self.Document()
pdf = self.Document()
pdf=self.dataDir +'input1.pdf'

# instansiasi objek dari SvgSaveOptions
save_options = self.SvgSaveOptions()

# jangan kompres gambar SVG ke arsip Zip
save_options.CompressOutputToZipArchive = False;

# Simpan output ke format XLS
doc.save(self.dataDir + "Output1.svg", save_options)

print "Dokumen telah berhasil dikonversi"
```

**Unduh Kode Berjalan**

Unduh **Convert PDF to SVG Format (Aspose.PDF)** dari salah satu situs pengkodean sosial yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_Python/test/WorkingWithDocumentConversion/PdfToSvg/PdfToSvg.py)