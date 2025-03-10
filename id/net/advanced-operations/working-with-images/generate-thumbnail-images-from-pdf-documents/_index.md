---
title: Menghasilkan Gambar Thumbnail dari PDF
linktitle: Menghasilkan Gambar Thumbnail
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 110
url: /id/net/generate-thumbnail-images-from-pdf-documents/
description: Bagian ini menjelaskan cara menghasilkan gambar thumbnail dari dokumen PDF
lastmod: "2022-02-17"
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Generate Thumbnail Images from PDF",
    "alternativeHeadline": "Generate Thumbnails from PDF Documents Effortlessly",
    "abstract": "Fitur baru ini memungkinkan pengguna untuk secara efisien menghasilkan gambar thumbnail langsung dari dokumen PDF. Fungsionalitas ini meningkatkan manajemen dokumen dengan mengubah halaman PDF menjadi format gambar yang mudah dibagikan, menyederhanakan alur kerja bagi pengembang dan pengguna. Dengan dukungan untuk berbagai format gambar, fitur ini menyederhanakan proses visualisasi konten PDF tanpa perlu perangkat lunak eksternal seperti Adobe Acrobat",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Generate Thumbnail Images, PDF documents, Aspose.PDF for .NET, Acrobat SDK, image formats, PDF Manipulation Library, JavaScript, interapplication communication, thumbnail images, JPEG conversion",
    "wordcount": "767",
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
    "url": "/net/generate-thumbnail-images-from-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/generate-thumbnail-images-from-pdf-documents/"
    },
    "dateModified": "2024-11-26",
    "description": "Bagian ini menjelaskan cara menghasilkan gambar thumbnail dari dokumen PDF"
}
</script>

{{% alert color="primary" %}}

SDK Adobe Acrobat adalah sekumpulan alat yang membantu Anda mengembangkan perangkat lunak yang berinteraksi dengan teknologi Acrobat. SDK ini berisi file header, pustaka tipe, utilitas sederhana, kode contoh, dan dokumentasi.

Dengan menggunakan SDK Acrobat, Anda dapat mengembangkan perangkat lunak yang terintegrasi dengan Acrobat dan Adobe Reader dengan beberapa cara:

- **JavaScript** — Tulis skrip, baik dalam dokumen PDF individu atau secara eksternal, untuk memperluas fungsionalitas Acrobat atau Adobe Reader.
- **Plug-in** — Buat plug-in yang terhubung secara dinamis dan memperluas fungsionalitas Acrobat atau Adobe Reader.
- **Komunikasi antar aplikasi** — Tulis proses aplikasi terpisah yang menggunakan komunikasi antar aplikasi (IAC) untuk mengontrol fungsionalitas Acrobat. DDE dan OLE didukung di Microsoft® Windows®, dan peristiwa Apple/AppleScript di Mac OS®. IAC tidak tersedia di UNIX®.

Aspose.PDF for .NET menyediakan banyak fungsionalitas yang sama, membebaskan Anda dari ketergantungan pada Automasi Adobe Acrobat. Artikel ini menunjukkan cara menghasilkan gambar thumbnail dari dokumen PDF menggunakan pertama SDK Acrobat dan kemudian Aspose.PDF.

{{% /alert %}}

## Mengembangkan Aplikasi menggunakan API komunikasi antar aplikasi Acrobat

Anggaplah API Acrobat memiliki dua lapisan yang berbeda yang menggunakan objek Komunikasi Antar Aplikasi (IAC) Acrobat:

- Lapisan aplikasi Acrobat (AV). Lapisan AV memungkinkan Anda mengontrol bagaimana dokumen ditampilkan. Misalnya, tampilan objek dokumen berada di lapisan yang terkait dengan Acrobat.
- Lapisan dokumen portabel (PD). Lapisan PD memberikan akses ke informasi dalam dokumen, seperti halaman. Dari lapisan PD Anda dapat melakukan manipulasi dasar dokumen PDF, seperti menghapus, memindahkan, atau mengganti halaman, serta mengubah atribut anotasi. Anda juga dapat mencetak halaman PDF, memilih teks, mengakses teks yang dimanipulasi, dan membuat atau menghapus thumbnail.

