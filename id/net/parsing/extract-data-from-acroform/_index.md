---
title:  Ekstrak data dari AcroForm menggunakan C#
linktitle:  Ekstrak data dari AcroForm
type: docs
weight: 50
url: id/net/extract-data-from-acroform/
description: Aspose.PDF memudahkan untuk mengekstrak data bidang formulir dari berkas PDF. Pelajari cara mengekstrak data dari AcroForms dan menyimpannya dalam format JSON, XML, atau FDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak bidang formulir dari dokumen PDF

Selain memungkinkan Anda menghasilkan bidang formulir dan mengisi bidang formulir, Aspose.PDF untuk .NET memudahkan untuk mengekstrak data bidang formulir atau informasi tentang bidang formulir dari berkas PDF.

Pada kode sampel di bawah ini kami menunjukkan cara mengulang setiap halaman dalam PDF untuk mengekstrak informasi tentang semua AcroForm dalam PDF serta nilai bidang formulir. Kode sampel ini mengasumsikan bahwa Anda tidak mengetahui nama bidang formulir sebelumnya.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractFormFields()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    // Dapatkan nilai dari semua bidang
    foreach (Field formField in document.Form)
    {
        Console.WriteLine("Nama Bidang : {0} ", formField.PartialName);
        Console.WriteLine("Nilai : {0} ", formField.Value);
    }
}
```
Jika Anda mengetahui nama dari field formulir yang ingin Anda ambil nilai dari, maka Anda dapat menggunakan indexer dalam koleksi Documents.Form untuk segera mengambil data ini. Lihat di bagian bawah artikel ini untuk contoh kode tentang cara menggunakan fungsi tersebut.

## Ambil nilai field formulir berdasarkan judul

Properti Value dari field formulir memungkinkan Anda untuk mendapatkan nilai dari field tertentu. Untuk mendapatkan nilai, ambil field formulir dari koleksi Form objek Dokumen. Contoh ini memilih TextBoxField dan mengambil nilainya menggunakan properti Value.

## Ekstrak field formulir dari dokumen PDF ke JSON

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void ExtractFormFieldsToJson()
{
    var document = new Aspose.Pdf.Document(Path.Combine(_dataDir, "StudentInfoFormElectronic.pdf"));
    var formData = document.Form.Cast<Field>().Select(f => new { Name = f.PartialName, f.Value });
    string jsonString = JsonSerializer.Serialize(formData);
    Console.WriteLine(jsonString);
}
```
## Ekstrak Data ke XML dari File PDF

Kelas Form memungkinkan Anda untuk mengekspor data ke file XML dari file PDF menggunakan metode ExportXml. Untuk mengekspor data ke XML, Anda perlu membuat objek dari kelas Form kemudian memanggil metode ExportXml menggunakan objek FileStream. Akhirnya, Anda dapat menutup objek FileStream dan membuang objek Form. Cuplikan kode berikut menunjukkan cara mengekspor data ke file XML.

Cuplikan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

// Buka dokumen
Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
form.BindPdf(dataDir + "input.pdf");
// Buat file xml.
System.IO.FileStream xmlOutputStream = new FileStream( dataDir + "input.xml", FileMode.Create);
// Ekspor data
form.ExportXml(xmlOutputStream);
// Tutup aliran file
xmlOutputStream.Close();

// Tutup dokumen
form.Dispose();
```
## Ekspor Data ke FDF dari File PDF

Kelas Form memungkinkan Anda untuk mengekspor data ke file FDF dari file PDF menggunakan metode ExportFdf. Untuk mengekspor data ke FDF, Anda perlu membuat objek dari kelas Form dan kemudian memanggil metode ExportFdf menggunakan objek FileStream. Akhirnya, Anda dapat menyimpan file PDF menggunakan metode Save dari kelas Form. Cuplikan kode berikut menunjukkan cara mengekspor data ke file FDF.

Cuplikan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Buka Dokumen
form.BindPdf(dataDir + "input.pdf");

// Buat file fdf.
System.IO.FileStream fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create);

// Ekspor data
form.ExportFdf(fdfOutputStream);

// Tutup aliran file
fdfOutputStream.Close();

// Simpan dokumen yang diperbarui
form.Save(dataDir + "ExportDataToPdf_out.pdf");
```
## Ekspor Data ke XFDF dari File PDF

Kelas Form memungkinkan Anda untuk mengekspor data ke file XFDF dari file PDF menggunakan metode ExportXfdf. Untuk mengekspor data ke XFDF, Anda perlu membuat objek dari kelas Form dan kemudian memanggil metode ExportXfdf menggunakan objek FileStream. Akhirnya, Anda dapat menyimpan file PDF menggunakan metode Save dari kelas Form. Potongan kode berikut menunjukkan cara mengekspor data ke file XFDF.

Potongan kode berikut juga berfungsi dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

Aspose.Pdf.Facades.Form form = new Aspose.Pdf.Facades.Form();
// Buka Dokumen
form.BindPdf(dataDir + "input.pdf");

// Buat file xfdf.
System.IO.FileStream xfdfOutputStream = new FileStream("student1.xfdf", FileMode.Create);

// Ekspor data
form.ExportXfdf(xfdfOutputStream);

// Tutup aliran file
xfdfOutputStream.Close();

// Simpan dokumen yang diperbarui
form.Save(dataDir + "ExportDataToXFDF_out.pdf");
```

