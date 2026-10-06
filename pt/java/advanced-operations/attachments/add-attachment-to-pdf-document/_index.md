---
title: Adicionar anexos ao PDF em Java
linktitle: Adicionar anexo a um documento PDF
type: docs
weight: 10
url: /pt/java/add-attachment-to-pdf-document/
description: Aprenda como adicionar anexos de arquivo a documentos PDF em Java usando Aspose.PDF.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar arquivos incorporados a documentos PDF com Java
Abstract: Este artigo mostra como anexar um arquivo externo a um documento PDF usando Aspose.PDF for Java. O exemplo abre um PDF existente, cria um FileSpecification para o anexo, o adiciona à coleção EmbeddedFiles do documento e salva o arquivo atualizado.
---
Para anexar um arquivo a um PDF, carregue o documento de origem, crie um `FileSpecification`, adicione-o à coleção de arquivos incorporados e salve o resultado.

## Adicionar um anexo a um documento PDF

Use este exemplo quando um arquivo externo deve ser incorporado a um PDF existente.

1. Abra o PDF de origem em um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Crie um [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/) para o arquivo que você deseja incorporar.
1. Adicione a especificação do arquivo ao `EmbeddedFiles` coletar e salve o documento atualizado.

```java
public static void addAttachments(Path inputFile, Path attachmentPath, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FileSpecification fileSpecification = new FileSpecification(attachmentPath.toString(), "Sample text file");
        document.getEmbeddedFiles().add(attachmentPath.getFileName().toString(), fileSpecification);
        document.save(outputFile.toString());
    }
}
```
