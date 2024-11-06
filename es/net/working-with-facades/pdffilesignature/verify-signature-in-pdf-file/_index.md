---
title: Verificar Firma en Archivo PDF
type: docs
weight: 30
url: es/net/verify-signature-in-pdf/
description: Esta sección explica cómo verificar la firma en un archivo PDF usando la clase PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Verificar Si el Archivo PDF Está Firmado Usando una Firma

Para verificar si un archivo PDF está firmado usando una [firma particular](/pdf/net/working-with-signature-in-a-pdf-file/), use el método VerifySigned de la clase [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature). Este método requiere el nombre de la firma y devuelve verdadero si el PDF está firmado usando ese nombre de firma. También es posible verificar que un [PDF está firmado](/pdf/net/working-with-signature-in-a-pdf-file/), sin verificar con qué firma está firmado.

### Verificando que un PDF Está Firmado con una Firma Dada

El siguiente fragmento de código le muestra cómo verificar si un PDF está firmado usando una firma dada.

```csharp
public static void IsPdfSigned()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.ContainsSignature())
                Console.WriteLine("Documento Firmado");
            pdfSign.Close();
        }
```

### Verificando que un PDF está firmado

Para determinar si un archivo está firmado, sin proporcionar el nombre de la firma, utilice el siguiente código.

```csharp
 public static void IsPdfSignedWithGivenSignature()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySigned("Signature1"))
            {
                Console.WriteLine("PDF Signed");
            }
            //if (pdfSign.VerifySigned("Signature2"))
            //{
            //    Console.WriteLine("PDF Signed");
            //}
        }
```

## Verificar si la firma es válida

El método [VerifySignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature/methods/verifysignature) de la clase [PdfFileSignature](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilesignature) le permite validar una firma en particular. Este método requiere el nombre de la firma como entrada y devuelve verdadero si la firma es válida. El siguiente fragmento de código muestra cómo validar una firma.

```csharp
public static void IsPdfSignatureValid()
        {
            PdfFileSignature pdfSign = new PdfFileSignature();
            pdfSign.BindPdf(_dataDir + "DigitallySign.pdf");
            if (pdfSign.VerifySignature("Signature1"))
            {
                Console.WriteLine("Firma Verificada");
            }
        }
```