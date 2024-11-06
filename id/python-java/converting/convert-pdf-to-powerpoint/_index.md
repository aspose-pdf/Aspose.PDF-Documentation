---
title: Convert PDF to PowerPoint dalam Python
linktitle: Convert PDF to PowerPoint
type: docs
weight: 30
url: id/python-java/convert-pdf-to-powerpoint/
description: Aspose.PDF memungkinkan Anda untuk mengonversi PDF ke format PPT (PowerPoint) menggunakan Python. Salah satu caranya adalah dengan mengonversi PDF ke PPTX dengan Slide sebagai Gambar.
lastmod: "2023-04-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## Ikhtisar

Apakah mungkin untuk mengonversi file PDF menjadi PowerPoint? Ya, Anda bisa! Dan itu mudah!
Artikel ini menjelaskan cara **mengonversi PDF ke PowerPoint menggunakan Python**. Ini mencakup topik-topik ini.

_Format_: **PPTX**
- [Python PDF ke PPTX](#python-pdf-to-pptx)
- [Python Mengonversi PDF ke PPTX](#python-pdf-to-pptx)
- [Python Cara mengonversi file PDF ke PPTX](#python-pdf-to-pptx)

_Format_: **PowerPoint**
- [Python PDF ke PowerPoint](#python-pdf-to-powerpoint)
- [Python Mengonversi PDF ke PowerPoint](#python-pdf-to-powerpoint)
- [Python Cara mengonversi file PDF ke PowerPoint](#python-pdf-to-powerpoint)


## Konversi PDF ke PowerPoint dan PPTX dalam Python

**Aspose.PDF untuk Python via Java** memungkinkan Anda melacak kemajuan konversi PDF ke PPTX.

Kami memiliki API bernama Aspose.Slides yang menawarkan fitur untuk membuat serta memanipulasi presentasi PPT/PPTX. API ini juga menyediakan fitur untuk mengonversi file PPT/PPTX ke format PDF. Selama konversi ini, halaman individual dari file PDF diubah menjadi slide terpisah dalam file PPTX.

Selama konversi PDF ke <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, teks dirender sebagai Teks di mana Anda dapat memilih/memperbaruinya. Harap dicatat bahwa untuk mengonversi file PDF ke format PPTX, Aspose.PDF menyediakan kelas bernama [`PptxSaveOptions`](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions). Sebuah objek dari kelas PptxSaveOptions diteruskan sebagai argumen kedua ke [`Document.Save(..) method`](https://reference.aspose.com/pdf/java/aspose.pdf/document/methods/save). Cuplikan kode berikut menunjukkan proses untuk mengonversi file PDF ke format PPTX.

## Konversi sederhana PDF ke PowerPoint menggunakan Python dan Aspose.PDF untuk Python

Untuk mengubah PDF ke PPTX, Aspose.PDF untuk Python menyarankan untuk menggunakan langkah-langkah kode berikut.

<a name="csharp-pdf-to-powerpoint"><strong>Langkah-langkah: Mengonversi PDF ke PowerPoint di Python</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Langkah-langkah: Mengonversi PDF ke PPTX di Python</strong></a>

1. Buat instance dari kelas [Document](https://reference.aspose.com/pdf/java/aspose.pdf/document)
2. Buat instance dari kelas [PptxSaveOptions](https://reference.aspose.com/pdf/java/aspose.pdf/pptxsaveoptions)
3. Gunakan metode **Save** dari objek **Document** untuk menyimpan PDF sebagai PPTX

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# Buka dokumen PDF
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SeparateImages = True
save_options._OptimizeTextBoxes = True

# Simpan file dalam format dokumen MS Word
document.save(output_pdf, save_options)
```


## Mengonversi PDF ke PPTX dengan Slide sebagai Gambar

{{% alert color="success" %}}
**Coba mengonversi PDF ke PowerPoint secara online**

Aspose.PDF untuk Python menyajikan aplikasi online gratis ["PDF ke PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), di mana Anda dapat mencoba menyelidiki fungsi dan kualitasnya bekerja.

[![Aspose.PDF Konversi PDF ke PPTX dengan Aplikasi Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Jika Anda perlu mengonversi PDF yang dapat dicari ke PPTX sebagai gambar, bukan teks yang dapat dipilih, Aspose.PDF menyediakan fitur seperti itu melalui kelas [Aspose.Pdf.PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/). Untuk mencapai ini, atur properti [SlidesAsImages](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/#properties) dari kelas [PptxSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/pptxsaveoptions/) ke 'true' seperti yang ditunjukkan dalam contoh kode berikut.

```python

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx_with_options.pptx"
# Buka dokumen PDF
document = Api.Document(input_pdf)

save_options = Api.PptxSaveOptions()
save_options._ImageResolution = 300
save_options._SlidesAsImages = True

# Simpan file ke format dokumen MS Word
document.save(output_pdf, save_options)
```


## Lihat Juga

Artikel ini juga mencakup topik-topik ini. Kode-kodenya sama seperti di atas.

_Format_: **PowerPoint**
- [Kode Python PDF ke PowerPoint](#python-pdf-to-powerpoint)
- [API Python PDF ke PowerPoint](#python-pdf-to-powerpoint)
- [Programatis Python PDF ke PowerPoint](#python-pdf-to-powerpoint)
- [Perpustakaan Python PDF ke PowerPoint](#python-pdf-to-powerpoint)
- [Simpan PDF sebagai PowerPoint dengan Python](#python-pdf-to-powerpoint)
- [Hasilkan PowerPoint dari PDF dengan Python](#python-pdf-to-powerpoint)
- [Buat PowerPoint dari PDF dengan Python](#python-pdf-to-powerpoint)
- [Pengonversi PDF ke PowerPoint dengan Python](#python-pdf-to-powerpoint)

_Format_: **PPTX**
- [Kode Python PDF ke PPTX](#python-pdf-to-pptx)
- [API Python PDF ke PPTX](#python-pdf-to-pptx)
- [Programatis Python PDF ke PPTX](#python-pdf-to-pptx)
- [Perpustakaan Python PDF ke PPTX](#python-pdf-to-pptx)
- [Simpan PDF sebagai PPTX dengan Python](#python-pdf-to-pptx)
- [Hasilkan PPTX dari PDF dengan Python](#python-pdf-to-pptx)
- [Buat PPTX dari PDF dengan Python](#python-pdf-to-pptx)
- [Pengonversi PDF ke PPTX dengan Python](#python-pdf-to-pptx)