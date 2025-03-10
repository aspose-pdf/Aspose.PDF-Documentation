---
title: Tambahkan tanda tangan digital atau tanda tangani PDF secara digital di C#
linktitle: Tanda tangan digital PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /id/net/digitally-sign-pdf-file/
description: Tanda tangani dokumen PDF secara digital menggunakan C# atau VB.NET. Verifikasi, atau validasi PDF yang ditandatangani secara digital menggunakan C# atau VB.NET.
lastmod: "2025-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add digital signature or digitally sign PDF in C#",
    "alternativeHeadline": "Working with digitally sign PDF",
    "abstract": "Aspose.PDF for .NET memperkenalkan kemampuan kuat untuk menandatangani dokumen PDF secara digital menggunakan C# atau VB.NET, meningkatkan integritas dan keamanan dokumen. Pengguna dapat menerapkan berbagai jenis tanda tangan, termasuk tanda tangan tidak terpisah dan terpisah dengan dukungan untuk PKCS7 dan ECDSA, memungkinkan proses penandatanganan yang dapat disesuaikan sesuai dengan standar kriptografi tertentu. Fitur ini tidak hanya memverifikasi keaslian dokumen tetapi juga memungkinkan penandaan waktu dan sertifikasi, memastikan penanganan dokumen yang tepercaya.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "digital signature, digitally sign PDF, C#, PDF signing, PKCS12 certificate, verify PDF signature, ECDSA signing, timestamp server, custom hash signing, Aspose.PDF for .NET",
    "wordcount": "2020",
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
    "url": "/net/digitally-sign-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/digitally-sign-pdf-file/"
    },
    "dateModified": "2025-02-07",
    "description": "Tanda tangani dokumen PDF secara digital menggunakan C# atau VB.NET. Verifikasi, atau validasi PDF yang ditandatangani secara digital menggunakan C# atau VB.NET."
}
</script>

Aspose.PDF for .NET mendukung fitur untuk menandatangani file PDF secara digital menggunakan kelas SignatureField. Anda juga dapat mengesahkan file PDF dengan Sertifikat PKCS12. Sesuatu yang mirip dengan [Menambahkan Tanda Tangan dan Keamanan di Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

Saat menandatangani dokumen PDF menggunakan tanda tangan, Anda pada dasarnya mengonfirmasi isinya "apa adanya". Akibatnya, setiap perubahan lain yang dilakukan setelahnya akan membatalkan tanda tangan dan dengan demikian, Anda akan tahu jika dokumen tersebut diubah. Sementara itu, mengesahkan dokumen terlebih dahulu memungkinkan Anda untuk menentukan perubahan yang dapat dilakukan pengguna pada dokumen tanpa membatalkan sertifikasi.

Dengan kata lain, dokumen tersebut masih dianggap mempertahankan integritasnya dan penerima masih dapat mempercayai dokumen tersebut. Untuk detail lebih lanjut, silakan kunjungi Mengesahkan dan menandatangani PDF. Secara umum, mengesahkan dokumen dapat dibandingkan dengan Penandatanganan Kode pada executable .NET.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/id/net/drawing/).

## Fitur penandatanganan Aspose.PDF for .NET

Kami dapat menggunakan kelas dan metode berikut untuk penandatanganan PDF

- Kelas [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature).
- Enumerasi [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions).
- Properti [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified) dalam kelas [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature).

Untuk membuat tanda tangan digital berdasarkan sertifikat PKCS12 (ekstensi file .p12, pfx), Anda harus membuat instance dari kelas `PdfFileSignature`, dengan melewatkan objek dokumen ke dalamnya. Selanjutnya, Anda harus menentukan metode tanda tangan digital yang diinginkan dengan membuat objek dari salah satu kelas:

- PKCS1.
- PKCS7.
- PKCS7Detached.

_Anda dapat mengatur algoritma digest hanya untuk `PKCS7Detached`. Untuk `PKCS1` dan `PKCS7`, algoritma digest selalu diatur ke SHA-1._

