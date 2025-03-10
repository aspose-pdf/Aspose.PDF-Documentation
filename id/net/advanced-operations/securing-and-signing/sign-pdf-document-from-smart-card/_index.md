---
title: Cara menambahkan tanda tangan Kartu Pintar ke PDF
linktitle: Penandatanganan PDF dengan Kartu Pintar
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /id/net/sign-pdf-document-from-smart-card/
description: Aspose.PDF for .NET memungkinkan Anda untuk menandatangani dokumen PDF dari kartu pintar menggunakan bidang tanda tangan.
lastmod: "2024-11-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "How to add Smart Card signature to PDF",
    "alternativeHeadline": "Add Smart Card Signatures to PDF Documents Easily",
    "abstract": "Aspose.PDF for .NET sekarang memungkinkan penandatanganan PDF yang mulus menggunakan kartu pintar, meningkatkan keamanan digital dengan memungkinkan pengguna untuk mengautentikasi dokumen dengan sertifikat digital yang disimpan. Fungsionalitas ini mendukung baik bidang tanda tangan maupun opsi penandatanganan lanjutan, memastikan kepatuhan dan integritas dalam transaksi PDF",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Smart Card signature, PDF signing, Aspose.PDF for .NET, digital signatures, external signing service, PKCS7 signature, certificate selection, hash algorithm, signature field, signing PDF documents",
    "wordcount": "755",
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
    "url": "/net/sign-pdf-document-from-smart-card/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/sign-pdf-document-from-smart-card/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET memungkinkan Anda untuk menandatangani dokumen PDF dari kartu pintar menggunakan bidang tanda tangan."
}
</script>

Aspose.PDF for .NET menawarkan fungsionalitas untuk menambahkan tanda tangan digital dari lokasi penyimpanan kunci. Anda dapat menerapkan tanda tangan dengan menerima sertifikat yang disediakan oleh penyimpanan sertifikat, kartu pintar atau [kartu PIV](https://whatis.techtarget.com/definition/personal-identity-verification-PIV-card) yang terhubung ke sistem saat waktu berjalan.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Berikut adalah potongan kode untuk menandatangani dokumen PDF dari kartu pintar:

## Tandatangani Dengan Kartu Pintar Menggunakan Bidang Tanda Tangan

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetSignatureInfo()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open a document stream
    using (var fs = new FileStream(dataDir + "blank.pdf", FileMode.Open, FileAccess.ReadWrite))
    {
        // Open PDF document from stream
        using (var document = new Aspose.Pdf.Document(fs))
        {
            // Create a signature field
            var field1 = new Aspose.Pdf.Forms.SignatureField(document.Pages[1], new Aspose.Pdf.Rectangle(100, 400, 10, 10));

            // Sign with certificate selection in the windows certificate store
            var store = new X509Store(StoreLocation.CurrentUser);
            store.Open(OpenFlags.ReadOnly);
            
            // Manually chose the certificate in the store
            var sel = X509Certificate2UI.SelectFromCollection(store.Certificates, null, null, X509SelectionFlag.SingleSelection);

            // Set an external signature settings
            var externalSignature = new Aspose.Pdf.Forms.ExternalSignature(sel[0])
            {
                Authority = "Me",
                Reason = "Reason",
                ContactInfo = "Contact"
            };
            // Set a name of signature field
            field1.PartialName = "sig1";
            // Add the signature field to the document
            document.Form.Add(field1, 1);
            // Sign the document
            field1.Sign(externalSignature);
            // Save PDF document
            document.Save(dataDir + "externalSignature1_out.pdf");
        }
    }
}

