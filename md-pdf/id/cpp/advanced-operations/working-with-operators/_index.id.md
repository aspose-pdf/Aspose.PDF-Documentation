---
title: Bekerja dengan Operator menggunakan C++
linktitle: Bekerja dengan Operator
type: docs
weight: 170
url: /cpp/operators/
description: Topik ini menjelaskan cara menggunakan operator dengan Aspose.PDF dalam C++. Kelas operator menyediakan fitur hebat untuk manipulasi PDF.
lastmod: "2021-12-14"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Pengenalan Operator PDF dan Penggunaannya

Operator adalah kata kunci PDF yang menentukan beberapa tindakan yang harus dilakukan, seperti melukis bentuk grafis di halaman. Kata kunci operator dibedakan dari objek bernama dengan tidak adanya karakter solidus awal (2Fh). Operator hanya bermakna di dalam aliran konten.

Aliran konten adalah objek aliran PDF yang datanya terdiri dari instruksi yang menggambarkan elemen grafis yang akan dilukis di halaman. Detail lebih lanjut tentang operator PDF dapat ditemukan di [spesifikasi PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### Detail Implementasi

Topik ini menjelaskan cara menggunakan operator dengan Aspose.PDF. ```
Contoh yang dipilih menambahkan gambar ke dalam file PDF untuk menggambarkan konsep tersebut. Untuk menambahkan gambar dalam file PDF, diperlukan operator yang berbeda. Contoh ini menggunakan [GSave](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_save), [ConcatenateMatrix](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.concatenate_matrix), [Do](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.do), dan [GRestore](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.operators.g_restore).

- Operator **GSave** menyimpan status grafis PDF saat ini.
- Operator **ConcatenateMatrix** (menggabungkan matriks) digunakan untuk menentukan bagaimana gambar harus ditempatkan pada halaman PDF.
- Operator **Do** menggambar gambar pada halaman.
- Operator **GRestore** mengembalikan status grafis.

Untuk menambahkan gambar ke dalam file PDF:

1. Buat objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/) dan buka dokumen PDF input.
1.
``` Dapatkan halaman tertentu tempat gambar akan ditambahkan.
1. Tambahkan gambar ke koleksi Sumber Daya halaman.
1. Gunakan operator untuk meletakkan gambar di halaman:
   - Pertama, gunakan operator GSave untuk menyimpan keadaan grafis saat ini.
   - Kemudian gunakan operator ConcatenateMatrix untuk menentukan di mana gambar akan ditempatkan.
   - Gunakan operator Do untuk menggambar gambar di halaman.
1. Terakhir, gunakan operator GRestore untuk menyimpan keadaan grafis yang diperbarui.

Cuplikan kode berikut menunjukkan cara menggunakan operator PDF.

```cpp
void ExampleUsingOperators()
{
    // Buka dokumen
    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + u"PDFOperators.pdf");

    // Tetapkan koordinat
    int lowerLeftX = 100;
    int lowerLeftY = 100;
    int upperRightX = 200;
    int upperRightY = 200;

    // Dapatkan halaman tempat gambar perlu ditambahkan
    auto page = document->get_Pages()->idx_get(1);

    // Muat gambar ke dalam stream
    auto imageStream = System::IO::File::OpenRead(_dataDir + u"PDFOperators.jpg");
    // Tambahkan gambar ke koleksi Gambar dari Sumber Daya Halaman
    page->get_Resources()->get_Images()->Add(imageStream);

    // Menggunakan operator GSave: operator ini menyimpan keadaan grafis saat ini
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Buat objek Rectangle dan Matrix
    auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
    auto matrix = MakeObject<Matrix>(
        new double[] {
            rectangle->get_URX() - rectangle->get_LLX(), 0, 0,
            rectangle->get_URY() - rectangle->get_LLY(),
            rectangle->get_LLX(),  rectangle->get_LLY() });
    // Menggunakan operator ConcatenateMatrix (menggabungkan matriks): mendefinisikan bagaimana gambar harus ditempatkan
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
    auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());
    // Menggunakan operator Do: operator ini menggambar gambar
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    // Menggunakan operator GRestore: operator ini mengembalikan keadaan grafis
    page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());


    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + u"PDFOperators_out.pdf");
}
```
## Menggambar XForm pada Halaman menggunakan Operator

Topik ini menunjukkan cara menggunakan operator GSave/GRestore, operator ContatenateMatrix untuk memposisikan xForm dan operator Do untuk menggambar xForm pada halaman.

Kode di bawah ini membungkus konten yang ada dari file PDF dengan pasangan operator GSave/GRestore. Pendekatan ini membantu mendapatkan keadaan grafis awal di akhir konten yang ada. Tanpa pendekatan ini, transformasi yang tidak diinginkan mungkin tetap ada di akhir rantai operator yang ada.

```cpp
void DrawXFormOnPageUsingOperators() {
    // Buka dokumen
    String _dataDir("C:\\Samples\\");

    String imageFile(_dataDir + u"aspose-logo.jpg");
    String inFile(_dataDir + u"DrawXFormOnPage.pdf");
    String outFile(_dataDir + u"blank-sample2_out.pdf");

    auto document = MakeObject<Document>(inFile);
    auto pageContents = document->get_Pages()->idx_get(1)->get_Contents();

    // Contoh ini menunjukkan
    // penggunaan operator GSave/GRestore
    // penggunaan operator ContatenateMatrix untuk memposisikan xForm
    // penggunaan operator Do untuk menggambar xForm pada halaman

    // Bungkus konten yang ada dengan pasangan operator GSave/GRestore
    // ini untuk mendapatkan keadaan grafis awal di akhir konten yang ada
    // jika tidak, mungkin ada beberapa transformasi yang tidak diinginkan di akhir rantai operator yang ada
    pageContents->Insert(1, MakeObject<Aspose::Pdf::Operators::GSave>());
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Tambahkan operator simpan keadaan grafis untuk membersihkan keadaan grafis dengan benar setelah perintah baru
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

    // Buat xForm

    auto form = XForm::CreateNewForm(document->get_Pages()->idx_get(1), document);
    document->get_Pages()->idx_get(1)->get_Resources()->get_Forms()->Add(form);
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Tentukan lebar dan tinggi gambar
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(200, 0, 0, 200, 0, 0));
    // Muat gambar ke dalam stream
    auto imageStream = System::IO::File::OpenRead(imageFile);
    // Tambahkan gambar ke koleksi Images dari XForm Resources
    form->get_Resources()->get_Images()->Add(imageStream);
    auto ximage = form->get_Resources()->get_Images()->idx_get(form->get_Resources()->get_Images()->get_Count());
    // Menggunakan operator Do: operator ini menggambar gambar
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
    form->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // ----------------------------------------------------

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Tempatkan form ke koordinat x=100 y=500
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 500));
    // Gambar form dengan operator Do
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GSave>());
    // Tempatkan form ke koordinat x=100 y=300
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(1, 0, 0, 1, 100, 300));
    // Gambar form dengan operator Do
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::Do>(form->get_Name()));
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

    // Pulihkan keadaan grafis dengan GRestore setelah GSave
    pageContents->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());
    document->Save(outFile);
}
```

## Menghapus Objek Grafis menggunakan Kelas Operator

Kelas operator menyediakan fitur hebat untuk manipulasi PDF. Ketika file PDF berisi grafis yang tidak dapat dihapus menggunakan metode [DeleteImage](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor#af7d23ef932737bf606f008ad5ec48380) dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_content_editor), kelas operator dapat digunakan untuk menghapusnya sebagai gantinya.

Cuplikan kode berikut menunjukkan cara menghapus grafis. Harap dicatat bahwa jika file PDF berisi label teks untuk grafis, mereka mungkin tetap ada dalam file PDF, menggunakan pendekatan ini. Oleh karena itu, cari operator grafis untuk metode alternatif untuk menghapus gambar semacam itu.

```cpp
void RemoveGraphicsObjects() {
    // Buka dokumen
    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + u"RemoveGraphicsObjects.pdf");

    auto page = document->get_Pages()->idx_get(2);
    auto oc = page->get_Contents();

    // Operator path-painting yang digunakan
    auto operators = MakeArray<System::SmartPtr<Operator>>({
            MakeObject<Aspose::Pdf::Operators::Stroke>(),
            MakeObject<Aspose::Pdf::Operators::ClosePathStroke>(),
            MakeObject<Aspose::Pdf::Operators::Fill>()
    });

    oc->Delete(operators);
    document->Save(_dataDir + u"No_Graphics_out.pdf");
}
```