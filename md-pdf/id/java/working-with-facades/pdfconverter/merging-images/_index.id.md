---
title: Menggabungkan gambar
type: docs
weight: 10
url: /java/merge-images/
description: Bagian ini menjelaskan cara menggabungkan gambar, dan dapat disimpan dalam format Tiff.
lastmod: "2021-07-01"
draft: false
---

Aspose.PDF 21.4 memungkinkan Anda untuk menggabungkan gambar. Metode [Merge Images](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfconverter/methods/mergeimages) memeriksa isi folder tertentu dan bekerja dengan tipe file yang ditentukan di dalamnya. Saat bekerja dengan menggabungkan gambar, kami menentukan 'inputImagesStreams', Format Gambar dan Mode Penggabungan Gambar (misalnya - vertikal) dari file kami. Kemudian kami menyimpan hasil kami dalam FileOutputStream.

Ikuti potongan kode berikut untuk menyelesaikan tugas Anda:

## Menggabungkan Gambar

```java
 public static void MergeImages01() {
        File f = new File(_dataDir);
        File[] images = f.listFiles((dir, name) -> name.toLowerCase().endsWith(".jpg"));
        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        for (File image : images) {
            try {
                inputImagesStreams.add(new FileInputStream(image));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        InputStream inputStream = PdfConverter.mergeImages(inputImagesStreams, com.aspose.pdf.ImageFormat.Jpeg,
                ImageMergeMode.Vertical, 1, 1);
        try {
            inputStream.transferTo(new FileOutputStream(_dataDir + "merged_images.jpg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
```


Contoh kedua bekerja sama seperti yang sebelumnya, tetapi gambar yang digabungkan akan disimpan secara horizontal.

```java
   public static void MergeImages02() {
        File f = new File(_dataDir);
        File[] images = f.listFiles((dir, name) ->  name.toLowerCase().endsWith(".jpg"));
        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        for (File image : images) {
            try {
                inputImagesStreams.add(new FileInputStream(image));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        InputStream inputStream = PdfConverter.mergeImages(
            inputImagesStreams, 
            com.aspose.pdf.ImageFormat.Jpeg,
            ImageMergeMode.Horizontal, 1, 1);
        try {
            inputStream.transferTo(new FileOutputStream(_dataDir + "merged_images.jpg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

```

Dalam contoh ketiga, kita akan menggabungkan gambar dengan memusatkannya.
 Dua secara horizontal, dua secara vertikal.

```java
 public static void MergeImages03() {
        File f = new File(_dataDir);
        File[] images = f.listFiles((dir, name) -> name.toLowerCase().endsWith(".jpg"));
        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        for (File image : images) {
            try {
                inputImagesStreams.add(new FileInputStream(image));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        InputStream inputStream = PdfConverter.mergeImages(inputImagesStreams, com.aspose.pdf.ImageFormat.Jpeg,
                ImageMergeMode.Center, 2, 2);
        try {
            inputStream.transferTo(new FileOutputStream(_dataDir + "merged_images.jpg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

```

Selain itu, Aspose.PDF untuk Java memberi Anda kesempatan untuk menggabungkan gambar dan menyimpannya dalam format Tiff, menggunakan [Metode MergeImagesAsTiff](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#saveAsTIFF-java.io.OutputStream-).
```java
   public static void MergeImages04() {
        File f = new File(_dataDir);
        File[] images = f.listFiles((dir, name) -> name.toLowerCase().endsWith(".jpg"));
        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        for (File image : images) {
            try {
                inputImagesStreams.add(new FileInputStream(image));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
        }

        InputStream inputStream = PdfConverter.mergeImagesAsTiff(inputImagesStreams);
        try {
            inputStream.transferTo(new FileOutputStream(_dataDir + "merged_images.jpg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

```

Untuk menyimpan gambar yang digabungkan sebagai satu gambar pada halaman PDF, kita menempatkannya dalam imageStream, menempatkan hasilnya pada halaman dengan metode addImage, di mana kita menentukan koordinat di mana kita ingin menempatkannya.

```java
    public static void MergeImages05()
    {
        File f = new File(_dataDir);
        File[] images = f.listFiles((dir, name) -> name.toLowerCase().endsWith(".jpg"));
        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        for (File image : images) {
            try {
                inputImagesStreams.add(new FileInputStream(image));
            } catch (FileNotFoundException e) {                
                e.printStackTrace();
            }
        }

        InputStream imageStream = PdfConverter.mergeImages(inputImagesStreams, com.aspose.pdf.ImageFormat.Jpeg,
                ImageMergeMode.Vertical, 1, 1);
        
        Document document = new Document();
        Page page=document.getPages().add();
        page.addImage(imageStream, new Rectangle(10,120,400,720));
    }

```