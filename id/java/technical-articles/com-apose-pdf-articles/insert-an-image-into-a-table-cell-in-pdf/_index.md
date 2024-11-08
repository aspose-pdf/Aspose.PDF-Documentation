---
title: Menyisipkan Gambar ke dalam Sel Tabel di PDF
type: docs
weight: 20
url: /id/java/insert-an-image-into-a-table-cell-in-pdf/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Tabel adalah elemen penting untuk menampilkan data. Mereka menyediakan format yang presentable untuk representasi data. Tabel sering digunakan untuk menampilkan informasi numerik. Aspose.PDF API menyediakan kelas, Table, yang menawarkan Anda kemampuan untuk membuat tabel dalam file PDF.

Daripada membuat tabel sederhana, Anda dapat mengatur berbagai opsi pemformatan, misalnya gaya batas tabel, informasi margin, perataan, warna latar belakang, lebar kolom, informasi judul, nilai baris yang akan diulang di setiap halaman, dan banyak lagi.

{{% /alert %}}

## Pendekatan Aspose.PDF

Menurut DOM (Document Object Model) kami, sebuah dokumen terdiri dari Halaman.
 Sebuah halaman berisi satu atau lebih paragraf, dan sebuah paragraf dapat berupa gambar, teks, bidang formulir, judul, kotak mengambang, grafik, lampiran, atau tabel. Sebuah tabel, pada gilirannya, memiliki kumpulan baris dan setiap baris memiliki kumpulan sel. Sebuah sel adalah kumpulan paragraf.

Jadi menurut DOM kami, sebuah sel tabel dapat berisi salah satu elemen paragraf yang disebutkan di atas, termasuk gambar.

## Memahami Lebar Sel

Seseorang harus memiliki pemahaman yang jelas tentang lebar sel, terutama ketika menampilkan gambar di sel tabel, sehingga lebar gambar diperbaiki sesuai dengan lebar sel sehingga ditampilkan dengan benar. Lebar gambar dapat diatur dengan menggunakan metode setFixedWidth() dari kelas Image.

## Contoh Kode

```java

 String dataDir = "C:\\temp\\";

//Instansiasi objek Document dengan memanggil konstruktor kosongnya

Document pdfDocument = new Document();

//Buat halaman dalam objek Document

com.aspose.pdf.Page page = pdfDocument.getPages().add();



//Instansiasi objek tabel

Table table = new Table();

//Tambahkan tabel dalam koleksi paragraf dari halaman yang diinginkan

page.getParagraphs().add(table);

//Atur lebar kolom tabel

table.setColumnWidths("100 100 120");



//Atur batas tabel menggunakan objek BorderInfo lain yang disesuaikan

table.setDefaultCellBorder(new BorderInfo(BorderSide.All, 1F));



//Buat objek gambar di halaman

com.aspose.pdf.Image img1 = new com.aspose.pdf.Image();

//Atur jalur file gambar

img1.setFile(dataDir + "logo.jpg");



img1.setFixWidth(100);

img1.setFixHeight(100);

//Buat baris dalam tabel dan kemudian sel dalam baris

Row row1 = table.getRows().add();

row1.getCells().add("Teks contoh dalam sel");

// Tambahkan sel yang berisi gambar

Cell cell2 = row1.getCells().add();

//Tambahkan gambar ke sel tabel

cell2.getParagraphs().add(img1);



row1.getCells().add("Sel sebelumnya dengan gambar");

row1.getCells().get_Item(2).setVerticalAlignment(VerticalAlignment.Center);



//Simpan dokumen

pdfDocument.save(dataDir + "Image_in_Cell.pdf");    

```