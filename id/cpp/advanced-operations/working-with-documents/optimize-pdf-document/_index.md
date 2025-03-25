---
title: Optimize PDF menggunakan C++
linktitle: Optimize PDF
type: docs
weight: 30
url: /id/cpp/optimize-pdf/
description: Optimalkan file PDF, perkecil semua gambar, kurangi ukuran PDF, hapus penyematan font, aktifkan penggunaan ulang konten halaman, hapus atau ratakan anotasi dengan C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Pertama-tama, setiap optimasi PDF yang Anda lakukan adalah untuk pengguna. Dalam PDF, optimasi pengguna sebagian besar tentang mengurangi ukuran PDF Anda untuk meningkatkan kecepatan pemuatannya. Ini adalah tugas yang paling populer. Kita dapat menggunakan beberapa teknik untuk mengoptimalkan PDF, tetapi yang paling esensial:

- Optimalkan konten halaman untuk penjelajahan online
- Perkecil atau kompres semua gambar
- Aktifkan penggunaan ulang konten halaman
- Gabungkan aliran duplikat
- Hapus penyematan font
- Hapus objek yang tidak digunakan
- Hapus bidang formulir rata
- Hapus atau ratakan anotasi

## Optimalkan Dokumen PDF untuk Web

Ketika Anda dihadapkan dengan tugas mengoptimalkan konten dokumen PDF Anda untuk peringkat yang lebih baik di mesin pencari, Aspose.PDF untuk C++ memiliki solusi.

1. Buka dokumen input dalam objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Gunakan metode [Optimize](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a04d95824c334f5e543c13f69a19d9cda).
1. Simpan dokumen yang telah dioptimalkan menggunakan metode Save.

