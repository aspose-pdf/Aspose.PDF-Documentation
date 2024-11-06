---
title: Verificar Assinatura em Arquivo PDF
type: docs
weight: 30
url: pt/java/verify-signature-in-pdf/
description: Esta seção explica como trabalhar com Assinatura em um Arquivo PDF usando a classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Verificar se o Arquivo PDF está Assinado Usando uma Assinatura

Para verificar se um arquivo PDF está assinado usando o método VerifySigned da classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature). Este método requer o nome da assinatura e retorna verdadeiro se o PDF estiver assinado usando esse nome de assinatura. Também é possível verificar que um [PDF está assinado](/pdf/java/working-with-signature-in-a-pdf-file/), sem verificar com qual assinatura ele está assinado.

### Verificando se um PDF está Assinado com uma Determinada Assinatura

O seguinte trecho de código mostra como verificar se um PDF está assinado usando uma determinada assinatura.

```java
    public static void IsPdfSigned() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.containsSignature())
            System.out.println("Documento Assinado");

        pdfSign.close();
    }
```


### Verificando se um PDF está Assinado

Para determinar se um arquivo está assinado, sem fornecer o nome da assinatura, use o seguinte código.

```java
    public static void IsPdfSignedWithGivenSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySigned("Signature1")) {
            System.out.println("PDF Assinado");
        }
    }
```

## Verificar se a Assinatura é Válida

O método [VerifySignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#verifySignature-java.lang.String-) da classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) permite validar uma assinatura específica. Este método requer o nome da assinatura como entrada e retorna verdadeiro se a assinatura for válida. O seguinte trecho de código mostra como validar uma assinatura.

```java
    public static void IsPdfSignatureValid() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");
        if (pdfSign.verifySignature("Signature1")) {
            System.out.println("Assinatura Verificada");
        }
    }
```