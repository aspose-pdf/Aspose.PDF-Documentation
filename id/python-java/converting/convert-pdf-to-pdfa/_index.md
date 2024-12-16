---
title: Konversi PDF ke format PDF/A dalam Python
linktitle: Konversi PDF ke format PDF/A
type: docs
weight: 100
url: /id/python-java/convert-pdf-to-pdfa/
lastmod: "2023-04-06"
description: Topik ini menunjukkan bagaimana Aspose.PDF untuk Python memungkinkan untuk mengonversi file PDF ke file PDF yang memenuhi standar PDF/A.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF untuk Python** memungkinkan Anda mengonversi file PDF ke file PDF yang memenuhi standar <abbr title="Portable Document Format / A">PDF/A</abbr>. Sebelum melakukannya, file harus divalidasi. Topik ini menjelaskan bagaimana caranya.

{{% alert color="primary" %}}

Harap dicatat bahwa kami mengikuti Adobe Preflight untuk memvalidasi kepatuhan PDF/A. Semua alat di pasaran memiliki "representasi" mereka sendiri tentang kepatuhan PDF/A. Silakan periksa artikel ini tentang alat validasi PDF/A untuk referensi. Kami memilih produk Adobe untuk memverifikasi bagaimana Aspose.PDF menghasilkan file PDF karena Adobe berada di pusat segala sesuatu yang terhubung dengan PDF.

{{% /alert %}}

Konversi file menggunakan metode Convert kelas Dokumen.
 Sebelum mengonversi PDF ke file yang sesuai dengan PDF/A, validasi PDF menggunakan metode Validate. Hasil validasi disimpan dalam file XML dan kemudian hasil ini juga diteruskan ke metode Convert. Anda juga dapat menentukan tindakan untuk elemen yang tidak dapat dikonversi menggunakan enumerasi ConvertErrorAction.

{{% alert color="success" %}}
**Coba konversi PDF ke PDF/A secara online**

Aspose.PDF untuk Python menghadirkan aplikasi online gratis ["PDF ke PDF/A-1A"](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Konversi Aspose.PDF PDF ke PDF/A dengan Aplikasi Gratis](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}


## Konversi file PDF ke PDF/A-1b

Cuplikan kode berikut menunjukkan cara mengonversi file PDF ke PDF yang sesuai dengan PDF/A-1b.

```python


from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"
input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pdfa.pdf"
output_log = DIR_OUTPUT + "convert_pdf_to_pdfa.log"
# Buka dokumen PDF
document = Api.Document(input_pdf)
# Konversi ke dokumen yang sesuai dengan PDF/A
document.convert(output_log, Api.PdfFormat.PDF_A_1B, Api.ConvertErrorAction.Delete)
# Simpan dokumen keluaran
document.save(output_pdf)
```