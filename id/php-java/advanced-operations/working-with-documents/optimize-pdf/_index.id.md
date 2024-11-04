---
title: Optimize, Compress or Reduce PDF Size in PHP
linktitle: Optimize PDF Document
type: docs
weight: 40
url: /php-java/optimize-pdf/
description: Optimalkan file PDF, perkecil semua gambar, kurangi ukuran PDF, Hapus font yang disematkan, Hapus objek yang tidak digunakan menggunakan PHP.
lastmod: "2024-06-05"
---

Dokumen PDF terkadang dapat mengandung data tambahan. Mengurangi ukuran file PDF akan membantu Anda mengoptimalkan transfer jaringan dan penyimpanan. Ini sangat berguna untuk dipublikasikan pada halaman web, dibagikan di media sosial, dikirim melalui e-mail, atau diarsipkan dalam penyimpanan. Kita dapat menggunakan beberapa teknik untuk mengoptimalkan PDF:

- Optimalkan konten halaman untuk penelusuran online
- Perkecil atau kompres semua gambar
- Aktifkan penggunaan ulang konten halaman
- Gabungkan aliran duplikat
- Hapus font yang disematkan
- Hapus objek yang tidak digunakan
- Hapus bidang formulir yang diratakan
- Hapus atau ratakan anotasi

## Optimalkan Dokumen PDF untuk Web

Optimalisasi atau linearisasi mengacu pada proses membuat file PDF cocok untuk penelusuran online menggunakan peramban web.
 Aspose.PDF mendukung proses ini.

Untuk mengoptimalkan PDF untuk tampilan web:

