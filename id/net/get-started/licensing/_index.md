---
title: Lisensi Aspose PDF
linktitle: Lisensi dan batasan
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /id/net/licensing/
description: Aspose. PDF untuk .NET mengundang pelanggannya untuk mendapatkan lisensi Classic dan Metered License. Serta menggunakan lisensi terbatas untuk menjelajahi produk dengan lebih baik.
lastmod: "2025-02-07"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Aspose PDF for .NET License",
    "alternativeHeadline": "Licensing Options for Aspose.PDF for .NET Users",
    "abstract": "Aspose PDF untuk .NET memperkenalkan kerangka lisensi yang kuat termasuk lisensi Classic dan Metered, memungkinkan pengguna untuk memilih antara harga tetap dan opsi penagihan berdasarkan penggunaan. Lisensi Classic dapat dengan mudah dimuat dari file atau stream, sementara lisensi Metered yang inovatif menyediakan pengukuran fleksibel berdasarkan penggunaan API, memenuhi berbagai kebutuhan pengguna. Strategi lisensi ganda ini meningkatkan aksesibilitas dan skalabilitas solusi PDF untuk pengembang",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "869",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/licensing/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/licensing/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Batasan versi evaluasi

Kami ingin pelanggan kami menguji komponen kami secara menyeluruh sebelum membeli, jadi versi evaluasi memungkinkan Anda menggunakannya seperti biasanya.

- **PDF yang dibuat dengan watermark evaluasi.** Versi evaluasi dari Aspose.PDF for .NET menyediakan fungsionalitas produk penuh, tetapi semua halaman dalam dokumen PDF yang dihasilkan diberi watermark dengan teks "Hanya Evaluasi. Dibuat dengan Aspose.PDF. Hak Cipta 2002-2025 Aspose Pty Ltd." di bagian atas.

- **Batasi jumlah halaman yang dapat diproses.**
Dalam versi evaluasi, Anda hanya dapat memproses empat halaman pertama dari sebuah dokumen.

