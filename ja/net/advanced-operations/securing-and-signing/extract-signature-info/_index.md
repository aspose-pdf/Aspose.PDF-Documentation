---
title: 画像と署名情報の抽出
linktitle: 画像と署名情報の抽出
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /ja/net/extract-image-and-signature-information/
description: C#を使用してSignatureFieldクラスを使って署名フィールドから画像を抽出し、署名情報を抽出できます。
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
    "abstract": "新しいAspose.PDF for .NET機能は、PDF署名フィールドから画像と詳細情報を抽出します。C#を使用して、開発者は署名画像と証明書データ（公開鍵、サムプリント、発行者の詳細を含む）を取得でき、PDF操作機能を向上させます。これにより、アプリケーション内でのデジタル署名の検証と管理が改善されます。",
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
    "description": "C#を使用してSignatureFieldクラスを使って署名フィールドから画像を抽出し、署名情報を抽出できます。"
}
</script>

次のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも動作します。

## 署名フィールドからの画像の抽出

Aspose.PDF for .NETは、[SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield)クラスを使用してPDFファイルにデジタル署名をする機能をサポートしており、文書に署名する際に`SignatureAppearance`の画像を設定することもできます。現在、このAPIは署名フィールドに関連付けられた画像と署名情報を抽出する機能も提供しています。

署名情報を抽出するために、SignatureFieldクラスに[ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractimage)メソッドを導入しました。以下のコードスニペットは、`SignatureField`オブジェクトから画像を抽出する手順を示しています。

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

### 署名画像の置き換え

時には、PDFファイル内の既存の署名フィールドの画像のみを置き換える必要がある場合があります。この要件を達成するために、まずPDFファイル内のフォームフィールドを検索し、署名フィールドを特定し、署名フィールドの寸法（矩形寸法）を取得し、同じ寸法に画像をスタンプする必要があります。

## 署名情報の抽出

Aspose.PDF for .NETは、SignatureFieldクラスを使用してPDFファイルにデジタル署名をする機能をサポートしています。現在、証明書の有効性を判断することもできますが、証明書全体を抽出することはできません。抽出できる情報は、公開鍵、サムプリント、発行者などです。

署名情報を抽出するために、[ExtractCertificate](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate)メソッドを[SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield)クラスに導入しました。以下のコードスニペットは、SignatureFieldオブジェクトから証明書を抽出する手順を示しています。

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

文書署名アルゴリズムに関する情報を取得できます。

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

上記の例のサンプル出力：
```
Sha256
Rsa
Pkcs7
Signature1
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