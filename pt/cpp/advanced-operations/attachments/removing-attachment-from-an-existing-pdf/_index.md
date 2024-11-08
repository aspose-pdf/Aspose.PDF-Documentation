---
title: Removendo anexo de PDF 
linktitle: Removendo anexo de um PDF existente
type: docs
weight: 30
url: /pt/cpp/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF para C++ pode remover anexos de seus documentos PDF. Use a API PDF C++ para remover anexos em arquivos PDF usando a biblioteca Aspose.PDF.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF pode remover anexos de arquivos PDF. Os anexos de um documento PDF são mantidos na coleção EmbeddedFiles do objeto Document.

Para excluir todos os anexos associados a um arquivo PDF:

1. Chame o método [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection#afff8b235b554a66c203464b61204b843) da coleção [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection).
1. Salve o arquivo atualizado usando o método Save do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

O seguinte trecho de código mostra como remover anexos de um documento PDF.

```cpp
void WorkingWithAttachments::RemovingAttachment() {

 String _dataDir("C:\\Samples\\");

 // Abrir documento
 auto pdfDocument = new Document(_dataDir + u"DeleteAllAttachments.pdf");

 // Excluir todos os anexos
 pdfDocument->get_EmbeddedFiles()->Delete();

 // Salvar arquivo atualizado
 pdfDocument->Save(_dataDir + u"DeleteAllAttachments_out.pdf");
}
```