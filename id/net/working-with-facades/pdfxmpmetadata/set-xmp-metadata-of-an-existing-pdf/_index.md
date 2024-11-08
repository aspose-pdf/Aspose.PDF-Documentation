---
title: Set XMP Metadata of an existing PDF
type: docs
weight: 20
url: /id/net/set-xmp-metadata-of-an-existing-pdf/
description: Bagian ini menjelaskan cara mengatur Metadata XMP dari PDF yang sudah ada dengan Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

Untuk mengatur metadata XMP dalam file PDF, Anda perlu membuat objek [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) dan mengikat file PDF menggunakan metode [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Anda dapat menggunakan metode [Add](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata/methods/add/index) dari kelas [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata) untuk menambahkan berbagai properti. Terakhir, panggil metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index) dari kelas [PdfXmpMetadata](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfxmpmetadata). Cuplikan kode berikut menunjukkan cara menambahkan metadata XMP dalam file PDF.

```csharp
// Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
// Jalur ke direktori dokumen.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_WorkingDocuments();

// Buat objek PdfXmpMetadata
PdfXmpMetadata xmpMetaData = new PdfXmpMetadata();

// Menghubungkan file pdf ke objek
xmpMetaData.BindPdf(dataDir+ "SetXMPMetadata.pdf");

// Tambahkan tanggal pembuatan
xmpMetaData.Add(DefaultMetadataProperties.CreateDate, System.DateTime.Now.ToString());

// Ubah tanggal metadata
xmpMetaData[DefaultMetadataProperties.MetadataDate] = System.DateTime.Now.ToString();

// Tambahkan alat pembuat
xmpMetaData.Add(DefaultMetadataProperties.CreatorTool, "Nama alat pembuat");

// Hapus tanggal modifikasi
xmpMetaData.Remove(DefaultMetadataProperties.ModifyDate);

// Tambahkan properti yang ditentukan pengguna
// Langkah #1: daftar awalan namespace dan URI
xmpMetaData.RegisterNamespaceURI("customNamespace", "http:// Www.customNameSpaces.com/ns/");
// Langkah #2: tambahkan properti pengguna dengan awalan
xmpMetaData.Add("customNamespace:UserPropertyName", "UserPropertyValue");

// Ubah properti yang ditentukan pengguna
xmpMetaData["customNamespace:UserPropertyName"] = "UserPropertyValue2";

// Simpan data meta xmp dalam file pdf
xmpMetaData.Save(dataDir+ "SetXMPMetadata_out.pdf");

// Tutup objek
xmpMetaData.Close();
```