---
title: Dapatkan Resolusi dan Dimensi Gambar Tertanam
linktitle: Dapatkan Resolusi dan Dimensi
type: docs
weight: 40
url: id/java/get-resolution-and-dimensions-of-embedded-images/
description: Bagian ini menunjukkan detail dalam mendapatkan resolusi dan dimensi Gambar Tertanam
lastmod: "2021-06-05"
---

Topik ini menjelaskan cara menggunakan kelas operator dalam namespace Aspose.PDF yang menyediakan kemampuan untuk mendapatkan informasi resolusi dan dimensi tentang gambar tanpa harus mengekstraknya.

Ada berbagai cara untuk mencapai ini. Artikel ini menjelaskan cara menggunakan sebuah `arraylist` dan [kelas penempatan Gambar](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImagePlacement).

1. Pertama, muat file PDF sumber (dengan gambar).
1. Kemudian buat objek ArrayList untuk menyimpan nama gambar apa pun dalam dokumen.
1. Dapatkan gambar menggunakan properti Page.Resources.Images.
1. Buat objek stack untuk menyimpan keadaan grafik gambar dan gunakan untuk melacak berbagai keadaan gambar.

1. Buat objek ConcatenateMatrix yang mendefinisikan transformasi saat ini. Ini juga mendukung penskalaan, pemutaran, dan pemiringan konten apa pun. Ini menggabungkan matriks baru dengan yang sebelumnya. Harap dicatat bahwa kita tidak dapat mendefinisikan transformasi dari awal tetapi hanya memodifikasi transformasi yang ada.
1. Karena kita dapat memodifikasi matriks dengan ConcatenateMatrix, kita mungkin juga perlu kembali ke status gambar asli. Gunakan operator GSave dan GRestore. Operator-operator ini berpasangan sehingga harus dipanggil bersama. Misalnya, jika Anda melakukan beberapa pekerjaan grafis dengan transformasi kompleks dan akhirnya mengembalikan transformasi ke keadaan awal, pendekatannya akan seperti ini:

```java
// Menggambar beberapa teks
GSave

ConcatenateMatrix  // memutar konten setelah operator

// Beberapa pekerjaan grafis

ConcatenateMatrix // skala (dengan rotasi sebelumnya) konten setelah operator

// Beberapa pekerjaan grafis lainnya

GRestore

// Menggambar beberapa teks
```

Sebagai hasilnya, teks digambar dalam bentuk biasa tetapi beberapa transformasi dilakukan di antara operator teks.
 Untuk menampilkan gambar atau menggambar objek dan gambar bentuk, kita perlu menggunakan operator Do.

Kita juga memiliki kelas bernama XImage yang menyediakan dua properti, yaitu Width dan Height, yang dapat digunakan untuk mendapatkan dimensi gambar.

1. Lakukan beberapa perhitungan untuk menghitung resolusi gambar.
2. Tampilkan informasi di Command Prompt bersama dengan nama gambar.

Cuplikan kode berikut menunjukkan cara mendapatkan dimensi dan resolusi gambar tanpa mengekstrak gambar dari dokumen PDF.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.operators.*;
import java.util.*;

public class ExampleImagesResolution {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void ExampleAddPageNumber() 
    {
        // Memuat file PDF sumber
        Document doc = new Document(_dataDir+ "ImageInformation.pdf");
        
        // Mendefinisikan resolusi default untuk gambar
        int defaultResolution = 72;

        Stack<Object> graphicsState = new Stack<Object>();

        // Mendefinisikan objek daftar array yang akan menyimpan nama gambar
        List<String> imageNames = Arrays.asList(doc.getPages().get_Item(1).getResources().getImages().getNames());
        //ArrayList imageNames = new ArrayList<>(Arrays.asList(names));
        // Menyisipkan objek ke dalam stack
        graphicsState.push(new Matrix(1, 0, 0, 1, 0, 0));

        // Mendapatkan semua operator pada halaman pertama dokumen
        for (Operator op : doc.getPages().get_Item(1).getContents())
        {
            // Gunakan operator GSave/GRestore untuk mengembalikan transformasi ke sebelumnya yang diatur
            GSave opSaveState = (GSave) op;
            GRestore opRestoreState = (GRestore) op;
            // Memanggil objek ConcatenateMatrix karena mendefinisikan matriks transformasi saat ini.
            ConcatenateMatrix opCtm = (ConcatenateMatrix) op;
            // Membuat operator Do yang menggambar objek dari sumber daya. Ini menggambar objek Form dan objek Gambar
            Do opDo = (Do) op;

            if (opSaveState != null)
            {
                // Simpan keadaan sebelumnya dan dorong keadaan saat ini ke atas stack
                Matrix m = new Matrix((Matrix)graphicsState.peek());
                graphicsState.push(m);
            }
            else if (opRestoreState != null)
            {
                // Buang keadaan saat ini dan pulihkan yang sebelumnya
                graphicsState.pop();
            }
            else if (opCtm != null)
            {
                Matrix cm = new Matrix(
                (float)opCtm.getMatrix().getA(),
                (float)opCtm.getMatrix().getB(),
                (float)opCtm.getMatrix().getC(),
                (float)opCtm.getMatrix().getD(),
                (float)opCtm.getMatrix().getE(),
                (float)opCtm.getMatrix().getF());

                // Kalikan matriks saat ini dengan matriks keadaan
                ((Matrix)graphicsState.peek()).multiply(cm);

                continue;
            }
            else if (opDo != null)
            {
                // Jika ini adalah operator penggambaran gambar
                if (imageNames.contains(opDo.getName()))
                {
                    Matrix lastCTM = (Matrix)graphicsState.peek();
                    // Membuat objek XImage untuk menyimpan gambar halaman pertama pdf
                    XImage image = doc.getPages().get_Item(1).getResources().getImages().get_Item(opDo.getName());

                    // Mendapatkan dimensi gambar
                    double scaledWidth = Math.sqrt(Math.pow(lastCTM.getElements()[0], 2) + Math.pow(lastCTM.getElements()[1], 2));
                    double scaledHeight = Math.sqrt(Math.pow(lastCTM.getElements()[2], 2) + Math.pow(lastCTM.getElements()[3], 2));
                    // Mendapatkan informasi Tinggi dan Lebar gambar
                    double originalWidth = image.getWidth();
                    double originalHeight = image.getHeight();

                    // Menghitung resolusi berdasarkan informasi di atas
                    double resHorizontal = originalWidth * defaultResolution / scaledWidth;
                    double resVertical = originalHeight * defaultResolution / scaledHeight;

                    // Menampilkan informasi Dimensi dan Resolusi dari setiap gambar
                    System.out.printf(_dataDir + "gambar %s (%.2f:%.2f): res %.2f x %.2f",
                                        opDo.getName(), scaledWidth, scaledHeight, resHorizontal,
                                        resVertical);
                }
                // Menyimpan dokumen keluaran
                doc.save(_dataDir);
            }
        }
    }
}
```