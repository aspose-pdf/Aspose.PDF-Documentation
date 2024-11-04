title: Tambahkan Anotasi Gambar menggunakan C++
linktitle: Anotasi Gambar
type: docs
weight: 30
url: /cpp/figures-annotation/
description: Artikel ini menjelaskan cara menambahkan, mendapatkan, dan menghapus anotasi gambar dari dokumen PDF Anda dengan Aspose.PDF untuk C++
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Anotasi Kotak atau Lingkaran

Anotasi Kotak dan Lingkaran akan menampilkan, masing-masing, sebuah persegi panjang atau elips pada halaman. Ketika dibuka, mereka akan menampilkan jendela pop-up yang berisi teks dari catatan terkait.
Anotasi Kotak mirip dengan anotasi Lingkaran (instans dari kelas Aspose.Pdf.Annotations.CircleAnnotation) kecuali bentuknya.

Langkah-langkah untuk membuat Anotasi Kotak dan Lingkaran:

1. Muat file PDF - baru [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1.
``` Buat [Circle Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.circle_annotation) dan atur parameter Circle (Rectangle baru, judul, warna, InteriorColor, Opacity).
1. Buat [PopupAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.popup_annotation) baru.
1. Selanjutnya kita perlu membuat [Square Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.square_annotation).
1. Atur parameter Square yang sama (Rectangle baru, judul, warna, InteriorColor, Opacity).
1. Setelah itu kita perlu Menambahkan Square dan Circle Annotations ke halaman.

Cuplikan kode berikut menunjukkan kepada Anda bagaimana menambahkan Circle Annotations dalam halaman PDF.

```cpp
void ShapesAnnotations::AddCircleAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"appartments.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Buat Circle Annotation
    auto circleAnnotation = MakeObject<CircleAnnotation>(page, MakeObject<Rectangle>(270, 160, 483, 383));
    circleAnnotation->set_Title(u"John Smith");
    circleAnnotation->set_Color(Color::get_Red());
    circleAnnotation->set_InteriorColor(Color::get_MistyRose());
    circleAnnotation->set_Opacity(0.5);
    circleAnnotation->set_Popup(MakeObject<PopupAnnotation>(page, MakeObject<Rectangle>(842, 316, 1021, 459)));

    // Buat Square Annotation
    auto squareAnnotation = MakeObject<SquareAnnotation>(page, MakeObject<Rectangle>(67, 317, 261, 459));
    squareAnnotation->set_Title(u"John Smith");
    squareAnnotation->set_Color(Color::get_Blue());
    squareAnnotation->set_InteriorColor(Color::get_BlueViolet());
    squareAnnotation->set_Opacity(0.25);
    squareAnnotation->set_Popup(MakeObject<PopupAnnotation>(page, MakeObject<Rectangle>(842, 196, 1021, 338)));

    // Tambahkan anotasi ke halaman
    page->get_Annotations()->Add(circleAnnotation);
    page->get_Annotations()->Add(squareAnnotation);
    document->Save(_dataDir + u"appartments_mod.pdf");
}
```
Sebagai contoh, kita akan melihat hasil berikut dari menambahkan anotasi Kotak dan Lingkaran ke dokumen PDF:

![Demo Anotasi Lingkaran dan Kotak](circle_demo.png)

### Dapatkan Anotasi Lingkaran

Silakan coba menggunakan potongan kode berikut untuk Mendapatkan Anotasi Lingkaran dari dokumen PDF.

```cpp
void ShapesAnnotations::GetCircleAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Memuat file PDF
    auto document = MakeObject<Document>(_dataDir + u"appartments_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        new CircleAnnotation(page, Rectangle::get_Trivial()));

    page->Accept(annotationSelector);
    auto circleAnnotations = annotationSelector->get_Selected();

    // cetak hasil
    for (auto ca : circleAnnotations) {
        Console::WriteLine(ca->get_Rect());
    }
}
```

### Hapus Anotasi Lingkaran

Potongan kode berikut menunjukkan cara Menghapus Anotasi Lingkaran dari file PDF.

```cpp
void ShapesAnnotations::DeleteCircleAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Memuat file PDF
    auto document = MakeObject<Document>(_dataDir + u"appartments_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        new CircleAnnotation(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);

    auto circleAnnotations = annotationSelector->get_Selected();

    for (auto ca : circleAnnotations) {
        page->get_Annotations()->Delete(ca);
    }
    document->Save(_dataDir + u"appartments_del.pdf");
}
```

## Tambahkan Anotasi Polygon dan Polyline

Alat Polyline memungkinkan Anda membuat bentuk dan garis dengan jumlah sisi yang sembarang pada dokumen.

**Anotasi Polygon** mewakili poligon pada halaman. Mereka dapat memiliki sejumlah titik sudut yang dihubungkan oleh garis lurus.

**Anotasi Polyline** juga mirip dengan poligon, perbedaannya adalah titik sudut pertama dan terakhir tidak terhubung secara implisit.

Langkah-langkah untuk membuat anotasi Polygon dan Polyline:

1. Muat file PDF - [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) baru.
1. Buat [Polygon Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.polygon_annotation) baru dan atur parameter Polygon (Rectangle baru, Points baru, judul, warna, InteriorColor dan Opacity).
1. Buat [PopupAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.popup_annotation) baru.
1. Berikutnya, Buat [PoliLine Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.polyline_annotation) dan ulangi semua tindakan.
1. Setelah itu kita bisa menambahkan anotasi ke halaman.

Cuplikan kode berikut menunjukkan cara menambahkan Anotasi Poligon dan Poliline ke file PDF:

```cpp
void ShapesAnnotations::AddPolygonAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"appartments.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Buat Anotasi Poligon
    auto points = MakeArray<System::SharedPtr<Point>>({
                 MakeObject<Point>(274, 381),
                 MakeObject<Point>(555, 381),
                 MakeObject<Point>(555, 304),
                 MakeObject<Point>(570, 304),
                 MakeObject<Point>(570, 195),
                 MakeObject<Point>(274, 195) });
    auto polygonAnnotation =
        MakeObject<PolygonAnnotation>(page,
        MakeObject<Rectangle>(270, 193, 571, 383),
        points);

    polygonAnnotation->set_Title(u"John Smith");
    polygonAnnotation->set_Color(Color::get_Blue());
    polygonAnnotation->set_InteriorColor(Color::get_BlueViolet());
    polygonAnnotation->set_Opacity(0.25);
    polygonAnnotation->set_Popup(MakeObject<PopupAnnotation>(page, MakeObject<Rectangle>(842, 196, 1021, 338)));

    // Buat Anotasi PoliLine
    auto polylineAnnotation = MakeObject<PolylineAnnotation>(page, MakeObject<Rectangle>(270, 193, 571, 383),
        MakeArray<System::SharedPtr<Point>>({
        MakeObject<Point>(545, 150),
        MakeObject<Point>(545, 190),
        MakeObject<Point>(667, 190),
        MakeObject<Point>(667, 110),
        MakeObject<Point>(626, 111)}));

    polygonAnnotation->set_Title(u"John Smith");
    polygonAnnotation->set_Color(Color::get_Red());
    polygonAnnotation->set_Popup(MakeObject<PopupAnnotation>(page, MakeObject<Rectangle>(842, 196, 1021, 338)));

    // Tambahkan anotasi ke halaman
    page->get_Annotations()->Add(polygonAnnotation);
    page->get_Annotations()->Add(polylineAnnotation);
    document->Save(_dataDir + u"appartments_mod.pdf");
}
```
### Dapatkan Anotasi Poligon dan Garis Poligon

Silakan coba gunakan cuplikan kode berikut untuk Mendapatkan Anotasi Poligon dan Garis Poligon dalam dokumen PDF.

```cpp
void ShapesAnnotations::GetPolyAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"appartments_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<PolylineAnnotation>(page, Rectangle::get_Trivial(), nullptr));
    page->Accept(annotationSelector);
    auto polyAnnotations = annotationSelector->get_Selected();

    for (auto pa : polyAnnotations) {
    Console::WriteLine(u"{0}", pa->get_Rect());
    }
}
```

### Hapus Anotasi Poligon dan Garis Poligon

Cuplikan kode berikut menunjukkan cara Menghapus Anotasi Poligon dan Garis Poligon dari file PDF.

```cpp
void ShapesAnnotations::DeletePolyAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"appartments_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        new PolylineAnnotation(page, Rectangle::get_Trivial(), nullptr));
    page->Accept(annotationSelector);
    auto polyAnnotations = annotationSelector->get_Selected();

    for (auto pa : polyAnnotations) {
        page->get_Annotations()->Delete(pa);
    }

    document->Save(_dataDir + u"Appartments_del.pdf");
}
```

## Cara Menambahkan Anotasi Garis ke dalam File PDF yang Ada

Tujuan dari Anotasi Garis adalah untuk menampilkan satu garis lurus pada halaman. Ketika dibuka, akan menampilkan jendela pop-up yang berisi teks dari catatan terkait.
Fitur ini memiliki entri tambahan khusus untuk anotasi garis. Entri-entri ini dienkripsi dalam bentuk huruf, misalnya, LL, BS, IC, dan sebagainya.

Selain itu, Anotasi Garis dapat menyertakan keterangan pada anotasi garis, yang ditentukan dengan mengatur Cap ke `true`.
Fitur berikutnya memungkinkan efek penerapan keterangan pada Anotasi Garis yang memiliki offset pemimpin.
Juga, jenis anotasi ini memungkinkan Anda untuk menentukan gaya akhir Garis.

Langkah-langkah untuk membuat anotasi Garis:

1. Muat file PDF - baru [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Buat [Line Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.line_annotation) baru dan atur parameter Garis (Rectangle baru, Point baru, judul, warna, lebar, StartingStyle dan EndingStyle).
1. Buat [PopupAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.popup_annotation) baru
1. Setelah itu kita bisa menambahkan anotasi ke halaman

Cuplikan kode berikut menunjukkan cara menambahkan Line Annotation ke file PDF:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLineAnnotation() {
    String _dataDir ("C:\\Samples\\");
    try {
        // Muat file PDF
        auto document = MakeObject<Document>(_dataDir + u"appartments.pdf");
        auto page = document->get_Pages()->idx_get(1);

        // Buat Line Annotation
        auto lineAnnotation = MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(
        page, new Rectangle(550, 93, 562, 439),
        new Point(556, 99), new Point(556, 443));

        lineAnnotation->set_Title(u"John Smith");
        lineAnnotation->set_Color(Color::get_Red());
        lineAnnotation->set_Width(3);
        lineAnnotation->set_StartingStyle(Aspose::Pdf::Annotations::LineEnding::OpenArrow);
        lineAnnotation->set_EndingStyle(Aspose::Pdf::Annotations::LineEnding::OpenArrow);
        lineAnnotation->set_Popup(MakeObject<Aspose::Pdf::Annotations::PopupAnnotation>(page, new Rectangle(842, 124, 1021, 266)));

        // Tambahkan anotasi ke halaman
        page->get_Annotations()->Add(lineAnnotation);
        document->Save(_dataDir + u"appartments_mod.pdf");
    }
    catch (Exception ex) {
        Console::WriteLine(ex->get_Message());
    }
}
```
### Dapatkan Anotasi Garis

