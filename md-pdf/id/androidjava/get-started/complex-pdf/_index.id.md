---
title: Membuat PDF kompleks menggunakan Aspose.PDF
linktitle: Membuat PDF kompleks
type: docs
weight: 30
url: /androidjava/complex-pdf-example/
description: Aspose.PDF untuk Android melalui Java memungkinkan Anda membuat dokumen yang lebih kompleks yang berisi gambar, fragmen teks, dan tabel dalam satu dokumen.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Contoh [Hello, World](/pdf/java/hello-world-example/) menunjukkan langkah-langkah sederhana untuk membuat dokumen PDF menggunakan Java dan Aspose.PDF. Dalam artikel ini, kita akan melihat cara membuat dokumen yang lebih kompleks dengan Java dan Aspose.PDF untuk Java. Sebagai contoh, kita akan mengambil dokumen dari perusahaan fiktif yang mengoperasikan layanan feri penumpang.
Dokumen kita akan berisi gambar, dua fragmen teks (header dan paragraf), dan sebuah tabel. Untuk membangun dokumen seperti itu, kita akan menggunakan pendekatan berbasis DOM. Anda dapat membaca lebih lanjut di bagian [Dasar-dasar API DOM](/pdf/java/basics-of-dom-api/).

Jika kita membuat dokumen dari awal, kita perlu mengikuti langkah-langkah tertentu:

1. Instansiasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document). Pada langkah ini kita akan membuat dokumen PDF kosong dengan beberapa metadata tetapi tanpa halaman.
1. Tambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) ke objek dokumen. Jadi, sekarang dokumen kita akan memiliki satu halaman.
1. Untuk menambahkan Gambar, kita membuat FileInputStream, menunjukkan jalur ke file yang kita butuhkan. Kemudian kita tambahkan gambar ke persegi panjang dengan koordinat yang diberikan.
1. Buat [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) untuk header. Untuk header kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.
1. Tambahkan header ke [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--) halaman.
1. Buat [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) untuk deskripsi. Untuk deskripsi kita akan menggunakan font Arial dengan ukuran font 24pt dan perataan tengah.

1. Tambahkan (deskripsi) ke Paragraf halaman. Kami menggunakan font "Helvetica" dan "Times Roman" dalam contoh kami, tetapi ingat bahwa hanya ada tiga font sistem luas di Android:

- normal (Droid Sans);
- serif (Droid Serif);
- monospace (Droid Sans Mono).

1. Buat tabel, tambahkan properti tabel.
1. Tambahkan (tabel) ke halaman [Paragraf](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getParagraphs--).
1. Simpan dokumen "Complex.pdf".

Pada akhirnya, sebuah pop-up ditampilkan dengan pesan "Dokumen PDF telah dibuat!".

![Contoh Kompleks dari Aspose.PDF untuk Android melalui Java](complex_example.png)

