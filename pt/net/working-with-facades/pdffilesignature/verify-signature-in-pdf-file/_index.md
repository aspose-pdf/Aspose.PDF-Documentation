---
title: Verificar Assinatura em Arquivo PDF
type: docs
weight: 30
url: /pt/net/verify-signature-in-pdf/
description: Esta seção explica como verificar assinatura em Arquivo PDF usando a classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Verificar Se o Arquivo PDF Está Assinado Usando uma Assinatura

Para verificar se um arquivo PDF está assinado usando uma [assinatura específica](/pdf/pt/net/working-with-signature-in-a-pdf-file/), use o método VerifySigned da classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Este método requer o nome da assinatura e retorna verdadeiro se o PDF estiver assinado usando esse nome de assinatura. Também é possível verificar se um [PDF está assinado](/pdf/pt/net/working-with-signature-in-a-pdf-file/), sem verificar com qual assinatura ele está assinado.

### Verificando se um PDF Está Assinado com uma Assinatura Dada

O trecho de código a seguir mostra como verificar se o PDF está assinado usando uma assinatura dada.

```csharp
public static void IsPdfSigned()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.ContainsSignature())
                Console.WriteLine("Documento Assinado");
            pdfSign.Close();
        }
```

### Verificando se um PDF está Assinado

Para determinar se um arquivo está assinado, sem fornecer o nome da assinatura, use o seguinte código.

```csharp
 public static void IsPdfSignedWithGivenSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySigned("Signature1"))
            {
                Console.WriteLine("PDF Assinado");
            }
            //if (pdfSign.VerifySigned("Signature2"))
            //{
            //    Console.WriteLine("PDF Assinado");
            //}
        }
```

## Verificar se a Assinatura é Válida

O método [VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) da classe [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) permite que você valide uma assinatura específica. Este método requer o nome da assinatura como entrada e retorna verdadeiro se a assinatura for válida. O trecho de código a seguir mostra como validar uma assinatura.

```csharp
public static void IsPdfSignatureValid()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySignature("Signature1"))
            {
                Console.WriteLine("Signature Verified");
            }
        }
```