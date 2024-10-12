---
title: Bekerja dengan Dokumen PDF di Qt
type: docs
weight: 130
url: /cpp/work-with-pdf-documents-in-qt/
lastmod: "2021-11-01"
---

Qt adalah kerangka kerja pengembangan aplikasi lintas platform yang memungkinkan pembuatan berbagai aplikasi desktop, seluler, web, dan sistem tertanam. Dalam artikel ini, kita akan melihat bagaimana Anda dapat mengintegrasikan perpustakaan PDF C++ kami untuk bekerja dengan dokumen PDF dalam aplikasi Qt Anda.

## Menggunakan Aspose.PDF untuk C++ dalam Qt

Untuk menggunakan Aspose.PDF untuk C++ dalam aplikasi Qt Anda pada Sistem Operasi Windows, unduh versi terbaru API dari bagian [downloads](https://downloads.aspose.com/pdf/cpp). Setelah API diunduh, Anda dapat menggunakan salah satu dari opsi berikut untuk menggunakannya dengan Qt.

- Menggunakan Qt Creator
- Menggunakan Visual Studio

Di sini, kami akan mendemonstrasikan cara mengintegrasikan dan menggunakan Aspose.PDF untuk C++ dalam aplikasi konsol Qt menggunakan Qt Creator.

### Membuat Aplikasi Konsol Qt

{{% alert color="primary" %}}

Artikel ini mengasumsikan bahwa Anda telah menginstal lingkungan pengembangan Qt dan Qt Creator dengan benar.

{{% /alert %}}

- Buka Qt Creator dan buat *Qt Console Application* baru.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application.jpg)

- Pilih opsi QMake dari dropdown *Build System*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Qt-Console-Application-QMake.jpg)

- Pilih kit yang sesuai dan selesaikan wizard.

Pada titik ini, Anda seharusnya memiliki Aplikasi Konsol Qt yang dapat dieksekusi dan seharusnya dapat dikompilasi tanpa masalah.

### Integrasikan Aspose.PDF untuk C++ API dengan Qt

- Ekstrak arsip Aspose.PDF untuk C++ yang telah Anda unduh sebelumnya
- Salin folder *Aspose.Pdf.Cpp* dan *CodePorting.Native.Cs2Cpp_vc14_20.4* dari paket yang diekstrak dari Aspose.PDF untuk C++ ke dalam root proyek. Proyek Anda harus terlihat seperti yang ditunjukkan pada gambar berikut.

![todo:image_alt_text](work-with-pdf-documents-in-qt_1.png)

- Untuk menambahkan jalur ke folder lib dan include, klik kanan pada proyek di panel LHS dan pilih *Add Library*.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library.jpg)

- Pilih opsi Pustaka Eksternal dan telusuri jalur untuk menyertakan dan folder lib satu per satu.

![todo:image_alt_text](https://blog.aspose.com/wp-content/uploads/sites/2/2020/04/Add-Word-Library-2.jpg)

- Setelah selesai, file proyek .pro Anda akan berisi entri berikut:

![todo:image_alt_text](work-with-pdf-documents-in-qt_2.png)

- Bangun aplikasi dan Anda selesai dengan integrasi.

### Buat Dokumen PDF di Qt

Sekarang Aspose.PDF untuk C++ telah diintegrasikan dengan Qt, kita siap untuk membuat dokumen PDF dengan beberapa teks dan menyimpannya ke disk. Untuk melakukan ini:

- Sertakan header berikut dalam main.cpp

```cpp

    #include "Aspose.PDF.Cpp/Document.h"
    #include "Aspose.PDF.Cpp/Page_.h"
    #include "Aspose.PDF.Cpp/PageCollection.h"
    #include "Aspose.PDF.Cpp/Generator/Paragraphs.h"
    #include "Aspose.PDF.Cpp/Text/TextFragment.h"
```

- Masukkan kode berikut dalam fungsi utama untuk menghasilkan dokumen PDF dan menyimpannya ke disk

```cpp

    using namespace System;
    using namespace Aspose::Pdf;
    using namespace Aspose::Pdf::Text;
    
    QString text = "Halo Dunia";
    auto doc = MakeObject<Document>();

    auto pages = doc->get_Pages();

    pages->Add();

    auto page = pages->idx_get(1);

    auto paragraps = page->get_Paragraphs();

    paragraps->Add(MakeObject<TextFragment>(text.toStdU16String().c_str()));

    doc->Save(file_name.toStdU16String().c_str());
```