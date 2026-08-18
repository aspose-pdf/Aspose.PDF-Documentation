---
title: Criando PDF compatível com PDF/3-A e anexando fatura ZUGFeRD em Java
linktitle: Anexar ZUGFeRD ao PDF
type: docs
weight: 10
url: /java/attach-zugferd/
description: Aprenda como anexar o XML da fatura ZUGFeRD a um PDF e convertê-lo para PDF/A-3A em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Anexe o XML da fatura ZUGFeRD a um documento PDF com Java
Abstract: Este artigo explica como criar um documento de fatura compatível com PDF/A-3A usando Aspose.PDF para Java. Abrange anexar o XML da fatura como um arquivo incorporado, definir o tipo MIME e o relacionamento do arquivo associado, converter o PDF em PDF/A-3A e salvar o documento final pronto para ZUGFeRD.
---
Use as APIs `Document` e `FileSpecification` quando precisar empacotar o XML da fatura dentro de um PDF para fluxos de trabalho no estilo ZUGFeRD.

## Anexe o XML da fatura ZUGFeRD a um PDF

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie o [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) para o arquivo XML da fatura.
1. Defina os metadados do arquivo incorporado, incluindo o tipo MIME e [AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/).
1. Adicione [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) à coleção de arquivos incorporados ao documento.
1. Converta o documento para [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A`.
1. Salve o [documento] PDF atualizado (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void attachInvoiceZugferdFormat(Path inputFile, Path invoiceFile, Path outputFile) {
        try (Document document = new Document(inputFile.toString())) {
            String description = "Invoice metadata conforming to ZUGFeRD standard";
            FileSpecification fileSpecification = new FileSpecification(invoiceFile.toString(), description);

            fileSpecification.setMIMEType("text/xml");
            fileSpecification.setAFRelationship(AFRelationship.Alternative);

            document.getEmbeddedFiles().add("factur", fileSpecification);

            String outputFileName = outputFile.toString();
            String logPath = outputFileName.replace(".pdf", "_log.xml");
            document.convert(logPath, PdfFormat.PDF_A_3A, ConvertErrorAction.Delete);
            document.save(outputFile.toString());
        }
        System.out.println("ZUGFeRD invoice attached to " + outputFile);
    }
```
