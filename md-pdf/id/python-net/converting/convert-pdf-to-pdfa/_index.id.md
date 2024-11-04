---
title: Mengonversi PDF ke format PDF/A di Python
linktitle: Mengonversi PDF ke format PDF/A
type: docs
weight: 100
url: /python-net/convert-pdf-to-pdfa/
lastmod: "2022-12-23"
description: Topik ini menunjukkan kepada Anda bagaimana Aspose.PDF untuk Python memungkinkan mengonversi file PDF ke file PDF yang sesuai dengan PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF untuk Python** memungkinkan Anda mengonversi file PDF ke file PDF yang sesuai dengan <abbr title="Portable Document Format / A">PDF/A</abbr>. Sebelum melakukannya, file harus divalidasi. Topik ini menjelaskan caranya.

{{% alert color="primary" %}}

Harap dicatat bahwa kami mengikuti Adobe Preflight untuk memvalidasi kesesuaian PDF/A. Semua alat di pasaran memiliki “representasi” sendiri tentang kesesuaian PDF/A. Silakan periksa artikel ini tentang alat validasi PDF/A sebagai referensi. Kami memilih produk Adobe untuk memverifikasi bagaimana Aspose.PDF menghasilkan file PDF karena Adobe berada di pusat segala sesuatu yang terhubung dengan PDF.

{{% /alert %}}

Konversi file menggunakan metode Convert dari kelas Document.
 Sebelum mengonversi PDF ke file yang sesuai dengan PDF/A, validasi PDF menggunakan metode Validate. Hasil validasi disimpan dalam file XML dan kemudian hasil ini juga diteruskan ke metode Convert. Anda juga dapat menentukan tindakan untuk elemen-elemen yang tidak dapat dikonversi menggunakan enumerasi ConvertErrorAction.

{{% alert color="success" %}}
**Cobalah untuk mengonversi PDF ke PDF/A secara online**

Aspose.PDF untuk Python menyajikan aplikasi gratis online ["PDF ke PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas cara kerjanya.

[![Aspose.PDF Konversi PDF ke PDF/A dengan Aplikasi Gratis](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

## Mengonversi file PDF ke PDF/A-1b

Cuplikan kode berikut menunjukkan cara mengonversi file PDF menjadi PDF yang sesuai dengan PDF/A-1b.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
    output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)
    # Konversi ke dokumen yang sesuai dengan PDF/A
    document.convert(output_log, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    # Simpan dokumen keluaran
    document.save(output_pdf)
```