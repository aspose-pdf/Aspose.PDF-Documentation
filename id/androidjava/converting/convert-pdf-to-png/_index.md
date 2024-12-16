title: Convert PDF ke PNG 
linktitle: Convert PDF ke PNG 
type: docs
weight: 20
url: /id/androidjava/convert-pdf-to-png/
lastmod: "2021-06-05"
description: Halaman ini menjelaskan cara mengonversi Halaman PDF ke gambar PNG, mengonversi semua dan halaman tunggal ke gambar PNG dengan Aspose.PDF untuk Android melalui Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Gunakan pustaka **Aspose.PDF untuk Android melalui Java** untuk mengonversi Halaman PDF ke Gambar <abbr title="Portable Network Graphics">PNG</abbr> dengan cara yang mudah diakses dan nyaman.

Kelas PngDevice memungkinkan Anda untuk mengonversi halaman PDF ke gambar PNG. Kelas ini menyediakan metode bernama Process yang memungkinkan Anda untuk mengonversi halaman tertentu dari file PDF ke format gambar PNG.

## Mengonversi Halaman PDF ke Gambar PNG

Untuk mengonversi semua halaman dalam file PDF ke file PNG, iterasikan melalui halaman individu dan konversi masing-masing ke format PNG. Cuplikan kode berikut menunjukkan cara menelusuri semua halaman dari file PDF dan mengonversi masing-masing ke gambar PNG.
```
{{% alert color="primary" %}}

Coba online. Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## Konversi satu halaman PDF ke gambar PNG

Berikan indeks halaman sebagai argumen ke metode Process(..).
Cuplikan kode berikut menunjukkan langkah-langkah untuk mengkonversi halaman pertama PDF ke format PNG.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Buat objek aliran untuk menyimpan gambar keluaran
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Buat objek Resolusi
            Resolution resolution = new Resolution(300);

            // Buat objek PngDevice dengan resolusi tertentu
            PngDevice PngDevice = new PngDevice(resolution);

            // Konversi halaman tertentu dan simpan gambar ke aliran
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Tutup aliran
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Mengonversi semua halaman PDF ke gambar PNG

Aspose.PDF untuk Android melalui Java menunjukkan kepada Anda cara mengonversi semua halaman dalam file PDF ke gambar:

1. Melakukan loop melalui semua halaman dalam file.
1. Mengonversi setiap halaman secara individu:
    1. Membuat objek dari kelas Document untuk memuat dokumen PDF.
    1. Mendapatkan halaman yang ingin Anda konversi.
    1. Memanggil metode Process untuk mengonversi halaman ke Png.

Cuplikan kode berikut menunjukkan kepada Anda cara mengonversi semua halaman PDF ke gambar PNG.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Melakukan loop melalui semua halaman file PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Membuat objek stream untuk menyimpan gambar keluaran
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Membuat objek Resolution
            Resolution resolution = new Resolution(300);
            // Membuat objek JpegDevice dengan resolusi tertentu
            PngDevice JpegDevice = new PngDevice(resolution);

            // Mengonversi halaman tertentu dan menyimpan gambar ke stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Menutup stream
            try {
                imageStream.close();
            } catch (Exception e) {
                resultMessage.setText(e.getMessage());
                return;
            }
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Mengonversi halaman PDF tertentu ke gambar PNG

Aspose.PDF untuk Android melalui Java menunjukkan cara mengonversi halaman tertentu ke format PNG:

```java
public void convertPDFtoPNG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Dapatkan persegi panjang dari area halaman tertentu
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // setel nilai CropBox sesuai dengan persegi panjang dari area halaman yang diinginkan
        document.getPages().get_Item(1).setCropBox(pageRect);
        // simpan dokumen yang dipotong ke dalam stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // buka dokumen PDF yang dipotong dari stream dan konversikan ke gambar
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Buat objek Resolution
        Resolution resolution = new Resolution(300);
        // Buat perangkat Jpeg dengan atribut yang ditentukan
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Konversi halaman tertentu dan simpan gambar ke stream
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```