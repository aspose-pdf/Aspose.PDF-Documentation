---
title: Adicionar Assinatura em Arquivo PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /pt/net/add-signature-in-pdf/
description: Esta seção explica como adicionar assinatura a um arquivo PDF usando a classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Add Signature in PDF File",
    "alternativeHeadline": "Add Custom Digital Signatures to PDF Files",
    "abstract": "Melhore seus documentos PDF com a nova capacidade de adicionar assinaturas digitais usando a classe PdfFileSignature. Este recurso permite que os usuários apliquem vários tipos de assinatura, incluindo PKCS#1, PKCS#7 e PKCS#7Detached, enquanto personalizam a aparência da assinatura com imagens e atributos específicos. Simplifique seu processo de verificação de documentos incorporando várias assinaturas em diferentes páginas com facilidade.",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "838",
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
    "url": "/net/add-signature-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/add-signature-in-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários e desenvolvedores avançados."
}
</script>

## Adicionar Assinatura Digital em um Arquivo PDF

A classe [PdfFileSignature](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffilesignature) permite que você adicione uma assinatura em um arquivo PDF. Você precisa criar um objeto da classe [PdfFileSignature](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffilesignature) usando os arquivos PDF de entrada e saída. Você também precisa criar um objeto [Rectangle](https://reference.aspose.com/pdf/pt/net/aspose.pdf/rectangle) onde deseja adicionar a assinatura e, para definir a aparência, pode especificar uma imagem usando a propriedade [SignatureAppearance](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffilesignature/properties/signatureappearance) do objeto [PdfFileSignature](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffilesignature). Aspose.Pdf.Facades também fornece diferentes tipos de assinaturas, como PKCS#1, PKCS#7 e PKCS#7Detached. Para criar uma assinatura de um tipo específico, você precisa criar um objeto da classe particular, como **PKCS1**, **PKCS7** ou **PKCS7Detached**, usando o arquivo de certificado e a senha.

Uma vez que o objeto de um tipo de assinatura específico é criado, você pode usar o método [Sign](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffilesignature/methods/sign/index) da classe [PdfFileSignature](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffilesignature) para assinar o PDF e passar o objeto de assinatura específico para esta classe. Você também pode especificar outros atributos para este método. Finalmente, você precisa salvar o PDF assinado usando o método [Save](https://reference.aspose.com/pdf/pt/net/aspose.pdf/document/methods/save/index) da classe [PdfFileSignature](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffilesignature). O seguinte trecho de código mostra como adicionar uma assinatura em um arquivo PDF.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for signature location
        System.Drawing.Rectangle rect = new System.Drawing.Rectangle(10, 10, 300, 50);
    
        // Set signature appearance
        pdFileSignature.SignatureAppearance = dataDir + "aspose-logo.png";

        // Create any of the three signature types
        var signature = new PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(1, "I'm document author", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect, signature);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

O seguinte exemplo de código nos mostra a capacidade de assinar um documento com duas assinaturas. Em nosso exemplo, colocamos a primeira assinatura na primeira página e a segunda na segunda página. Você pode especificar as páginas que precisa.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddTwoSignature()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create a rectangle for 1st signature location
        System.Drawing.Rectangle rect1 = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create 1st signature object
        var signature1 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(1, "I'm document author", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect1, signature1);
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");

        // Sign with 2nd signature
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "DigitallySign_out.pdf");

        // Create a rectangle for 2nd signature location
        System.Drawing.Rectangle rect2 = new System.Drawing.Rectangle(10, 10, 300, 50);

        // Create 2nd signature object
        var signature2 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345"); // PKCS#1

        pdFileSignature.Sign(2, "I'm document reviewer", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Australia", true, rect2, signature2);

        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign2_out.pdf");
    }
}
```

Para um documento com formulários ou acroforms que precisa ser assinado, veja o seguinte exemplo. Você precisa criar um objeto da classe [PdfFileSignature](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades/pdffilesignature) usando os arquivos PDF de entrada e saída. Use [BindPdf](https://reference.aspose.com/pdf/pt/net/aspose.pdf.facades.pdffilesignature/bindpdf/methods/1) para vinculação. Crie uma assinatura com a capacidade de adicionar as propriedades necessárias. Em nosso exemplo, elas são 'Reason' e 'CustomAppearance'.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignatureField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "input.pdf");

        // Create any of the three signature types
        var signature = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Author",
            CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
            {
                FontSize = 6,
                FontFamilyName = "Calibri"
            }
        }; // PKCS#1
        
        pdFileSignature.Sign("Signature1", signature);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
    }
}
```

Se nosso documento tiver dois campos, o algoritmo para assiná-lo é semelhante ao primeiro exemplo.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AddPdfFileSignatureField2()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_SecuritySignatures();

    using (var pdFileSignature = new Aspose.Pdf.Facades.PdfFileSignature())
    {
        // Bind PDF document
        pdfFileSignature.BindPdf(dataDir + "input.pdf");

        // Create any of the three signature types
        var signature1 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Author",
            CustomAppearance = new Aspose.Pdf.Forms.SignatureCustomAppearance
            {
                FontSize = 6
            }
        }; // PKCS#1
        pdFileSignature.Sign("Signature1", signature1);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign_out.pdf");
        // Bind PDF document
        pdFileSignature.BindPdf(dataDir + "DigitallySign_out.pdf");

        // Create any of the three signature types
        var signature2 = new Aspose.Pdf.Forms.PKCS1(dataDir + "rsa_cert.pfx", "12345")
        {
            Reason = "Sign as Reviwer",
            CustomAppearance = new SignatureCustomAppearance
            {
                FontSize = 6
            }
        }; // PKCS#1
        
        pdFileSignature.Sign("Signature2", signature2);
        // Save PDF document
        pdFileSignature.Save(dataDir + "DigitallySign2_out.pdf");
    }
}
```