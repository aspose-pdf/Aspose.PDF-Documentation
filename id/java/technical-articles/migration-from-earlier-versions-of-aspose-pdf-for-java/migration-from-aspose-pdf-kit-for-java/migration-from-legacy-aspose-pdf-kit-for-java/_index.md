---
title: Migrasi dari Aspose.Pdf.Kit untuk Java yang lama
type: docs
weight: 10
url: id/java/migration-from-legacy-aspose-pdf-kit-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Komponen Aspose.PDF.Kit untuk Java saat ini menyediakan fitur untuk memanipulasi file PDF yang sudah ada. Namun, dalam waktu dekat, komponen ini akan dihentikan sebagai produk terpisah karena kami telah mem-porting semua kelas dan enumerasi di bawah paket **com.aspose.pdf.facades** dari rilis autoported baru Aspose.PDF untuk Java (4.x.x). Sekarang rilis autoported tunggal ini menyediakan kemampuan untuk membuat serta memanipulasi file PDF yang sudah ada.

{{% /alert %}}

## Dukungan untuk kode lama

Selama seluruh kegiatan migrasi, kami telah mempertimbangkan dampak kegiatan ini terhadap pelanggan yang ada dan kami telah berusaha semaksimal mungkin untuk meminimalkan dampak ini sejauh mungkin.
 Lebih lanjut, kami juga berfokus pada membuat rilis autoported baru yang kompatibel ke belakang sehingga basis kode pelanggan yang ada memerlukan perubahan minimal. Meskipun rilis autoported baru menyediakan Document Object Model (DOM) di bawah paket com.aspose.pdf untuk membuat serta memanipulasi file PDF yang ada, tetapi jika Anda ingin terus menggunakan kode warisan yang dikembangkan dengan Aspose.PDF.Kit untuk Java, Anda hanya perlu mengimpor paket **com.aspose.pdf.facades** dan kode Anda harus berfungsi (*kecuali untuk memperbarui referensi kelas eksplisit*).

Cuplikan kode berikut menunjukkan kepada Anda bagaimana menjalankan kode Aspose.PDF.Kit untuk Java yang ada dengan Aspose.PDF untuk Java yang baru di-autoport.

```java

import com.aspose.pdf.facades.*;

public class template {

    public static void main(String[] args) {

        try{

            // memuat file PDF yang ada

            com.aspose.pdf.facades.PdfFileInfo fileInfo = new com.aspose.pdf.facades.PdfFileInfo("input.pdf");

            System.out.println("TITLE: " + fileInfo.getTitle());

            System.out.println("AUTHOR:" + fileInfo.getAuthor());

            System.out.println("CREATIONDATE:" + fileInfo.getCreationDate());

            System.out.println("CREATOR:" + fileInfo.getCreator());

            System.out.println("KeyWORDS:" + fileInfo.getKeywords());

            System.out.println("MODDATE:" + fileInfo.getModDate());

           }


catch(Exception ex)


{System.out.println(ex);}


}

}
```

## Menggunakan Kelas ReplaceTextStrategy

Untuk memigrasikan kode untuk kelas ReplaceTextStrategy, metode **setScope(..)** telah diperbarui menjadi **setReplaceScope(..)**. Silakan lihat potongan kode berikut.

```java

 // membuat objek PdfContentEditor

com.aspose.pdf.facades.PdfContentEditor editor = new com.aspose.pdf.facades.PdfContentEditor();

// mengikat file PDF sumber

editor.bindPdf("input.pdf");

// membuat strategi penggantian teks

com.aspose.pdf.facades.ReplaceTextStrategy strategy = new com.aspose.pdf.facades.ReplaceTextStrategy();

// mengatur penjajaran untuk penggantian teks

strategy.setAlignment(com.aspose.pdf.facades.AlignmentType.Left);

// lingkup untuk penggantian teks

strategy.setReplaceScope(com.aspose.pdf.facades.ReplaceTextStrategy.Scope.REPLACE_ALL);

// mengatur strategi penggantian

editor.setReplaceTextStrategy(strategy);

editor.replaceText("test","replaced");

// menyimpan file yang diperbarui

editor.save("TxtReplaceTest.pdf");
```