---
title: Assine documentos PDF de um cartão inteligente em Java
linktitle: Assinatura de PDF com cartão inteligente
type: docs
weight: 30
url: /java/sign-pdf-document-from-smart-card/
description: Revise a cobertura atual do exemplo Java para assinatura de PDF baseada em certificado em Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cobertura de assinatura de PDF baseada em certificado no conjunto de exemplos Java atual
Abstract: Esta página descreve o escopo atual dos exemplos de assinatura disponíveis na árvore de origem da documentação Java. O repositório inclui exemplos de assinatura de PDF baseados em certificados com credenciais PFX ou PKCS7, mas atualmente não inclui um exemplo de armazenamento de certificados de cartão inteligente dedicado para Java.
---
O repositório Java atual não inclui um exemplo de assinatura de cartão inteligente baseado em origem dedicado em `facades/pdffilesignature`, mas o fluxo de trabalho a seguir mostra o padrão de API típico para assinar um PDF com um certificado selecionado em um armazenamento de certificados local.

## Assine um documento PDF a partir de um cartão inteligente

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie uma fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) e vincule o documento PDF de origem.
1. Recupere o certificado local e crie a [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) necessária.
1. Configure a aparência da assinatura visual e o alvo [Retângulo](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Aplique a assinatura ao documento PDF através de [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Salve o documento PDF atualizado.
1. Vincule o documento carregado à fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) com `bindPdf(...)`.
1. Recupere o certificado local que representa a credencial do cartão inteligente chamando `getLocalCertificate()`.
1. Verifique se um certificado foi encontrado. Caso contrário, salve o arquivo de saída inalterado e interrompa o fluxo de trabalho.
1. Crie uma [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) a partir do certificado selecionado.
1. Defina a imagem de aparência da assinatura visual com `setSignatureAppearance(...)`.
1. Chame `sign(...)` com a página de destino, motivo, contato, localização, sinalizador de visibilidade, assinatura [Retângulo](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/) e objeto de assinatura externa.
1. Salve o PDF assinado no caminho de saída.

```java
public static void signWithSmartCard(Path inputFile, Path outputFile, Path pngFile) {
    try (Document document = new Document(inputFile.toString());
            PdfFileSignature pdfSignature = new PdfFileSignature()) {
        pdfSignature.bindPdf(document);
        X509Certificate2 selectedCertificate = getLocalCertificate();
        if (selectedCertificate == null) {
            System.out.println("Local certificate was not found.");
            document.save(outputFile.toString());
            return;
        }

        ExternalSignature externalSignature = new ExternalSignature(selectedCertificate, null);
        pdfSignature.setSignatureAppearance(pngFile.toString());
        pdfSignature.sign(1, "Reason", "Contact", "Location", true,
                new java.awt.Rectangle(100, 100, 200, 200), externalSignature);
        pdfSignature.save(outputFile.toString());
    }
}
```
