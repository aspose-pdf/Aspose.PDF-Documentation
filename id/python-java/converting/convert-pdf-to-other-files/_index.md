---
title: Mengonversi PDF ke EPUB, LaTeX, Teks, XPS dalam Python
linktitle: Mengonversi PDF ke format lain
type: docs
weight: 90
url: /id/python-java/convert-pdf-to-other-files/
lastmod: "2023-04-06"
description: Topik ini menunjukkan cara mengonversi file PDF ke format file lain seperti EPUB, LaTeX, Teks, XPS, dll menggunakan Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Mengonversi PDF ke EPUB

{{% alert color="success" %}}
**Coba mengonversi PDF ke EPUB secara online**

Aspose.PDF untuk Python menghadirkan aplikasi online gratis ["PDF ke EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Mengonversi PDF ke EPUB dengan Aplikasi Gratis](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** adalah standar e-book gratis dan terbuka dari International Digital Publishing Forum (IDPF).
 Files have the extension .epub.  
EPUB dirancang untuk konten yang dapat diatur ulang, yang berarti bahwa pembaca EPUB dapat mengoptimalkan teks untuk perangkat tampilan tertentu. EPUB juga mendukung konten dengan tata letak tetap. Format ini dimaksudkan sebagai format tunggal yang dapat digunakan oleh penerbit dan rumah konversi di dalam perusahaan, serta untuk distribusi dan penjualan. Ini menggantikan standar Open eBook.

Aspose.PDF untuk Python juga mendukung fitur untuk mengonversi dokumen PDF ke format EPUB. Aspose.PDF untuk Python memiliki kelas bernama 'EpubSaveOptions' yang dapat digunakan sebagai argumen kedua untuk metode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) untuk menghasilkan file EPUB.  
Silakan coba gunakan cuplikan kode berikut untuk memenuhi persyaratan ini dengan Python.

```python

from asposepdf import Api

# inisialisasi lisensi
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# Konversi ke Epub
documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.epub"
doc.save(documentOutName, Api.SaveFormat.Epub)
```

## Mengubah PDF ke LaTeX/TeX

**Aspose.PDF untuk Python via Java** mendukung konversi PDF ke LaTeX/TeX. Format file LaTeX adalah format file teks dengan markup khusus dan digunakan dalam sistem penyiapan dokumen berbasis TeX untuk penataan huruf berkualitas tinggi.

{{% alert color="success" %}}
**Coba konversi PDF ke LaTeX/TeX secara online**

Aspose.PDF untuk Python mempersembahkan aplikasi gratis online ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitasnya.

[![Aspose.PDF Konversi PDF ke LaTeX/TeX dengan Aplikasi Gratis](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

Untuk mengonversi file PDF ke TeX, Aspose.PDF memiliki kelas [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/latexsaveoptions/) yang menyediakan properti OutDirectoryPath untuk menyimpan gambar sementara selama proses konversi.

Cuplikan kode berikut menunjukkan proses konversi file PDF menjadi format TEX dengan Python.

```python
from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.tex"
doc.save(documentOutName, Api.SaveFormat.TeX)
```

## Konversi PDF ke Teks

**Aspose.PDF untuk Python** mendukung konversi seluruh dokumen PDF dan halaman tunggal menjadi file Teks.

### Konversi dokumen PDF ke file Teks

Anda dapat mengonversi dokumen PDF ke file TXT menggunakan kelas 'TextDevice'.

Cuplikan kode berikut menjelaskan cara mengekstrak teks dari semua halaman.

```python

from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_text"
# Buka dokumen PDF
document = Api.Document(input_pdf)

device = Device.TextDevice()

for i in range(0, document.getPages.size):
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.txt"
    # Konversi halaman tertentu dan simpan sebagai file teks
    device.process(document.getPages.getPage(i + 1), imageFileName)
```
**Coba konversi PDF ke Teks online**
{{% alert color="success" %}}

Aspose.PDF untuk Python menawarkan aplikasi online gratis ["PDF ke Teks"](https://products.aspose.app/pdf/conversion/pdf-to-txt), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke Teks dengan Aplikasi Gratis](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Konversi PDF ke XPS

**Aspose.PDF untuk Python** memberikan kemungkinan untuk mengonversi file PDF ke format <abbr title="XML Paper Specification">XPS</abbr>. Mari coba gunakan cuplikan kode yang disajikan untuk mengonversi file PDF ke format XPS dengan Python.

{{% alert color="success" %}}
**Coba konversi PDF ke XPS online**

Aspose.PDF untuk Python menawarkan aplikasi online gratis ["PDF ke XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke XPS dengan Aplikasi Gratis](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

Tipe file XPS terutama diasosiasikan dengan Spesifikasi Kertas XML oleh Microsoft Corporation. Spesifikasi Kertas XML (XPS), sebelumnya bernama kode Metro dan menggabungkan konsep pemasaran Next Generation Print Path (NGPP), adalah inisiatif Microsoft untuk mengintegrasikan pembuatan dan penayangan dokumen ke dalam sistem operasi Windows.

Untuk mengonversi file PDF ke XPS, Aspose.PDF memiliki kelas [XpsSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/xpssaveoptions/) yang digunakan sebagai argumen kedua untuk metode [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) untuk menghasilkan file XPS.

Potongan kode berikut menunjukkan proses mengonversi file PDF ke format XPS.

```python

from asposepdf import Api

documentName = "../../testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "../../testout/out.xps"
doc.save(documentOutName, Api.SaveFormat.Xps)

```