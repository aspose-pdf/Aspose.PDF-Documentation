---
title: Bekerja dengan Portofolio dalam PDF
linktitle: Portofolio
type: docs
weight: 40
url: /cpp/portfolio/
description: Buat Portofolio PDF dengan Aspose.PDF untuk C++. Anda harus menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat Portofolio PDF.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cara Membuat Portofolio PDF

Aspose.PDF memungkinkan pembuatan dokumen Portofolio PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Tambahkan file ke dalam objek Document.Collection setelah mendapatkannya dengan kelas [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification). Ketika file telah ditambahkan, gunakan metode Save dari kelas Document untuk menyimpan dokumen portofolio.

Contoh berikut menggunakan File Microsoft Excel, dokumen Word, dan file gambar untuk membuat Portofolio PDF.

Kode di bawah ini menghasilkan portofolio berikut.

### Portofolio PDF yang dibuat dengan Aspose.PDF

![Portofolio PDF yang dibuat dengan Aspose.PDF untuk C++](working-with-pdf-portfolio_1.jpg)

```cpp
void WorkingWithAttachments::CreatePortfolio()
{
    String _dataDir("C:\\Samples\\");

    // Membuat objek Dokumen
    auto pdfDocument = MakeObject<Document>();

    // Membuat objek Koleksi dokumen
    pdfDocument->set_Collection(MakeObject<Collection>());

    // Dapatkan File untuk ditambahkan ke Portofolio
    auto excel = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.xlsx");
    auto word = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.docx");
    auto image = MakeObject<FileSpecification>(_dataDir + u"sample.jpg");

    // Berikan deskripsi file
    excel->set_Description(u"File Excel");
    word->set_Description(u"File Word");
    image->set_Description(u"File Gambar");

    // Tambahkan file ke koleksi dokumen
    pdfDocument->get_Collection()->Add(excel);
    pdfDocument->get_Collection()->Add(word);
    pdfDocument->get_Collection()->Add(image);

    // Simpan dokumen Portofolio
    pdfDocument->Save(_dataDir + u"PDFPortfolio.pdf");
}
```

## Ekstrak file dari Portofolio PDF

PDF Portfolios memungkinkan Anda untuk mengumpulkan konten dari berbagai sumber (misalnya, file PDF, Word, Excel, JPEG) ke dalam satu wadah yang terintegrasi. File asli mempertahankan identitas individual mereka tetapi disusun menjadi file PDF Portfolio. Pengguna dapat membuka, membaca, mengedit, dan memformat setiap file komponen secara independen dari file komponen lainnya.

Aspose.PDF memungkinkan pembuatan dokumen PDF Portfolio menggunakan kelas [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Ini juga menawarkan kemampuan untuk mengekstrak file dari portofolio PDF.

Cuplikan kode berikut menunjukkan langkah-langkah untuk mengekstrak file dari portofolio PDF.

```cpp
void WorkingWithAttachments::ExtractPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // Open a document
    auto pdfDocument = MakeObject <Document>(_dataDir + u"PDFPortfolio.pdf");
    // Get collection of embedded files
    auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

    // Iterate through individual file of Portfolio
    for (auto fileSpecification : embeddedFiles) {
    auto initialStream = fileSpecification->get_Contents();
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
    auto filename = System::IO::Path::GetFileName(fileSpecification->get_Name());
    // Save the extracted file to some location
    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"_out_" + filename);
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    // Close the stream object
    fileStream->Close();
    }
}
```

![Extract files from PDF Portfolio](working-with-pdf-portfolio_2.jpg)

## Hapus File dari PDF Portfolio

Untuk menghapus/menghilangkan file dari PDF portfolio, coba gunakan baris kode berikut.

```cpp
void WorkingWithAttachments::RemoveFilesFromPDFPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // Muat PDF Portfolio sumber
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PDFPortfolio.pdf");
    pdfDocument->get_Collection()->Delete();
    pdfDocument->Save(_dataDir + u"No_PortFolio_out.pdf");
}
```