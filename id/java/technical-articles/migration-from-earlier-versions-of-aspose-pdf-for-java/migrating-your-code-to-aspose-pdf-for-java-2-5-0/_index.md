---
title: Memigrasikan kode Anda ke Aspose.PDF untuk Java 2.5.0
type: docs
weight: 10
url: id/java/migrating-your-code-to-aspose-pdf-for-java-2-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Dalam artikel ini kami mencoba menyoroti beberapa area dari kode yang ada dari Aspose.PDF untuk Java agar kompatibel dengan versi rilis terbaru.

{{% /alert %}}

## Detail

Dengan rilis Aspose.PDF untuk Java 2.5.0, terdapat banyak perubahan dalam struktur API dan konstruksi kelas. Sebagian besar nama anggota kelas diperbarui, beberapa anggota kelas yang ada dihapus dan juga beberapa metode dan properti baru ditambahkan ke kelas yang ada. Untuk memberikan gambaran singkat tentang perubahan, kami akan melihat kode sederhana berikut, berdasarkan versi Aspose.PDF untuk Java yang diterbitkan sebelum 2.5.0.

Dalam kode sederhana ini, kami akan menambahkan hyperlink dan tautan ke halaman dalam dokumen PDF yang sama.

```java
import com.aspose.pdf.elements.*;
com.aspose.pdf.License lic = new com.aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}


//Memulai objek Pdf dengan memanggil konstruktor kosongnya

Pdf pdf1 = new Pdf();

//Membuat sebuah bagian dalam objek Pdf

Section sec1 = pdf1.getSections().add();

//Membuat paragraf teks dengan referensi dari sebuah bagian

Text text1 = new Text(sec1);

//Menambahkan paragraf teks ke dalam koleksi paragraf dari bagian tersebut

sec1.getParagraphs().add(text1);

//Menambahkan segmen teks dalam paragraf teks

Segment segment1 = text1.getSegments().add("ini adalah tautan lokal");

//Mengatur teks dalam segmen teks untuk digarisbawahi

segment1.getTextInfo().setUnderLine(true);


//Mengatur tipe tautan dari segmen teks ke Lokal

//Menetapkan id dari paragraf yang diinginkan sebagai id target untuk segmen teks

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

//Membuat paragraf teks untuk ditautkan dengan segmen teks

Text text3 = new Text(sec1,"informasi produk 1 ...");

//Menambahkan paragraf teks ke koleksi paragraf dari bagian tersebut

sec1.getParagraphs().add(text3);

//Mengatur paragraf ini menjadi yang pertama agar dapat ditampilkan di halaman terpisah

//dalam dokumen

text3.setFirstParagraph(true);

//Mengatur id dari segmen teks ini menjadi "product1"

text3.setID("product1"); 


// menyimpan file PDF

FileOutputStream out = new FileOutputStream(new File("UpdateOfCode_Test.pdf"));

pdf1.save(out);
```


Ketika menggunakan versi sebelum Aspose.PDF untuk Java 2.5.0, kode dapat berhasil dieksekusi dan dokumen PDF hasil yang mengandung hyperlink menuju halaman dalam dokumen yang sama, dapat dihasilkan. Namun, ketika kode yang sama dikompilasi dengan 2.5.0, Anda akan melihat sejumlah kesalahan karena telah terjadi perubahan dalam anggota kelas dan juga beberapa metode dalam kelas telah dihapus. Sekarang mari kita mulai dengan modifikasi kode untuk versi 2.5.0

Gunakan `import aspose.pdf.*`; alih-alih `import com.aspose.pdf.elements.*`; untuk menyertakan paket.

Untuk inisialisasi lisensi, silakan perbarui kode Anda yang ada dari

{{% alert color="primary" %}}
**com.aspose.pdf.License lic = new com.aspose.pdf.License();**

```java

try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```

{{% /alert %}}

menjadi

{{% alert color="primary" %}}
**aspose.pdf.License lic = new aspose.pdf.License();**

```java

try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```


{{% /alert %}}