Silakan coba menggunakan cuplikan kode berikut untuk Mendapatkan Anotasi Garis dalam dokumen PDF.

```cpp
void GetLineAnnotation() {
    String _dataDir("C:\\Samples\\");
    // Memuat file PDF
    auto document = MakeObject<Document>(_dataDir + u"appartments_mod.pdf");

    // Memfilter anotasi menggunakan AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto lineAnnotations = annotationSelector->get_Selected();

    // mencetak hasil
    for (auto la : lineAnnotations) {
        auto l = System::DynamicCast<Aspose::Pdf::Annotations::LineAnnotation>(la);
        Console::WriteLine(u"[{0},{1}] [{2},{3}]",
            l->get_Starting()->get_X(),l->get_Starting()->get_Y(),
            l->get_Ending()->get_X(), l->get_Ending()->get_Y());
    }
    }
```

### Hapus Anotasi Garis

Cuplikan kode berikut menunjukkan cara Menghapus Anotasi Garis dari file PDF.

```cpp
void DeleteLineAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Memuat file PDF
    auto document = MakeObject<Document>(_dataDir + u"appartments_mod.pdf");

    // Memfilter anotasi menggunakan AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto lineAnnotations = annotationSelector->get_Selected();

    // mencetak hasil
    for (auto la : lineAnnotations) {
        page->get_Annotations()->Delete(la);
    }
    document->Save(_dataDir + u"appartments_del.pdf");
}
```

