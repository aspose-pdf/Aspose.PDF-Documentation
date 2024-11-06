---
title: Adding Attachment to PDF document 
linktitle: Adding Attachment to PDF document 
type: docs
weight: 10
url: pt/java/add-attachment-to-pdf-document/
description: Esta página descreve como adicionar um anexo a um arquivo PDF com Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Os anexos podem conter uma grande variedade de informações e podem ser de vários tipos de arquivos. Este artigo explica como adicionar um anexo a um arquivo PDF.

1. Crie um objeto [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) que contém o arquivo que você deseja anexar e a descrição do arquivo.

1. Adicione o objeto [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) à coleção [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) de um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) usando o método [add(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification). A coleção [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) contém todos os anexos adicionados a um arquivo PDF.

O trecho de código a seguir mostra como adicionar um anexo em um documento PDF.

```java
public class ExampleAttachments {
    
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Attachments/";

    public static void AddingAttachment() {
        // Abra um documento
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Configure um novo arquivo para ser adicionado como anexo
  FileSpecification fileSpecification = new FileSpecification("sample.txt", "Arquivo de texto de exemplo");
  // Adicione um anexo à coleção de anexos do documento
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // Salve o documento atualizado
  pdfDocument.save("output.pdf");
    }
}
```