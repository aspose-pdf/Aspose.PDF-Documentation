---
title: Menggunakan Aspose.PDF untuk .NET dengan Python
linktitle: Integrasi dengan Python
type: docs
weight: 100
url: /id/net/python-net/
description: Dalam tutorial ini, Anda akan menjelajahi berbagai cara membuat dan memodifikasi file PDF dalam Python.
lastmod: "2022-01-10"
sitemap:
    changefreq: "weekly"
    priority: 0.5
---

Artikel ini menggambarkan contoh singkat bagaimana membuat PDF menggunakan integrasi Aspose.PDF untuk .NET dengan Python.

## Prasyarat

Untuk menggunakan Aspose.PDF untuk .NET di Python silakan gunakan `requirments.txt` berikut:

```bash
pip==21.3.1
pycparser==2.21
pythonnet==2.5.2
setuptools==60.1.0
```

Anda juga harus meletakkan `Aspose.PDF.dll` di folder yang diinginkan.

## Membuat PDF Sederhana menggunakan Python

Untuk bekerja kita akan perlu mengintegrasikan [PythonNet](https://github.com/pythonnet/pythonnet) ke aplikasi kita dan melakukan beberapa pengaturan.

```python
import clr

aspose_pdf = clr.AddReference("D:\\aspose-python-net\\Aspose.PDF.dll")

from System import TimeSpan

from Aspose.Pdf import Document, Color, License, BorderInfo, BorderSide, Rectangle, HorizontalAlignment
from Aspose.Pdf import Table, MarginInfo
from Aspose.Pdf.Text import TextFragment, Position, TextBuilder,FontRepository
```
### Membuat dokumen sederhana

Mari membuat PDF sederhana dengan teks klasik "Hello, world". Untuk penjelasan lebih detail, silakan menuju ke [halaman ini](https://docs.aspose.com/pdf/net/hello-world-example/)

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):

        # Inisialisasi objek dokumen
        document = Document()
        # Tambahkan halaman
        page = document.Pages.Add()
        # Tambahkan teks ke halaman baru
        textFragment = TextFragment("Hello,world!")
        textFragment.Position = Position(100, 600)

        textFragment.TextState.FontSize = 12
        textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman")
        textFragment.TextState.BackgroundColor = Color.Blue
        textFragment.TextState.ForegroundColor = Color.Yellow

        # Buat objek TextBuilder
        textBuilder = TextBuilder(page)

        # Tambahkan fragmen teks ke halaman PDF
        textBuilder.AppendText(textFragment)

        document.Save("HelloWorld_out.pdf")
```
## Membuat PDF Kompleks Menggunakan Python

Contoh berikut menunjukkan bagaimana kita dapat membuat dokumen PDF kompleks dengan gambar dan tabel. Contoh ini berdasarkan [halaman berikut](https://docs.aspose.com/pdf/net/complex-pdf-example/).

```python
class HelloWorld(object):
    def __init__(self,licence_path):
        self.dataDir = "C:\\Samples\\"
        if licence_path:
            self.licence_path = licence_path
            self.aspose_license = License()
            self.aspose_license.SetLicense(self.licence_path)

    def run_simple(self):
    # ... dilewati ...

    # Membuat Dokumen Kompleks
    def run_complex(self):

        # Inisialisasi objek dokumen
        document = Document()
        # Tambahkan halaman
        page = document.Pages.Add()

        # Tambahkan gambar
        imageFileName = self.dataDir + "logo.png"
        page.AddImage(imageFileName, Rectangle(20, 730, 120, 830))

        # Tambahkan Header
        header = TextFragment("Rute ferry baru pada Musim Gugur 2020")
        header.TextState.Font = FontRepository.FindFont("Arial")
        header.TextState.FontSize = 24
        header.HorizontalAlignment = HorizontalAlignment.Center
        header.Position = Position(130, 720)
        page.Paragraphs.Add(header)

        # Tambahkan deskripsi
        descriptionText = "Pengunjung harus membeli tiket secara online dan tiket terbatas hanya 5.000 per hari. \
        Layanan ferry beroperasi dengan kapasitas setengah dan jadwal yang dikurangi. Harapkan antrean."
        description = TextFragment(descriptionText)
        description.TextState.Font = FontRepository.FindFont("Times New Roman")
        description.TextState.FontSize = 14
        description.HorizontalAlignment = HorizontalAlignment.Left
        page.Paragraphs.Add(description)


        # Tambahkan tabel
        table = Table()

        table.ColumnWidths = "200"
        table.Border = BorderInfo(BorderSide.Box, 1.0, Color.DarkSlateGray)
        table.DefaultCellBorder = BorderInfo(BorderSide.Box, 0.5, Color.Black)
        table.DefaultCellPadding = MarginInfo(4.5, 4.5, 4.5, 4.5)
        table.Margin.Bottom = 10
        table.DefaultCellTextState.Font =  FontRepository.FindFont("Helvetica")

        headerRow = table.Rows.Add()
        headerRow.Cells.Add("Kota Keberangkatan")
        headerRow.Cells.Add("Pulau Keberangkatan")

        i=0
        while(i<headerRow.Cells.Count):
            headerRow.Cells[i].BackgroundColor = Color.Gray
            headerRow.Cells[i].DefaultCellTextState.ForegroundColor = Color.WhiteSmoke
            i+=1

        time = TimeSpan(6, 0, 0)
        incTime = TimeSpan(0, 30, 0)

        i=0
        while (i<10):
            dataRow = table.Rows.Add()
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            time=time.Add(incTime)
            dataRow.Cells.Add(time.ToString("hh\:mm"))
            i+=1

        page.Paragraphs.Add(table)

        document.Save(self.dataDir + "Complex.pdf")
```
## Cara Menjalankan Pembuatan PDF di Windows

Snippet ini menunjukkan cara menjalankan contoh di atas pada PC Windows. Kami mengasumsikan bahwa `class HelloWorld` berada dalam file `example_get_started.py`.
Jika Anda menjalankan versi trial dari Aspose.PDF untuk .NET, Anda harus memberikan string kosong sebagai `license_path`.

```python
import example_get_started

def main():

    example = example_get_started.HelloWorld("<license_path>")
    example.run_simple()
    example.run_complex()


if __name__ == '__main__':
    main()
```
