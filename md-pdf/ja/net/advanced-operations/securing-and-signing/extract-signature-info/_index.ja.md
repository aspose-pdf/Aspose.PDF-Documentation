---
title: 画像と署名情報を抽出
linktitle: 画像と署名情報を抽出
type: docs
weight: 30
url: /net/extract-image-and-signature-information/
description: 署名フィールドから画像を抽出し、SignatureField クラスを使用して署名情報を抽出することができます。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "画像と署名情報を抽出",
    "alternativeHeadline": "PDFから画像と署名を抽出する方法",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "PDF文書生成",
    "keywords": "PDF, C#, 署名抽出",
    "wordcount": "302",
    "proficiencyLevel":"初心者",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "dateModified": "2022-02-04",
    "description": "署名フィールドから画像を抽出し、SignatureField クラスを使用して署名情報を抽出することができます。"
}
</script>
以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/net/drawing/) ライブラリでも動作します。

## 署名フィールドから画像を抽出する

Aspose.PDF for .NET は、[SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) クラスを使用して PDF ファイルにデジタル署名する機能をサポートしており、ドキュメントに署名する際に SignatureAppearance 用の画像も設定できます。現在、この API は署名情報と署名フィールドに関連付けられた画像を抽出する機能も提供しています。

署名情報を抽出するために、SignatureField クラスに [ExtractImage](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractimage) メソッドを導入しました。次のコードスニペットをご覧ください。これは、SignatureField オブジェクトから画像を抽出する手順を示しています：

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

string input = dataDir+ @"ExtractingImage.pdf";
using (Document pdfDocument = new Document(input))
{
    foreach (Field field in pdfDocument.Form)
    {
        SignatureField sf = field as SignatureField;
        if (sf != null)
        {
            string outFile = dataDir+ @"output_out.jpg";
            using (Stream imageStream = sf.ExtractImage())
            {
                if (imageStream != null)
                {
                    using (System.Drawing.Image image = Bitmap.FromStream(imageStream))
                    {
                        image.Save(outFile, System.Drawing.Imaging.ImageFormat.Jpeg);
                    }
                }
            }
        }
    }
}
```
### 署名画像の置換

PDFファイル内に既に存在する署名フィールドの画像のみを置き換える必要がある場合があります。この要件を達成するために、まずPDFファイル内のフォームフィールドを検索し、署名フィールドを特定し、署名フィールドの寸法（矩形の寸法）を取得してから、同じ寸法に画像をスタンプします。

## 署名情報の抽出

Aspose.PDF for .NETは、SignatureFieldクラスを使用してPDFファイルにデジタル署名する機能をサポートしています。現在、証明書の有効性を判断することもできますが、証明書全体を抽出することはできません。抽出可能な情報には、公開鍵、サムプリント、発行者などがあります。

署名情報を抽出するために、[SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) クラスに [ExtractCertificate](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) メソッドを導入しました。
署名情報を抽出するために、[SignatureField](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield) クラスに [ExtractCertificate](https://reference.aspose.com/pdf/net/aspose.pdf.forms/signaturefield/methods/extractcertificate) メソッドを導入しました。

```csharp
// 完全な例とデータファイルについては、https://github.com/aspose-pdf/Aspose.PDF-for-.NET をご覧ください。
// ドキュメントディレクトリへのパス。
string dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

string input = dataDir + "ExtractSignatureInfo.pdf";
using (Document pdfDocument = new Document(input))
{
    foreach (Field field in pdfDocument.Form)
    {
        SignatureField sf = field as SignatureField;
        if (sf != null)
        {
            Stream cerStream = sf.ExtractCertificate();
            if (cerStream != null)
            {
                using (cerStream)
                {
                    byte[] bytes = new byte[cerStream.Length];
                    using (FileStream fs = new FileStream(dataDir + @"input.cer", FileMode.CreateNew))
                    {
                        cerStream.Read(bytes, 0, bytes.Length);
                        fs.Write(bytes, 0, bytes.Length);
                    }
                }
            }
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
                "contactType": "営業",
                "areaServed": "US",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "営業",
                "areaServed": "GB",
                "availableLanguage": "英語"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "営業",
                "areaServed": "AU",
                "availableLanguage": "英語"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": ".NET用PDF操作ライブラリ",
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
```