## Cara menambahkan Anotasi Tinta ke file PDF

Anotasi Tinta mewakili "coretan" bebas yang terdiri dari satu atau lebih jalur terpisah. Ketika dibuka, itu akan menampilkan jendela pop-up yang berisi teks dari catatan terkait.

[InkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.ink_annotation) mewakili coretan tangan bebas yang terdiri dari satu atau lebih titik yang tidak terhubung. Silakan coba gunakan potongan kode berikut untuk menambahkan InkAnnotation dalam dokumen PDF.

```cpp
void ShapesAnnotations::AddInkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"appartments.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto arect = MakeObject<Rectangle>(320.086, 189.286, 384.75, 228.927);
    auto inkList = MakeObject<System::Collections::Generic::List<System::SmartPtr<System::Array<System::SmartPtr<Aspose::Pdf::Point>>>>>();

    //data dalam ppts, diterima dari mouse atau perangkat penunjuk lainnya
    double ppts[] = { 328.002, 222.017, 328.648, 222.017, 329.294, 222.017, 329.617, 222.34, 330.91, 222.663,
            331.556, 222.663, 332.203, 222.986, 333.495, 223.633, 334.141, 223.956, 334.788, 224.279, 335.434,
            224.602, 336.08, 224.602, 336.727, 224.925, 337.373, 225.248, 337.696, 225.248, 338.342, 225.572,
            338.989, 225.895, 341.897, 225.895, 343.513, 226.218, 346.098, 226.218, 348.683, 226.541, 350.622,
            226.541, 352.238, 226.541, 353.208, 226.541, 353.854, 226.541, 355.146, 226.541, 356.439, 226.541,
            357.732, 226.541, 358.378, 226.541, 359.024, 226.541, 360.64, 226.541, 361.286, 226.541, 361.933,
            226.541, 362.256, 226.541, 362.902, 226.541, 363.548, 226.541, 363.872, 226.541, 363.872, 226.218,
            365.164, 226.218, 365.487, 226.218, 365.811, 226.218, 367.103, 226.218, 367.749, 226.218, 368.719,
            226.218, 370.012, 226.218, 370.981, 226.218, 371.627, 226.218, 372.597, 225.895, 372.92, 225.895,
            373.243, 225.895, 373.243, 225.572, 373.566, 225.572, 374.213, 225.248, 374.536, 225.248, 375.182,
            224.602, 375.182, 224.279, 375.828, 223.956, 376.475, 223.31, 377.121, 222.986, 377.767, 222.986,
            378.414, 222.017, 379.383, 221.371, 379.706, 220.724, 380.029, 219.432, 380.676, 219.109, 380.676,
            218.462, 381.645, 217.493, 381.968, 217.17, 381.968, 216.523, 382.291, 215.554, 382.615, 215.231,
            382.615, 214.261, 382.938, 213.292, 382.938, 212.645, 382.938, 211.999, 382.938, 211.353, 382.938,
            210.707, 382.938, 209.737, 382.938, 208.768, 382.938, 208.444, 382.615, 207.475, 382.615, 206.829,
            382.291, 206.505, 382.291, 205.859, 381.968, 204.89, 381.968, 204.243, 381.645, 203.92, 380.999,
            203.274, 380.999, 202.951, 380.676, 202.305, 380.353, 201.658, 380.029, 201.335, 380.029, 200.689,
            380.029, 200.366, 379.383, 199.719, 379.06, 199.719, 378.737, 199.073, 377.767, 198.103, 377.121,
            197.780, 376.475, 197.457, 375.505, 196.488, 374.859, 196.165, 374.536, 195.841, 372.92, 195.195,
            371.951, 194.549, 370.658, 194.226, 368.719, 193.902, 367.426, 193.256, 366.457, 193.256, 363.872,
            192.933, 362.902, 192.933, 361.61, 192.61, 359.024, 192.61, 357.409, 192.61, 356.439, 192.61,
            353.531, 192.61, 352.561, 192.61, 350.945, 192.61, 349.007, 192.933, 348.36, 193.256, 347.391,
            193.256, 346.098, 193.902, 345.452, 193.902, 344.806, 193.902, 343.513, 193.902, 342.867, 193.902,
            342.220, 193.902, 341.574, 193.902, 341.251, 194.226, 340.928, 194.226, 340.928, 194.549, 340.605,
            194.549, 340.605, 194.872, 339.635, 195.195, 339.635, 195.518, 338.989, 195.518, 338.989, 195.841,
            338.666, 196.165, 338.019, 196.811, 338.019, 197.134, 337.373, 197.457, 336.404, 198.427, 335.757,
            198.427, 335.434, 198.75, 334.141, 199.719, 333.818, 199.719, 333.818, 200.042, 332.849, 200.366,
            332.203, 200.366, 331.556, 201.335, 330.91, 201.981, 330.587, 202.305, 330.264, 202.305, 329.294,
            202.628, 328.971, 202.951, 328.002, 203.274, 328.002, 203.597, 327.355, 204.243, 326.709, 204.567,
            326.386, 204.89, 326.063, 205.536, 325.416, 205.859, 325.093, 205.859, 324.447, 205.859, 324.124,
            206.182, 324.124, 206.505, 323.477, 206.829, 323.477, 207.152, 323.477, 207.798, 322.831, 207.798,
            322.831, 208.121, 322.831, 208.444, 322.508, 208.444, 322.508, 209.091, 322.185, 209.414, 322.185,
            209.737, 322.185, 210.383, 322.185, 211.03, 322.185, 211.353, 322.185, 211.676, 322.185, 212.322,
            323.154, 213.292, 323.154, 213.938, 324.447, 214.584, 325.093, 215.877, 325.416, 216.2, 325.416,
            216.846, 325.739, 217.17, 326.063, 217.493, 326.386, 218.139, 326.709, 218.139, 326.709, 218.462,
            327.032, 219.109, 327.032, 219.432, 327.032, 219.755, 327.355, 220.078, 327.355, 220.401, 327.678,
            221.371, 328.002, 221.371, 328.002, 222.017, 328.325, 222.663, 328.648, 222.663, 328.971, 222.986,
            329.294, 223.31, 329.617, 223.956, 329.617, 224.279 };
    auto points = MakeArray<System::SmartPtr<Aspose::Pdf::Point>>();
    //konversi data menjadi titik

    for (int i = 0, j = 0; i < _countof(ppts) / 2; i++, j += 2) {
        points->Add(MakeObject<Point>(ppts[j], ppts[j + 1]));
    }
    inkList->Add(points);
    auto ia = MakeObject<InkAnnotation>(page, arect, inkList);
    ia->set_Title(u"Aspose User");
    ia->set_Color(Color::get_Red());
    ia->set_CapStyle(CapStyle::Rounded);

    auto border = MakeObject<Border>(ia);
    border->set_Width(3);
    ia->set_Opacity(0.75);

    page->get_Annotations()->Add(ia);
    document->Save(_dataDir + u"appartments_mod.pdf");
}
```
### Get InkAnnotation

Silakan coba gunakan potongan kode berikut untuk mendapatkan InkAnnotation dalam dokumen PDF.

```cpp
void ShapesAnnotations::GetInkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"appartments_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);


    // Saring anotasi menggunakan AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<InkAnnotation>(page, Rectangle::get_Trivial(), nullptr));
    page->Accept(annotationSelector);
    auto inkAnnotations = annotationSelector->get_Selected();

    // cetak hasil
    for (auto ia : inkAnnotations) {
        Console::WriteLine(ia->get_Rect());
    }
}
```

### Delete InkAnnotation

Potongan kode berikut menunjukkan cara menghapus InkAnnotation dari file PDF.

```cpp
void ShapesAnnotations::DeleteInkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"appartments_mod.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Saring anotasi menggunakan AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<InkAnnotation>(page, Rectangle::get_Trivial(), nullptr));
    page->Accept(annotationSelector);
    auto InkAnnotations = annotationSelector->get_Selected();

    for (auto ca : InkAnnotations) {
       page->get_Annotations()->Delete(ca);
    }
    document->Save(_dataDir + u"appartments_del.pdf");
}
```