```java
package com.aspose.pdf.examplecomplex;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Environment;
import android.widget.Button;
import android.widget.Toast;

import com.aspose.pdf.BorderInfo;
import com.aspose.pdf.BorderSide;
import com.aspose.pdf.Cell;
import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.FontRepository;
import com.aspose.pdf.HorizontalAlignment;
import com.aspose.pdf.Page;
import com.aspose.pdf.Position;
import com.aspose.pdf.Rectangle;
import com.aspose.pdf.Row;
import com.aspose.pdf.Table;
import com.aspose.pdf.TextFragment;

import java.io.File;
import java.io.FileInputStream;
import java.time.Duration;
import java.time.LocalTime;

public class MainActivity extends AppCompatActivity {

    Button generate_button;
    File myExternalFile;
    String filepath;
    String filename;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        generate_button = (Button) findViewById(R.id.button);
        generate_button.setOnClickListener(v->RunComplexExample());

        if(!isExternalStorageAvailable()||isExternalStorageReadOnly()){
            generate_button.setEnabled(false);
        }
        else{
            filepath = "MyFileStorage";
            filename = "SampleFile.pdf";
            myExternalFile=new File(getExternalFilesDir(filepath), filename);
        }

    }

    private void RunComplexExample() {
        // Inisialisasi objek dokumen
        Document document = new Document();

        // Tambahkan halaman
        Page page = document.getPages().add();

        // Tambahkan gambar
        java.io.FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream("/storage/0F03-0F02/Android/data/com.aspose.pdf.examplecomplex/files/MyFileStorage/logo.png");
        } catch (Exception e) {
            e.printStackTrace();
        }

        // Tambahkan gambar ke halaman
        page.addImage(imageStream, new Rectangle(20, 730, 120, 830));

        // Tambahkan Header
        TextFragment header = new TextFragment("Rute feri baru pada Musim Gugur 2020");
        header.getTextState().setFont(FontRepository.findFont("Helvetica"));
        header.getTextState().setFontSize(24);
        header.setHorizontalAlignment (HorizontalAlignment.Center);
        header.setPosition(new Position(130, 720));
        page.getParagraphs().add(header);

        // Tambahkan deskripsi
        String descriptionText = "Pengunjung harus membeli tiket secara online dan tiket " +
                "dibatasi hingga 5.000 per hari. Layanan feri beroperasi pada kapasitas setengah dan" +
                " dengan jadwal yang dikurangi. Harapkan antrian.";

        TextFragment description = new TextFragment(descriptionText);
        description.getTextState().setFont(FontRepository.findFont("Helvetica"));
        description.getTextState().setFontSize(14);
        description.setHorizontalAlignment(HorizontalAlignment.Left);
        page.getParagraphs().add(description);


        // Tambahkan tabel
        Table table = new Table();
        table.setColumnWidths("200");
        table.setBorder(new BorderInfo(BorderSide.Box, 1f, Color.getDarkSlateGray()));
        table.setDefaultCellBorder(new BorderInfo(BorderSide.Box, 0.5f, Color.getBlack()));
        table.getMargin().setBottom(10);
        table.getDefaultCellTextState().setFont(FontRepository.findFont("Times Roman"));

        Row headerRow = table.getRows().add();
        headerRow.getCells().add("Berangkat dari Kota");
        headerRow.getCells().add("Berangkat dari Pulau");


        for (Cell headerRowCell : (Iterable<? extends Cell>) headerRow.getCells())
        {
            headerRowCell.setBackgroundColor(Color.getGray());
            headerRowCell.getDefaultCellTextState()
                    .setForegroundColor(Color.getWhiteSmoke().toRgb());
        }

        LocalTime time = LocalTime.of(6,0);
        Duration incTime = Duration.ofMinutes(30);

        for (int i = 0; i < 10; i++)
        {
            Row dataRow = table.getRows().add();
            dataRow.getCells().add(time.toString());
            time=time.plus(incTime);
            dataRow.getCells().add(time.toString());
        }

        page.getParagraphs().add(table);

        document.save("/storage/0F03-0F02/Android/data/com.aspose.pdf.examplecomplex/files/MyFileStorage/sample.pdf");

        Toast toast = Toast.makeText(MainActivity.this,
                "Dokumen PDF telah dibuat!", Toast.LENGTH_LONG);
        toast.show();
    }

    private static boolean isExternalStorageReadOnly(){
        String extStorageState= Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED_READ_ONLY.equals(extStorageState);
    }

    private static boolean isExternalStorageAvailable(){
        String extStorageState=Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED.equals(extStorageState);
    }

}
```


```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="32dp"
        android:layout_marginLeft="32dp"
        android:layout_marginRight="32dp"
        android:text="@string/title"
        android:textSize="24sp"
        android:visibility="visible"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Button
        android:id="@+id/button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="64dp"
        android:layout_marginLeft="32dp"
        android:layout_marginRight="32dp"
        android:text="@string/generate_btn" />

</LinearLayout>
```