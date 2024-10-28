---
title: Create Document
type: docs
weight: 10
url: /java/create-pdf-document/
description: Aspose.PDF untuk Java membantu Anda membuat dokumen PDF dan file PDF yang dapat dicari dalam beberapa langkah mudah.
lastmod: "2021-06-05"
---

Dalam artikel ini, kami akan menunjukkan cara menggunakan Aspose.PDF untuk Java API untuk dengan mudah menghasilkan dan membaca file PDF dalam aplikasi Java.

Aspose.PDF untuk Java API memungkinkan pengembang aplikasi Java untuk menyematkan fungsionalitas pemrosesan dokumen PDF dalam aplikasi mereka. Ini dapat digunakan untuk membuat dan membaca file PDF tanpa memerlukan perangkat lunak lain yang terpasang pada mesin dasar. Aspose.PDF untuk Java dapat digunakan dalam berbagai jenis aplikasi Java seperti aplikasi Desktop, JSP, dan JSF.

## Cara Membuat File PDF menggunakan Java

Untuk membuat file PDF menggunakan Java, langkah-langkah berikut dapat digunakan.

1. Buat objek dari kelas [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)

1. Tambahkan objek [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page) ke koleksi Pages dari objek Document
1. Tambahkan [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) ke koleksi [Paragraphs](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/paragraphs) pada halaman
1. Simpan dokumen PDF yang dihasilkan

```java
package com.aspose.pdf.examples;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Scanner;

import javax.imageio.ImageIO;

import com.aspose.pdf.*;
import com.aspose.pdf.Document.CallBackGetHocr;

public class ExampleCreate {
    
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";
    
    public static void Create() {        
        Document document = new Document();
 
        //Tambahkan halaman
        Page page = document.getPages().add();
         
        // Tambahkan teks ke halaman baru
        page.getParagraphs().add(new TextFragment("Hello World!"));
         
        // Simpan PDF yang diperbarui
        document.save(_dataDir+"HelloWorld_out.pdf");
    }
```


Dalam kasus ini, kita membuat dokumen satu halaman PDF dengan ukuran halaman A4, orientasi potret. Halaman kita akan berisi "Hello, World" di bagian kiri atas halaman.

Juga, Aspose.PDF untuk Java menyediakan kemampuan untuk membuat bagaimana cara membuat PDF yang dapat dicari. Mari kita pelajari cuplikan kode berikut:

```java
public static void CreateSearchablePDF() {                
        Document doc = new Document(_dataDir + "sample1.pdf");
        
        // Buat callBack - logika mengenali teks untuk gambar pdf. Gunakan OCR luar yang mendukung standar HOCR(http://en.wikipedia.org/wiki/HOCR).
        // Kami telah menggunakan google tesseract OCR gratis(http://en.wikipedia.org/wiki/Tesseract_%28software%29)
        
        CallBackGetHocr cbgh = new CallBackGetHocr() {
            @Override
            public String invoke(java.awt.image.BufferedImage img) {
                File outputfile = new File(_dataDir + "test.jpg");
                try {
                    ImageIO.write(img, "jpg", outputfile);
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
        
                try {
                    java.lang.Process process = Runtime.getRuntime().exec("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    System.out.println("tesseract" + " " + _dataDir + "test.jpg" + " " + _dataDir + "out hocr");
                    process.waitFor();
        
                } catch (IOException e) {
                    e.printStackTrace();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
        
                // membaca out.html ke string
                File file = new File(_dataDir + "out.hocr");
                StringBuilder fileContents = new StringBuilder((int) file.length());
                Scanner scanner = null;
                try {
                    scanner = new Scanner(file);
                    String lineSeparator = System.getProperty("line.separator");
        
                    while (scanner.hasNextLine()) {
                        fileContents.append(scanner.nextLine() + lineSeparator);
                    }
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                } finally {
                    if (scanner != null)
                        scanner.close();
                }
        
                // menghapus file sementara
                File fileOut = new File(_dataDir + "out.hocr");
                if (fileOut.exists()) {
                    fileOut.delete();
                }
                File fileTest = new File(_dataDir + "test.jpg");
                if (fileTest.exists()) {
                    fileTest.delete();
                }
        
                return fileContents.toString();
            }
        };
        // Akhir callBack
        
        doc.convert(cbgh);
        doc.save(_dataDir + "output971.pdf");        
    }
}
```