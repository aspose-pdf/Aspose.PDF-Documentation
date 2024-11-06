---
title: Ekstrak dan Simpan Lampiran
linktitle: Ekstrak dan Simpan Lampiran
type: docs
weight: 20
url: id/cpp/extract-and-save-an-attachment/
description: Aspose.PDF untuk C++ memungkinkan Anda untuk mendapatkan semua lampiran dari dokumen PDF. Juga, Anda dapat mendapatkan lampiran individual dari dokumen Anda.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dapatkan Semua Lampiran

Dengan Aspose.PDF, dimungkinkan untuk mendapatkan semua lampiran dari dokumen PDF. Ini berguna baik ketika Anda ingin menyimpan dokumen secara terpisah dari PDF, atau jika Anda perlu menghilangkan lampiran dari PDF.

Untuk mendapatkan semua lampiran dari file PDF:

1.
``` Loop melalui koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) dari objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) berisi semua lampiran. Setiap elemen dari koleksi ini mewakili objek [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification). Setiap iterasi dari loop foreach melalui koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) mengembalikan objek [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification).
1. Setelah objek tersedia, ambil semua properti file yang terlampir atau file itu sendiri.

Potongan kode berikut menunjukkan cara mendapatkan semua lampiran dari dokumen PDF.

```cpp
void WorkingWithAttachments::GetAllAttachments()
{
 String _dataDir("C:\\Samples\\");

 // Buka dokumen
 auto pdfDocument = new Document(_dataDir + u"GetAlltheAttachments.pdf");

 // Dapatkan koleksi file tertanam
 auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

 // Dapatkan jumlah file tertanam
 Console::WriteLine(u"Total files : {0}", embeddedFiles->get_Count());

 int count = 1;

 // Loop melalui koleksi untuk mendapatkan semua lampiran
 for (auto fileSpecification : embeddedFiles)
 {
  Console::WriteLine(u"Name: {0}", fileSpecification->get_Name());
  Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
  Console::WriteLine(u"Mime Type: {0}", fileSpecification->get_MIMEType());

  // Periksa apakah objek parameter berisi parameter
  if (fileSpecification->get_Params() != nullptr)
  {
   Console::WriteLine(u"CheckSum: {0}",
    fileSpecification->get_Params()->get_CheckSum());
   Console::WriteLine(u"Creation Date: {0}",
    fileSpecification->get_Params()->get_CreationDate());
   Console::WriteLine(u"Modification Date: {0}",
    fileSpecification->get_Params()->get_ModDate());
   Console::WriteLine(u"Size: {0}", fileSpecification->get_Params()->get_Size());
  }

  // Dapatkan lampiran dan tulis ke file atau stream
  auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
  fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
  auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test" + count + u"_out.txt");
  fileStream->Write(fileContent, 0, fileContent->get_Length());
  fileStream->Close();
  count += 1;
 }
}
```
## Mendapatkan Lampiran Individual

Untuk mendapatkan lampiran individual, kita dapat menentukan indeks lampiran pada objek `EmbeddedFiles` dari instance Dokumen. Silakan coba gunakan potongan kode berikut.

```cpp
void WorkingWithAttachments::GetIndividualAttachment() {
    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto pdfDocument = MakeObject<Document>(_dataDir + u"GetIndividualAttachment.pdf");

    // Dapatkan file tersemat tertentu
    auto fileSpecification = pdfDocument->get_EmbeddedFiles()->idx_get(1);

    // Dapatkan properti file
    Console::WriteLine(u"Name: {0}", fileSpecification->get_Name());
    Console::WriteLine(u"Description: {0}", fileSpecification->get_Description());
    Console::WriteLine(u"Mime Type: {0}", fileSpecification->get_MIMEType());

    // Periksa apakah objek parameter berisi parameter
    if (fileSpecification->get_Params() != nullptr)
    {
        Console::WriteLine(u"CheckSum: {0}",
        fileSpecification->get_Params()->get_CheckSum());
        Console::WriteLine(u"Creation Date: {0}",
        fileSpecification->get_Params()->get_CreationDate());
        Console::WriteLine(u"Modification Date: {0}",
        fileSpecification->get_Params()->get_ModDate());
        Console::WriteLine(u"Size: {0}",
        fileSpecification->get_Params()->get_Size());
    }


    // Dapatkan lampiran dan tulis ke file atau stream
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());

    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"test_out.txt");
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    fileStream->Close();

}
```