**TextInfo** tidak lagi mengandung metode **setUnderLine(...)**. Silakan coba gunakan **TextInfo.setIsUnderline(...)** ** sebagai gantinya **.**

Kelas bernama **HyperLinkToLocalPdf** telah dihapus. Jadi, silakan perbarui kode Anda yang ada seperti

{{% alert color="primary" %}}
**//Tetapkan jenis tautan dari segmen teks ke Lokal**

```java

 //Tetapkan id dari paragraf yang diinginkan sebagai id target untuk segmen teks

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

```

{{% /alert %}}

menjadi

{{% alert color="primary" %}}
**segment1.getHyperlink().setLinkType(HyperlinkType.Local);**

```java

 segment1.getHyperlink().setTargetID("product1");

```

{{% /alert %}}

Nama metode **setFirstParagraph** dihapus dari kelas Text.
 Jadi untuk menampilkan segmen teks di halaman baru, Anda perlu membuat objek Section baru dan menambahkan objek teks ke section yang baru dibuat. Karena secara default setiap section ditampilkan di halaman baru, jadi tidak perlu memanggil metode seperti **sec2.setIsNewPage(true**)**;

## Metode Save yang Diperbarui

Metode save dalam kelas Pdf yang sebelumnya menggunakan objek FileOutputStream sebagai argumen, telah dihapus. Dalam versi baru, Anda dapat menggunakan salah satu dari metode save yang di-overload berikut.

- save(BasicStream stream)
- save(java.lang.String pdfFile)
- save(java.lang.String fileName, SaveType saveType, aspose.pdf.HttpResponse response)

Setelah membuat semua perubahan yang ditentukan di atas, ketika menggunakan Aspose.PDF untuk Java 2.5.0, kode akan dikompilasi dan dijalankan tanpa menampilkan pesan kesalahan. Potongan kode yang diperbarui lengkap ditentukan di bawah ini.

```java
import aspose.pdf.*;
aspose.pdf.License lic = new aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}

try {

//Instansiasi objek Pdf dengan memanggil konstruktor kosongnya

Pdf pdf1 = new Pdf();

//Buat section dalam objek Pdf

Section sec1 = pdf1.getSections().add();

//Buat paragraf teks dengan referensi pada section

Text text1 = new Text(sec1);

//Tambahkan paragraf teks dalam koleksi paragraf dari section

sec1.getParagraphs().add(text1);

//Tambahkan segmen teks dalam paragraf teks

Segment segment1 = text1.getSegments().add("ini adalah tautan lokal");

//Setel teks dalam segmen teks agar digarisbawahi

segment1.getTextInfo().setIsUnderline(true);


//Setel tipe tautan dari segmen teks ke Lokal

//Tetapkan id dari paragraf yang diinginkan sebagai target id untuk segmen teks

segment1.getHyperlink().setLinkType(HyperlinkType.Local);

segment1.getHyperlink().setTargetID("product1");

// tambahkan section baru yang akan memegang objek teks dengan ID "Product 1"

Section sec2 = pdf1.getSections().add();

//Buat paragraf teks untuk dihubungkan dengan segmen teks

Text text3 = new Text(sec1,"info produk 1 ...");

//Tambahkan paragraf teks ke koleksi paragraf dari section

sec2.getParagraphs().add(text3);

//Tetapkan id dari segmen teks ini ke "product1"

text3.setID("product1");


// simpan file PDF

pdf1.save("UpdateOfCode_Test.pdf");


     }catch(Exception e)

{

System.out.println(e.getMessage());

}
```

## Kesimpulan

Pada topik di atas, kami telah menjelaskan beberapa kelas dan metode yang telah diubah dalam rilis baru. Untuk daftar lengkap semua kelas dan anggotanya, silakan kunjungi [Aspose.PDF for Java API Reference](http://www.aspose.com/documentation/java-components/aspose.pdf-for-java/aspose.pdf-for-java-api-reference.html)

Untuk mempelajari lebih lanjut tentang Aspose dan produknya, silakan klik di sini <http://www.aspose.com/>