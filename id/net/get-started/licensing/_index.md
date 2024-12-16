---
title: Lisensi Aspose PDF
linktitle: Lisensi dan Batasan
type: docs
weight: 90
url: /id/net/licensing/
description: Aspose. PDF untuk .NET mengundang pelanggannya untuk mendapatkan lisensi Klasik dan Lisensi Metered. Serta menggunakan lisensi terbatas untuk lebih menjelajahi produk.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Batasan versi evaluasi

Kami ingin pelanggan kami menguji komponen kami secara menyeluruh sebelum membeli sehingga versi evaluasi memungkinkan Anda menggunakannya seperti biasa.

- **PDF dibuat dengan watermark evaluasi.** Versi evaluasi dari Aspose.PDF untuk .NET menyediakan fungsionalitas produk penuh, tetapi semua halaman dalam dokumen PDF yang dihasilkan di-watermark dengan "Evaluasi Saja. Dibuat dengan Aspose.PDF. Hak Cipta 2002-2020 Aspose Pty Ltd" di bagian atas.

- **Batasan jumlah item koleksi yang dapat diproses.**
Dalam versi evaluasi dari koleksi apa pun, Anda hanya dapat memproses empat elemen (misalnya, hanya 4 halaman, 4 bidang formulir, dll.).
Dalam versi evaluasi dari setiap koleksi, Anda hanya dapat memproses empat elemen (misalnya, hanya 4 halaman, 4 bidang formulir, dll.).

>Jika Anda ingin menguji Aspose.HTML untuk .NET tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara 30 hari. Silakan lihat [Cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)

## Lisensi klasik

Lisensi dapat dimuat dari berkas atau objek aliran. Cara termudah untuk mengatur lisensi adalah dengan meletakkan berkas lisensi di folder yang sama dengan berkas Aspose.PDF.dll dan menentukan nama berkas tanpa jalur, seperti yang ditunjukkan pada contoh di bawah ini.

Jika Anda menggunakan komponen Aspose lainnya untuk .NET bersama dengan Aspose.PDF untuk .NET, silakan tentukan ruang nama untuk Lisensi seperti [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license).

### Memuat lisensi dari berkas

Cara termudah untuk menerapkan lisensi adalah dengan meletakkan berkas lisensi di folder yang sama dengan berkas Aspose.PDF.dll dan menentukan hanya nama berkas tanpa jalur.

Ketika Anda memanggil metode [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index), nama lisensi yang Anda berikan harus sesuai dengan berkas lisensi Anda.
Ketika Anda memanggil metode [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index), nama lisensi yang Anda berikan harus sesuai dengan nama file lisensi Anda.

```csharp
public static void SetLicenseExample()
{
    // Inisialisasi objek lisensi
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    try
    {
        // Mengatur lisensi
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // terjadi kesalahan
        throw;
    }
    Console.WriteLine("Lisensi berhasil diatur.");
}
```
### Memuat lisensi dari objek stream

Contoh berikut menunjukkan cara memuat lisensi dari stream.

```csharp
public static void SetLicenseFromStream()
{
    // Inisialisasi objek lisensi
    Aspose.Pdf.License license = new Aspose.Pdf.License();
    // Memuat lisensi dari file stream
    System.IO.FileStream myStream =
        new System.IO.FileStream(
            "Aspose.Pdf.lic",
            System.IO.FileMode.Open);
    // Mengatur lisensi
    license.SetLicense(myStream);
    Console.WriteLine("Lisensi berhasil diatur.");
}
```
## Lisensi Metered

Aspose.PDF memungkinkan pengembang untuk menerapkan kunci metered. Ini adalah mekanisme lisensi baru. Mekanisme lisensi baru akan digunakan bersama dengan metode lisensi yang ada. Pelanggan yang ingin ditagih berdasarkan penggunaan fitur API dapat menggunakan lisensi metered. Untuk informasi lebih lanjut, silakan merujuk ke bagian FAQ Lisensi Metered.

Kelas baru Metered telah diperkenalkan untuk menerapkan kunci metered. Berikut adalah contoh kode yang menunjukkan cara mengatur kunci publik dan privat metered.

Untuk informasi lebih lanjut, silakan merujuk ke bagian [FAQ Lisensi Metered](https://purchase.aspose.com/faqs/licensing/metered).

```csharp
public static void SetMeteredLicense()
{
    // set metered public and private keys
    Aspose.Pdf.Metered metered = new Aspose.Pdf.Metered();
    // Akses properti setMeteredKey dan lewatkan kunci publik dan privat sebagai parameter
    metered.SetMeteredKey(
        "<type public key here>",
        "<type private key here>");

    // Muat dokumen dari disk.
    Document doc = new Document("input.pdf");
    //Dapatkan jumlah halaman dokumen
    Console.WriteLine(doc.Pages.Count);
}
```
Harap dicatat bahwa aplikasi COM yang bekerja dengan **Aspose.PDF for .NET** juga harus menggunakan kelas License.

Satu poin yang perlu dipertimbangkan:
Harap dicatat bahwa sumber daya yang tertanam disertakan dalam perakitan sebagaimana adanya, yaitu jika Anda menambahkan file teks sebagai sumber daya yang tertanam dalam aplikasi dan membuka EXE yang dihasilkan di notepad, Anda akan melihat isi file teks dengan tepat. Jadi, ketika menggunakan file lisensi sebagai sumber daya yang tertanam, siapa pun dapat membuka file exe di editor teks sederhana dan melihat/mengekstrak isi dari lisensi yang tertanam.

Oleh karena itu, untuk menambahkan lapisan keamanan ekstra saat menyematkan lisensi dengan aplikasi, Anda dapat mengompres/mengenkripsi lisensi dan setelah itu, Anda dapat menyematkannya ke dalam perakitan. Misalkan kita memiliki file lisensi Aspose.PDF.lic, mari kita buat Aspose.PDF.zip dengan kata sandi tes dan sematkan file zip ini ke dalam solusi. Potongan kode berikut dapat digunakan untuk menginisialisasi lisensi:

```csharp
using System;
using System.IO;
using System.IO.Compression;
using System.Reflection;

namespace Aspose.Pdf.Examples
{
    class ExampleLicensing
    {
        public static void LicenseDemo()
        {
            License license = new License();
            license.SetLicense(GetSecureLicenseFromStream());
            Document doc = new Document("document.pdf");
            //Dapatkan jumlah halaman dari dokumen
            Console.WriteLine(doc.Pages.Count);
        }

        private static Stream GetSecureLicenseFromStream()
        {
            var assembly = Assembly.GetExecutingAssembly();
            var memoryStream = new MemoryStream();
            using (var zipToOpen = assembly.GetManifestResourceStream("Aspose.Pdf.Examples.License.Aspose.PDF.zip"))
            {
                using (ZipArchive archive = new ZipArchive(zipToOpen ?? throw new InvalidOperationException(), ZipArchiveMode.Read))
                {
                    var unpackedLicense  = archive.GetEntry("Aspose.PDF.lic");
                    unpackedLicense?.Open().CopyTo(memoryStream);
                }
            }

            memoryStream.Position = 0;
            return memoryStream;
        }
    }
}
```
### Menerapkan Lisensi yang Dibeli Sebelum 2005/01/22

Aspose.PDF untuk .NET tidak lagi mendukung lisensi gaya lama. Jika Anda memiliki lisensi dari sebelum 22 Januari 2005 dan Anda telah memperbarui ke versi Aspose.PDF yang lebih baru, silakan hubungi tim Penjualan kami untuk mendapatkan berkas lisensi baru.
