---
title: Ekstrak Informasi Gambar dan Tanda Tangan
linktitle: Ekstrak Informasi Gambar dan Tanda Tangan
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /id/net/extract-image-and-signature-information/
description: Anda dapat mengekstrak gambar dari bidang tanda tangan dan mengekstrak informasi tanda tangan menggunakan kelas SignatureField dengan C#.
lastmod: "2024-11-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Image and Signature Information",
    "alternativeHeadline": "Extract PDF signature images and certificate details",
    "abstract": "Fungsi baru Aspose.PDF for .NET mengekstrak gambar dan informasi detail dari bidang tanda tangan PDF. Menggunakan C#, pengembang dapat mengambil gambar tanda tangan dan data sertifikat, termasuk kunci publik, sidik jari, dan detail penerbit, meningkatkan kemampuan manipulasi PDF. Ini meningkatkan verifikasi dan manajemen tanda tangan digital dalam aplikasi",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Extract Image, SignatureField class, ExtractImage method, ExtractCertificate method, C#, Aspose.PDF for .NET, PDF Signature, digital signature, signature information",
    "wordcount": "583",
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
    "url": "/net/extract-image-and-signature-information/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-image-and-signature-information/"
    },
    "dateModified": "2024-11-25",
    "description": "Anda dapat mengekstrak gambar dari bidang tanda tangan dan mengekstrak informasi tanda tangan menggunakan kelas SignatureField dengan C#."
}
</script>

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Mengekstrak Gambar dari Bidang Tanda Tangan

Aspose.PDF for .NET mendukung fitur untuk menandatangani file PDF secara digital menggunakan kelas [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) dan saat menandatangani dokumen, Anda juga dapat menetapkan gambar untuk `SignatureAppearance`. Sekarang, API ini juga menyediakan kemampuan untuk mengekstrak informasi tanda tangan serta gambar yang terkait dengan bidang tanda tangan.

Untuk mengekstrak informasi tanda tangan, kami telah memperkenalkan metode [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractimage) ke kelas SignatureField. Silakan lihat potongan kode berikut yang menunjukkan langkah-langkah untuk mengekstrak gambar dari objek `SignatureField`:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractImagesFromSignatureField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractingImage.pdf"))
    {
        // Searching for signature fields
        foreach (var field in document.Form)
        {
            var sf = field as Aspose.Pdf.Forms.SignatureField;
            if (sf == null)
            {
                continue;
            }

            using (Stream imageStream = sf.ExtractImage())
            {
                if (imageStream != null)
                {
                    continue;
                }

                using (System.Drawing.Image image = System.Drawing.Bitmap.FromStream(imageStream))
                {
                    // Save the image
                    image.Save(dataDir + "output_out.jpg", System.Drawing.Imaging.ImageFormat.Jpeg);
                }
            }
        }
    }
}
```

### Ganti Gambar Tanda Tangan

Terkadang Anda mungkin memiliki kebutuhan untuk hanya mengganti gambar dari bidang tanda tangan yang sudah ada di dalam file PDF. Untuk memenuhi kebutuhan ini, pertama-tama, kita perlu mencari bidang formulir di dalam file PDF, mengidentifikasi bidang Tanda Tangan, mendapatkan dimensi (dimensi persegi panjang) dari bidang tanda tangan dan kemudian menempelkan gambar di atas dimensi yang sama.

## Ekstrak Informasi Tanda Tangan

Aspose.PDF for .NET mendukung fitur untuk menandatangani file PDF secara digital menggunakan kelas SignatureField. Saat ini, kita juga dapat menentukan keabsahan sertifikat tetapi kita tidak dapat mengekstrak seluruh sertifikat. Informasi yang dapat diekstrak adalah kunci publik, sidik jari, penerbit, dll.

Untuk mengekstrak informasi tanda tangan, kami telah memperkenalkan metode [ExtractCertificate](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) ke kelas [SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield). Silakan lihat potongan kode berikut yang menunjukkan langkah-langkah untuk mengekstrak sertifikat dari objek SignatureField:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractCertificate()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ExtractSignatureInfo.pdf"))
    {
        // Searching for signature fields
        foreach (var field in document.Form)
        {
            var sf = field as Aspose.Pdf.Forms.SignatureField;
            if (sf == null)
            {
                continue;
            }
            // Extract certificate
            Stream cerStream = sf.ExtractCertificate();
            if (cerStream == null)
            {
                continue;
            }
            // Save certificate
            using (cerStream)
            {
                byte[] bytes = new byte[cerStream.Length];
                using (FileStream fs = new FileStream(dataDir + "input.cer", FileMode.CreateNew))
                {
                    cerStream.Read(bytes, 0, bytes.Length);
                    fs.Write(bytes, 0, bytes.Length);
                }
            }
        }
    }
}
```

