---
title:  Ekstrak data dari AcroForm 
linktitle:  Ekstrak data dari AcroForm
type: docs
weight: 50
url: /id/cpp/extract-data-from-acroform/
description: Aspose.PDF memudahkan ekstraksi data bidang formulir dari file PDF. Pelajari cara mengekstrak data dari AcroForms dan menyimpannya dalam format XML, atau FDF.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak bidang formulir dari dokumen PDF

Aspose.PDF untuk C++ memungkinkan Anda tidak hanya membuat bidang formulir dan mengisi bidang formulir tetapi juga memudahkan untuk mengekstrak data bidang formulir atau informasi bidang formulir dari file PDF.

Dalam contoh kode di bawah ini, kami menunjukkan cara mengiterasi setiap halaman dalam PDF untuk mengekstrak informasi tentang semua AcroForms dalam PDF serta nilai bidang formulir. Contoh kode ini mengasumsikan bahwa Anda tidak mengetahui nama-nama bidang formulir sebelumnya.

```cpp
void ExtractFormFields() {
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("StudentInfoFormElectronic.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Dapatkan nilai dari semua bidang
    for (auto formField : document->get_Form()->get_Fields()) {
        std::cout << "Nama Bidang :" << formField->get_PartialName() << std::endl;
        std::cout << "Nilai : " << formField->get_Value() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Ekstrak Data ke XML dari File PDF

Kelas [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) memungkinkan Anda untuk mengekspor data ke file XML dari file PDF menggunakan metode ExportXml. Untuk mengekspor data ke XML, Anda perlu membuat objek dari kelas Form dan kemudian memanggil metode ExportXml menggunakan objek FileStream. Selanjutnya Anda harus menutup objek FileStream dan membuang objek Form.

Cuplikan kode berikut menunjukkan bagaimana mengekspor data ke file XML.

```cpp
void ExtractFormFieldsToXML() {
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String xmlFileName(_dataDir + u"StudentInfoFormElectronic.xml");

    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);
    auto fdfOutputStream = System::IO::File::OpenWrite(xmlFileName);

    // Ekspor data
    form->ExportXml(fdfOutputStream);

    // Tutup aliran file
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Mengekspor Data ke FDF dari File PDF

Kelas [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) memungkinkan Anda untuk mengekspor data ke file FDF dari file PDF menggunakan metode ExportFdf. Untuk mengekspor data ke FDF, Anda perlu membuat objek dari kelas Form dan kemudian memanggil metode ExportFdf menggunakan objek FileStream. Setelah itu, Anda dapat menyimpan file PDF menggunakan metode Save dari kelas Form.

Cuplikan kode berikut menunjukkan kepada Anda cara mengekspor data ke file FDF.

```cpp
void ExtractFormExportFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String fdfFileName(_dataDir+ u"StudentInfoFormElectronic.fdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // Ekspor data
    form->ExportFdf(fdfOutputStream);

    // Tutup file stream
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Ekspor Data ke XFDF dari File PDF

Aspose PDF untuk C++ dengan kelas [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) memungkinkan Anda untuk mengekspor data ke file XFDF dari file PDF menggunakan metode ExportXfdf. Untuk mengekspor data ke XFDF, Anda perlu membuat objek dari kelas Form dan kemudian memanggil metode ExportXfdf menggunakan objek FileStream.

Pada akhirnya, Anda dapat menyimpan file PDF menggunakan metode Save dari kelas Form.

Cuplikan kode berikut menunjukkan cara mengekspor data ke file XFDF.

```cpp
void ExtractFormExportXFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("StudentInfoFormElectronic.pdf");
    String fdfFileName("StudentInfoFormElectronic.xfdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // Ekspor data
    form->ExportXfdf(fdfOutputStream);

    // Tutup file stream
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```