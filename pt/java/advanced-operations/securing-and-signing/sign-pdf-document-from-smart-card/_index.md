---
title: Assinar documentos PDF a partir de um Smart Card em Java
linktitle: Assinatura de PDF com Smart Card
type: docs
weight: 30
url: /pt/java/sign-pdf-document-from-smart-card/
description: Revisar a cobertura atual de exemplos Java para assinatura de PDF baseada em certificado no Aspose.PDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cobertura de assinatura de PDF baseada em certificado no conjunto atual de exemplos Java
Abstract: Esta página descreve o escopo atual dos exemplos de assinatura disponíveis na árvore de código-fonte da documentação Java. O repositório inclui exemplos de assinatura de PDF baseada em certificado com credenciais PFX ou PKCS7, mas atualmente não inclui um exemplo dedicado de armazenamento de certificados em smart‑card para Java.
---
O repositório atual de Java não inclui um exemplo dedicado de assinatura com cartão inteligente baseado em fonte sob `facades/pdffilesignature`, mas o fluxo de trabalho a seguir mostra o padrão típico de API para assinar um PDF com um certificado selecionado de um armazenamento de certificados local.

## Assinar um documento PDF a partir de um cartão inteligente

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) fachada e vincule o documento PDF de origem.
1. Recupere o certificado local e crie o necessário [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/).
1. Configure a aparência da assinatura visual e o destino [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/).
1. Aplique a assinatura ao documento PDF através de [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/).
1. Salve o documento PDF atualizado.
1. Vincule o documento carregado à fachada [PdfFileSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesignature/) com `bindPdf(...)`.
1. Recupere o certificado local que representa a credencial do cartão inteligente chamando `getLocalCertificate()`.
1. Verifique se um certificado foi encontrado. Caso contrário, salve o arquivo de saída inalterado e interrompa o fluxo de trabalho.
1. Crie um [ExternalSignature](https://reference.aspose.com/pdf/java/com.aspose.pdf/externalsignature/) a partir do certificado selecionado.
1. Defina a imagem de aparência da assinatura visual com `setSignatureAppearance(...)`.
1. Chame `sign(...)` com a página de destino, motivo, contato, localização, sinalizador de visibilidade, assinatura [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/rectangle/), e objeto de assinatura externa.
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
