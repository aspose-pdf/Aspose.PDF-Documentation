---
title: Como assinar digitalmente PDF
linktitle: Assinar PDF Digitalmente
type: docs
weight: 10
url: /java/assinar-arquivo-pdf-digitalmente/
description: Assine documentos PDF digitalmente usando Java. Verifique ou valide PDFs assinados digitalmente com uma aplicação baseada em Java com a Biblioteca PDF. Você pode certificar um arquivo PDF com um Certificado PKCS1.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Ao assinar um documento PDF usando uma assinatura, você basicamente confirma que seu conteúdo deve permanecer "como está". Consequentemente, quaisquer alterações feitas posteriormente invalidam a assinatura e, assim, você sabe se o documento foi alterado. Certificar um documento primeiro permite que você especifique as alterações que um usuário pode fazer no documento sem invalidar a certificação.

Em outras palavras, o documento ainda seria considerado como mantendo sua integridade e o destinatário ainda poderia confiar no documento. Para mais detalhes, por favor visite Certificando e assinando um PDF.

Para cumprir o requisito mencionado acima, as seguintes alterações na API pública foram feitas.

isCertified(…) método é adicionado à classe PdfFileSignature.

## Assinar PDF com assinaturas digitais

```java
public class ExampleDigitallySign {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Secure-Sign/";

    public static void SignDocument() {
        String inFile = _dataDir + "DigitallySign.pdf";
        String outFile = _dataDir + "DigitallySign_out.pdf";
        Document document = new Document(inFile);

        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Pa$$w0rd2020"); // Use objetos PKCS7/PKCS7Detached
        signature.sign(1, true, new java.awt.Rectangle(300, 100, 400, 200), pkcs);
        // Salvar arquivo PDF de saída
        signature.save(outFile);
    }
```

## Adicionar carimbo de data/hora à assinatura digital

Aspose.PDF para Java suporta assinar digitalmente o PDF com um servidor de carimbo de data/hora ou serviço Web.

Para cumprir este requisito, a classe [TimestampSettings](https://reference.aspose.com/pdf/java/com.aspose.pdf/TimestampSettings) foi adicionada ao namespace Aspose.PDF. Por favor, veja o seguinte trecho de código que obtém o timestamp e o adiciona ao documento PDF:

```java
    public static void SignWithTimeStampServer() {
        Document document = new Document(_dataDir + "SimpleResume.pdf");
        PdfFileSignature signature = new PdfFileSignature(document);

        PKCS7 pkcs = new PKCS7("/home/aspose/pdf-examples/Samples/test.pfx", "Start2020");
        TimestampSettings timestampSettings = new TimestampSettings("https://freetsa.org/tsr", ""); // Usuário/Senha podem
                                                                                                    // ser omitidos
        pkcs.setTimestampSettings(timestampSettings);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 200, 100);
        // Crie qualquer um dos três tipos de assinatura
        signature.sign(1, "Motivo da Assinatura", "Contato", "Localização", true, rect, pkcs);
        // Salvar arquivo PDF de saída
        signature.save(_dataDir + "DigitallySignWithTimeStamp_out.pdf");
    }
```