>Jika Anda ingin menguji Aspose.PDF for .NET tanpa batasan versi evaluasi, Anda juga dapat meminta Lisensi Sementara selama 30 hari. Silakan merujuk ke [Bagaimana cara mendapatkan Lisensi Sementara?](https://purchase.aspose.com/temporary-license)

## Lisensi Classic

Lisensi dapat dimuat dari file atau objek stream. Cara termudah untuk mengatur lisensi adalah dengan menempatkan file lisensi di folder yang sama dengan file Aspose.PDF.dll dan menentukan nama file tanpa jalur, seperti yang ditunjukkan dalam contoh di bawah ini.

Jika Anda menggunakan komponen Aspose untuk .NET lainnya bersama dengan Aspose.PDF for .NET, silakan tentukan namespace untuk Lisensi seperti [Aspose.Pdf.License](https://reference.aspose.com/pdf/net/aspose.pdf/license).

### Memuat lisensi dari file

Cara termudah untuk menerapkan lisensi adalah dengan menempatkan file lisensi di folder yang sama dengan file Aspose.PDF.dll dan hanya menentukan nama file tanpa jalur.

Ketika Anda memanggil metode [SetLicense](https://reference.aspose.com/pdf/net/aspose.pdf/license/methods/setlicense/index), nama lisensi yang Anda berikan harus sesuai dengan nama file lisensi Anda. Misalnya, jika Anda mengubah nama file lisensi menjadi "Aspose.PDF.lic.xml", berikan nama file itu ke metode Pdf.SetLicense(…) .

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseExample()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    try
    {
        // Set license
        license.SetLicense("Aspose.Pdf.lic");
    }
    catch (Exception)
    {
        // Something went wrong
        throw;
    }
    Console.WriteLine("License set successfully.");
}
```
### Memuat lisensi dari objek stream

Contoh berikut menunjukkan cara memuat lisensi dari stream.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // Initialize license object
    var license = new Aspose.Pdf.License();
    // Load license from the file stream
    var myStream = new FileStream(
            "Aspose.Pdf.lic",
            FileMode.Open);
    // Set license
    license.SetLicense(myStream);
    Console.WriteLine("License set successfully.");
}
```
## Lisensi Metered

Aspose.PDF memungkinkan pengembang untuk menerapkan kunci metered. Mekanisme lisensi metered akan digunakan bersama dengan metode lisensi yang ada. Pelanggan yang ingin ditagih berdasarkan penggunaan fitur API dapat menggunakan lisensi metered. Untuk detail lebih lanjut, silakan merujuk ke bagian FAQ Lisensi Metered.
Panduan ini memberikan praktik terbaik untuk implementasi yang lancar dan mencegah gangguan akibat perubahan status lisensi.

Kelas "Metered" digunakan untuk menerapkan kunci metered. Berikut adalah contoh kode yang menunjukkan cara mengatur kunci publik dan privat metered.

Untuk detail lebih lanjut, silakan merujuk ke bagian [FAQ Lisensi Metered](https://purchase.aspose.com/faqs/licensing/metered).

__Metode Lisensi Metered__

Menerapkan Lisensi Metered menggunakan metode `SetMeteredKey` untuk mengaktifkan lisensi metered dengan memberikan kunci publik dan privat Anda. Ini harus dilakukan sekali selama inisialisasi aplikasi untuk memastikan lisensi yang tepat.

Contoh:

```csharp
 var metered = new Aspose.Pdf.Metered();
 metered.SetMeteredKey("your-public-key", "your-private-key");
 ```
Memeriksa Status Lisensi menggunakan `IsMeteredLicensed()` untuk memverifikasi apakah lisensi metered aktif.

Contoh:

```csharp
bool isLicensed = Aspose.Pdf.License.IsMeteredLicensed();
if (!isLicensed) 
{
    metered.SetMeteredKey("your-public-key", "your-private-key");
}
 ```
Metode `Metered.GetConsumptionCredit()` digunakan untuk mendapatkan informasi tentang kredit konsumsi.
Metode `Metered.GetConsumptionQuantity()` digunakan untuk mendapatkan informasi tentang ukuran file konsumsi.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetMeteredLicense()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    // Set metered public and private keys
    var metered = new Aspose.Pdf.Metered();
    // Access the setMeteredKey property and pass public and private keys as parameters
    metered.SetMeteredKey("your public key", "your private key");
    // Get current Consumption Credit and Quantity
    var currentMonthCreditsSpent = Aspose.Pdf.Metered.GetConsumptionCredit();
    var currentMonthConsumedMegabytes = Aspose.Pdf.Metered.GetConsumptionQuantity();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Add five pages
        AddPages(document, 5);

        // Save PDF document
        document.Save(dataDir + "output.pdf");

        // Wait to be sure the transaction completed
        System.Threading.Thread.Sleep(10000);
        // Get current Consumption Credit and Quantity
        var nowCredit = Aspose.Pdf.Metered.GetConsumptionCredit();
        var nowQuantity = Aspose.Pdf.Metered.GetConsumptionQuantity();
        Console.WriteLine("Credit: was={0} now={1} difference={2}", currentMonthCreditsSpent, nowCredit, nowCredit - currentMonthCreditsSpent);
        Console.WriteLine("Quantity: was={0} now={1} difference={2}", currentMonthConsumedMegabytes, nowQuantity, nowQuantity - currentMonthConsumedMegabytes); 
    }
}

private static void AddPages(Document document, int n)
{
    for (int i = 0; i < n; i++)
    {
        document.Pages.Add();
    }
}
```

__Praktik Terbaik untuk Lisensi Metered__

✅ Pendekatan yang Direkomendasikan: Pola Singleton
Untuk memastikan pengaturan lisensi yang stabil:

- Terapkan lisensi sekali saat aplikasi dimulai.
- Gunakan pola singleton (atau pendekatan serupa) untuk membuat dan menggunakan kembali instance lisensi metered.
- Periksa status lisensi secara berkala menggunakan `IsMeteredLicensed()`. Terapkan kembali lisensi hanya jika menjadi tidak valid.
- Jika diterapkan dengan benar, lisensi tetap valid selama 24 jam bahkan jika server lisensi tidak tersedia sementara.

Contoh: Implementasi Singleton

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
public class AsposeLicenseManager
{
    private static AsposeLicenseManager _instance;
    private static readonly object _lock = new object();
    private Aspose.Pdf.Metered _metered;

    private AsposeLicenseManager()
    {
        _metered = new Aspose.Pdf.Metered();
        _metered.SetMeteredKey("your-public-key", "your-private-key");
    }

    public static AsposeLicenseManager Instance
    {
        get
        {
            lock (_lock)
            {
                if (_instance == null)
                {
                    _instance = new AsposeLicenseManager();
                }
                return _instance;
            }
        }
    }

    public void ValidateLicense()
    {
        if (!Aspose.Pdf.License.IsMeteredLicensed())
        {
        _metered.SetMeteredKey("your-public-key", "your-private-key");
        }
    }
}
```

❌ Kesalahan Umum yang Harus Dihindari:

- Aplikasi Lisensi yang Sering
- Jangan membuat instance lisensi metered baru untuk setiap operasi.
- Jika server lisensi tidak dapat dijangkau selama inisialisasi, lisensi dapat kembali ke mode evaluasi.
- Jangan menerapkan lisensi berulang kali untuk setiap operasi.
- Aplikasi lisensi yang sering dapat menyebabkan fallback ke mode percobaan jika server lisensi tidak tersedia sementara.

__Ringkasan:__

✅ Atur lisensi metered sekali saat aplikasi dimulai.
✅ Gunakan pola singleton untuk mengelola satu instance.
✅ Periksa dan terapkan kembali lisensi secara berkala jika diperlukan.
❌ Hindari aplikasi lisensi yang sering untuk mencegah fallback ke mode percobaan.
Dengan mengikuti praktik terbaik ini, Anda memastikan penggunaan Aspose.PDF yang lancar dan tidak terputus dengan lisensi metered.

Jika lisensi telah diinisialisasi, maka selama objek ini "hidup", bahkan jika koneksi ke server lisensi hilang karena alasan tertentu, lisensi akan dianggap aktif selama 7 hari lagi. Jika Anda menginisialisasi lisensi setiap kali Anda perlu melakukan sesuatu dan tidak ada koneksi ke server pada saat inisialisasi, maka lisensi akan masuk ke mode Eval.
Perlu ditekankan lebih lanjut bahwa jika seorang pengguna telah menginisialisasi lisensi, maka selama objek ini "hidup", bahkan jika koneksi ke server lisensi hilang karena alasan tertentu, lisensi akan dianggap aktif selama 24 jam lagi. Jika Anda menginisialisasi lisensi setiap kali Anda perlu melakukan sesuatu dan tidak ada koneksi ke server pada saat inisialisasi, maka lisensi akan masuk ke mode Eval.

Harap dicatat bahwa aplikasi COM yang bekerja dengan **Aspose.PDF for .NET** juga harus menggunakan kelas Lisensi.

Satu poin yang perlu dipertimbangkan:
Harap dicatat bahwa sumber daya yang disematkan disertakan dalam assembly seperti yang ditambahkan, yaitu jika Anda menambahkan file teks sebagai sumber daya yang disematkan dalam aplikasi dan membuka EXE yang dihasilkan di notepad, Anda akan melihat isi file teks yang tepat. Jadi saat menggunakan file lisensi sebagai sumber daya yang disematkan, siapa pun dapat membuka file exe di beberapa editor teks sederhana dan melihat/mengambil isi lisensi yang disematkan.

Oleh karena itu, untuk menambahkan lapisan keamanan ekstra saat menyematkan lisensi dengan aplikasi, Anda dapat mengompres/mengenskripsi lisensi dan setelah itu, Anda dapat menyematkannya ke dalam assembly. Misalkan kita memiliki file lisensi Aspose.PDF.lic, jadi mari kita buat Aspose.PDF.zip dengan kata sandi test dan sematkan file zip ini ke dalam solusi. Potongan kode berikut dapat digunakan untuk menginisialisasi lisensi:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SetLicenseFromStream()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();
    var license = new Aspose.Pdf.License();
    license.SetLicense(GetSecureLicenseFromStream());
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Get the page count of document
        Console.WriteLine(document.Pages.Count);
    }
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
```