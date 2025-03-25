---
title: Bekerja dengan JavaScript
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 120
url: /id/net/working-with-javascript/
description: Pelajari cara menambahkan, memodifikasi, dan mengeksekusi JavaScript dalam dokumen PDF menggunakan Aspose.PDF for .NET. Tingkatkan interaktivitas dan otomatisasi.
lastmod: "2025-02-07"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with JavaScript",
    "alternativeHeadline": "Enhance PDF with Custom JavaScript Actions",
    "abstract": "Temukan kemampuan yang ditingkatkan dari mengintegrasikan JavaScript dalam dokumen PDF melalui Aspose.PDF for .NET. Fitur baru ini memungkinkan pengembang untuk menambahkan dan mengelola tindakan JavaScript di tingkat dokumen dan halaman, memungkinkan pengalaman PDF yang interaktif dan dinamis yang ditujukan untuk meningkatkan keterlibatan pengguna dan fungsionalitas. Buka potensi JavaScript untuk membuat formulir PDF yang canggih yang meniru perilaku seperti web, meningkatkan alur kerja pembuatan dokumen Anda.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "JavaScript, Acrobat JavaScript, PDF document generation, JavaScript collection, document level JavaScript, JavaScript Action, interactive PDF forms, manipulate PDF files, HTML JavaScript, Aspose.PDF for .NET",
    "wordcount": "423",
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
    "url": "/net/working-with-javascript/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-javascript/"
    },
    "dateModified": "2025-02-07",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Menambahkan JavaScript (DOM)

### Apa itu Acrobat JavaScript?

Acrobat JavaScript adalah bahasa yang didasarkan pada inti JavaScript versi 1.5 dari ISO-16262, yang sebelumnya dikenal sebagai ECMAScript, sebuah bahasa skrip berorientasi objek yang dikembangkan oleh Netscape Communications. JavaScript diciptakan untuk memindahkan pemrosesan halaman Web dari server ke klien dalam aplikasi berbasis Web. Acrobat JavaScript menerapkan ekstensi, dalam bentuk objek baru dan metode serta properti yang menyertainya, ke bahasa JavaScript. Objek khusus Acrobat ini memungkinkan pengembang untuk mengelola keamanan dokumen, berkomunikasi dengan basis data, menangani lampiran file, memanipulasi file PDF sehingga berperilaku seperti formulir interaktif yang mendukung web, dan sebagainya. Karena objek khusus Acrobat ditambahkan di atas JavaScript inti, Anda masih memiliki akses ke kelas standar, termasuk Math, String, Date, Array, dan RegExp.

### Acrobat JavaScript vs HTML (Web) JavaScript

Dokumen PDF memiliki fleksibilitas yang besar karena dapat ditampilkan baik dalam perangkat lunak Acrobat maupun di browser Web. Oleh karena itu, penting untuk menyadari perbedaan antara Acrobat JavaScript dan JavaScript yang digunakan di browser Web, yang juga dikenal sebagai HTML JavaScript:

- Acrobat JavaScript tidak memiliki akses ke objek dalam halaman HTML. Demikian pula, HTML JavaScript tidak dapat mengakses objek dalam file PDF.
- HTML JavaScript dapat memanipulasi objek seperti Window. Acrobat JavaScript tidak dapat mengakses objek tertentu ini tetapi dapat memanipulasi objek khusus PDF.

Anda dapat menambahkan JavaScript di tingkat dokumen dan halaman menggunakan [Aspose.PDF for .NET](/pdf/id/net/). Untuk menambahkan JavaScript:

### Menambahkan JavaScript ke Tindakan Dokumen atau Halaman

1. Deklarasikan dan instansiasi objek JavascriptAction dengan pernyataan JavaScript yang diinginkan sebagai argumen konstruktor.
1. Tetapkan objek JavascriptAction ke tindakan yang diinginkan dari dokumen atau halaman PDF.

