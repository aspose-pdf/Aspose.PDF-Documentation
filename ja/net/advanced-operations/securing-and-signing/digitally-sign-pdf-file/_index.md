---
title: C#でデジタル署名を追加またはPDFにデジタル署名する
linktitle: PDFにデジタル署名
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /ja/net/digitally-sign-pdf-file/
description: C#またはVB.NETを使用してPDF文書にデジタル署名します。C#またはVB.NETを使用してデジタル署名されたPDFを検証または確認します。
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
    "abstract": "Aspose.PDF for .NETは、C#またはVB.NETを使用してPDF文書にデジタル署名するための強力な機能を提供し、文書の完全性とセキュリティを向上させます。ユーザーは、PKCS7およびECDSAをサポートする非分離型および分離型のさまざまな署名タイプを実装でき、特定の暗号基準に合わせたカスタマイズ可能な署名プロセスを可能にします。この機能は、文書の真正性を確認するだけでなく、タイムスタンプと認証を可能にし、信頼できる文書の取り扱いを保証します。",
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
    "description": "C#またはVB.NETを使用してPDF文書にデジタル署名します。C#またはVB.NETを使用してデジタル署名されたPDFを検証または確認します。"
}
</script>

Aspose.PDF for .NETは、SignatureFieldクラスを使用してPDFファイルにデジタル署名する機能をサポートしています。また、PKCS12証明書を使用してPDFファイルを認証することもできます。これは、[Adobe Acrobatでの署名とセキュリティの追加](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6)に似ています。

署名を使用してPDF文書に署名する際、基本的にはその内容を「そのまま」確認することになります。したがって、その後に行われた他の変更は署名を無効にし、文書が変更されたかどうかを知ることができます。一方、文書を最初に認証することで、ユーザーが認証を無効にすることなく文書に対して行える変更を指定できます。

言い換えれば、文書はその完全性を保持していると見なされ、受取人は文書を信頼できるままでいることができます。詳細については、PDFの認証と署名を参照してください。一般的に、文書の認証は.NET実行可能ファイルのコード署名に例えることができます。

以下のコードスニペットは、[Aspose.PDF.Drawing](/pdf/ja/net/drawing/)ライブラリでも機能します。

## Aspose.PDF for .NETの署名機能

PDF署名には以下のクラスとメソッドを使用できます。

