---
title: Contoh Java Hello World
linktitle: Contoh Hello World
type: docs
weight: 20
url: /androidjava/hello-world-example/
description: Halaman ini menunjukkan bagaimana menggunakan pemrograman sederhana untuk membuat dokumen PDF yang berisi teks - Hello World menggunakan Aspose.PDF untuk Android.
lastmod: "2021-08-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Contoh Hello World

Contoh "Hello World" secara tradisional digunakan untuk memperkenalkan fitur-fitur dari bahasa pemrograman atau perangkat lunak dengan kasus penggunaan sederhana.

Aspose.PDF untuk Android melalui Java API memungkinkan pengembang aplikasi Java untuk membuat, membaca, mengedit, dan memanipulasi file PDF dalam aplikasi mereka. Ini memungkinkan Anda membaca dan mengonversi beberapa jenis file yang berbeda ke dan dari format file PDF. Artikel Hello World ini menunjukkan bagaimana membuat file PDF di Java menggunakan Aspose.PDF untuk Android melalui Java API.
Setelah [meninstal Aspose.PDF untuk Android melalui Java](/pdf/androidjava/installation/) di lingkungan Anda, Anda dapat menjalankan contoh kode di bawah ini untuk melihat bagaimana API Aspose.PDF bekerja.

Cuplikan kode di bawah ini mengikuti langkah-langkah berikut:

1. Instansiasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Tambahkan [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page) ke objek dokumen
1. Buat objek [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment)
1. Tambahkan TextFragment ke koleksi [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) dari halaman
1. Simpan dokumen PDF yang dihasilkan

Cuplikan kode berikut menunjukkan langkah-langkah dasar kerja Aspose.PDF untuk API Android.

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
                // Inisialisasi objek dokumen
                Document document = new Document();

                // Tambah halaman
                Page page = document.getPages().add();

                myData = inputText.getText().toString().trim();
                if (myData.equals("")) {
                    myData = "Hello, world!";
                }

                // Tambahkan teks ke halaman baru
                page.getParagraphs().add(new TextFragment(myData));

                // Simpan PDF yang diperbarui
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
                // Inisialisasi objek dokumen
                Document document = new Document(myExternalFile.getAbsolutePath());
                myData = "Dokumen berisi "+document.getPages().size()+" halaman.";
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