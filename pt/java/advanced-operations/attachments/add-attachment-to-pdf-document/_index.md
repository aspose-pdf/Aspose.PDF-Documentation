---
title: Adicionar anexos a PDF em Java
linktitle: Adicionando anexo a um documento PDF
type: docs
weight: 10
url: /java/add-attachment-to-pdf-document/
description: Aprenda como adicionar anexos de arquivos a documentos PDF em Java usando Aspose.PDF.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicione arquivos incorporados a documentos PDF com Java
Abstract: Este artigo mostra como anexar um arquivo externo a um documento PDF usando Aspose.PDF para Java. O exemplo abre um PDF existente, cria um FileSpecification para o anexo, adiciona-o à coleção EmbeddedFiles do documento e salva o arquivo atualizado.
---
Para anexar um arquivo a um PDF, carregue o documento de origem, crie um `FileSpecification`, adicione-o à coleção de arquivos incorporada e salve o resultado.

## Adicionar um anexo a um documento PDF

Use este exemplo quando um arquivo externo precisar ser incorporado em um PDF existente.

1. Abra o PDF de origem [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie uma [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) para o arquivo que deseja incorporar.
1. Adicione a especificação do arquivo à coleção `EmbeddedFiles` e salve o documento atualizado.

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```