private static void VerifyExternalSignature()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "externalSignature1.pdf"))
    {
        using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var sigNames = pdfSign.GetSignatureNames();
            for (int index = 0; index <= sigNames.Count - 1; index++)
            {
                if (!pdfSign.VerifySignature(sigNames[index]))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}
```

## Tandatangani Dengan Kartu Pintar Menggunakan Tanda Tangan File PDF

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void SignWithSmartCard()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "blank.pdf"))
    {
        using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
        {   
            // Bind PDF document
            pdfSign.BindPdf(document);

            // Sign with certificate selection in the windows certificate store
            var store = new X509Store(StoreLocation.CurrentUser);
            store.Open(OpenFlags.ReadOnly);
            // Manually chose the certificate in the store
            var sel = X509Certificate2UI.SelectFromCollection(store.Certificates, null, null, X509SelectionFlag.SingleSelection);
            
            // Set an external signature settings
            var externalSignature = new Aspose.Pdf.Forms.ExternalSignature(sel[0]);
            pdfSign.SignatureAppearance = dataDir + "demo.png";
            // Sign the document
            pdfSign.Sign(1, "Reason", "Contact", "Location", true, new System.Drawing.Rectangle(100, 100, 200, 200), externalSignature);
            // Save PDF document
            pdfSign.Save(dataDir + "externalSignature2_out.pdf");
        }
    }
}

private static void VerifyExternalSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "externalSignature1.pdf"))
    {
        using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var sigNames = pdfSign.GetSignatureNames();
            for (int index = 0; index <= sigNames.Count - 1; index++)
            {
                if (!pdfSign.VerifySignature(sigNames[index]))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}
```

Anda dapat menggunakan kelas ExternalSignature untuk layanan penandatanganan eksternal. ExternalSignature membuat tanda tangan PKCS7 dan tanda tangan PKCS7 terpisah.
Anda dapat melewatkan algoritma hashing yang diinginkan ke konstruktor ExternalSignature. Perhatikan bahwa tanda tangan yang tidak terpisah hanya dapat menggunakan SHA1.
Ini akan dipilih secara otomatis jika Anda tidak secara eksplisit menentukan algoritma hashing. Untuk tanda tangan yang tidak terpisah, itu akan menjadi SHA1; untuk terpisah, itu akan menjadi SHA-256 untuk kunci RSA. Untuk kunci ECDSA, ukuran hash tergantung pada ukuran kunci.

Konstruktor ExternalSignature juga menerima sertifikat kunci (itu bisa dalam format Base64). Anda dapat melewatkan sertifikat yang berisi kunci privat dan sertifikat yang hanya berisi kunci publik. Dalam kedua kasus, tanda tangan akan dilakukan secara eksternal dalam kode delegasi CustomSignHash, tetapi algoritma eksternal harus membuat tanda tangan yang sesuai dengan kunci dari sertifikat yang dilewatkan. Sertifikat diperlukan untuk menghasilkan dokumen yang ditandatangani dengan benar. Tanda tangan ECDSA tidak mendukung SHA-1.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithExternalService()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "blank.pdf"))
    {
        using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
        {
            // Bind PDF document
            sign.BindPdf(document);

            // Get public certificate
            X509Certificate2 signerCert = GetPublicCertificate();

            // Set a certificate and a digest algorithm
            var signature = new Aspose.Pdf.Forms.ExternalSignature(signerCert, Aspose.Pdf.DigestHashAlgorithm.Sha256);

            // Define a delegate to external sign
            Aspose.Pdf.Forms.SignHash customSignHash = delegate(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
            {
                return CallExternalSignatureService(signableHash, digestHashAlgorithm);
            };
            // Set a sign hash
            signature.CustomSignHash = customSignHash;
            sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), signature);
            // Save PDF document
            sign.Save(dataDir + "ExternalSignature_out.pdf");
        }
    }
}

private static X509Certificate2 GetPublicCertificate()
{
    // Your code to get a public certificate. The certificate can be supplied by a third-party service or a smart card
}

private static byte[] CallExternalSignatureService(byte[] hash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
{
    // Call a third-party service that provides a digital signature service
    // The method must return signed data
    // The digestHashAlgorithm argument points to the digest algorithm that was applied to the data to produce the value of the hash argument
}
```

Untuk membuat tanda tangan, perkiraan awal panjang tanda tangan digital yang akan datang diperlukan.
Jika Anda menggunakan SignHash untuk membuat tanda tangan digital, Anda mungkin menemukan bahwa delegasi dipanggil dua kali selama proses penyimpanan dokumen.
Jika karena alasan tertentu Anda tidak dapat mengizinkan dua panggilan, misalnya, jika permintaan kode PIN terjadi selama panggilan, Anda dapat menggunakan opsi __AvoidEstimatingSignatureLength__ untuk kelas PKCS1, PKCS7, PKCS7Detached, dan ExternalSignature.
Mengatur opsi ini menghindari langkah estimasi panjang tanda tangan dengan menetapkan nilai tetap sebagai panjang yang diharapkan - __DefaultSignatureLength__. Nilai default untuk properti DefaultSignatureLength adalah 3000 byte.
Opsi AvoidEstimatingSignatureLength hanya berfungsi jika delegasi SignHash diatur dalam properti CustomSignHash.
Jika panjang tanda tangan yang dihasilkan melebihi panjang yang diharapkan yang ditentukan oleh properti DefaultSignatureLength, Anda akan menerima __SignatureLengthMismatchException__ yang menunjukkan panjang yang sebenarnya.
Anda dapat menyesuaikan nilai parameter DefaultSignatureLength sesuai kebijaksanaan Anda.

Untuk __ExternalSignature__, opsi AvoidEstimatingSignatureLength dapat digunakan bahkan jika CustomSignHash tidak digunakan.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithExternalService()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "blank.pdf"))
    {
        using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
        {
            // Bind PDF document
            sign.BindPdf(document);

            // Get public certificate
            X509Certificate2 signerCert = GetPublicCertificate();

            // Set a certificate and a digest algorithm
            var signature = new Aspose.Pdf.Forms.ExternalSignature(signerCert, Aspose.Pdf.DigestHashAlgorithm.Sha256);

            // Define a delegate to external sign
            Aspose.Pdf.Forms.SignHash customSignHash = delegate(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
            {
                return CallExternalSignatureService(signableHash, digestHashAlgorithm);
            };
            // Set a sign hash
            signature.CustomSignHash = customSignHash;

            // Set an option to avoiding twice SignHash calling.
            signature.AvoidEstimatingSignatureLength = true;
            signature.DefaultSignatureLength = 3500;

            sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), signature);
            // Save PDF document
            sign.Save(dataDir + "ExternalSignature_out.pdf");
        }
    }
}

private static X509Certificate2 GetPublicCertificate()
{
    // Your code to get a public certificate. The certificate can be supplied by a third-party service or a smart card
}

private static byte[] CallExternalSignatureService(byte[] hash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
{
    // Call a third-party service that provides a digital signature service
    // The method must return signed data
    // The digestHashAlgorithm argument points to the digest algorithm that was applied to the data to produce the value of the hash argument
}
```

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