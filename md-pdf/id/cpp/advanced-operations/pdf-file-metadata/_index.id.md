---
title: Metadata File PDF
type: docs
weight: 20
url: /cpp/pdf-file-metadata/
---

## Mendapatkan/Mengatur Informasi File PDF

Untuk mendapatkan informasi khusus file dari file PDF, Anda perlu memanggil **get_Info()** dari kelas Document. Setelah objek DocumentInfo diambil, Anda dapat mendapatkan nilai dari masing-masing properti. Selanjutnya, Anda juga dapat mengatur properti dengan menggunakan metode yang sesuai dari kelas DocumentInfo. Cuplikan kode berikut menunjukkan, bagaimana cara mendapatkan/mengatur informasi File PDF menggunakan Aspose.PDF untuk C++:

{{% alert color="primary" %}}

Harap dicatat bahwa Anda tidak dapat mengatur nilai terhadap kolom **Application** dan **Producer**, karena Aspose Ltd. dan Aspose.PDF untuk C++ x.x.x akan ditampilkan terhadap kolom-kolom ini.

{{% /alert %}}

```cpp
void WorkingWithPDFMetadata::GetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // Buka dokumen
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetFileInfo.pdf");
    // Dapatkan informasi dokumen
    auto docInfo = pdfDocument->get_Info();
    // Tampilkan informasi dokumen
    Console::WriteLine(u"Author: {0}", docInfo->get_Author());
    Console::WriteLine(u"Creation Date: {0}", docInfo->get_CreationDate());
    Console::WriteLine(u"Keywords: {0}", docInfo->get_Keywords());
    Console::WriteLine(u"Modify Date: {0}", docInfo->get_ModDate());
    Console::WriteLine(u"Subject: {0}", docInfo->get_Subject());
    Console::WriteLine(u"Title: {0}", docInfo->get_Title());
}

void WorkingWithPDFMetadata::SetPDFFileInformation()
{
    String _dataDir("C:\\Samples\\");
    // Buka dokumen
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetFileInfo.pdf");

    // Tentukan informasi dokumen
    auto docInfo = MakeObject<DocumentInfo>(pdfDocument);

    docInfo->set_Author(u"Aspose");
    docInfo->set_CreationDate(DateTime::get_Now());
    docInfo->set_Keywords (u"Aspose.Pdf, DOM, API");
    docInfo->set_ModDate (DateTime::get_Now());
    docInfo->set_Subject (u"Informasi PDF");
    docInfo->set_Title (u"Mengatur Informasi Dokumen PDF");

    // Simpan dokumen keluaran
    pdfDocument->Save(_dataDir + u"SetFileInfo_out.pdf");
}
```

## Dapatkan/Atur Metadata XMP dari File PDF

Aspose.PDF untuk C++ memungkinkan Anda mengakses metadata XMP dari file PDF serta mengaturnya. Untuk mendapatkan/mengatur metadata file PDF:

1. Buat objek Dokumen dan buka file PDF input.
1. Dapatkan/atur metadata file menggunakan metode yang sesuai.

Cuplikan kode berikut menunjukkan cara mendapatkan/mengatur metadata dari file PDF.

```cpp
void WorkingWithPDFMetadata::GetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // Buka dokumen
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetXMPMetadata.pdf");

    // Dapatkan properti
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CreateDate"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:Nickname"));
    Console::WriteLine(pdfDocument->get_Metadata()->idx_get(u"xmp:CustomProperty"));
}

void WorkingWithPDFMetadata::SetXMPMetadata()
{
    String _dataDir("C:\\Samples\\");
    // Buka dokumen
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");

    // Atur properti
    pdfDocument->get_Metadata()->idx_set(u"xmp:CreateDate", MakeObject<XmpValue>(DateTime::get_Now()));
    pdfDocument->get_Metadata()->idx_set(u"xmp:Nickname", MakeObject<XmpValue>(u"Nickname"));
    pdfDocument->get_Metadata()->idx_set(u"xmp:CustomProperty", MakeObject<XmpValue>(u"Custom Value"));

    // Simpan dokumen
    pdfDocument->Save(_dataDir + u"SetXMPMetadata_out.pdf");
}

void WorkingWithPDFMetadata::InsertMetadataWithPrefix()
{
    String _dataDir("C:\\Samples\\");
    // Buka dokumen
    auto pdfDocument = MakeObject<Document>(_dataDir + u"SetXMPMetadata.pdf");
    pdfDocument->get_Metadata()->RegisterNamespaceUri(u"xmp", u"http:// Ns.adobe.com/xap/1.0/"); // xmlns prefix has been removed
    pdfDocument->get_Metadata()->idx_set(u"xmp:ModifyDate", MakeObject<XmpValue>(DateTime::get_Now()));

    // Simpan dokumen
    pdfDocument->Save(_dataDir + u"SetPrefixMetadata_out.pdf");
}
```