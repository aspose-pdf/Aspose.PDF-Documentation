---
title: Bekerja dengan Tanda Tangan di File PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /id/net/working-with-signature-in-a-pdf-file/
description: Bagian ini menjelaskan cara mengekstrak informasi tanda tangan, mengekstrak gambar dari tanda tangan, mengubah bahasa, dan lain-lain menggunakan kelas PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with Signature in PDF File",
    "alternativeHeadline": "Extract Signature Details and Images from PDFs",
    "abstract": "Fungsi baru dalam Aspose.PDF for .NET meningkatkan keamanan dokumen PDF dengan memungkinkan pengguna untuk mengekstrak informasi dan gambar tanda tangan menggunakan kelas PdfFileSignature. Fitur ini juga mencakup kemampuan untuk menyesuaikan tanda tangan digital, menyembunyikan informasi tertentu seperti lokasi dan alasan, serta mengubah pengaturan bahasa untuk teks tanda tangan, menyediakan seperangkat alat yang komprehensif untuk mengelola tanda tangan PDF secara efisien.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "878",
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
    "url": "/net/working-with-signature-in-a-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-signature-in-a-pdf-file/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF dapat melakukan tidak hanya tugas yang sederhana dan mudah tetapi juga menangani tujuan yang lebih kompleks. Periksa bagian berikut untuk pengguna dan pengembang tingkat lanjut."
}
</script>

## Cara Mengekstrak Informasi Tanda Tangan

Aspose.PDF for .NET mendukung fitur untuk menandatangani file PDF secara digital menggunakan kelas PdfFileSignature. Saat ini, juga dimungkinkan untuk menentukan keabsahan sertifikat tetapi kami tidak dapat mengekstrak seluruh sertifikat. Informasi yang dapat diekstrak adalah kunci publik, sidik jari, dan penerbit, dll.

Untuk mengekstrak informasi tanda tangan, kami telah memperkenalkan metode ExtractCertificate(..) ke dalam kelas PdfFileSignature. Silakan lihat cuplikan kode berikut yang menunjukkan langkah-langkah untuk mengekstrak sertifikat dari objek PdfFileSignature:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSignatureInfo()
{ 
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "signed_rsa.pdf");
        // Get list of signature names
        var sigNames = pdfFileSignature.GetSignatureNames();
        if (sigNames.Count > 0)
        {
            SignatureName sigName = sigNames[0];            
            // Extract signature certificate
            Stream cerStream = pdfFileSignature.ExtractCertificate(sigName);
            if (cerStream != null)
            {
                using (cerStream)
                {
                    using (FileStream fs = new FileStream(dataDir + "extracted_cert.pfx", FileMode.CreateNew))
                    {
                        cerStream.CopyTo(fs);
                    }
                }
            }
            
        }
    }
}
```

## Mengekstrak Gambar dari Bidang Tanda Tangan (PdfFileSignature)

Aspose.PDF for .NET mendukung fitur untuk menandatangani file PDF secara digital menggunakan kelas PdfFileSignature dan saat menandatangani dokumen, Anda juga dapat mengatur gambar untuk SignatureAppearance. Sekarang API ini juga menyediakan kemampuan untuk mengekstrak informasi tanda tangan serta gambar yang terkait dengan bidang tanda tangan.

Untuk mengekstrak informasi tanda tangan, kami telah memperkenalkan metode ExtractImage(..) ke dalam kelas PdfFileSignature. Silakan lihat cuplikan kode berikut yang menunjukkan langkah-langkah untuk mengekstrak gambar dari objek PdfFileSignature:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractSignatureImage()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var signature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        signature.BindPdf(dataDir + "ExtractingImage.pdf");

        if (signature.ContainsSignature())
        {
            // Get list of signature names
            foreach (string sigName in signature.GetSignatureNames())
            {                
                // Extract signature image
                using (Stream imageStream = signature.ExtractImage(sigName))
                {
                    if (imageStream != null)
                    {
                        imageStream.Position = 0;
                        using (FileStream fs = new FileStream(dataDir + "ExtractImages_out.jpg", FileMode.OpenOrCreate))
                        {
                            imageStream.CopyTo(fs);
                        }
                    }
                }
            }
        }
    }
}
```

