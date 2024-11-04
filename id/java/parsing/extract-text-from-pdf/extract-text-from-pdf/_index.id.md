---
title: Ekstraksi teks mentah dari file PDF 
linktitle: Ekstrak teks dari PDF
type: docs
weight: 10
url: /java/extract-text-from-all-pdf/
description: Artikel ini menjelaskan berbagai cara untuk mengekstrak teks dari dokumen PDF menggunakan Aspose.PDF untuk Java. Dari seluruh halaman, dari bagian tertentu, berdasarkan kolom, dll.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Teks Dari Semua Halaman Dokumen PDF

Mengekstrak teks dari dokumen PDF adalah kebutuhan umum. Dalam contoh ini, Anda akan melihat bagaimana Aspose.PDF untuk Java memungkinkan mengekstraksi teks dari semua halaman dokumen PDF.
Untuk mengekstrak teks dari semua halaman PDF:

1. Buat objek dari kelas [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. Buka PDF menggunakan kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan panggil metode [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) dari koleksi [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
2. Kelas [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) menyerap teks dari dokumen dan mengembalikannya dalam properti **Text**.

Cuplikan kode berikut menunjukkan cara mengekstrak teks dari semua halaman dokumen PDF.

```java
public static void ExtractFromAllPages(){
    // Jalur ke direktori dokumen.
    String _dataDir = "/home/admin1/pdf-examples/Samples/";
    String filePath = _dataDir + "ExtractTextAll.pdf";

    // Buka dokumen
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // Buat objek TextAbsorber untuk mengekstrak teks
    com.aspose.pdf.TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();
    
    // Terima absorber untuk semua halaman
    pdfDocument.getPages().accept(textAbsorber);
    
    // Dapatkan teks yang diekstrak
    String extractedText = textAbsorber.getText();                
    try {
        java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
        // Tulis satu baris teks ke file
        writer.write(extractedText);            
        // Tutup stream
        writer.close();
    } catch (java.io.IOException e) {
        e.printStackTrace();
    }

}
```


## Ekstrak Teks dari Halaman menggunakan Perangkat Teks

Anda dapat menggunakan kelas **TextDevice** untuk mengekstrak teks dari file PDF. TextDevice menggunakan [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) dalam implementasinya, sehingga, pada kenyataannya, mereka melakukan hal yang sama tetapi TextDevice hanya diimplementasikan untuk menyatukan pendekatan "Device" untuk mengekstrak apapun dari halaman seperti ImageDevice, PageDevice, dll. TextAbsorber dapat mengekstrak teks dari Halaman, seluruh PDF atau XForm, TextAbsorber ini lebih universal.

### Ekstrak teks dari semua halaman

Langkah-langkah dan potongan kode berikut menunjukkan cara mengekstrak teks dari PDF menggunakan perangkat teks.

1. Buat objek dari kelas Document dengan file PDF input yang ditentukan
2. Buat objek dari kelas TextDevice
3. Gunakan objek dari kelas TextExtractOptions untuk menentukan opsi ekstraksi
4. Gunakan metode Process dari kelas TextDevice untuk mengubah konten menjadi teks
5. Simpan teks ke file output

```java
public static void extractTextFromAllPagesOfPDF() throws IOException {
    // buka dokumen
    Document pdfDocument = new Document("input.pdf");
    // file teks di mana teks yang diekstrak akan disimpan
    java.io.OutputStream text_stream = new java.io.FileOutputStream("ExtractedText.txt", false);
    // iterasi melalui semua halaman dari file PDF
    for (Page page : (Iterable<Page>) pdfDocument.getPages()) {
        // buat perangkat teks
        TextDevice textDevice = new TextDevice();
        // setel opsi ekstraksi teks - setel mode ekstraksi teks (Raw atau
        // Pure)
        TextExtractionOptions textExtOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Raw);
        textDevice.setExtractionOptions(textExtOptions);
        // dapatkan teks dari halaman-halaman PDF dan simpan ke objek OutputStream
        textDevice.process(page, text_stream);
    }
    // tutup objek stream
    text_stream.close();
}
```


## Ekstrak Teks dari wilayah halaman tertentu

Kelas [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) menyediakan kemampuan untuk mengekstrak teks dari halaman tertentu atau semua halaman dari dokumen PDF. Kelas ini mengembalikan teks yang diekstraksi dalam properti **Text**. Namun, jika kita memiliki kebutuhan untuk mengekstrak teks dari wilayah halaman tertentu, kita dapat menggunakan properti **Rectangle** dari [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions). Properti Rectangle mengambil objek Rectangle sebagai nilai dan dengan menggunakan properti ini, kita dapat menentukan wilayah halaman dari mana kita perlu mengekstrak teks.

Metode [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) dari sebuah halaman dipanggil untuk mengekstrak teks.
 Buat objek dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) dan [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber). Panggil metode [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) pada halaman individu, sebagai Indeks **Page**, dari objek **Document**. **Index** adalah nomor halaman tertentu dari mana teks perlu diekstraksi. Anda dapat mendapatkan teks dari properti **Text** dari kelas [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber). Cuplikan kode berikut menunjukkan cara mengekstrak teks dari halaman individu.

```java
public static void ExtractTextFromParticularPageRegion(String[] args) throws IOException {
    // buka dokumen
    Document doc = new Document("page_0001.pdf");
    // buat objek TextAbsorber untuk mengekstrak teks
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // terima absorber untuk halaman pertama
    doc.getPages().get_Item(1).accept(absorber);
    // dapatkan teks yang diekstraksi
    String extractedText = absorber.getText();
    // buat penulis dan buka file
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // tulis konten yang diekstraksi
    writer.write(extractedText);
    // Tutup penulis
    writer.close();
}
```

## Ekstrak teks berdasarkan kolom

File PDF mungkin terdiri dari elemen Teks, Gambar, Anotasi, Lampiran, Grafik, dll dan Aspose.PDF untuk .NET menawarkan fitur untuk Menambahkan serta memanipulasi semua elemen ini. API ini luar biasa ketika datang ke penambahan dan ekstraksi Teks dari dokumen PDF dan kita mungkin menghadapi skenario di mana dokumen PDF terdiri dari lebih dari satu kolom (multi-kolom) dokumen PDF dan kita perlu mengekstrak konten halaman sambil menghormati tata letak yang sama, maka Aspose.PDF untuk .NET adalah pilihan yang tepat untuk mencapai persyaratan ini. Salah satu pendekatannya adalah dengan mengurangi ukuran font dari konten di dalam dokumen PDF dan kemudian melakukan ekstraksi teks. Cuplikan kode berikut menunjukkan langkah-langkah untuk mengurangi ukuran teks dan kemudian mencoba mengekstrak teks dari dokumen PDF.

```java
public static void ExtractTextBasedOnColumns() throws IOException {
    // buka dokumen
    Document doc = new Document("page_0001.pdf");
    // buat objek TextAbsorber untuk mengekstrak teks
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // terima absorber untuk halaman pertama
    doc.getPages().get_Item(1).accept(absorber);
    // dapatkan teks yang diekstrak
    String extractedText = absorber.getText();
    // buat penulis dan buka file
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // tulis konten yang diekstrak
    writer.write(extractedText);
    // Tutup penulis
    writer.close();
}
```


### Pendekatan kedua - Menggunakan ScaleFactor

Dalam rilis baru ini, kami juga telah memperkenalkan beberapa peningkatan di TextAbsorber dan dalam mekanisme pemformatan teks internal. Jadi sekarang, selama ekstraksi teks menggunakan mode 'Pure', Anda dapat menentukan opsi ScaleFactor dan ini dapat menjadi pendekatan lain untuk mengekstrak teks dari dokumen PDF multi-kolom selain pendekatan yang disebutkan di atas. Faktor skala ini dapat diatur untuk menyesuaikan grid yang digunakan untuk mekanisme pemformatan teks internal selama ekstraksi teks. Menentukan nilai ScaleFactor antara 1 dan 0.1 (termasuk 0.1) memiliki efek yang sama seperti pengurangan font.

Menentukan nilai ScaleFactor antara 0.1 dan -0.1 dianggap sebagai nilai nol, tetapi ini membuat algoritma menghitung faktor skala yang dibutuhkan selama ekstraksi teks secara otomatis. Perhitungan didasarkan pada lebar rata-rata glyph dari font yang paling populer di halaman, tetapi kami tidak dapat menjamin bahwa dalam teks yang diekstrak tidak ada string kolom yang mencapai awal kolom berikutnya. Harap dicatat bahwa jika nilai ScaleFactor tidak ditentukan, nilai default 1.0 akan digunakan. Ini berarti tidak ada penskalaan yang akan dilakukan. Jika nilai ScaleFactor yang ditentukan lebih dari 10 atau kurang dari -0.1, nilai default 1.0 akan digunakan.

Kami mengusulkan penggunaan auto-scaling (ScaleFactor = 0) saat memproses sejumlah besar file PDF untuk ekstraksi konten teks. Atau atur secara manual pengurangan berlebih dari lebar grid (sekitar ScaleFactor = 0.5). Namun, Anda tidak boleh menentukan apakah skala diperlukan untuk dokumen konkret atau tidak. Jika Anda mengatur pengurangan berlebih dari lebar grid untuk dokumen (yang tidak membutuhkannya), konten teks yang diekstraksi akan tetap sepenuhnya memadai. Silakan lihat cuplikan kode berikut.

```java
public static void usingSetScaleFactorMethod() {
    Document pdfDocument = new Document("inputFile.pdf");
    TextAbsorber textAbsorber = new TextAbsorber();
    textAbsorber.setExtractionOptions(new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure));
    // Mengatur faktor skala ke 0.5 sudah cukup untuk membagi kolom di sebagian besar dokumen
    // Pengaturan nol memungkinkan algoritma memilih faktor skala secara otomatis
    textAbsorber.getExtractionOptions().setScaleFactor((double) 0.5);
    pdfDocument.getPages().accept(textAbsorber);
    String extractedText = textAbsorber.getText();
}
```


{{% alert color="primary" %}}

Harap dicatat bahwa tidak ada korespondensi langsung antara ScaleFactor baru dan koefisien lama pengurangan font secara manual. Namun, secara default algoritma memperhitungkan nilai ukuran font yang telah berkurang karena beberapa alasan internal. Misalnya, mengurangi ukuran font dari 10 ke 7 memiliki efek yang sama dengan mengatur faktor skala ke 5/8 (= 0.625).

{{% /alert %}}

## Ekstrak Teks yang Disorot dari Dokumen PDF

Dalam berbagai skenario ekstraksi teks dari dokumen PDF, Anda mungkin memiliki persyaratan untuk mengekstrak hanya teks yang disorot dari dokumen PDF. Untuk mengimplementasikan fungsionalitas ini, kami telah menambahkan metode TextMarkupAnnotation.GetMarkedText() dan TextMarkupAnnotation.GetMarkedTextFragments() dalam API. Anda dapat mengekstrak teks yang disorot dari dokumen PDF dengan memfilter TextMarkupAnnotation dan menggunakan metode yang disebutkan. Cuplikan kode berikut menunjukkan bagaimana Anda dapat mengekstrak teks yang disorot dari dokumen PDF.

```java
public static void ExtractHighlightedText() {
    Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
    // Loop melalui semua anotasi
    for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations())
    {
        // Filter TextMarkupAnnotation
        if (annotation.getAnnotationType()==AnnotationType.Highlight)
        {
            HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
            // Ambil fragmen teks yang disorot
            TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
            for (TextFragment tf : collection)
            {
                // Tampilkan teks yang disorot
                System.out.println(tf.getText());
            }
        }
    }        
}
```


## Akses Elemen Fragmen Teks dan Segmen dari XML

Terkadang kita perlu mengakses item TextFragment atau TextSegment saat memproses dokumen PDF yang dihasilkan dari XML. Aspose.PDF untuk .NET menyediakan akses ke item tersebut berdasarkan nama. Cuplikan kode di bawah ini menunjukkan cara menggunakan fungsionalitas ini.

```java
public static void AccessTextFragmentAndSegmentElements() {
    String inXml = "40014.xml";        
    Document doc = new Document();
    doc.bindXml(_dataDir + inXml);

    TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
    segment = (TextSegment) doc.getObjectById("strongHtml");

    System.out.println(segment.getText());
    
}
```