Selanjutnya, Anda perlu menggunakan objek algoritma tanda tangan yang diterima dalam metode `PdfFileSignature.Sign()`. Tanda tangan digital akan diatur untuk dokumen setelah disimpan.

## Tanda tangan PDF dengan tanda tangan digital

Contoh di bawah ini membuat tanda tangan PKCS7 tidak terpisah dengan algoritma digest SHA-1.
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignDocument()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7(dataDir + "rsa_cert.pfx", "12345");
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

Contoh di bawah ini membuat tanda tangan terpisah dalam format PKCS7Detached dengan algoritma digest SHA-256. Algoritma kunci tergantung pada kunci sertifikat. DSA, RSA, ECDSA didukung.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignDocument(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DigitallySign.pdf"))
    {
        // Instantiate PdfFileSignature object using the opened document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create PKCS#7 detached object for sign
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(pfxFilePath, password, Aspose.Pdf.DigestHashAlgorithm.Sha256);
            // Sign PDF file
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200),pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySign_out.pdf");
        }
    }
}
```

Anda dapat memverifikasi tanda tangan dengan menggunakan metode PdfFileSignature.VerifySignature(). Sebelumnya, metode `GetSignNames()` digunakan untuk mendapatkan nama tanda tangan. Mulai versi 25.02, metode `GetSignatureNames()` harus digunakan, yang mengembalikan daftar `SignatureName`. `SignatureName` mencegah tabrakan saat memverifikasi tanda tangan dengan nama yang sama. Metode yang menerima tipe `SignatureName` alih-alih nama tanda tangan string juga harus digunakan.

_Catatan, metode __PdfFileSignature.VerifySigned()__ sudah tidak digunakan lagi._

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void Verify()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "signed_rsa.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {         
            // Get a list of signature names in the document
            var sigNames = signature.GetSignatureNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                if (!signature.VerifySignature(sigName))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}
```

## Tambahkan cap waktu ke tanda tangan digital

### Cara menandatangani PDF secara digital dengan cap waktu

Aspose.PDF for .NET mendukung untuk menandatangani PDF secara digital dengan server cap waktu atau layanan Web.

Untuk memenuhi persyaratan ini, kelas [TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings) telah ditambahkan ke namespace Aspose.PDF. Silakan lihat potongan kode berikut yang memperoleh cap waktu dan menambahkannya ke dokumen PDF:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithTimeStampServer(string pfxFilePath, string password)
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "SimpleResume.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            var pkcs = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);
            // Create TimestampSettings settings
            var timestampSettings = new Aspose.Pdf.TimestampSettings("https://freetsa.org/tsr", string.Empty); // User/Password can be omitted
            pkcs.TimestampSettings = timestampSettings;
            System.Drawing.Rectangle rect = new System.Drawing.Rectangle(100, 100, 200, 100);
            // Create any of the three signature types
            signature.Sign(1, "Signature Reason", "Contact", "Location", true, rect, pkcs);
            // Save PDF document
            signature.Save(dataDir + "DigitallySignWithTimeStamp_out.pdf");
        }
    }
}
```

## Tanda tangan PDF dengan X509Certificate2 dalam format base64

Kode ini menandatangani PDF menggunakan sertifikat eksternal, mungkin berinteraksi dengan server untuk mengambil hash yang ditandatangani dan menyematkan tanda tangan ke dalam dokumen PDF.

Langkah-langkah untuk menandatangani PDF:

1. Buat instance dari PdfFileSignature.
1. Tentukan Hash Tanda Tangan Kustom.
1. Memuat sertifikat.
1. Menandatangani data.
1. Mengikat dan Menandatangani PDF.
1. Menyimpan PDF yang Ditandatangani.

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithBase64Certificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    var base64Str = "Certificate in base64 format";
    using (var pdfSign = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        var sign = new Aspose.Pdf.Forms.ExternalSignature(base64Str, false);// without Private Key
        sign.ShowProperties = false;
        // Create a delegate to external sign
        Aspose.Pdf.Forms.SignHash customSignHash = delegate (byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
        {
            // Simulated Server Part (This will probably just be sending data and receiving a response)
            var signerCert = new X509Certificate2(pfxFilePath, password, X509KeyStorageFlags.Exportable);// must have Private Key
            var rsaCSP = new RSACryptoServiceProvider();
            var xmlString = signerCert.PrivateKey.ToXmlString(true);
            rsaCSP.FromXmlString(xmlString);
            byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
            return signedData;
        };
        sign.CustomSignHash = customSignHash;
        // Bind PDF document
        pdfSign.BindPdf(dataDir + "input.pdf");
        // Sign the file
        pdfSign.Sign(1, "second approval", "second_user@example.com", "Australia", false,
            new System.Drawing.Rectangle(200, 200, 200, 100),
            sign);
        // Save PDF document
        pdfSign.Save(dataDir + "SignWithBase64Certificate_out.pdf");
    }
}
```

