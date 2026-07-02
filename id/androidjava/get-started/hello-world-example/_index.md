---
title: Contoh Hello World Java
linktitle: Contoh Hello World
type: docs
weight: 20
url: /id/androidjava/hello-world-example/
description: Halaman ini menunjukkan cara menggunakan pemrograman sederhana untuk membuat dokumen PDF yang berisi teks - Hello World menggunakan Aspose.PDF untuk Android.
lastmod: "2026-07-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Contoh Hello World

Contoh \"Hello World\" secara tradisional digunakan untuk memperkenalkan fitur-fitur bahasa pemrograman atau perangkat lunak dengan kasus penggunaan yang sederhana.

Aspose.PDF untuk Android melalui Java API memberdayakan pengembang aplikasi Java untuk membuat, membaca, mengedit, dan memanipulasi file PDF dalam aplikasi mereka. Ini memungkinkan Anda membaca dan mengonversi beberapa jenis file yang berbeda ke dan dari format file PDF. Artikel Hello World ini menunjukkan cara membuat file PDF dalam Java menggunakan Aspose.PDF untuk Android melalui Java API.
Setelah [menginstal Aspose.PDF untuk Android melalui Java](/pdf/id/androidjava/installation/) di lingkungan Anda, Anda dapat menjalankan contoh kode di bawah ini untuk melihat cara kerja API Aspose.PDF.

Potongan kode di bawah ini mengikuti langkah-langkah berikut:

1. Instansiasi sebuah [Dokumen](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) objek
1. Tambahkan sebuah [Halaman](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) ke objek dokumen
1. Buat sebuah [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) objek
1. Tambahkan TextFragment ke [Paragraf](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) koleksi halaman
1. Simpan dokumen PDF yang dihasilkan

Potongan kode berikut menunjukkan langkah-langkah dasar cara kerja API Aspose.PDF untuk Android.

```java
package com.aspose.pdf.examplesimple;

import android.app.Activity;
import android.os.Bundle;
import android.os.Environment;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.TextFragment;

import java.io.File;


public class MainActivity extends Activity {
    EditText inputText;
    TextView response;
    Button saveButton,readButton;

    File myExternalFile;
    String myData = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputText = (EditText) findViewById(R.id.myInputText);
        response = (TextView) findViewById(R.id.response);


        saveButton =
                (Button) findViewById(R.id.saveExternalStorage);
        saveButton.setOnClickListener(v -> {
            try {
                // Initialize document object
                Document document = new Document();

                //Add page
                Page page = document.getPages().add();

                myData = inputText.getText().toString().trim();
                if (myData.equals("")) {
                    myData = "Hello, world!";
                }

                // Add text to new page
                page.getParagraphs().add(new TextFragment(myData));

                // Save updated PDF
                document.save(myExternalFile.getAbsolutePath());

            } catch (Exception e) {
                e.printStackTrace();
            }
            inputText.setText("");
            response.setText(R.string.save_message);
        });

        readButton = (Button) findViewById(R.id.getExternalStorage);
        readButton.setOnClickListener(v -> {
            try {
                // Initialize document object
                Document document = new Document(myExternalFile.getAbsolutePath());
                myData = "Document contain "+document.getPages().size()+" page(s).";
            } catch (Exception e) {
                e.printStackTrace();
            }
            inputText.setText(myData);
            response.setText(R.string.read_message);
        });

        if (!isExternalStorageAvailable() || isExternalStorageReadOnly()) {
            saveButton.setEnabled(false);
        }
        else {
            String filename = "SampleFile.pdf";
            String filepath = "MyFileStorage";
            myExternalFile = new File(getExternalFilesDir(filepath), filename);
        }
    }
    private static boolean isExternalStorageReadOnly() {
        String extStorageState = Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED_READ_ONLY.equals(extStorageState);
    }

    private static boolean isExternalStorageAvailable() {
        String extStorageState = Environment.getExternalStorageState();
        return Environment.MEDIA_MOUNTED.equals(extStorageState);
    }
}
```

