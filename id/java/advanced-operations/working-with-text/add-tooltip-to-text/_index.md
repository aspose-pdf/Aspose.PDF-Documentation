---
title: Menggunakan Tooltip
linktitle: Tooltip PDF
type: docs
weight: 20
url: /id/java/pdf-tooltip/
description: Pelajari cara menambahkan tooltip ke fragmen teks dalam PDF menggunakan Java dan Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Tambahkan Tooltip ke Teks yang Dicari dengan Menambahkan Tombol Tak Terlihat

Seringkali diperlukan untuk menambahkan beberapa detail untuk frasa atau kata tertentu sebagai tooltip dalam dokumen PDF sehingga dapat muncul ketika pengguna mengarahkan kursor mouse ke teks. Aspose.PDF for Java menyediakan fitur ini untuk membuat tooltips dengan menambahkan tombol tak terlihat di atas teks yang dicari. Cuplikan kode berikut akan menunjukkan cara mencapai fungsi ini:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.ButtonField;
import com.aspose.pdf.Document;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.TextFragmentAbsorber;
import com.aspose.pdf.TextFragmentCollection;

public class ExampleToolTip {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddToolTip() {
        String outputFile = _dataDir + "Tooltip_out.pdf";

        // Buat dokumen contoh dengan teks
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("Arahkan kursor mouse di sini untuk menampilkan tooltip"));
        doc.getPages().get_Item(1).getParagraphs().add(new TextFragment("Arahkan kursor mouse di sini untuk menampilkan tooltip yang sangat panjang"));
        doc.save(outputFile);

        // Buka dokumen dengan teks
        Document document = new Document(outputFile);
        // Buat objek TextAbsorber untuk menemukan semua frasa yang cocok dengan ekspresi reguler
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("Arahkan kursor mouse di sini untuk menampilkan tooltip");
        // Terima absorber untuk halaman dokumen
        document.getPages().accept(absorber);
        // Dapatkan fragmen teks yang diekstraksi
        TextFragmentCollection textFragments = absorber.getTextFragments();

        // Loop melalui fragmen
        for(TextFragment fragment : textFragments)
        {
            // Buat tombol tak terlihat pada posisi fragmen teks
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // Nilai AlternateName akan ditampilkan sebagai tooltip oleh aplikasi viewer
            field.setAlternateName ("Tooltip untuk teks.");
            // Tambahkan field tombol ke dokumen
            document.getForm().add(field);
        }

        // Berikutnya akan menjadi contoh tooltip yang sangat panjang
        absorber = new TextFragmentAbsorber("Arahkan kursor mouse di sini untuk menampilkan tooltip yang sangat panjang");
        document.getPages().accept(absorber);
        textFragments = absorber.getTextFragments();

        for(TextFragment fragment : textFragments)
        {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // Setel teks yang sangat panjang
            field.setAlternateName ("Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        // Simpan dokumen
        document.save(outputFile);
    }
}
```


{{% alert color="primary" %}}

Mengenai panjang tooltip, teks tooltip terkandung dalam dokumen PDF sebagai tipe string PDF, di luar aliran konten. Tidak ada batasan efektif pada string tersebut dalam file PDF (Lihat PDF Reference Appendix C.). Namun, pembaca yang sesuai (misalnya Adobe Acrobat) yang berjalan pada prosesor tertentu dan dalam lingkungan operasi tertentu memang memiliki batasan tersebut. Silakan merujuk ke dokumentasi aplikasi pembaca PDF Anda.

{{% /alert %}}

## Membuat Blok Teks Tersembunyi dan Menampilkannya saat Mouse Ditarik

Dalam Aspose.PDF, fitur untuk menyembunyikan tindakan diimplementasikan di mana dimungkinkan untuk menampilkan/menyembunyikan bidang kotak teks (atau jenis anotasi lainnya) saat mouse memasuki/keluar dari beberapa tombol tak terlihat. Untuk tujuan ini, Aspose.Pdf.Annotations.HideAction Class digunakan untuk menetapkan tindakan sembunyi/tampilkan pada blok teks. Silakan gunakan potongan kode berikut untuk Menampilkan/Menyembunyikan Blok Teks saat Mouse Memasuki/Keluar.

Harap juga diperhatikan bahwa tindakan PDF dalam dokumen bekerja dengan baik pada pembaca yang sesuai (misalnya.
 Adobe Reader) tetapi tidak ada jaminan untuk pembaca PDF lainnya (misalnya, plugin peramban web). Kami telah melakukan investigasi singkat dan menemukan:

- Semua implementasi dari aksi sembunyi dalam dokumen PDF berfungsi dengan baik di Internet Explorer v.11.0.
- Semua implementasi dari aksi sembunyi juga berfungsi di Opera v.12.14, tetapi kami melihat ada beberapa penundaan respons pada pembukaan pertama dokumen.
- Hanya implementasi yang menggunakan konstruktor HideAction yang menerima nama bidang yang berfungsi jika Google Chrome v.61.0 membuka dokumen; Silakan gunakan konstruktor yang sesuai jika browsing di Google Chrome signifikan:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```java
    public static void name() {
        String outputFile = _dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

        // Buat dokumen contoh dengan teks
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("Pindahkan kursor mouse di sini untuk menampilkan teks melayang"));
        doc.save(outputFile);

