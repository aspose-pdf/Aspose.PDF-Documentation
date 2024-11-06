---  
title: Mengonversi PDF ke PowerPoint di Python  
linktitle: Mengonversi PDF ke PowerPoint  
type: docs  
weight: 30  
url: id/python-net/convert-pdf-to-powerpoint/  
description: Aspose.PDF memungkinkan Anda untuk mengonversi PDF ke format PPT (PowerPoint) menggunakan Python. Salah satu cara ada kemungkinan untuk mengonversi PDF ke PPTX dengan Slide sebagai Gambar.  
lastmod: "2022-12-23"  
sitemap:  
    changefreq: "monthly"  
    priority: 0.7  
---  
## Tinjauan  

Apakah mungkin mengonversi file PDF menjadi PowerPoint? Ya, Anda bisa! Dan itu mudah!  
Artikel ini menjelaskan bagaimana **mengonversi PDF ke PowerPoint menggunakan Python**. Ini mencakup topik-topik ini.  

_Format_: **PPTX**  
- [Python PDF ke PPTX](#python-pdf-to-pptx)  
- [Python Mengonversi PDF ke PPTX](#python-pdf-to-pptx)  
- [Python Cara mengonversi file PDF ke PPTX](#python-pdf-to-pptx)  

_Format_: **PowerPoint**  
- [Python PDF ke PowerPoint](#python-pdf-to-powerpoint)  
- [Python Mengonversi PDF ke PowerPoint](#python-pdf-to-powerpoint)  
- [Python Cara mengonversi file PDF ke PowerPoint](#python-pdf-to-powerpoint)  

## Konversi PDF ke PowerPoint dan PPTX di Python  

**Aspose.PDF for Python via .NET** memungkinkan Anda melacak kemajuan konversi PDF ke PPTX.

Kami memiliki API bernama Aspose.Slides yang menawarkan fitur untuk membuat serta memanipulasi presentasi PPT/PPTX. API ini juga menyediakan fitur untuk mengonversi file PPT/PPTX ke format PDF. Selama konversi ini, halaman individual dari file PDF dikonversi menjadi slide terpisah dalam file PPTX.

Selama konversi PDF ke <abbr title="Microsoft PowerPoint 2007 XML Presentation">PPTX</abbr>, teks dirender sebagai Teks di mana Anda dapat memilih/memperbaruinya. Harap dicatat bahwa untuk mengonversi file PDF ke format PPTX, Aspose.PDF menyediakan kelas bernama [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Sebuah objek dari kelas PptxSaveOptions diteruskan sebagai argumen kedua ke [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods). Cuplikan kode berikut menunjukkan proses untuk mengonversi file PDF ke format PPTX.

## Konversi sederhana PDF ke PowerPoint menggunakan Python dan Aspose.PDF untuk Python

Untuk mengonversi PDF ke PPTX, Aspose.PDF untuk Python menyarankan menggunakan langkah-langkah kode berikut.

<a name="csharp-pdf-to-powerpoint"><strong>Langkah-langkah: Mengonversi PDF ke PowerPoint dalam Python</strong></a> | <a name="csharp-pdf-to-pptx"><strong>Langkah-langkah: Mengonversi PDF ke PPTX dalam Python</strong></a>

1. Buat instance kelas [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
2. Buat instance kelas [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/)
3. Gunakan metode **Save** dari objek **Document** untuk menyimpan PDF sebagai PPTX

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_pptx.pptx"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)
    # Instansiasi PptxSaveOptions
    save_option = ap.PptxSaveOptions()
    # Simpan file ke dalam format MS PowerPoint
    document.save(output_pdf, save_option)
```

## Mengonversi PDF ke PPTX dengan Slide sebagai Gambar


{{% alert color="success" %}}
**Coba konversi PDF ke PowerPoint secara online**

Aspose.PDF untuk Python menyajikan aplikasi online gratis ["PDF ke PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), di mana Anda dapat mencoba menyelidiki fungsionalitas dan kualitas kerjanya.

[![Aspose.PDF Konversi PDF ke PPTX dengan Aplikasi Gratis](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}

Jika Anda perlu mengonversi PDF yang dapat dicari ke PPTX sebagai gambar alih-alih teks yang dapat dipilih, Aspose.PDF menyediakan fitur tersebut melalui kelas [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/). Untuk mencapai ini, atur properti [slides_as_images](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/#properties) dari kelas [PptxSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/pptxsaveoptions/) ke 'true' seperti yang ditunjukkan dalam contoh kode berikut.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_pptx_with_slides_as_images.pptx"
    # Buka dokumen PDF
    document = ap.Document(input_pdf)
    # Buat instance PptxSaveOptions
    save_option = ap.PptxSaveOptions()
    save_option.slides_as_images = True
    # Simpan file ke format MS PowerPoint
    document.save(output_pdf, save_option)
```


## Lihat Juga

Artikel ini juga mencakup topik-topik ini. Kode-kodenya sama seperti di atas.

_Format_: **PowerPoint**
- [Kode Python dari PDF ke PowerPoint](#python-pdf-to-powerpoint)
- [API Python dari PDF ke PowerPoint](#python-pdf-to-powerpoint)
- [Program Python dari PDF ke PowerPoint](#python-pdf-to-powerpoint)
- [Perpustakaan Python dari PDF ke PowerPoint](#python-pdf-to-powerpoint)
- [Simpan PDF sebagai PowerPoint dengan Python](#python-pdf-to-powerpoint)
- [Hasilkan PowerPoint dari PDF dengan Python](#python-pdf-to-powerpoint)
- [Buat PowerPoint dari PDF dengan Python](#python-pdf-to-powerpoint)
- [Pengonversi Python dari PDF ke PowerPoint](#python-pdf-to-powerpoint)

_Format_: **PPTX**
- [Kode Python dari PDF ke PPTX](#python-pdf-to-pptx)
- [API Python dari PDF ke PPTX](#python-pdf-to-pptx)
- [Program Python dari PDF ke PPTX](#python-pdf-to-pptx)
- [Perpustakaan Python dari PDF ke PPTX](#python-pdf-to-pptx)
- [Simpan PDF sebagai PPTX dengan Python](#python-pdf-to-pptx)
- [Hasilkan PPTX dari PDF dengan Python](#python-pdf-to-pptx)
- [Buat PPTX dari PDF dengan Python](#python-pdf-to-pptx)

- [Pengonversi Python dari PDF ke PPTX](#python-pdf-to-pptx)