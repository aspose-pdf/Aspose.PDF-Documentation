---
title: Memodifikasi AcroForms
linktitle: Memodifikasi AcroForms
type: docs
weight: 40
url: /id/java/modifing-form/
description: Bagian ini menjelaskan cara memodifikasi formulir dalam dokumen PDF Anda dengan Aspose.PDF untuk PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Menetapkan Font Bidang Formulir Kustom

Bidang formulir dalam file PDF Adobe dapat dikonfigurasi untuk menggunakan font default tertentu. Aspose.PDF memungkinkan pengembang untuk menerapkan font apa pun sebagai font default bidang, baik salah satu dari 14 font inti atau font kustom. Untuk menetapkan dan memperbarui font default yang digunakan untuk bidang formulir, Aspose.PDF memiliki kelas DefaultAppearance (Font font, double size, Color color). Kelas ini dapat diakses menggunakan com.aspose.pdf.DefaultAppearance. Untuk menggunakan objek ini, gunakan metode setDefaultAppearance(..) dari kelas Field.

Cuplikan kode berikut menunjukkan cara menetapkan font default untuk bidang formulir PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Dapatkan bidang formulir tertentu dari dokumen
    $field = $document->getForm()->get("textbox1");

    // Buat objek font
    $fontRepository = new FontRepository();
    $font = $fontRepository->findFont("ComicSansMS");

    $colors = new Color();
    $blackColor = $colors->getBlack();

    // Tetapkan informasi font untuk bidang formulir
    $field->setDefaultAppearance(new DefaultAppearance($font, 10, $blackColor));

    // Simpan dokumen yang diperbarui
    $document->save($outputFile);
    $document->close();        

    $document->close();
```


## Dapatkan/Setel FieldLimit

Kode ini menunjukkan penggunaan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) untuk membuka dokumen, mengambil field formulir, menetapkan panjang maksimum, mengambil panjang maksimum dengan metode 'setMaxLen', dan 'getMaxLen'.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Ambil field formulir tertentu dari dokumen
    $field = $document->getForm()->get("textbox1");
    
    $field->setMaxLen(10);

    // Mendapatkan batas field maksimum menggunakan DOM
    $responseData = "Limit: " . $field->getMaxLen();          

    $document->close();
```

Anda juga dapat mendapatkan nilai yang sama menggunakan namespace Aspose.PDF.Facades menggunakan cuplikan kode berikut.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Ambil field formulir tertentu dari dokumen
    $field = $document->getForm()->get("textbox1");

    // Mendapatkan batas field maksimum menggunakan DOM
    $responseData = "Limit: " . $field->getMaxLen();          

    $document->close();
```


Similarly, Aspose.PDF memiliki metode yang mendapatkan batasan field menggunakan pendekatan DOM. Cuplikan kode berikut menunjukkan langkah-langkahnya.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Dapatkan field formulir tertentu dari dokumen
    $field = $document->getForm()->get("textbox1");

    // Hapus field
    $field->delete();
    
    $document->close();
```
## Hapus Field Formulir Tertentu dari Dokumen PDF

Semua field formulir terdapat dalam koleksi Form dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document). Koleksi ini menyediakan berbagai metode yang mengelola field formulir, termasuk metode hapus. Jika Anda ingin menghapus field tertentu, berikan nama field sebagai parameter ke metode hapus dan kemudian simpan dokumen PDF yang telah diperbarui.

Cuplikan kode berikut menunjukkan cara menghapus field bernama dari dokumen PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Dapatkan field formulir tertentu dari dokumen
    $field = $document->getForm()->get("textbox1");

    // Hapus field
    $field->delete();
    
    $document->close();
```


## Memodifikasi Bidang Formulir dalam Dokumen PDF

Koleksi Form dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) memungkinkan Anda untuk mengelola bidang formulir dalam dokumen PDF.

Untuk memodifikasi bidang formulir, ambil bidang dari koleksi Form dan atur propertinya. Kemudian simpan dokumen PDF yang telah diperbarui.

Cuplikan kode berikut menunjukkan cara memodifikasi bidang formulir yang ada dalam dokumen PDF.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Dapatkan bidang formulir tertentu dari dokumen
    $field = $document->getForm()->get("textbox1");

    // Memodifikasi nilai bidang
    $field->setValue("Nilai yang Diperbarui");

    // Atur bidang sebagai hanya baca
    $field->setReadOnly(true);

    // Simpan dokumen yang telah diperbarui
    $document->save($outputFile);        
    $document->close();
```

### Memindahkan Bidang Formulir ke Lokasi Baru dalam File PDF

Jika Anda ingin memindahkan bidang formulir ke lokasi baru pada halaman PDF, pertama ambil objek bidang tersebut dan kemudian tentukan nilai baru untuk metode setRect-nya.
 Sebuah objek [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) dengan koordinat baru ditetapkan ke metode setRect(..). Kemudian simpan PDF yang telah diperbarui menggunakan metode save dari objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Cuplikan kode berikut menunjukkan cara memindahkan field formulir ke lokasi baru.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Dapatkan field formulir tertentu dari dokumen
    $field = $document->getForm()->get("textbox1");

    // Ubah lokasi field
    $field->setRect(new Rectangle(300, 400, 600, 500));

    // Simpan dokumen yang diperbarui
    $document->save($outputFile);        
    $document->close();
```