Karena niat kami adalah mengubah halaman PDF menjadi gambar thumbnail, kami lebih fokus pada IAC. API IAC berisi objek seperti PDDoc, PDPage, PDAnnot, dan lainnya, yang memungkinkan pengguna untuk berurusan dengan lapisan dokumen portabel (PD). Contoh kode berikut memindai folder dan mengonversi halaman PDF menjadi gambar thumbnail. Dengan menggunakan SDK Acrobat, kami juga dapat membaca metadata PDF dan mengambil jumlah halaman dalam dokumen.

### Pendekatan Acrobat

Untuk menghasilkan gambar thumbnail untuk setiap dokumen, kami telah menggunakan SDK Adobe Acrobat 7.0 dan Microsoft .NET 2.0 Framework.

[SDK Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/) yang dikombinasikan dengan versi lengkap Adobe Acrobat mengekspos pustaka COM objek (sayangnya Adobe Reader gratis tidak mengekspos antarmuka COM) yang dapat digunakan untuk memanipulasi dan mengakses informasi PDF. Dengan menggunakan objek COM ini melalui COM Interop, muat dokumen PDF, ambil halaman pertama dan render halaman tersebut ke clipboard. Kemudian, dengan .NET Framework, salin ini ke bitmap, skala dan gabungkan gambar dan simpan hasilnya sebagai file GIF atau PNG.

Setelah Adobe Acrobat terinstal, gunakan regedit.exe dan lihat di bawah HKEY_CLASSES_ROOT untuk entri yang disebut AcroExch.PDDoc.

**Registri menunjukkan entri AcroExch.PDDDoc**

