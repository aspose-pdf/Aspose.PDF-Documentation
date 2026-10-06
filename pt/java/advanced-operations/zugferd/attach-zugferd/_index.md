---
title: Criar PDF/3-A compatível e anexar fatura ZUGFeRD em Java
linktitle: Anexar ZUGFeRD ao PDF
type: docs
weight: 10
url: /pt/java/attach-zugferd/
description: Saiba como anexar o XML da fatura ZUGFeRD a um PDF e convertê-lo para PDF/A-3A em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Anexar o XML da fatura ZUGFeRD a um documento PDF com Java
Abstract: Este artigo explica como criar um documento de fatura compatível com PDF/A-3A usando Aspose.PDF for Java. Ele aborda a anexação do XML da fatura como um arquivo incorporado, a definição do tipo MIME e da relação de arquivo associado, a conversão do PDF para PDF/A-3A e a gravação do documento final pronto para ZUGFeRD.
---
Use as APIs `Document` e `FileSpecification` quando precisar empacotar XML de fatura dentro de um PDF para fluxos de trabalho em estilo ZUGFeRD.

## Anexar XML da fatura ZUGFeRD a um PDF

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie o [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) para o arquivo XML da fatura.
1. Defina os metadados do arquivo incorporado, incluindo o tipo MIME e [AFRelationship](https://reference.aspose.com/pdf/java/com.aspose.pdf/afrelationship/).
1. Adicione o [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) à coleção de arquivos incorporados do documento.
1. Converta o documento para [PdfFormat](https://reference.aspose.com/pdf/java/com.aspose.pdf/pdfformat/) `PDF_A_3A`.
1. Salve o PDF atualizado [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
