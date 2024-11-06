---
title: Removendo anexo de um PDF existente
linktitle: Removendo anexo de um PDF existente
type: docs
weight: 30
url: pt/java/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF pode remover anexos de seus documentos PDF. Use a API de PDF para Java para remover anexos em arquivos PDF com a biblioteca Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF pode remover anexos de arquivos PDF. Os anexos de um documento PDF são mantidos na coleção EmbeddedFiles do objeto Document.

Os anexos de um documento PDF são mantidos na coleção [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection) do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

Para excluir todos os anexos associados a um arquivo PDF:

1. Chame o método delete(..) da coleção [EmbeddedFiles](https://reference.aspose.com/pdf/java/com.aspose.pdf/EmbeddedFileCollection).

1. Salve o arquivo atualizado usando o método save do objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

O trecho de código a seguir mostra como deletar todos os anexos de um documento PDF.

```java
   public static void DeleteAllAttachmentsFromPDF(){
  // Abrir um documento
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // Deletar todos os anexos
  pdfDocument.getEmbeddedFiles().delete();
  // Salvar o arquivo atualizado
  pdfDocument.save("output.pdf");

    }
```