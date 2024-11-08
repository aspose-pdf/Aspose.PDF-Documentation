---
title: Add Signature in PDF File
type: docs
weight: 10
url: /pt/java/add-signature-in-pdf/
description: Esta seção explica como trabalhar com Assinatura em um Arquivo PDF usando a classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Adicionar Assinatura Digital em um Arquivo PDF (facades)

A classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) permite que você adicione uma assinatura em um arquivo PDF. Você precisa criar um objeto da classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) usando arquivos PDF de entrada e saída. Você também precisa criar um objeto Rectangle no qual deseja adicionar a assinatura e, para definir a aparência, pode especificar uma imagem usando a propriedade setSignatureAppearance do objeto [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature).

Aspose.Pdf.Facades também fornece diferentes tipos de assinaturas como PKCS#1, PKCS#7 e PKCS#7Detached.
 Para criar uma assinatura de um tipo específico, você precisa criar um objeto da classe específica como PKCS1, PKCS7 ou PKCS7Detached usando o arquivo de certificado e a senha.

Uma vez que o objeto de um tipo específico de assinatura é criado, você pode usar o método sign da classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) para assinar o PDF e passar o objeto de assinatura específico para esta classe. Você também pode especificar outros atributos para este método. Finalmente, você precisa salvar o PDF assinado usando o método save da classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature). O trecho de código a seguir mostra como adicionar uma assinatura em um arquivo PDF.

```java
public static void AddPdfFileSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Criar um retângulo para a localização da assinatura
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);
        // Definir aparência da assinatura
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // Criar qualquer um dos três tipos de assinatura
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "Eu sou o autor do documento", "test01@aspose-pdf-demo.local", "Aspose Pdf Demo, Austrália", true, rect,
                signature);
        // Salvar arquivo PDF de saída
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```

O exemplo de código a seguir nos mostra a capacidade de assinar um documento com duas assinaturas. Em nosso exemplo, colocamos a primeira assinatura na primeira página e a segunda na segunda página. Você pode especificar as páginas que precisa.

```java
    public static void AddTwoSignature() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        // Assinar com a 1ª assinatura

        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Criar um retângulo para a localização da 1ª assinatura
        java.awt.Rectangle rect1 = new java.awt.Rectangle(10, 10, 300, 50);

        // Criar objeto da 1ª assinatura
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "Sou o autor do documento", "test@aspose-pdf-demo.local", "Aspose Pdf Demo, Austrália", true, rect1,
                signature1);
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        // Assinar com a 2ª assinatura

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // Criar um retângulo para a localização da 2ª assinatura
        java.awt.Rectangle rect2 = new java.awt.Rectangle(10, 10, 300, 50);

        // Criar objeto da 2ª assinatura
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(2, "Sou o revisor do documento", "test02@aspose-pdf-demo.local", "Aspose Pdf Demo, Austrália", true,
                rect2, signature2);

        // Salvar arquivo PDF de saída
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


Para um documento com formulários ou acroforms que precisa ser assinado, veja o exemplo a seguir. Você precisa criar um objeto da classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) usando arquivos PDF de entrada e saída. Use bindPdf para vinculação. Crie uma assinatura com a capacidade de adicionar as propriedades necessárias. Em nosso exemplo, elas são 'Reason' e 'CustomAppearance'.

```java
  public static void AddPdfFileSignatureField() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample02.pdf");

        // Crie qualquer um dos três tipos de assinatura
        PKCS1 signature = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature.setReason("Assinar como Autor");

        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        // PKCS#1
        pdfSign.sign("Signature1", signature);
        // Salve o arquivo PDF de saída
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


Se o nosso documento tiver dois campos, o algoritmo para assiná-lo é semelhante ao primeiro exemplo.

```java
   public static void AddPdfFileSignatureField2() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample03.pdf");

        // Crie qualquer um dos três tipos de assinatura
        PKCS1 signature1 = new PKCS1(_dataDir + "test01.pfx", "Aspose2021");
        SignatureCustomAppearance sca = new SignatureCustomAppearance();
        signature1.setCustomAppearance(sca);
        sca.setFontSize(6);
        sca.setFontFamilyName("Calibri");

        signature1.setReason("Assinar como Autor"); // PKCS#1
        pdfSign.sign("Signature1", signature1);

        // Salvar arquivo PDF de saída
        pdfSign.save(_dataDir + "DigitallySign.pdf");

        pdfSign.bindPdf(_dataDir + "DigitallySign.pdf");

        // Crie qualquer um dos três tipos de assinatura
        PKCS1 signature2 = new PKCS1(_dataDir + "test02.pfx", "Aspose2021");
        signature2.setReason("Assinar como Revisor"); // PKCS#1
        signature2.setCustomAppearance(sca);
        pdfSign.sign("Signature2", signature2);
        // Salvar arquivo PDF de saída
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```