        // Buka dokumen dengan teks
        Document document = new Document(outputFile);
        // Buat objek TextAbsorber untuk menemukan semua frasa yang cocok dengan ekspresi reguler
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("Pindahkan kursor mouse di sini untuk menampilkan teks melayang");
        // Terima absorber untuk halaman dokumen
        document.getPages().accept(absorber);
        // Dapatkan fragmen teks pertama yang diekstraksi
        TextFragmentCollection textFragments = absorber.getTextFragments();
        TextFragment fragment = textFragments.get_Item(1);

        // Buat bidang teks tersembunyi untuk teks melayang di persegi panjang yang ditentukan dari halaman
        TextBoxField floatingField = new TextBoxField(fragment.getPage(), new Rectangle(100, 700, 220, 740));
        // Tetapkan teks untuk ditampilkan sebagai nilai bidang
        floatingField.setValue("Ini adalah \"bidang teks melayang\".");
        // Kami merekomendasikan untuk membuat bidang 'readonly' untuk skenario ini
        floatingField.setReadOnly(true);

        // Tetapkan bendera 'hidden' untuk membuat bidang tidak terlihat saat dokumen dibuka
        floatingField.setFlags(floatingField.getFlags() | AnnotationFlags.Hidden);

        // Menetapkan nama bidang yang unik tidak perlu tetapi diperbolehkan
        floatingField.setPartialName("FloatingField_1");

        // Menetapkan karakteristik penampilan bidang tidak perlu tetapi membuatnya lebih baik
        DefaultAppearance da = new DefaultAppearance("Helvetica", 16, java.awt.Color.RED);
        floatingField.setDefaultAppearance(da);
        //new DefaultAppearance("Helv", 10, Color.getBlue()
        floatingField.getCharacteristics().setBackground(Color.getLightBlue());
        floatingField.getCharacteristics().setBorder(Color.getDarkBlue());
        floatingField.setBorder(new Border(floatingField));
        floatingField.getBorder().setWidth(1);
        floatingField.setMultiline(true);

        // Tambahkan bidang teks ke dokumen
        document.getForm().add(floatingField);

        // Buat tombol tak terlihat di posisi fragmen teks
        Field buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
        // Buat aksi sembunyi baru untuk bidang yang ditentukan (anotasi) dan bendera ketidaknampakan.
        // (Anda juga dapat merujuk ke bidang melayang dengan nama jika Anda menentukannya di atas.)
        // Tambahkan aksi saat mouse masuk/keluar di bidang tombol tak terlihat
        buttonField.getActions().setOnEnter(new HideAction(floatingField, false));
        buttonField.getActions().setOnExit(new HideAction(floatingField));

        // Tambahkan bidang tombol ke dokumen
        document.getForm().add(buttonField);

        // Simpan dokumen
        document.save(outputFile);
    }
```