## Tanda tangan PDF dengan fungsi penandatanganan HASH

Dengan menggunakan fungsi penandatanganan hash kustom, otoritas penandatangan dapat menerapkan standar kriptografi tertentu atau kebijakan keamanan internal yang melampaui metode penandatanganan standar, memastikan integritas dokumen. Pendekatan ini membantu memverifikasi bahwa dokumen tidak diubah sejak tanda tangan diterapkan dan memberikan tanda tangan digital yang mengikat secara hukum dengan bukti yang dapat diverifikasi tentang identitas penandatangan menggunakan sertifikat PFX.

Potongan kode ini menunjukkan cara menandatangani dokumen PDF secara digital menggunakan sertifikat PFX (PKCS#12) dengan fungsi penandatanganan hash kustom dalam C#.

Mari kita lihat lebih dekat proses penandatanganan DPF:

1. Tentukan Jalur File dan Informasi Sertifikat:

- inputPdf: Jalur ke dokumen PDF input yang perlu ditandatangani.
- inputP12: Jalur ke file sertifikat .p12 (PFX) yang digunakan untuk penandatanganan.
- inputPfxPassword: Kata sandi untuk sertifikat PFX.
- outputPdf: Jalur di mana PDF yang ditandatangani akan disimpan.

2. Proses Tanda Tangan:

- Objek `PdfFileSignature` dibuat dan diikat ke PDF input.
- Objek `PKCS7` diinisialisasi menggunakan sertifikat PFX dan kata sandinya. Metode 'CustomSignHash' ditetapkan sebagai fungsi penandatanganan hash kustom.
- Metode `Sign` dipanggil, menentukan nomor halaman (1 dalam hal ini), detail tanda tangan (alasan, konten, lokasi), dan posisi (sebuah persegi panjang dengan koordinat (0, 0, 500, 500)) untuk tanda tangan.
- PDF yang ditandatangani kemudian disimpan ke jalur output yang ditentukan.

3. Penandatanganan Hash Kustom:

- Metode `CustomSignHash` menerima array byte signableHash (hash yang akan ditandatangani).
- Ini memuat sertifikat PFX yang sama dan mengambil kunci privatnya.
- Kunci privat digunakan untuk menandatangani hash menggunakan `RSACryptoServiceProvider` dan algoritma SHA-1.
- Data yang ditandatangani (array byte) dikembalikan untuk diterapkan pada tanda tangan PDF.

Algoritma digest dapat ditentukan dalam konstruktor PKCS7Detached. Layanan pihak ketiga dapat dipanggil dalam delegasi CustomSignHash. Algoritma tanda tangan yang digunakan dalam CustomSignHash harus cocok dengan algoritma kunci dalam sertifikat yang diteruskan ke PKCS7/PKCS7Detached.

Contoh di bawah ini membuat tanda tangan tidak terpisah dengan algoritma RSA dan algoritma digest SHA-1. Jika Anda menggunakan PKCS7Detached alih-alih PKCS7, Anda dapat menggunakan ECDCA dan mengatur algoritma digest yang diinginkan.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithCertificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {   
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        // Create PKCS#7 object to sign
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);// You can use PKCS7Detached with digest algorithm argument
        // Set the delegate to external sign
        pkcs7.CustomSignHash = CustomSignHash;
        // Sign the file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Custom hash signing function to generate a digital signature
    byte[] CustomSignHash(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
    {
        var inputP12 = "111.p12";
        var inputPfxPassword = "123456";
        X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
        RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    }
}
```

Untuk membuat tanda tangan, perkiraan awal panjang tanda tangan digital yang akan datang diperlukan. Jika Anda menggunakan SignHash untuk membuat tanda tangan digital, Anda mungkin menemukan bahwa delegasi dipanggil dua kali selama proses penyimpanan dokumen. Jika karena alasan tertentu Anda tidak dapat mengizinkan dua panggilan, misalnya, jika permintaan kode PIN terjadi selama panggilan, Anda dapat menggunakan opsi `AvoidEstimatingSignatureLength` untuk kelas PKCS1, PKCS7, PKCS7Detached, dan ExternalSignature. Mengatur opsi ini menghindari langkah estimasi panjang tanda tangan dengan menetapkan nilai tetap sebagai panjang yang diharapkan - `DefaultSignatureLength`. Nilai default untuk properti DefaultSignatureLength adalah 3000 byte. Opsi AvoidEstimatingSignatureLength hanya berfungsi jika delegasi SignHash diatur dalam properti CustomSignHash. Jika panjang tanda tangan yang dihasilkan melebihi panjang yang diharapkan yang ditentukan oleh properti DefaultSignatureLength, Anda akan menerima `SignatureLengthMismatchException` yang menunjukkan panjang sebenarnya. Anda dapat menyesuaikan nilai parameter DefaultSignatureLength sesuai kebijaksanaan Anda.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void SignWithCertificate(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var sign = new Aspose.Pdf.Facades.PdfFileSignature())
    {   
        // Bind PDF document
        sign.BindPdf(dataDir + "input.pdf");
        // Create PKCS#7 object to sign
        var pkcs7 = new Aspose.Pdf.Forms.PKCS7(pfxFilePath, password);// You can use PKCS7Detached with digest algorithm argument
        // Set the delegate to external sign
        pkcs7.CustomSignHash = CustomSignHash;
        // Set an option to avoiding twice SignHash calling.
        pkcs7.AvoidEstimatingSignatureLength = true;
        // Sign the file
        sign.Sign(1, "reason", "cont", "loc", false, new System.Drawing.Rectangle(0, 0, 500, 500), pkcs7);
        // Save PDF document
        sign.Save(dataDir + "SignWithCertificate_out.pdf");
    }

    // Custom hash signing function to generate a digital signature
    byte[] CustomSignHash(byte[] signableHash, Aspose.Pdf.DigestHashAlgorithm digestHashAlgorithm)
    {
        var inputP12 = "111.p12";
        var inputPfxPassword = "123456";
        X509Certificate2 signerCert = new X509Certificate2(inputP12, inputPfxPassword, X509KeyStorageFlags.Exportable);
        RSACryptoServiceProvider rsaCSP = new RSACryptoServiceProvider();
        var xmlString = signerCert.PrivateKey.ToXmlString(true);
        rsaCSP.FromXmlString(xmlString);
        byte[] signedData = rsaCSP.SignData(signableHash, CryptoConfig.MapNameToOID("SHA1"));
        return signedData;
    }
}
```

## Menandatangani dokumen PDF menggunakan ECDSA

Menandatangani dokumen PDF menggunakan ECDSA (Elliptic Curve Digital Signature Algorithm) melibatkan pemanfaatan kriptografi kurva elips untuk menghasilkan tanda tangan digital. Ini menawarkan keamanan dan efisiensi tinggi, terutama untuk lingkungan seluler dan yang terbatas sumber daya. Pendekatan ini memastikan bahwa dokumen PDF Anda ditandatangani secara digital dengan keuntungan keamanan dari kriptografi kurva elips.

Aspose.PDF mendukung pembuatan dan verifikasi tanda tangan digital berbasis ECDSA. Kurva elips berikut didukung untuk pembuatan dan verifikasi tanda tangan digital:

- P-192(secp192r1).
- P-256(secp256r1).
- P-384(secp384r1).
- P-521(secp521r1).
- brainpoolP192r1.
- brainpoolP256r1.
- brainpoolP384r1.
- brainpoolP512r1.

Algoritma digest default adalah SHA2 dengan panjang yang bergantung pada ukuran kunci ECDSA. Anda dapat menentukan algoritma digest dalam konstruktor `PKCS7Detached`.

Tanda tangan digital ECDSA dengan algoritma digest berikut dapat ditandatangani: SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512. Tanda tangan digital ECDSA dengan algoritma digest berikut dapat diverifikasi: SHA-256, SHA-384, SHA3–512, SHA3–256, SHA3–384, SHA3–512.

Anda dapat memeriksa tanda tangan dan verifikasi dengan membuat sertifikat PFX(output.pfx) di OpenSSL.

```bash
openssl ecparam -genkey -name brainpoolP512r1 -out private.key
openssl ec -in private.key -pubout -out public.pem
openssl req -new -x509 -days 365 -key private.key -out certificate.crt -subj "/C=PL/ST=Silesia/L=Katowice/O=My2 Organization/CN=example2.com"
openssl pkcs12 -export -out output.pfx -inkey private.key -in certificate.crt
```

Nama kurva yang tersedia untuk tanda tangan dan verifikasi di Aspose.PDF (daftar kurva di OpenSSL dapat diperoleh dengan perintah 'openssl ecparam -list_curves'): prime256v1, secp384r1, secp521r1, brainpoolP256r1, brainpoolP384r1, brainpoolP512r1.

Untuk menandatangani dokumen PDF menggunakan ECDSA, langkah-langkah umum dalam C# adalah:

1. Anda memerlukan sertifikat ECDSA dalam format PFX atau P12. Sertifikat ini berisi kunci publik dan privat yang diperlukan untuk penandatanganan.
1. Menggunakan pustaka Aspose.PDF, Anda mengikat dokumen ke pengelola tanda tangan.
1. Gunakan kunci privat ECDSA untuk menandatangani hash dari konten dokumen.
1. Tempatkan tanda tangan yang dihasilkan di dalam file PDF bersama dengan metadata seperti alasan penandatanganan, lokasi, dan detail kontak.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void VerifyEcda()
{
   // The path to the documents directory
   var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

   // Open PDF document
   using (var document = new Aspose.Pdf.Document(dataDir + "signed_ecdsa.pdf"))
    {
        // Create an instance of PdfFileSignature for working with signatures in the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Check if the document contains any digital signatures
            if (!signature.ContainsSignature())
            {
                throw new Exception("Not contains signature");
            }

            // Get a list of signature names in the document
            var sigNames = signature.GetSignatureNames();

            // Loop through all signature names to verify each one
            foreach (var sigName in sigNames)
            {
                // Verify that the signature with the given name is valid
                if (!signature.VerifySignature(sigName))
                {
                    throw new Exception("Not verified");
                }
            }
        }
    }
}

private static void SignEcdsa(string pfxFilePath, string password)
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures(); 

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "input.pdf"))
    {
        // Create an instance of PdfFileSignature to sign the document
        using (var signature = new Aspose.Pdf.Facades.PdfFileSignature(document))
        {
            // Create a PKCS7Detached object using the provided certificate and password
            var pkcs = new Aspose.Pdf.Forms.PKCS7Detached(cert, "12345", Aspose.Pdf.DigestHashAlgorithm.Sha256);

            // Sign the first page of the document, setting the signature's appearance at the specified location
            signature.Sign(1, true, new System.Drawing.Rectangle(300, 100, 400, 200), pkcs);

            // Save PDF document
            signature.Save(dataDir + "SignEcdsa_out.pdf");
        }
    }
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