1. Buka dokumen input dalam objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).
1. Gunakan metode [optimize()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#optimize--).
1. Simpan dokumen yang telah dioptimalkan menggunakan metode save(..).

Cuplikan kode berikut menunjukkan cara mengoptimalkan dokumen PDF untuk web.

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Optimalkan untuk web
    $document->optimize();

    // Simpan dokumen yang diperbarui
    $document->save($outputFile);
    $document->close();
```

## Kurangi Ukuran File PDF

Topik ini menjelaskan langkah-langkah untuk mengoptimalkan/mengurangi ukuran file PDF. Aspose.PDF API menyediakan kelas [OptimizationOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf.optimization/class-use/OptimizationOptions) yang memberikan fleksibilitas untuk mengoptimalkan output PDF dengan menghapus objek yang tidak diperlukan dan mengompresi file PDF yang memiliki gambar. Kedua opsi ini dijelaskan dalam bagian berikut.

### Menghapus Objek yang Tidak Diperlukan

Kita dapat mengoptimalkan ukuran dokumen PDF dengan menghapus objek yang duplikat dan tidak terpakai. Cuplikan kode berikut menunjukkan caranya.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    
    // Optimalkan dokumen PDF. Namun, perlu dicatat bahwa metode ini tidak dapat menjamin
    // pengecilan dokumen
    $document->optimizeResources();

    // Simpan dokumen yang diperbarui
    $document->save($outputFile);
    $document->close();

```

## Mengecilkan atau Mengompresi Semua Gambar

Jika file PDF sumber berisi gambar, pertimbangkan untuk mengompresi gambar dan mengatur kualitasnya. Untuk mengaktifkan kompresi gambar, berikan nilai true sebagai argumen ke metode setCompressImages(..). Semua gambar dalam dokumen akan dikompresi ulang. Kompresi ditentukan oleh metode setImageQuality(..), yang merupakan nilai kualitas dalam persen. 100% adalah kualitas dan ukuran gambar yang tidak berubah. Untuk mengurangi ukuran gambar, berikan argumen kurang dari 100 ke metode setImageQuality(..).

```php

    // Buka dokumen
    $document = new Document($inputFile);
    
    // Inisialisasi OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    // Atur opsi CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // Atur opsi ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(50);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Simpan dokumen yang telah diperbarui
    $document->save($outputFile);
    $document->close();
```

Cara lain adalah mengubah ukuran gambar dengan resolusi yang lebih rendah. Dalam kasus ini, kita harus mengatur ResizeImages ke true dan MaxResolution ke nilai yang sesuai.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    
    // Inisialisasi OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    // Atur opsi CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);
    
    // Atur opsi ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);

    // Atur opsi ResizeImage
    $optimizationOptions->getImageCompressionOptions()->setResizeImages(true);

    // Atur opsi MaxResolution
    $optimizationOptions->getImageCompressionOptions()->setMaxResolution(300);

    // Simpan dokumen yang diperbarui
    $document->save($outputFile);
    $document->close();
```

Masalah penting lainnya adalah waktu eksekusi. Tetapi sekali lagi, kita dapat mengatur pengaturan ini juga. Saat ini, kita dapat menggunakan dua algoritma - Standar dan Cepat. Untuk mengendalikan waktu eksekusi kita harus mengatur properti Versi. Cuplikan berikut menunjukkan algoritma Cepat:

```php
    // Buka dokumen
    $document = new Document($inputFile);
    
    // Inisialisasi OptimizationOptions
    $optimizationOptions = new optimization_OptimizationOptions();

    // Atur opsi CompressImages
    $optimizationOptions->getImageCompressionOptions()->setCompressImages(true);

    // Atur opsi ImageQuality
    $optimizationOptions->getImageCompressionOptions()->setImageQuality(75);
    $optimization_ImageCompressionVersion = new optimization_ImageCompressionVersion();

    // Atur Versi Kompresi Gambar ke cepat
    $optimizationOptions->getImageCompressionOptions()->setVersion($optimization_ImageCompressionVersion->Fast);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Simpan dokumen yang diperbarui
    $document->save($outputFile);
    $document->close();
```

## Menghapus Objek yang Tidak Digunakan

Dokumen PDF terkadang mengandung objek PDF yang tidak direferensikan dari objek lain dalam dokumen. Hal ini bisa terjadi, misalnya, ketika sebuah halaman dihapus dari pohon halaman dokumen tetapi objek halaman itu sendiri tidak dihapus. Menghapus objek-objek ini tidak membuat dokumen menjadi tidak valid melainkan mengecilkannya.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    
    // Inisialisasi OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedObjects(true);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Simpan dokumen yang telah diperbarui
    $document->save($outputFile);
    $document->close();
```

## Menghapus Stream yang Tidak Digunakan

Terkadang sebuah dokumen mengandung stream sumber daya yang tidak digunakan.
 Aliran ini bukan "objek yang tidak digunakan" karena mereka dirujuk dari kamus sumber daya halaman. Hal ini dapat terjadi dalam kasus di mana gambar telah dihapus dari halaman tetapi tidak dari sumber daya halaman. Juga, situasi ini sering terjadi ketika halaman-halaman diekstraksi dari dokumen dan halaman dokumen memiliki sumber daya “umum”, yaitu, objek Sumber Daya yang sama. Konten halaman dianalisis untuk menentukan apakah aliran sumber daya digunakan atau tidak. Aliran yang tidak digunakan akan dihapus. Terkadang ini mengurangi ukuran dokumen.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    
    // Inisialisasi OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setRemoveUnusedStreams(true);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Simpan dokumen yang telah diperbarui
    $document->save($outputFile);
    $document->close();
```

## Menghubungkan Aliran Duplikat

Terkadang sebuah dokumen mengandung beberapa aliran sumber daya yang identik (misalnya gambar). Ini mungkin terjadi misalnya ketika sebuah dokumen digabungkan dengan dirinya sendiri. Dokumen keluaran berisi dua salinan independen dari aliran sumber daya yang sama. Kami menganalisis semua aliran sumber daya dan membandingkannya. Jika aliran diduplikasi, mereka digabungkan, yaitu, hanya satu salinan yang tersisa, referensi diubah dengan tepat dan salinan objek dihapus. Terkadang ini mengurangi ukuran dokumen.

```php
    // Buka dokumen
    $document = new Document($inputFile);
    
    // Inisialisasi OptimizationOptions
    $optimizationOptions = new OptimizationOptions();
    
    $optimizationOptions->setLinkDuplcateStreams(true);
    
    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Simpan dokumen yang telah diperbarui
    $document->save($outputFile);
    $document->close();
```

Selain itu, kita dapat menggunakan pengaturan AllowReusePageContent. Jika properti ini diatur ke true, konten halaman akan digunakan kembali saat mengoptimalkan dokumen untuk halaman yang identik.

```php
    // Buka dokumen
    $document = new Document($inputFile);
    
    // Inisialisasi OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setAllowReusePageContent(true);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Simpan dokumen yang telah diperbarui
    $document->save($outputFile);
    $document->close();
```

## Unembedding Fonts

Jika dokumen menggunakan font yang disematkan, itu berarti semua data font ditempatkan dalam dokumen. Keuntungannya adalah dokumen dapat dilihat terlepas dari apakah font terpasang di mesin pengguna atau tidak. Namun, menyematkan font membuat dokumen menjadi lebih besar. Metode unembed fonts menghilangkan semua font yang disematkan. Ini mengurangi ukuran dokumen tetapi dokumen mungkin menjadi tidak terbaca jika font yang benar tidak terpasang.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    
    // Inisialisasi OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    $document->optimizeResources($optimizationOptions);

    // Simpan dokumen yang telah diperbarui
    $document->save($outputFile);
    $document->close();
```

## Menghapus atau Memadatkan Anotasi

Anotasi dapat dihapus ketika tidak diperlukan.
 Ketika mereka dibutuhkan tetapi tidak memerlukan pengeditan tambahan, mereka dapat diratakan. Kedua teknik ini akan mengurangi ukuran file.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    $pages = $document->getPages();

    for ($i=1; $i < $pages->size() ; $i++) { 
        $page = $pages->get_Item($i);
        $annotations = $page->getAnnotations();
        for ($idx=0; $idx < $annotations->size(); $idx++) { 
            $annotation = $annotations->get_Item($idx);
            $annotation->flatten();
        }
    }
     
    // Simpan dokumen yang telah diperbarui
    $document->save($outputFile);
    $document->close();
```

## Menghapus Bidang Formulir

Jika dokumen PDF berisi AcroForms, kita dapat mencoba mengurangi ukuran file dengan meratakan bidang formulir.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    
    // Ratakan Formulir
    $fields = $document->getForm()->getFields();
    foreach ($fields as $field) {
        $field->flatten();
    }            

    // Simpan dokumen yang telah diperbarui
    $document->save($outputFile);
    $document->close();
```

## Mengonversi PDF dari ruang warna RGB ke skala abu-abu

File PDF terdiri dari Teks, Gambar, Lampiran, Anotasi, Grafik, dan objek lainnya. Anda mungkin menghadapi persyaratan untuk mengonversi PDF dari ruang warna RGB ke Skala Abu-abu agar lebih cepat saat mencetak file PDF tersebut. Juga ketika file dikonversi ke Skala Abu-abu, ukuran dokumen juga berkurang tetapi dengan perubahan ini, kualitas dokumen dapat menurun. Saat ini, fitur ini didukung oleh fitur Pre-Flight dari Adobe Acrobat, tetapi ketika berbicara tentang otomatisasi Office, Aspose.PDF adalah solusi utama untuk memberikan kemudahan semacam itu untuk manipulasi dokumen.

Untuk memenuhi persyaratan ini, potongan kode berikut dapat digunakan.

```php

    // Buka dokumen
    $document = new Document($inputFile);
    
    $strategy = new RgbToDeviceGrayConversionStrategy();
    for ($idxPage = 1; $idxPage <= $document->getPages()->size(); $idxPage++) {
        $page = $document->getPages()->get_Item($idxPage);
        $strategy->convert($page);
    }          

    // Simpan dokumen yang telah diperbarui
    $document->save($outputFile);
    $document->close();
```


## FlateDecode Compression

Aspose.PDF untuk PHP via Java menyediakan dukungan kompresi FlateDecode untuk fungsionalitas Optimasi PDF. Potongan kode berikut menunjukkan cara menggunakan opsi dalam Optimasi untuk menyimpan gambar dengan kompresi FlateDecode:

```php

    // Buka dokumen
    $document = new Document($inputFile);

    // Inisialisasi OptimizationOptions
    $optimizationOptions = new OptimizationOptions();

    $optimizationOptions->setUnembedFonts(true);

    // Optimalkan dokumen PDF menggunakan OptimizationOptions
    $optimizationOptions->getImageCompressionOptions()->setEncoding(optimization_ImageEncoding::$Flate);

    // Simpan dokumen yang diperbarui
    $document->save($outputFile);
    $document->close();
```

## Simpan Gambar dalam XImageCollection

Aspose.PDF untuk PHP via Java menyediakan kemampuan untuk menyimpan gambar baru ke dalam [XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/XImageCollection) dengan kompresi FlateDecode.
 Untuk mengaktifkan opsi ini, Anda dapat menggunakan flag ImageFilterType.Flate. Cuplikan kode berikut menunjukkan cara menggunakan fungsionalitas ini:

```php
    // Buka dokumen
    $document = new Document($inputFile);

    // Inisialisasi Dokumen
    $page = $document->getPages()->get_Item(1);

    // Muat gambar ke dalam aliran
    $imageStream = new java("java.io.FileInputStream",$inputFile);
    $imageFilterType = new ImageFilterType();
    $page->getResources()->getImages()->add($imageStream, $imageFilterType->Flate);
    $idx = $page->getResources()->getImages()->size();
    $ximage = $page->getResources()->getImages()->get_Item($idx);
    $page->getContents()->add(new operators_GSave());

    // Tetapkan koordinat
    $lowerLeftX = 0;
    $lowerLeftY = 0;
    $upperRightX = 600;
    $upperRightY = 600;
    $rectangle = new Rectangle($lowerLeftX, $lowerLeftY, $upperRightX, $upperRightY);
    $matrixData = [
        $rectangle->getURX() - $rectangle->getLLX(), 0, 
        0, $rectangle->getURY() - $rectangle->getLLY(), 
        $rectangle->getLLX(), $rectangle->getLLY()];
    $matrix = new Matrix($matrixData);

    // Menggunakan operator ConcatenateMatrix (menggabungkan matriks): mendefinisikan bagaimana gambar harus ditempatkan
    $page->getContents()->add(new operators_ConcatenateMatrix($matrix));
    $page->getContents()->add(new operators_Do($ximage->getName()));
    $page->getContents()->add(new operators_GRestore());

    // Simpan dokumen yang diperbarui
    $document->save($outputFile);
    $document->close();
```