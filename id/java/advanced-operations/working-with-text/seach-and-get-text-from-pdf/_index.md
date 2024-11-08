---
title: Mencari dan Mendapatkan Teks dari Halaman Dokumen PDF 
linktitle: Mencari dan Mendapatkan Teks
type: docs
weight: 60
url: /id/java/search-and-get-text-from-pdf/
description: Artikel ini menjelaskan cara menggunakan berbagai alat untuk mencari dan mendapatkan teks dari dokumen PDF. Kita dapat mencari dengan ekspresi reguler dari halaman tertentu atau seluruh halaman.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Mencari dan Mendapatkan Teks dari Semua Halaman Dokumen PDF

TextFragmentAbsorber memungkinkan Anda untuk menemukan teks, yang cocok dengan frasa tertentu, dari semua halaman dokumen PDF.

Untuk mencari teks di seluruh dokumen, panggil metode accept() koleksi [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 The [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) method takes a TextFragmentAbsorber object as a parameter, which returns a collection of TextFragment objects. Loop through all the fragments to get their properties, for example Text, Position, XIndent, YIndent, FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor etc.

Metode [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) menerima objek TextFragmentAbsorber sebagai parameter, yang mengembalikan koleksi objek TextFragment. Loop melalui semua fragmen untuk mendapatkan propertinya, misalnya Text, Position, XIndent, YIndent, FontName, FontSize, IsAccessible, IsEmbedded, IsSubset, ForegroundColor dll.

The following code snippet shows how to search an the entire document and display all matches in a console.

Cuplikan kode berikut menunjukkan bagaimana mencari seluruh dokumen dan menampilkan semua kecocokan di konsol.

```java
// Open document
// Buka dokumen
Document pdfDocument = new Document("input.pdf");

// Create TextAbsorber object to find all instances of the input search phrase
// Buat objek TextAbsorber untuk menemukan semua instansi dari frasa pencarian input
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// Accept the absorber for all the pages
// Terima absorber untuk semua halaman
pdfDocument.getPages().accept(textFragmentAbsorber);

// Get the extracted text fragments into collection
// Dapatkan fragmen teks yang diekstraksi ke dalam koleksi
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Loop through the fragments
// Loop melalui fragmen
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("Text :- " + textFragment.getText());
    System.out.println("Position :- " + textFragment.getPosition());
    System.out.println("XIndent :- " + textFragment.getPosition().getXIndent());
    System.out.println("YIndent :- " + textFragment.getPosition().getYIndent());
    System.out.println("Font - Name :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("Font - IsAccessible :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("Font - IsEmbedded - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("Font - IsSubset :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("Font Size :- " + textFragment.getTextState().getFontSize());
    System.out.println("Foreground Color :- " + textFragment.getTextState().getForegroundColor());
}
```

Untuk mencari teks pada halaman tertentu dan mendapatkan properti yang terkait dengannya, sediakan indeks halaman:

```java
// Terima absorber untuk halaman pertama dokumen
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## Mencari dan Mendapatkan Segmen Teks dari Halaman PDF

Untuk mencari segmen teks di semua halaman dalam dokumen, dapatkan objek TextFragment dari dokumen tersebut.

TextFragmentAbsorber memungkinkan Anda menemukan teks yang cocok dengan frasa tertentu dari semua halaman dalam dokumen PDF. Untuk mencari teks di seluruh dokumen, panggil metode [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) dari koleksi [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection). Metode [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) menerima objek TextFragmentAbsorber sebagai parameter, yang mengembalikan koleksi objek TextFragment.

{{% alert color="primary" %}}

Ketika koleksi TextFragmentCollection telah diambil dari dokumen, lakukan perulangan melalui koleksi tersebut untuk mendapatkan koleksi TextSegmentCollection dari setiap objek TextFragment.
 Setelah itu, Anda dapat mendapatkan properti objek TextSegment individual.

{{% /alert %}}

Cuplikan kode berikut menunjukkan cara mencari segmen teks di semua halaman.

```java
// Buka dokumen
Document pdfDocument = new Document("input.pdf");

// Buat objek TextAbsorber untuk menemukan semua instance dari frasa pencarian input
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// Terima absorber untuk halaman pertama dokumen
pdfDocument.getPages().accept(textFragmentAbsorber);

// Dapatkan fragmen teks yang diekstraksi ke dalam koleksi
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Loop melalui fragmen teks
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    // Iterasi melalui segmen teks
    for (TextSegment textSegment : (Iterable<TextSegment>) textFragment.getSegments()) {
        System.out.println("Teks :- " + textSegment.getText());
        System.out.println("Posisi :- " + textSegment.getPosition());
        System.out.println("XIndent :- " + textSegment.getPosition().getXIndent());
        System.out.println("YIndent :- " + textSegment.getPosition().getYIndent());
        System.out.println("Font - Nama :- " + textSegment.getTextState().getFont().getFontName());
        System.out.println("Font - IsAccessible :- " + textSegment.getTextState().getFont().isAccessible());
        System.out.println("Font - IsEmbedded - " + textSegment.getTextState().getFont().isEmbedded());
        System.out.println("Font - IsSubset :- " + textSegment.getTextState().getFont().isSubset());
        System.out.println("Ukuran Font :- " + textSegment.getTextState().getFontSize());
        System.out.println("Warna Depan :- " + textSegment.getTextState().getForegroundColor());
    }
}
```

Untuk mencari segmen teks tertentu dan mendapatkan properti terkait, tentukan indeks halaman untuk halaman yang ingin Anda cari:

```java
// Terima absorber untuk halaman pertama dokumen.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## Mencari dan Mendapatkan Teks dari halaman menggunakan Ekspresi Reguler

