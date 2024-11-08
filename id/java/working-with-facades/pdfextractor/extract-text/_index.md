---
title: Ekstrak Gambar dari PDF (facades)
type: docs
weight: 30
url: /id/java/extract-images/
description: Bagian ini menjelaskan cara mengekstrak gambar dengan Aspose.PDF Facades menggunakan Kelas PdfExtractor.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Kelas [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) memungkinkan Anda untuk mengekstrak gambar dari file PDF.
 First off, you need to create an object of [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) class and bind input PDF file using bindPdf method. After that, call [extractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--) method to extract all the images into memory. Once the images are extracted, you can get those images with the help of hasNextImage and getNextImage methods. You need to loop through all the extracted images using a while loop. In order to save the images to disk, you can call the overload of the getNextImage method which takes file path as argument. The following code snippet shows you how to extract images from the whole PDF to files.

Pertama, Anda perlu membuat objek dari kelas [PdfExtractor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor) dan mengikat file PDF input menggunakan metode bindPdf. Setelah itu, panggil metode [extractImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractImage--) untuk mengekstrak semua gambar ke dalam memori. Setelah gambar diekstraksi, Anda dapat mendapatkan gambar-gambar tersebut dengan bantuan metode hasNextImage dan getNextImage. Anda perlu melakukan loop melalui semua gambar yang diekstraksi menggunakan loop while. Untuk menyimpan gambar ke disk, Anda dapat memanggil overload dari metode getNextImage yang mengambil jalur file sebagai argumen. Cuplikan kode berikut menunjukkan cara mengekstrak gambar dari seluruh PDF ke file.

```java   
public static void ExtractImages()
 {
    //Create an extractor and bind it to the document
    //Buat ekstraktor dan ikat ke dokumen
    Document document = new Document(_dataDir + "sample.pdf");
    PdfExtractor extractor = new PdfExtractor(document);
    extractor.setStartPage(1);
    extractor.setEndPage(3);            

    //Run the extractor
    //Jalankan ekstraktor
    extractor.extractImage();
    int imageNumber = 1;
    //Iterate througth extracted images collection
    //Iterasi melalui koleksi gambar yang diekstraksi
    while (extractor.hasNextImage())
    {
        //Retrieve image from collection and save it in a file 
        //Ambil gambar dari koleksi dan simpan dalam file
        extractor.getNextImage(_dataDir + String.format("image%03d.png", imageNumber++),ImageType.getPng());
    }
}
```