![todo:image_alt_text](generate-thumbnail-images-from-pdf-documents_1.png)

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // Acrobat objects
    Acrobat.CAcroPDDoc pdfDoc;
    Acrobat.CAcroPDPage pdfPage;
    Acrobat.CAcroRect pdfRect;
    Acrobat.CAcroPoint pdfPoint;

    AppSettingsReader appSettings = new AppSettingsReader();
    string pdfInputPath = appSettings.GetValue("pdfInputPath", typeof(string)).ToString();
    string pngOutputPath = appSettings.GetValue("pngOutputPath", typeof(string)).ToString();
    string templatePortraitFile = Application.StartupPath + @"\pdftemplate_portrait.gif";
    string templateLandscapeFile = Application.StartupPath + @"\pdftemplate_landscape.gif";

    // Get list of files to process from the input path
    string[] files = Directory.GetFiles(pdfInputPath, "*.pdf");

    for (int n = 0; n < files.Length; n++)
    {
        string inputFile = files[n];
        string outputFile = Path.Combine(pngOutputPath, Path.GetFileNameWithoutExtension(inputFile) + ".png");

        // Create PDF document
        pdfDoc = (Acrobat.CAcroPDDoc)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.PDDoc", "");

        if (pdfDoc.Open(inputFile) == 0)
        {
            throw new FileNotFoundException($"Unable to open PDF file: {inputFile}");
        }

        int pageCount = pdfDoc.GetNumPages();
        pdfPage = (Acrobat.CAcroPDPage)pdfDoc.AcquirePage(0);
        pdfPoint = (Acrobat.CAcroPoint)pdfPage.GetSize();

        pdfRect = (Acrobat.CAcroRect)Microsoft.VisualBasic.Interaction.CreateObject("AcroExch.Rect", "");
        pdfRect.Left = 0;
        pdfRect.right = pdfPoint.x;
        pdfRect.Top = 0;
        pdfRect.bottom = pdfPoint.y;

        pdfPage.CopyToClipboard(pdfRect, 0, 0, 100);
        IDataObject clipboardData = Clipboard.GetDataObject();

        if (clipboardData.GetDataPresent(DataFormats.Bitmap))
        {
            Bitmap pdfBitmap = (Bitmap)clipboardData.GetData(DataFormats.Bitmap);

            int thumbnailWidth = 45;
            int thumbnailHeight = 59;
            string templateFile = pdfPoint.x < pdfPoint.y ? templatePortraitFile : templateLandscapeFile;

            if (pdfPoint.x > pdfPoint.y)
            {
                // Swap width and height for landscape orientation
                (thumbnailWidth, thumbnailHeight) = (thumbnailHeight, thumbnailWidth);
            }

            Bitmap templateBitmap = new Bitmap(templateFile);
            Image pdfImage = pdfBitmap.GetThumbnailImage(thumbnailWidth, thumbnailHeight, null, IntPtr.Zero);

            Bitmap thumbnailBitmap = new Bitmap(thumbnailWidth + 7, thumbnailHeight + 7, System.Drawing.Imaging.PixelFormat.Format32bppArgb);

            templateBitmap.MakeTransparent();

            using (Graphics thumbnailGraphics = Graphics.FromImage(thumbnailBitmap))
            {
                thumbnailGraphics.DrawImage(pdfImage, 2, 2, thumbnailWidth, thumbnailHeight);
                thumbnailGraphics.DrawImage(templateBitmap, 0, 0);
                thumbnailBitmap.Save(outputFile, System.Drawing.Imaging.ImageFormat.Png);
            }

            Console.WriteLine("Generated thumbnail: {0}", outputFile);

            pdfDoc.Close();
            Marshal.ReleaseComObject(pdfPage);
            Marshal.ReleaseComObject(pdfRect);
            Marshal.ReleaseComObject(pdfDoc);
        }
    }
}
```

## Pendekatan Aspose.PDF for .NET

Aspose.PDF for .NET menyediakan dukungan luas untuk menangani dokumen PDF. Ini juga mendukung kemampuan untuk mengonversi halaman dokumen PDF ke berbagai format gambar. Fungsionalitas yang dijelaskan di atas dapat dengan mudah dicapai menggunakan Aspose.PDF for .NET.

Aspose.PDF memiliki manfaat yang berbeda:

- Anda tidak perlu menginstal Adobe Acrobat di sistem Anda untuk bekerja dengan file PDF.
- Menggunakan Aspose.PDF for .NET sederhana dan mudah dipahami dibandingkan dengan Automasi Acrobat.

Jika kita perlu mengonversi halaman PDF menjadi JPEG, namespace [Aspose.PDF.Devices](https://reference.aspose.com/pdf/net/aspose.pdf.devices) menyediakan kelas bernama [JpegDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/jpegdevice) untuk merender halaman PDF menjadi gambar JPEG. Silakan lihat cuplikan kode berikut.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GenerateThumbnailImagesFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Images();

    // Retrieve names of all the PDF files in a particular directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

    // Iterate through all the files entries in array
    for (int counter = 0; counter < fileEntries.Length; counter++)
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(fileEntries[counter]))
        {
            for (int pageCount = 1; pageCount <= document.Pages.Count; pageCount++)
            {
                using (FileStream imageStream = new FileStream(dataDir + @"\Thumbanils" + counter.ToString() + "_" + pageCount + ".jpg", FileMode.Create))
                {
                    var resolution = new Aspose.Pdf.Devices.Resolution(300);
                    var jpegDevice = new Aspose.Pdf.Devices.JpegDevice(45, 59, resolution, 100);
                    // Convert a particular page and save the image to stream
                    jpegDevice.Process(document.Pages[pageCount], imageStream);
                }
            }
        }
    }
}
```

{{% alert color="primary" %}}

- Terima kasih kepada CodeProject untuk [Menghasilkan Gambar Thumbnail dari dokumen PDF](https://www.codeproject.com/Articles/5887/Generate-Thumbnail-Images-from-PDF-Documents).
- Terima kasih kepada Acrobat untuk [referensi SDK Acrobat](https://opensource.adobe.com/dc-acrobat-sdk-docs/acrobatsdk/documentation.html).

{{% /alert %}}

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