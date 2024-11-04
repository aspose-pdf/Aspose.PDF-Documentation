---
title: Membuat PDF/3-A yang sesuai dan melampirkan faktur ZUGFeRD di C#
linktitle: Melampirkan ZUGFeRD ke PDF
type: docs
weight: 10
url: /net/attach-zugferd/
description: Pelajari cara menghasilkan dokumen PDF dengan ZUGFeRD di Aspose.PDF untuk .NET
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Melampirkan ZUGFeRD ke PDF

Potongan kode berikut juga berfungsi dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Kami merekomendasikan langkah-langkah berikut untuk melampirkan ZUGFeRD ke PDF:

* Tentukan variabel jalur yang menunjuk ke folder tempat file PDF masukan dan keluaran berada.
* Buat objek dokumen dengan memuat file PDF yang ada (misalnya "ZUGFeRD-test.pdf") dari jalur tersebut.
* Buat objek [FileSpecification](https://reference.aspose.com/pdf/net/aspose.pdf/filespecification/) dengan menyediakan jalur dan deskripsi file lain bernama "factur-x.xml", yang berisi metadata faktur yang sesuai dengan standar ZUGFeRD.
* Tambahkan properti ke objek spesifikasi file, seperti deskripsi, tipe MIME, dan hubungan AF.
* Tambahkan properti ke objek spesifikasi file, seperti deskripsi, tipe MIME, dan hubungan AF.
* Tambahkan objek spesifikasi file ke koleksi file tersemat dokumen. Nama file harus ditentukan sesuai standar ZUGFeRD, misalnya "factur-x.xml".
* Konversi dokumen menjadi format PDF/A-3U, subset dari PDF yang memastikan pelestarian jangka panjang dokumen elektronik. PDF/A-3U memungkinkan penyematan file dalam format apa pun di dokumen PDF.
* Simpan dokumen yang telah dikonversi sebagai file PDF baru (misalnya "ZUGFeRD-res.pdf").

```cs
var path = @"C:\Samples\ZUGFeRD\";

var document = new Aspose.Pdf.Document(Path.Combine(path,"ZUGFeRD-test.pdf"));
// Setup new file to be added as attachment
var description = "Metadata faktur sesuai dengan standar ZUGFeRD";
var fileSpecification = new Aspose.Pdf.FileSpecification(Path.Combine(path, "factur-x.xml"), description)
{
    Description = "Zugferd",
    MIMEType = "text/xml",
    AFRelationship = Aspose.Pdf.AFRelationship.Alternative
};
// Add attachment to document's attachment collection
document.EmbeddedFiles.Add(fileSpecification);
document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.PDF_A_3U, Aspose.Pdf.ConvertErrorAction.Delete);
document.Save(Path.Combine(path, "ZUGFeRD-res.pdf"));
```
Metode convert mengambil stream, format PDF, dan aksi kesalahan konversi sebagai parameter. Parameter stream dapat digunakan untuk menyimpan log konversi. Parameter aksi kesalahan konversi menentukan apa yang harus dilakukan jika terjadi kesalahan selama konversi. Dalam hal ini, diatur ke "Delete", yang berarti elemen apa pun yang tidak sesuai dengan format PDF/A-3U akan dihapus dari dokumen.
