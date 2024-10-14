---
title: Mengonversi Halaman PDF menjadi Gambar dan Mengenali Barcode
type: docs
weight: 10
url: /net/convert-pdf-pages-to-images-and-recognize-barcodes/
---

{{% alert color="primary" %}}

Dokumen PDF biasanya terdiri dari teks, gambar, tabel, lampiran, grafik, anotasi, dan objek lainnya. Beberapa pelanggan kami perlu menyematkan barcode dalam dokumen dan kemudian mengidentifikasi barcode dalam file PDF. Artikel berikut menjelaskan cara mengubah halaman dalam file PDF menjadi gambar dan mengidentifikasi barcode dalam gambar dengan Aspose.Barcode untuk .NET.

{{% /alert %}}
### **Mengonversi Halaman menjadi Gambar dan Mengenali Barcode**

{{% alert color="primary" %}}

Aspose.PDF untuk .NET adalah produk yang sangat kuat untuk mengelola dokumen PDF. Produk ini memudahkan konversi halaman dalam dokumen PDF menjadi gambar. Aspose.BarCode untuk .NET adalah produk yang sama kuatnya untuk menghasilkan dan mengenali barcode.

Kelas PdfConverter di bawah ruang nama Aspose.PDF.Facades mendukung konversi halaman PDF ke berbagai format gambar.
Kelas PdfConverter di bawah ruang nama Aspose.PDF.Facades mendukung konversi halaman PDF ke berbagai format gambar.

Setelah halaman telah dikonversi menjadi format gambar, kita dapat menggunakan Aspose.BarCode untuk .NET untuk mengidentifikasi barcode di dalamnya. Contoh kode di bawah ini menunjukkan cara mengonversi halaman menggunakan PdfConverter atau PngDevice.

{{% /alert %}}

#### **Menggunakan Aspose.PDF.Facades**

{{% alert color="primary" %}}

Kelas PdfConverter berisi sebuah metode yang bernama GetNextImage yang menghasilkan sebuah gambar dari halaman PDF saat ini. Untuk menentukan format gambar keluaran, metode ini menerima sebuah argumen dari enumerasi System.Drawing.Imaging.ImageFormat.

Aspose.Barcode mengandung ruang nama, BarCodeRecognition, yang berisi kelas BarCodeReader. Kelas BarCodeReader memungkinkan Anda membaca, menentukan, dan mengidentifikasi barcode dari file gambar.

Untuk tujuan contoh ini, pertama-tama konversikan sebuah halaman dalam file PDF menjadi gambar dengan Aspose.PDF.Facades.PdfConverter.
Untuk tujuan contoh ini, pertama-tama konversikan halaman dalam file PDF menjadi gambar dengan Aspose.PDF.Facades.PdfConverter.

##### **Contoh Pemrograman**
**C#**

{{< highlight csharp >}}

 //Buat objek PdfConverter

PdfConverter converter = new PdfConverter();

//Ikat file PDF masukan

converter.BindPdf("Source.pdf");

// Tentukan halaman awal yang akan diproses

converter.StartPage = 1;

// Tentukan halaman akhir untuk diproses

converter.EndPage = 1;

// Buat objek Resolution untuk menentukan resolusi gambar hasil

converter.Resolution = new Aspose.PDF.Devices.Resolution(300);

//Inisialisasi proses konversi

converter.DoConvert();

// Buat objek MemoryStream untuk menampung gambar hasil

MemoryStream imageStream = new MemoryStream();

//Periksa jika halaman ada dan kemudian konversikan menjadi gambar satu per satu

while (converter.HasNextImage())

{

    // Simpan gambar dalam format gambar yang diberikan

    converter.GetNextImage(imageStream, System.Drawing.Imaging.ImageFormat.Png);

    // Atur posisi stream ke awal stream

// Mengatur posisi stream ke awal stream

imageStream.Position = 0;

// Membuat objek BarCodeReader

Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

// String txtResult.Text = "";

while (barcodeReader.Read())

{

    // Mendapatkan teks barcode dari gambar barcode

    string code = barcodeReader.GetCodeText();

    // Menulis teks barcode ke output Console

    Console.WriteLine("BARCODE : " + code);

}

// Menutup objek BarCodeReader untuk melepaskan file gambar

barcodeReader.Close();

}

// Menutup instansi PdfConverter dan melepaskan sumber daya

converter.Close();

// Menutup stream yang memegang objek gambar

imageStream.Close();

{{< /highlight >}}

{{% alert color="primary" %}}

Pada potongan kode di atas, gambar keluaran disimpan ke objek MemoryStream.
Di atas potongan kode, gambar keluaran disimpan ke objek MemoryStream.

#### **Menggunakan Kelas PngDevice**
Di Aspose.PDF.Devices, terdapat PngDevice. Kelas ini memungkinkan Anda mengonversi halaman dalam dokumen PDF menjadi gambar PNG.

Untuk tujuan contoh ini, muat file PDF sumber ke Document dan konversikan halaman dokumen menjadi gambar PNG. Setelah gambar telah dibuat, gunakan kelas BarCodeReader di bawah Aspose.BarCodeRecognition untuk mengidentifikasi dan membaca barcode pada gambar tersebut.

Kode sampel yang diberikan di sini melintasi halaman-halaman dokumen PDF dan mencoba mengidentifikasi barcode di setiap halaman.

##### **Contoh Pemrograman**
**C#**

```csharp
 //Buka dokumen PDF

Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// Melintasi halaman-halaman individu dari file PDF

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)

{

    using (MemoryStream imageStream = new MemoryStream())
```

    using (MemoryStream imageStream = new MemoryStream())
    {
        //Membuat objek Resolution
        Aspose.PDF.Devices.Resolution resolution = new Aspose.PDF.Devices.Resolution(300);

        //Menginstansiasi objek PngDevice sambil mengirimkan objek Resolution sebagai argumen ke konstruktornya
        Aspose.PDF.Devices.PngDevice pngDevice = new Aspose.PDF.Devices.PngDevice(resolution);

        //Mengkonversi halaman tertentu dan menyimpan gambar ke stream
        pngDevice.Process(pdfDocument.Pages[pageCount], imageStream);

        //Mengatur posisi stream ke awal Stream
        imageStream.Position = 0;

        //Menginstansiasi objek BarCodeReader
        Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);

        // String txtResult.Text = "";
        while (barcodeReader.Read())
        {
            //Mendapatkan teks barcode dari gambar barcode
            string code = barcodeReader.GetCodeText();
```


string code = barcodeReader.GetCodeText();

// Tulis teks barcode ke output Console

Console.WriteLine("BARCODE : " + code);

}

// Tutup objek BarCodeReader untuk melepaskan file gambar

barcodeReader.Close();

}

}

{{< /highlight >}}



{{% alert color="primary" %}}

Untuk informasi lebih lanjut tentang topik yang dibahas di artikel ini, silakan kunjungi:

- Konversi Halaman PDF ke Berbagai Format Gambar (Facades)
- Konversi semua halaman PDF ke Gambar PNG
- [Membaca Barcodes](https://docs.aspose.com/barcode/net/read-barcodes/)


{{% /alert %}}
```