- クラス [DocMDPSignature](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpsignature)。
- 列挙 [DocMDPAccessPermissions](https://reference.aspose.com/pdf/net/aspose.pdf.forms/docmdpaccesspermissions)。
- [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature)クラスのプロパティ [IsCertified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/properties/iscertified)。

PKCS12証明書（拡張子.p12、pfx）に基づくデジタル署名を作成するには、`PdfFileSignature`クラスのインスタンスを作成し、文書オブジェクトを渡します。
次に、次のクラスのいずれかのオブジェクトを作成して、希望するデジタル署名メソッドを指定する必要があります。

- PKCS1。
- PKCS7。
- PKCS7Detached。

_ダイジェストアルゴリズムは、`PKCS7Detached`のみに設定できます。`PKCS1`および`PKCS7`の場合、ダイジェストアルゴリズムは常にSHA-1に設定されます。_

次に、受け取った署名アルゴリズムオブジェクトを`PdfFileSignature.Sign()`メソッドで使用する必要があります。
デジタル署名は、文書が保存された後に設定されます。

## デジタル署名でPDFに署名する

以下の例は、SHA-1ダイジェストアルゴリズムを使用してPKCS7非分離型署名を作成します。
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

以下の例は、SHA-256ダイジェストアルゴリズムを使用してPKCS7Detached形式の分離型署名を作成します。キーアルゴリズムは証明書のキーに依存します。DSA、RSA、ECDSAがサポートされています。

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

PdfFileSignature.VerifySignature()メソッドを使用して署名を検証できます。
以前は、署名名を取得するために`GetSignNames()`メソッドが使用されていましたが、バージョン25.02以降は、`GetSignatureNames()`メソッドを使用する必要があります。このメソッドは、`SignatureName`のリストを返します。
`SignatureName`は、同じ名前の署名を検証する際の衝突を防ぎます。
文字列署名名の代わりに`SignatureName`型を受け入れるメソッドも使用する必要があります。

_注意：__PdfFileSignature.VerifySigned()__メソッドは非推奨です。_

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

## デジタル署名にタイムスタンプを追加する

### タイムスタンプ付きでPDFにデジタル署名する方法

Aspose.PDF for .NETは、タイムスタンプサーバーまたはWebサービスを使用してPDFにデジタル署名することをサポートしています。

この要件を達成するために、[TimestampSettings](https://reference.aspose.com/pdf/net/aspose.pdf/timestampsettings)クラスがAspose.PDF名前空間に追加されました。以下のコードスニペットを見て、タイムスタンプを取得し、PDF文書に追加する方法を確認してください。

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

## base64形式のX509Certificate2でPDFに署名する

このコードは、外部証明書を使用してPDFに署名し、サーバーと対話して署名されたハッシュを取得し、PDF文書に署名を埋め込む可能性があります。

PDFに署名する手順：

1. PdfFileSignatureのインスタンスを作成します。
1. カスタム署名ハッシュを定義します。
1. 証明書を読み込みます。
1. データに署名します。
1. PDFをバインドして署名します。
1. 署名されたPDFを保存します。

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

## ハッシュ署名機能でPDFに署名する

カスタムハッシュ署名機能を使用することで、署名権限は標準的な署名方法を超えた特定の暗号基準や内部セキュリティポリシーを実装でき、文書の完全性を確保します。
このアプローチは、署名が適用されて以来文書が変更されていないことを確認し、PFX証明書を使用して署名者の身元の検証可能な証拠を提供する法的拘束力のあるデジタル署名を提供します。

このコードスニペットは、C#でカスタムハッシュ署名機能を使用してPFX（PKCS#12）証明書を使用してPDF文書にデジタル署名する方法を示しています。

PDF署名プロセスを詳しく見てみましょう：

1. ファイルパスと証明書情報を定義します：

- inputPdf: 署名が必要な入力PDF文書へのパス。
- inputP12: 署名に使用される.p12（PFX）証明書ファイルへのパス。
- inputPfxPassword: PFX証明書のパスワード。
- outputPdf: 署名されたPDFが保存されるパス。

2. 署名プロセス：

- `PdfFileSignature`オブジェクトが作成され、入力PDFにバインドされます。
- PFX証明書とそのパスワードを使用して`PKCS7`オブジェクトが初期化されます。'CustomSignHash'メソッドがカスタムハッシュ署名機能として割り当てられます。
- `Sign`メソッドが呼び出され、ページ番号（この場合は1）、署名の詳細（理由、連絡先、場所）、および署名の位置（座標(0, 0, 500, 500)の長方形）を指定します。
- 署名されたPDFは、指定された出力パスに保存されます。

3. カスタムハッシュ署名：

- `CustomSignHash`メソッドは、署名可能なハッシュ（署名されるハッシュ）のバイト配列を受け入れます。
- 同じPFX証明書を読み込み、その秘密鍵を取得します。
- 秘密鍵を使用して、`RSACryptoServiceProvider`とSHA-1アルゴリズムを使用してハッシュに署名します。
- 署名されたデータ（バイト配列）がPDF署名に適用されるために返されます。

ダイジェストアルゴリズムは、PKCS7Detachedコンストラクタで指定できます。カスタムハッシュ署名デリゲートでサードパーティサービスを呼び出すことができます。CustomSignHashで使用される署名アルゴリズムは、PKCS7/PKCS7Detachedに渡される証明書のキーアルゴリズムと一致する必要があります。

以下の例は、RSAアルゴリズムとSHA-1ダイジェストアルゴリズムを使用して非分離型署名を作成します。
PKCS7の代わりにPKCS7Detachedを使用する場合、ECDCAを使用し、希望するダイジェストアルゴリズムを設定できます。

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

署名を作成するには、将来のデジタル署名の長さの予備的な見積もりが必要です。
SignHashを使用してデジタル署名を作成する場合、文書保存プロセス中にデリゲートが2回呼び出されることがあります。
何らかの理由で2回の呼び出しを許可できない場合、たとえば、呼び出し中にPINコードの要求が発生する場合、PKCS1、PKCS7、PKCS7Detached、およびExternalSignatureクラスのために`AvoidEstimatingSignatureLength`オプションを使用できます。
このオプションを設定すると、期待される長さとして固定値`DefaultSignatureLength`を設定することで署名長さの見積もりステップを回避します。DefaultSignatureLengthプロパティのデフォルト値は3000バイトです。
AvoidEstimatingSignatureLengthオプションは、CustomSignHashプロパティにSignHashデリゲートが設定されている場合にのみ機能します。
結果として得られた署名の長さがDefaultSignatureLengthプロパティで指定された期待される長さを超えると、実際の長さを示す`SignatureLengthMismatchException`が発生します。
DefaultSignatureLengthパラメータの値は、任意に調整できます。

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

## ECDSAを使用したPDF文書の署名

ECDSA（楕円曲線デジタル署名アルゴリズム）を使用してPDF文書に署名することは、楕円曲線暗号を利用してデジタル署名を生成することを含みます。これは、高いセキュリティと効率を提供し、特にモバイルやリソース制約のある環境に適しています。このアプローチは、PDF文書が楕円曲線暗号のセキュリティの利点を持ってデジタル署名されることを保証します。

Aspose.PDFは、ECDSAベースのデジタル署名の作成と検証をサポートしています。
デジタル署名の作成と検証にサポートされている楕円曲線は次のとおりです：

- P-192(secp192r1)。
- P-256(secp256r1)。
- P-384(secp384r1)。
- P-521(secp521r1)。
- brainpoolP192r1。
- brainpoolP256r1。
- brainpoolP384r1。
- brainpoolP512r1。

デフォルトのダイジェストアルゴリズムはSHA2で、長さはECDSAキーサイズに依存します。
ダイジェストアルゴリズムは、`PKCS7Detached`コンストラクタで指定できます。

次のダイジェストアルゴリズムを使用してECDSAデジタル署名を作成できます：SHA-256、SHA-384、SHA3–512、SHA3–256、SHA3–384、SHA3–512。
次のダイジェストアルゴリズムを使用してECDSAデジタル署名を検証できます：SHA-256、SHA-384、SHA3–512、SHA3–256、SHA3–384、SHA3–512。

署名と検証を確認するには、OpenSSLでPFX(output.pfx)証明書を作成します。

```bash
openssl ecparam -genkey -name brainpoolP512r1 -out private.key
openssl ec -in private.key -pubout -out public.pem
openssl req -new -x509 -days 365 -key private.key -out certificate.crt -subj "/C=PL/ST=Silesia/L=Katowice/O=My2 Organization/CN=example2.com"
openssl pkcs12 -export -out output.pfx -inkey private.key -in certificate.crt
```

Aspose.PDFでの署名と検証に使用可能な曲線名（OpenSSLでの曲線のリストは、コマンド'openssl ecparam -list_curves'で取得できます）：prime256v1、secp384r1、secp521r1、brainpoolP256r1、brainpoolP384r1、brainpoolP512r1。

ECDSAを使用してPDF文書に署名するには、C#での一般的な手順は次のとおりです：

1. PFXまたはP12形式のECDSA証明書が必要です。これらの証明書には、署名に必要な公開鍵と秘密鍵の両方が含まれています。
1. Aspose.PDFライブラリを使用して、文書を署名ハンドラーにバインドします。
1. ECDSA秘密鍵を使用して文書内容のハッシュに署名します。
1. 生成された署名をPDFファイル内に配置し、署名の理由、場所、連絡先の詳細などのメタデータを含めます。

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