Anda dapat mendapatkan informasi tentang algoritma tanda tangan dokumen.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void GetSignaturesInfo()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "signed_rsa.pdf"))
    {
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var sigNames = signature.GetSignatureNames();
            var signaturesInfoList =  signature.GetSignaturesInfo();
            foreach (var sigInfo in signaturesInfoList)
            {
                Console.WriteLine(sigInfo.DigestHashAlgorithm);
                Console.WriteLine(sigInfo.AlgorithmType);
                Console.WriteLine(sigInfo.CryptographicStandard);
                Console.WriteLine(sigInfo.SignatureName);
            }
        }
    }
}
```

Contoh output untuk contoh di atas:
```
Sha256
Rsa
Pkcs7
Signature1
```


## Memeriksa tanda tangan untuk kompromi

Anda dapat menggunakan kelas **SignaturesCompromiseDetector** untuk memverifikasi tanda tangan digital untuk kompromi.
Panggil metode **Check()** untuk memeriksa tanda tangan dokumen.
Jika tidak ada kompromi tanda tangan yang terdeteksi, metode ini akan mengembalikan true.
Jika metode ini mengembalikan false, Anda dapat memeriksa apakah tanda tangan yang dikompromikan menggunakan properti **HasCompromisedSignatures** dan mengambil daftar tanda tangan yang dikompromikan melalui properti **CompromisedSignatures**.

Untuk memverifikasi apakah tanda tangan yang ada mencakup seluruh dokumen, gunakan properti **SignaturesCoverage**.
Properti ini dapat memiliki nilai berikut:
- **Undefined** – jika salah satu tanda tangan secara eksplisit dikompromikan atau pemeriksaan cakupan gagal.
- **EntirelySigned** – jika tanda tangan mencakup seluruh dokumen.
- **PartiallySigned** – jika tanda tangan tidak mencakup seluruh dokumen dan ada konten yang tidak ditandatangani.

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Check(string pdfFile)
{
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(pdfFile))
    {   
        // Create the compromise detector instance
        var detector = new Aspose.Pdf.SignaturesCompromiseDetector(document);
        CompromiseCheckResult result;
    
        // Check for compromise
        if (detector.Check(out result))
        {
            Console.WriteLine("No signature compromise detected");
            return;
        }
         
        // Get information about compromised signatures
        if (result.HasCompromisedSignatures)
        {
            Console.WriteLine($"Count of compromised signatures: {result.CompromisedSignatures.Count}");
            foreach (var signatureName in result.CompromisedSignatures)
            {
                Console.WriteLine($"Signature name: {signatureName.FullName}");
            }
        }
         
        // Get info about signatures coverage
        Console.WriteLine(result.SignaturesCoverage);   
    }
}
```
{{< /tab >}}
{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Check(string pdfFile)
{
    // Open PDF document
    using var document = new Aspose.Pdf.Document(pdfFile);
    // Create the compromise detector instance
    var detector = new Aspose.Pdf.SignaturesCompromiseDetector(document);

    // Check for compromise
    if (detector.Check(out var result))
    {
        Console.WriteLine("No signature compromise detected");
        return;
    }
         
    // Get information about compromised signatures
    if (result.HasCompromisedSignatures)
    {
        Console.WriteLine($"Count of compromised signatures: {result.CompromisedSignatures.Count}");
        foreach (var signatureName in result.CompromisedSignatures)
        {
            Console.WriteLine($"Signature name: {signatureName.FullName}");
        }
    }
         
    // Get info about signatures coverage
    Console.WriteLine(result.SignaturesCoverage);
}
```
{{< /tab >}}
{{< /tabs >}}

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