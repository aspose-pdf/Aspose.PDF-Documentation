---
title: Removendo anexo de PDF usando Python
linktitle: Removendo anexo de um PDF existente
type: docs
weight: 30
url: /pt/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF pode remover anexos dos seus documentos PDF. Use a API PDF para Python para remover anexos em arquivos PDF usando Aspose.PDF para Python via biblioteca .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como excluir anexos de PDF com Python
Abstract: Este artigo discute como remover anexos de arquivos PDF usando Aspose.PDF para Python. Os anexos em um documento PDF são armazenados na coleção `EmbeddedFiles` do objeto `Document`. Para excluir todos os anexos de um PDF, você pode invocar o método `delete()` na coleção `EmbeddedFiles` e então salvar o documento atualizado usando o método `save()` do objeto `Document`. Um trecho de código é fornecido para demonstrar esse processo, exibindo as etapas de abrir um documento, excluir seus anexos e salvar o arquivo modificado.
---

Aspose.PDF para Python pode remover anexos de arquivos PDF. Os anexos de um documento PDF são mantidos na coleção [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) do objeto Document.

Para excluir todos os anexos associados a um arquivo PDF:

1. Chame o método [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) da coleção [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/).
1. Salve o arquivo atualizado usando o método [save()] do objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

O trecho de código a seguir mostra como remover anexos de um documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Delete all attachments
    document.embedded_files.delete()

    # Save updated file
    document.save(output_pdf)
```


