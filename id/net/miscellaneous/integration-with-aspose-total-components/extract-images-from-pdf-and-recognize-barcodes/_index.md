---
title: Ekstrak Gambar dari PDF dan Kenali Kode Batang
type: docs
weight: 20
url: id/net/extract-images-from-pdf-and-recognize-barcodes/
---

{{% alert color="primary" %}}

Dokumen PDF biasanya terdiri dari Teks, Gambar, Tabel, Lampiran, Grafik, Anotasi, dan objek terkait lainnya. Terdapat kasus dimana Kode Batang tertanam di dalam file PDF dan beberapa pelanggan memiliki kebutuhan untuk mengidentifikasi Kode Batang yang ada di dalam file PDF tersebut. Artikel berikut menjelaskan langkah-langkah tentang cara mengekstrak gambar dari halaman PDF dan mengidentifikasi Kode Batang di dalamnya.

{{% /alert %}}

Menurut Model Objek Dokumen dari Aspose.PDF untuk .NET, sebuah file PDF mengandung satu atau lebih halaman dimana setiap halaman berisi kumpulan Gambar, Formulir, dan Font dalam objek Sumber Daya.
Menurut Model Objek Dokumen dari Aspose.PDF untuk .NET, sebuah file PDF mengandung satu atau lebih halaman di mana setiap halaman memiliki kumpulan Gambar, Formulir, dan Font dalam objek Sumber Daya.

**C#**

```csharp

//buka dokumen
Aspose.PDF.Document pdfDocument = new Aspose.PDF.Document("source.pdf");

// berjalan melalui halaman-halaman individu dari file PDF

for (int pageCount = 1; pageCount <= pdfDocument.Pages.Count; pageCount++)
{
    // berjalan melalui setiap gambar yang diambil dari halaman PDF
    foreach (XImage xImage in pdfDocument.Pages[pageCount].Resources.Images)
    {
        using (MemoryStream imageStream = new MemoryStream())
        {
            //simpan gambar keluaran
            xImage.Save(imageStream, System.Drawing.Imaging.ImageFormat.Jpeg);
   
            // atur posisi stream ke awal Stream
            imageStream.Position = 0;
   
            // Instansiasi objek BarCodeReader
   
            Aspose.BarCodeRecognition.BarCodeReader barcodeReader = new Aspose.BarCodeRecognition.BarCodeReader(imageStream, Aspose.BarCodeRecognition.BarCodeReadType.Code39Extended);
   
            while (barcodeReader.Read())
            {
                // dapatkan teks BarCode dari gambar BarCode
                string code = barcodeReader.GetCodeText();
   
                // tulis teks BarCode ke keluaran Konsol
                Console.WriteLine("BARCODE : " + code);
            }
   
            // tutup objek BarCodeReader untuk melepaskan file Gambar
   
            barcodeReader.Close();
        }
    }
}

```
Untuk detail lebih lanjut mengenai topik yang dibahas dalam artikel ini, silakan kunjungi tautan berikut

- [Ekstrak Gambar dari File PDF](/net/extract-images-from-the-pdf-file/)
- [Baca Barcode](https://docs.aspose.com/barcode/net/read-barcodes/)