Contoh di bawah ini menerapkan OpenAction ke dokumen tertentu.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Adding JavaScript at Document Level
        // Instantiate JavascriptAction with desired JavaScript statement
        var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

        // Assign JavascriptAction object to desired action of Document
        document.OpenAction = javaScript;

        // Adding JavaScript at Page Level
        document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
        document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

        // Save PDF Document
        document.Save(dataDir + "JavaScriptAdded_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "input.pdf");

    // Adding JavaScript at Document Level
    // Instantiate JavascriptAction with desired JavaScript statement
    var javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    // Assign JavascriptAction object to desired action of Document
    document.OpenAction = javaScript;

    // Adding JavaScript at Page Level
    document.Pages[2].Actions.OnOpen = new JavascriptAction("app.alert('page 1 opened')");
    document.Pages[2].Actions.OnClose = new JavascriptAction("app.alert('page 1 closed')");

    // Save PDF Document
    document.Save(dataDir + "JavaScriptAdded_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

### Menambahkan/Menghapus JavaScript di Tingkat Dokumen

Sebuah properti baru bernama JavaScript ditambahkan dalam kelas Document yang memiliki tipe koleksi JavaScript dan memberikan akses ke skenario JavaScript berdasarkan kuncinya. Properti ini digunakan untuk menambahkan JavaScript tingkat Dokumen. Koleksi JavaScript memiliki properti dan metode berikut:

- string this(string key)– Mendapatkan atau menetapkan JavaScript berdasarkan namanya.
- IList Keys – menyediakan daftar kunci yang ada dalam koleksi JavaScript.
- bool Remove(string key) – menghapus JavaScript berdasarkan kuncinya.

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();
        document.JavaScript["func1"] = "function func1() { hello(); }";
        document.JavaScript["func2"] = "function func2() { hello(); }";
        document.Save(dataDir + "AddJavascript.pdf");
    }

    // Remove Document level JavaScript
    using (var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf"))
    {
        var keys = (IList)document1.JavaScript.Keys;

        Console.WriteLine("=============================== ");

        foreach (string key in keys)
        {
            Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
        }

        document1.JavaScript.Remove("func1");

        Console.WriteLine("Key 'func1' removed ");
        Console.WriteLine("=============================== ");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddJavaScript()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();
    document.JavaScript["func1"] = "function func1() { hello(); }";
    document.JavaScript["func2"] = "function func2() { hello(); }";
    document.Save(dataDir + "AddJavascript.pdf");

    // Remove Document level JavaScript
    using var document1 = new Aspose.Pdf.Document(dataDir + "AddJavascript.pdf");
    IList keys = (IList)document1.JavaScript.Keys;

    Console.WriteLine("=============================== ");

    foreach (string key in keys)
    {
        Console.WriteLine(key + " ==> " + document1.JavaScript[key]);
    }

    document1.JavaScript.Remove("func1");

    Console.WriteLine("Key 'func1' removed ");
    Console.WriteLine("=============================== ");
}
```
{{< /tab >}}
{{< /tabs >}}

### Mengatur Tanggal Kedaluwarsa Dokumen PDF Menggunakan Tindakan JavaScript

Aspose.PDF memungkinkan Anda untuk mengatur tanggal kedaluwarsa untuk dokumen PDF dengan menyematkan Tindakan JavaScript. Fungsionalitas ini memastikan PDF menjadi tidak dapat diakses setelah tanggal dan waktu tertentu, meningkatkan keamanan dan kontrol dokumen. Dengan memanfaatkan Tindakan JavaScript, Anda dapat mendefinisikan kondisi kedaluwarsa yang tepat hingga detik, memastikan aksesibilitas dokumen diatur dengan ketat.

**Anda dapat mencapai ini dengan mengikuti langkah-langkah berikut**

1. **Inisialisasi Dokumen:** Buat dokumen PDF baru dan tambahkan halaman kosong atau buka dokumen PDF yang sudah ada.
2. **Tentukan Tanggal dan Waktu Kedaluwarsa:** Atur tanggal dan waktu setelah dokumen akan kedaluwarsa.
3. **Siapkan Kode JavaScript:** 
    - Ambil tanggal dan waktu saat ini.
    - Tentukan tanggal dan waktu kedaluwarsa yang tepat, dengan mempertimbangkan bahwa bulan dimulai dari nol dalam JavaScript.
    - Bandingkan tanggal dan waktu saat ini dengan tanggal dan waktu kedaluwarsa.
    - Jika tanggal dan waktu saat ini melebihi tanggal dan waktu kedaluwarsa, tampilkan peringatan dan tutup dokumen.
4. **Atur Tindakan Buka:** Kaitkan tindakan JavaScript dengan tindakan buka dokumen.
5. **Simpan Dokumen:** Simpan PDF dengan JavaScript yang disematkan yang menegakkan kondisi kedaluwarsa.

Di bawah ini adalah potongan kode yang menunjukkan fungsionalitas ini dalam C# (.NET) dan Java.

Potongan kode C# berikut menunjukkan cara mengatur tanggal dan waktu kedaluwarsa untuk dokumen PDF menggunakan Tindakan JavaScript dengan Aspose.PDF:

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        document.Pages.Add();

        // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
        DateTime expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

        // Create JavaScript code to enforce the expiry date and time
        string jsCode =
            // Get the current date and time
            "var rightNow = new Date();\n" +
            // Set the expiry date and time
            "var endDate = new Date(" +
            $"{expiryDateTime.Year}," +
            $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
            $"{expiryDateTime.Day}," +
            $"{expiryDateTime.Hour}," +
            $"{expiryDateTime.Minute}," +
            $"{expiryDateTime.Second}" +
            ");\n" +
            "if(rightNow > endDate)\n" +
            "{\n" +
            "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
            "    this.closeDoc();\n" +
            "}";

        // Create a JavascriptAction with the defined JavaScript code
        var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

        // Set the JavaScript action to execute when the document is opened
        document.OpenAction = javaScript;

        // Save PDF document
        document.Save(dataDir + "PDFExpiry_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CreateDocumentWithExpiryDate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_WorkingDocuments();

    // Create PDF document
    using var document = new Aspose.Pdf.Document();
    document.Pages.Add();

    // Define the expiry date and time (e.g., April 1, 2025, 12:00:00 PM)
    var expiryDateTime = new DateTime(2025, 4, 1, 12, 0, 0);

    // Create JavaScript code to enforce the expiry date and time
    string jsCode =
        // Get the current date and time
        "var rightNow = new Date();\n" +
        // Set the expiry date and time
        "var endDate = new Date(" +
        $"{expiryDateTime.Year}," +
        $"{expiryDateTime.Month - 1}," + // Months are zero-based in JavaScript
        $"{expiryDateTime.Day}," +
        $"{expiryDateTime.Hour}," +
        $"{expiryDateTime.Minute}," +
        $"{expiryDateTime.Second}" +
        ");\n" +
        "if(rightNow > endDate)\n" +
        "{\n" +
        "    app.alert(\"This Document has Expired as of \" + endDate.toLocaleString() + \".\");\n" +
        "    this.closeDoc();\n" +
        "}";

    // Create a JavascriptAction with the defined JavaScript code
    var javaScript = new Aspose.Pdf.Annotations.JavascriptAction(jsCode);

    // Set the JavaScript action to execute when the document is opened
    document.OpenAction = javaScript;

    // Save PDF document
    document.Save(dataDir + "PDFExpiry_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

- **Objek Tanggal JavaScript:** Dalam JavaScript, indeks bulan dimulai dari `0` untuk Januari dan berakhir di `11` untuk Desember. Pastikan bahwa nilai bulan disesuaikan dengan benar saat mengatur tanggal dan waktu kedaluwarsa.
  
- **Pertimbangan Keamanan:** Meskipun tindakan JavaScript dapat mengontrol perilaku dokumen PDF, mereka bergantung pada dukungan penampil PDF untuk JavaScript. Tidak semua penampil PDF mungkin menghormati skrip ini, dan pengguna mungkin telah menonaktifkan eksekusi JavaScript demi alasan keamanan.

- **Kustomisasi:** Modifikasi kode JavaScript untuk melakukan tindakan tambahan setelah kedaluwarsa, seperti menonaktifkan fitur tertentu, mengalihkan ke halaman tertentu, atau mencatat peristiwa. Selain itu, jika perlu, Anda dapat memeriksa hanya tanggal kedaluwarsa tanpa menentukan waktu.

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>