TextFragmentAbsorber membantu Anda mencari dan mengambil teks dari semua halaman dalam dokumen, berdasarkan ekspresi reguler.

Untuk mencari dan mendapatkan teks dari sebuah dokumen:

1. Berikan istilah pencarian sebagai ekspresi reguler ke konstruktor TextFragmentAbsorber.
2. Atur properti TextSearchOptions objek TextFragmentAbsorber.
   Properti ini memerlukan objek TextSearchOptions: berikan nilai true ke konstruktornya saat membuat objek baru.
3. Untuk mengambil teks yang cocok dari semua halaman, panggil metode [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) dari koleksi [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection).

   TextFragmentAbsorber mengembalikan TextFragmentCollection yang berisi semua fragmen yang sesuai dengan kriteria yang ditentukan oleh ekspresi reguler.

Cuplikan kode berikut menunjukkan cara mencari semua halaman dalam dokumen dan mendapatkan teks berdasarkan ekspresi reguler.

```java
// Buka dokumen
Document pdfDocument = new Document("source.pdf");

// Buat objek TextAbsorber untuk menemukan semua instance dari frasa pencarian yang dimasukkan
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // seperti 1999-2000

// Setel opsi pencarian teks untuk menentukan penggunaan ekspresi reguler
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

// Terima penyerap untuk halaman pertama dokumen
pdfDocument.getPages().accept(textFragmentAbsorber);

// Dapatkan fragmen teks yang diekstrak ke dalam koleksi
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// Loop melalui fragmen
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("Teks :- " + textFragment.getText());
    System.out.println("Posisi :- " + textFragment.getPosition());
    System.out.println("XIndentasi :- " + textFragment.getPosition().getXIndent());
    System.out.println("YIndentasi :- " + textFragment.getPosition().getYIndent());
    System.out.println("Font - Nama :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("Font - Dapat Diakses :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("Font - Tertanam :- " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("Font - Subset :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("Ukuran Font :- " + textFragment.getTextState().getFontSize());
    System.out.println("Warna Depan :- " + textFragment.getTextState().getForegroundColor());
}
```


Untuk mencari teks pada halaman tertentu dan mendapatkan propertinya, tentukan indeks halaman:

```java
// Terima absorber untuk halaman pertama dokumen.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber)
```

Untuk mencari string baik dalam huruf besar atau kecil, Anda dapat mempertimbangkan menggunakan ekspresi reguler.

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));
```

Contoh:

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[\\S]+");
```