## Menyembunyikan Lokasi dan Alasan

Fungsi Aspose.PDF memungkinkan konfigurasi yang fleksibel untuk instance tanda tangan digital. Kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) menyediakan kemampuan untuk menandatangani file PDF. Implementasi metode Sign memungkinkan untuk menandatangani PDF dan meneruskan objek tanda tangan tertentu ke kelas ini. Metode Sign berisi sekumpulan atribut untuk kustomisasi tanda tangan digital keluaran. Jika Anda perlu menyembunyikan beberapa atribut teks dari hasil tanda tangan, Anda dapat membiarkannya kosong. Cuplikan kode berikut menunjukkan cara menyembunyikan dua baris Lokasi dan Alasan dari blok tanda tangan:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SupressLocationReason()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
        // Set signature appearance
        pdfFileSignature.SignatureAppearance = dataDir + "aspose-logo.png";

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdfFileSignature.Sign(1, string.Empty, "test01@aspose-pdf-demo.local", string.Empty, true, rect, signature);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

## Fitur Kustomisasi untuk Tanda Tangan Digital

Aspose.PDF for .NET memungkinkan fitur kustomisasi untuk tanda tangan digital. Metode Sign dari kelas [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) diimplementasikan dengan 6 overload untuk kenyamanan penggunaan Anda. Misalnya, Anda dapat mengonfigurasi tanda tangan hasil hanya dengan instance kelas SignatureCustomAppearance dan nilai propertinya. Cuplikan kode berikut menunjukkan cara menyembunyikan keterangan "Ditandatangani secara digital oleh" dari tanda tangan digital keluaran PDF Anda.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CustomizationFeaturesForDigitalSign()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1
        // Create signature appearance
        var signatureCustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
        {
            FontSize = 6,
            FontFamilyName = "Times New Roman",
            DigitalSignedLabel = "Signed by:"
        };
        // Set signature appearance
        signature.CustomAppearance = signatureCustomAppearance;

        pdfFileSignature.Sign(1, true, rect, signature);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

## Mengubah Bahasa dalam Teks Tanda Tangan Digital

Dengan menggunakan API Aspose.PDF for .NET, Anda dapat menandatangani file PDF menggunakan salah satu dari tiga jenis tanda tangan berikut:

- PKCS#1.
- PKCS#7.
- PKCS#12.

Setiap tanda tangan yang disediakan berisi sekumpulan properti konfigurasi yang diimplementasikan untuk kenyamanan Anda (lokalisasi, format tanggal waktu, keluarga font, dll). Kelas [SignatureCustomAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturecustomappearance) menyediakan fungsionalitas yang sesuai. Cuplikan kode berikut menunjukkan cara mengubah bahasa dalam teks tanda tangan digital: 

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ChangeLanguageInDigitalSignText()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();   
    
    using (var pdfFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");
        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(310, 45, 200, 50);

        // Create any of the three signature types
        var pkcs = new Aspose.Pdf.Forms.PKCS7(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Pruebas Firma",
            ContactInfo = "Contacto Pruebas",
            Location = "Población (Provincia)",
            Date = DateTime.Now
        };
        
        var signatureCustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
        {
            DateSignedAtLabel = "Fecha",
            DigitalSignedLabel = "Digitalmente firmado por",
            ReasonLabel = "Razón",
            LocationLabel = "Localización",
            FontFamilyName = "Arial",
            FontSize = 10d,
            Culture = System.Globalization.CultureInfo.InvariantCulture,
            DateTimeFormat = "yyyy.MM.dd HH:mm:ss"
        };
        // Set signature appearance
        pkcs.CustomAppearance = signatureCustomAppearance;
        // Sign the PDF file
        pdfFileSignature.Sign(1, true, rect, pkcs);
        // Save PDF document
        pdfFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```