Cuplikan kode berikut menunjukkan cara mengoptimalkan dokumen PDF untuk web.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
//Optimalkan Dokumen PDF untuk Web
void OptimizeForWeb() {
    // String untuk nama path
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String outfilename("OptimizeDocument_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>();

    // Lakukan beberapa operasi (tambah halaman, gambar, dll)
    // ...

    // Optimalkan untuk web
    document->Optimize();

    // Simpan dokumen keluaran
    document->Save(_dataDir + outfilename);
}
```

## Kurangi Ukuran PDF

Metode [OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) memungkinkan Anda untuk mengurangi ukuran dokumen dengan menghapus informasi yang tidak diperlukan. Secara default, metode ini bekerja sebagai berikut:

- Sumber daya yang tidak digunakan pada halaman dokumen dihapus
- Sumber daya yang sama digabungkan menjadi satu objek
- Objek yang tidak digunakan dihapus

Cuplikan di bawah ini adalah contoh. Namun, perlu dicatat bahwa metode ini tidak dapat menjamin penyusutan dokumen.

```cpp
void ReduceSizePDF() {

    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String outfilename("ShrinkDocument_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>();
    // Lakukan beberapa operasi (tambahkan halaman, gambar, dll) 
    // ...

    // Optimalkan dokumen PDF. Namun, perlu dicatat bahwa metode ini tidak dapat menjamin penyusutan dokumen
    document->OptimizeResources();

    // Simpan dokumen keluaran
    document->Save(_dataDir + outfilename);
}
```

## Manajemen Strategi Optimalisasi

Kita juga dapat menyesuaikan strategi optimalisasi. Saat ini, metode [OptimizeResources()](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aea33aac69a42423efb82bcdb359f2ec6) menggunakan 5 teknik. Teknik-teknik ini dapat diterapkan menggunakan metode OptimizeResources() dengan parameter [OptimizationOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.optimization_options/).

### Mengecilkan atau Mengompresi Semua Gambar

Untuk mengoptimalkan gambar dalam dokumen PDF Anda, kami akan menggunakan [Aspose.Pdf.Optimization](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.optimization).
Untuk menyelesaikan masalah dengan optimasi gambar, kami memiliki opsi berikut: mengurangi kualitas gambar dan/atau mengubah resolusi mereka. Dalam hal apapun, [ImageCompressionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options/) harus diterapkan. Dalam contoh berikut, kami mengecilkan gambar dengan mengurangi [ImageQuality](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a92ee855b042a6b310984b4966ea7154e) menjadi 50.

```cpp
void CompressImage() {
    // String untuk nama path
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inisialisasi OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Setel opsi CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Setel opsi ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(50);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    document->OptimizeResources(optimizationOptions); 
    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outfilename);
}
```
Untuk mengatur gambar pada resolusi lebih rendah, atur [ResizeImages](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a0e5aad7e140ee380c09ebbb8a5238ff6) ke true dan [MaxResolution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#a05a4d1ace23ef074b3dc203cb213755e) ke nilai yang sesuai.

```cpp
void ResizeImagesWithLowerResolution() {
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inisialisasi OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Atur opsi CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Atur opsi ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // Atur opsi ResizeImage
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // Atur opsi MaxResolution
    optimizationOptions->get_ImageCompressionOptions()->set_MaxResolution(300);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    document->OptimizeResources(optimizationOptions);
    // Simpan dokumen yang telah diperbarui
    document->Save(_dataDir + outfilename);
}
```

Aspose.PDF untuk C++ juga menawarkan Anda kontrol atas pengaturan runtime. Saat ini, kita dapat menggunakan dua algoritma - Standar dan Cepat. Untuk mengontrol waktu eksekusi kita harus mengatur properti [Version](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.image_compression_options#aa2f1d93725ce56f8fabe692152bbf3a4).

Cuplikan berikut menunjukkan algoritma Cepat:

```cpp
void ResizeImagesWithLowerResolutionFast() {
    auto time = System::DateTime::get_Now().get_Ticks();
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String infilename("ResizeImage.pdf");
    String outfilename("ResizeImages_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inisialisasi OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Atur opsi CompressImages
    optimizationOptions->get_ImageCompressionOptions()->set_CompressImages(true);
    // Atur opsi ImageQuality
    optimizationOptions->get_ImageCompressionOptions()->set_ImageQuality(75);

    // Atur opsi ResizeImage
    optimizationOptions->get_ImageCompressionOptions()->set_ResizeImages(true);
    // Atur Versi Kompresi Gambar menjadi cepat
    optimizationOptions->get_ImageCompressionOptions()->set_Version (Aspose::Pdf::Optimization::ImageCompressionVersion::Fast);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    document->OptimizeResources(optimizationOptions);
    // Simpan dokumen yang telah diperbarui
    document->Save(_dataDir + outfilename);
    std::cout << "Ticks: " << System::DateTime::get_Now().get_Ticks() - time << std::endl;
}
```

### Menghapus Objek yang Tidak Digunakan

Terkadang Anda mungkin perlu menghapus beberapa objek yang tidak digunakan dari dokumen PDF Anda yang tidak direferensikan pada halaman. Ini mungkin terjadi, misalnya, ketika sebuah halaman dihapus dari pohon halaman dokumen tetapi objek halaman itu sendiri tidak dihapus. Menghapus objek-objek ini tidak membuat dokumen menjadi tidak valid tetapi justru memperkecilnya. Periksa cuplikan kode berikut:

```cpp
void RemovingUnusedObject() { 
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inisialisasi OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Atur opsi RemoveUsedObject
    optimizationOptions->set_RemoveUnusedObjects(true);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outfilename); 
}
```

### Menghapus Stream yang Tidak Digunakan

Terkadang dokumen berisi stream sumber daya yang tidak digunakan. Stream ini bukan "objek yang tidak digunakan" karena mereka direferensikan dari kamus sumber daya halaman. Oleh karena itu, mereka tidak dihapus dengan metode "menghapus objek yang tidak digunakan". Namun, stream ini tidak pernah digunakan dengan konten halaman. Hal ini dapat terjadi dalam kasus ketika sebuah gambar telah dihapus dari halaman tetapi tidak dari sumber daya halaman. Juga, situasi ini sering terjadi ketika halaman-halaman diekstraksi dari dokumen dan halaman-halaman dokumen memiliki sumber daya "umum", yaitu, objek Sumber Daya yang sama. Konten halaman dianalisis untuk menentukan apakah stream sumber daya digunakan atau tidak. Stream yang tidak digunakan dihapus. Terkadang ini mengurangi ukuran dokumen. Penggunaan teknik ini mirip dengan langkah sebelumnya:

```cpp
void RemovingUnusedStreams() { 
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>();

    // Inisialisasi OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Setel opsi RemoveUsedStreams
    optimizationOptions->set_RemoveUnusedStreams(true);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outfilename); 
}
```

### Menautkan Stream Duplikat

Beberapa dokumen dapat berisi beberapa stream sumber daya duplikat (seperti gambar, misalnya). Ini dapat terjadi, misalnya ketika sebuah dokumen digabung dengan dirinya sendiri. Dokumen keluaran berisi dua salinan independen dari stream sumber daya yang sama. Kami menganalisis semua stream sumber daya dan membandingkannya. Jika stream terduplikasi, mereka digabungkan, yaitu hanya satu salinan yang tersisa. Referensi diubah dengan tepat, dan salinan objek dihapus. Dalam beberapa kasus, ini membantu mengurangi ukuran dokumen.

```cpp
void LinkingDuplicateStreams() { 
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inisialisasi OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Setel opsi LinkDuplicateStreams
    optimizationOptions->set_LinkDuplcateStreams(true);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outfilename); 
}
```

Selain itu, kita dapat menggunakan pengaturan [AllowReusePageContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.optimization.optimization_options#aedaab36eaf8ed5059a2b1e11275bf6d8). Jika properti ini diatur ke true, konten halaman akan digunakan kembali saat mengoptimalkan dokumen untuk halaman yang identik.

```cpp
void AllowReusePageContent() { 
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Inisialisasi OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Atur opsi AllowReusePageContent
    optimizationOptions->set_AllowReusePageContent(true);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Simpan dokumen yang telah diperbarui
    document->Save(_dataDir + outfilename); 
}
```

### Melepas Sematan Font

Ketika Anda membuat versi PDF dari file desain pribadi Anda, salinan semua font yang diperlukan ditambahkan ke file PDF itu sendiri. Ini adalah penyematan. Terlepas dari di mana PDF ini dibuka, apakah itu di komputer Anda, komputer teman Anda, atau komputer penyedia cetak Anda, semua font yang benar akan ada dan akan ditampilkan dengan benar.

Namun, jika dokumen menggunakan font yang disematkan, itu berarti semua data font disimpan dalam dokumen. Keuntungannya adalah dokumen dapat dilihat terlepas dari apakah font diinstal pada mesin pengguna atau tidak. Tetapi penyematan font membuat dokumen menjadi lebih besar. Metode melepas sematan font menghapus semua font yang disematkan. Dengan demikian, ukuran dokumen berkurang tetapi dokumen itu sendiri mungkin menjadi tidak dapat dibaca jika font yang benar tidak diinstal.

```cpp
void UnembedFonts() {
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String infilename("ShrinkDocument.pdf");
    String outfilename("ShrinkDocument_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir+infilename);

    // Inisialisasi OptimizationOptions
    auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

    // Atur opsi AllowReusePageContent
    optimizationOptions->set_UnembedFonts(true);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    document->OptimizeResources(optimizationOptions);

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outfilename);
}
```

Sumber daya optimasi menerapkan metode-metode ini pada dokumen. Jika salah satu dari metode ini diterapkan, ukuran dokumen kemungkinan besar akan berkurang. Jika tidak ada metode ini yang diterapkan, ukuran dokumen tidak akan berubah, yang jelas.

## Cara Tambahan untuk Mengurangi Ukuran Dokumen PDF

### Menghapus atau Meratakan Anotasi

Kehadiran anotasi dalam dokumen PDF Anda secara alami meningkatkan ukurannya. Anotasi dapat dihapus ketika tidak diperlukan. Ketika diperlukan tetapi tidak memerlukan pengeditan tambahan, mereka dapat diratakan. Kedua teknik ini akan mengurangi ukuran file.

```cpp
void FlatteningAnnotation() {
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String infilename("OptimizeDocument.pdf");
    // String untuk nama file output
    String outfilename("OptimizeDocument_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Meratakan anotasi
    for(auto page : document->get_Pages())
    {
        for(auto annotation : page->get_Annotations())
        {
        annotation->Flatten();
        }
    }
    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outfilename);
}
```

### Menghapus Bidang Formulir

Menghapus formulir dari PDF Anda juga akan mengoptimalkan dokumen Anda. Jika dokumen PDF berisi AcroForms, kita dapat mencoba mengurangi ukuran file dengan meratakan bidang formulir.

```cpp
void FlatteningFormFields() {
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String infilename("OptimizeFormField.pdf");
    // String untuk nama file output
    String outfilename("OptimizeFormField_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Ratakan bidang formulir
    // Ratakan Formulir
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for(auto item : document->get_Form()->get_Fields())
        {
            item->Flatten();
        }
    }
    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + outfilename);
}
```

### Mengonversi PDF dari ruang warna RGB ke skala abu-abu

File PDF terdiri dari Teks, Gambar, Lampiran, Anotasi, Grafik, dan objek lainnya. Anda mungkin menemui persyaratan untuk mengonversi PDF dari ruang warna RGB ke skala abu-abu agar lebih cepat saat mencetak file PDF tersebut. Selain itu, ketika file dikonversi ke skala abu-abu, ukuran dokumen juga berkurang, tetapi ini juga dapat menyebabkan penurunan kualitas dokumen. Fitur ini saat ini didukung oleh fitur Pre-Flight dari Adobe Acrobat, tetapi ketika berbicara tentang otomatisasi Office, Aspose.PDF adalah solusi utama untuk memberikan kemudahan semacam itu untuk manipulasi dokumen. Untuk memenuhi persyaratan ini, cuplikan kode berikut dapat digunakan.

```cpp
void ConvertPDFfromColorspaceToGrayscale() {
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\");

    // String untuk nama file input
    String infilename("OptimizeDocument.pdf");
    // String untuk nama file output
    String outfilename("Test-gray_out.pdf");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto strategy = MakeObject<Aspose::Pdf::RgbToDeviceGrayConversionStrategy>();
    for (int idxPage = 1; idxPage <= document->get_Pages()->get_Count(); idxPage++)
    {
        // Dapatkan instance dari halaman tertentu dalam PDF
        auto page = document->get_Pages()->idx_get(idxPage);
        // Konversi gambar ruang warna RGB ke ruang warna GrayScale
        strategy->Convert(page);
    }
    // Simpan file hasil
    document->Save(_dataDir + outfilename); 
}
```
### FlateDecode Compression

Aspose.PDF untuk C++ menyediakan dukungan kompresi FlateDecode untuk fungsionalitas Optimasi PDF. Untuk mengoptimalkan gambar menggunakan Kompresi FlateDecode, atur opsi optimasi ke Flate. Cuplikan kode berikut menunjukkan cara menggunakan opsi dalam Optimasi untuk menyimpan gambar dengan kompresi **FlateDecode**:

```cpp
void FlatDecodeCompression() {
 // String untuk nama jalur
 String _dataDir("C:\\Samples\\");

 // String untuk nama file input
 String infilename("FlateDecodeCompression.pdf");
 // String untuk nama file output
 String outfilename("FlateDecodeCompression_out.pdf");

 // Buka dokumen
 auto document = MakeObject<Document>(_dataDir + infilename);

 // Inisialisasi OptimizationOptions
 auto optimizationOptions = MakeObject<Aspose::Pdf::Optimization::OptimizationOptions>();

 // Untuk mengoptimalkan gambar menggunakan Kompresi FlateDecode, atur opsi optimasi ke Flate
 optimizationOptions->get_ImageCompressionOptions()->set_Encoding(Aspose::Pdf::Optimization::ImageEncoding::Flate);

 // Optimalkan dokumen PDF menggunakan OptimizationOptions
 document->OptimizeResources(optimizationOptions);

 // Simpan dokumen yang diperbarui
 document->Save(_dataDir + outfilename);
}
```

### **Simpan Gambar di XImageCollection**

Aspose.PDF untuk C++ menyediakan kemampuan untuk menyimpan gambar baru ke dalam [XImageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.x_image_collection) dengan kompresi FlateDecode. Untuk mengaktifkan opsi ini, Anda dapat menggunakan flag **ImageFilterType.Flate**.
Cuplikan kode berikut menunjukkan cara menggunakan fungsionalitas ini:

```cpp
void StoreImageInXImageCollection() {

 // String untuk nama jalur
 String _dataDir("C:\\Samples\\");

 // String untuk nama file keluaran
 String outfilename("FlateDecodeCompression_out.pdf");

 // Buka dokumen
 auto document = MakeObject<Document>();
 
 auto page = document->get_Pages()->Add();
 
 auto imageStream = System::IO::File::OpenRead(_dataDir + u"aspose-logo.jpg");
 
 page->get_Resources()->get_Images()->Add(imageStream, Aspose::Pdf::ImageFilterType::Flate);
 
 auto ximage = page->get_Resources()->get_Images()->idx_get(page->get_Resources()->get_Images()->get_Count());

 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GSave>());

 // Atur koordinat
 int lowerLeftX = 0;
 int lowerLeftY = 0;
 int upperRightX = 600;
 int upperRightY = 600;
 
 auto rectangle = MakeObject<Rectangle>(lowerLeftX, lowerLeftY, upperRightX, upperRightY);

 auto matrix = MakeObject<Matrix>(new double[] {rectangle->get_URX() - rectangle->get_LLX(), 0, 0, rectangle->get_URY() - rectangle->get_LLY(), rectangle->get_LLX(), rectangle->get_LLY()});
 // Menggunakan operator ConcatenateMatrix (menggabungkan matriks): menentukan bagaimana gambar harus ditempatkan
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::ConcatenateMatrix>(matrix));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::Do>(ximage->get_Name()));
 page->get_Contents()->Add(MakeObject<Aspose::Pdf::Operators::GRestore>());

 document->Save(_dataDir + outfilename);
}
```