---
title: Trabalhando com Assinatura em Arquivo PDF
type: docs
weight: 40
url: /pt/java/working-with-signature-in-a-pdf-file/
description: Esta seção explica como trabalhar com Assinatura em um Arquivo PDF usando a classe PdfFileSignature.
lastmod: "2021-06-05"
draft: false
---

## Como Extrair Informações da Assinatura

Aspose.PDF para Java suporta o recurso de assinar digitalmente arquivos PDF usando a classe PdfFileSignature. Atualmente, também é possível determinar a validade de um certificado, mas não podemos extrair o certificado inteiro. As informações que podem ser extraídas são a chave pública, impressão digital e emissor, etc.

Para extrair informações da assinatura, introduzimos o método extractCertificate(..) na classe PdfFileSignature. Por favor, veja o seguinte trecho de código que demonstra os passos para extrair o certificado do objeto PdfFileSignature:

```java
public static void ExtractSignatureInfo() {
        String input = _dataDir + "DigitallySign.pdf";
        String certificateFileName = "extracted_cert.pfx";
        PdfFileSignature pdfFileSignature = new PdfFileSignature();
        pdfFileSignature.bindPdf(input);
        List<String> sigNames = pdfFileSignature.getSignNames();

        if (sigNames.size() > 0) {
            String sigName = sigNames.get(0);
            if (sigName != "") {
                InputStream cerStream = pdfFileSignature.extractCertificate(sigName);
                if (cerStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(_dataDir + certificateFileName);
                        cerStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }

                }
            }
        }
    }
```


## Extraindo Imagem do Campo de Assinatura (PdfFileSignature)

Aspose.PDF para Java suporta o recurso de assinar digitalmente os arquivos PDF usando a classe PdfFileSignature e, ao assinar o documento, você também pode definir uma imagem para SignatureAppearance. Agora esta API também oferece a capacidade de extrair informações de assinatura, bem como a imagem associada ao campo de assinatura.

Para extrair informações de assinatura, introduzimos o método [extractImage(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature#extractImage-java.lang.String-) na classe PdfFileSignature. Por favor, veja o trecho de código a seguir que demonstra os passos para extrair a imagem do objeto PdfFileSignature:

```java
 public static void ExtractSignatureImage() {
        PdfFileSignature signature = new PdfFileSignature();
        signature.bindPdf(_dataDir + "DigitallySign.pdf");
        if (signature.containsSignature()) {
            for (String sigName : signature.getSignNames()) {
                String outFile = _dataDir + sigName + "_ExtractImages_out.jpg";
                InputStream imageStream = signature.extractImage(sigName);
                if (imageStream != null) {
                    FileOutputStream fs;
                    try {
                        fs = new FileOutputStream(outFile);
                        imageStream.transferTo(fs);
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
```


## Suprimir Localização e Motivo

A funcionalidade do Aspose.PDF permite uma configuração flexível para instâncias de assinatura digital. A classe [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileSignature) fornece a capacidade de assinar um arquivo PDF. A implementação do método Sign permite assinar o PDF e passar o objeto de assinatura específico para esta classe. O método Sign contém um conjunto de atributos para a personalização da assinatura digital de saída. Caso você precise suprimir alguns atributos de texto da assinatura resultante, você pode deixá-los vazios. O trecho de código a seguir demonstra como suprimir as duas linhas de Localização e Motivo do bloco de assinatura:

```java
public static void SupressLocationReason() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Criar um retângulo para a localização da assinatura
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // Definir a aparência da assinatura
        pdfSign.setSignatureAppearance(_dataDir + "aspose-logo.png");

        // Criar qualquer um dos três tipos de assinatura
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        pdfSign.sign(1, "", "test01@aspose-pdf-demo.local", "", true, rect, signature);
        // Salvar o arquivo PDF de saída
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## Recursos de Personalização para Assinatura Digital

Aspose.PDF para Java permite recursos de personalização para uma assinatura digital. O método Sign da classe SignatureCustomAppearance é implementado com 6 sobrecargas para seu uso confortável. Por exemplo, você pode configurar a assinatura resultante apenas pela instância da classe SignatureCustomAppearance e seus valores de propriedades. O seguinte trecho de código demonstra como ocultar a legenda "Assinado digitalmente por" da assinatura digital de saída do seu PDF.

```java
    public static void CustomizationFeaturesForDigitalSign() {
        PdfFileSignature pdfSign = new PdfFileSignature();
        pdfSign.bindPdf(_dataDir + "sample01.pdf");

        // Cria um retângulo para a localização da assinatura
        java.awt.Rectangle rect = new java.awt.Rectangle(10, 10, 300, 50);

        // Cria qualquer um dos três tipos de assinatura
        PKCS1 signature = new PKCS1(_dataDir + "test01.pfx", "Aspose2021"); // PKCS#1

        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setFontSize(6);
        signatureCustomAppearance.setFontFamilyName("Times New Roman");
        signatureCustomAppearance.setDigitalSignedLabel("ASSINADO POR:");
        signature.setCustomAppearance(signatureCustomAppearance);

        pdfSign.sign(1, true, rect, signature);
        // Salva o arquivo PDF de saída
        pdfSign.save(_dataDir + "DigitallySign.pdf");
    }
```


## Alterar Idioma No Texto Da Assinatura Digital

Usando Aspose.PDF para Java API, você pode assinar um arquivo PDF usando qualquer um dos três tipos de assinaturas a seguir:

- PKCS#1
- PKCS#7
- PKCS#7

Cada uma das assinaturas fornecidas contém um conjunto de propriedades de configuração implementadas para sua conveniência (localização, formato de data e hora, família de fontes, etc.). A classe SignatureCustomAppearance fornece a funcionalidade correspondente. O snippet de código a seguir demonstra como alterar o idioma no texto da assinatura digital:

```java
     public static void ChangeLanguageInDigitalSignText() {
        String inFile = _dataDir + "sample01.pdf";
        String outFile = _dataDir + "DigitallySign.pdf";

        PdfFileSignature pdfSign = new PdfFileSignature();

        pdfSign.bindPdf(inFile);
        // criar um retângulo para a localização da assinatura
        java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);

        // criar qualquer um dos três tipos de assinatura
        PKCS7 pkcs = new PKCS7(_dataDir + "test01.pfx", "Aspose2021");
        pkcs.setReason("Pruebas Firma");
        pkcs.setContactInfo("Contacto Pruebas");
        pkcs.setLocation("Población (Provincia)");
        pkcs.setDate(new Date());
        SignatureCustomAppearance signatureCustomAppearance = new SignatureCustomAppearance();
        signatureCustomAppearance.setDateSignedAtLabel("Fecha");
        signatureCustomAppearance.setDigitalSignedLabel("Digitalmente firmado por");
        signatureCustomAppearance.setReasonLabel("Razón");
        signatureCustomAppearance.setLocationLabel("Localización");
        signatureCustomAppearance.setFontFamilyName("Arial");
        signatureCustomAppearance.setFontSize(10);
        signatureCustomAppearance.setCulture(new Locale("es", "ES"));
        // signatureCustomAppearance.setCulture (Locale.ROOT);
        signatureCustomAppearance.setDateTimeFormat("yyyy.MM.dd HH:mm:ss");
        pkcs.setCustomAppearance(signatureCustomAppearance);
        // assinar o arquivo PDF
        pdfSign.sign(1, true, rect, pkcs);
        // salvar o arquivo PDF de saída
        pdfSign.save(outFile);
    }
```