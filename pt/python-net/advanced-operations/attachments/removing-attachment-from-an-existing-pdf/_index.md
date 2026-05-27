---
title: Remover Anexos de PDF em Python
linktitle: Removendo anexo de um PDF existente
type: docs
weight: 30
url: /pt/python-net/removing-attachment-from-an-existing-pdf/
description: Aspose.PDF pode remover anexos dos seus documentos PDF. Use a API PDF para Python para remover anexos em arquivos PDF usando a biblioteca Aspose.PDF for Python via .NET.
lastmod: "2026-05-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como excluir anexos de PDF com Python
Abstract: Este artigo discute como remover anexos de arquivos PDF usando Aspose.PDF for Python. Os anexos em um documento PDF são armazenados dentro da coleção `EmbeddedFiles` do objeto `Document`. Para excluir todos os anexos de um PDF, você pode invocar o método `delete()` na coleção `EmbeddedFiles` e, em seguida, salvar o documento atualizado usando o método `save()` do objeto `Document`. Um trecho de código é fornecido para demonstrar esse processo, mostrando as etapas de abertura de um documento, exclusão de seus anexos e salvamento do arquivo modificado.
---

Aspose.PDF for Python pode remover anexos de arquivos PDF. Os anexos de um documento PDF são mantidos no objeto `Document` [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) coleção.

Esse fluxo de trabalho é útil quando você precisa limpar arquivos incorporados desatualizados, reduzir o tamanho do pacote ou preparar um PDF para redistribuição sem materiais de origem anexados.

Para excluir todos os anexos associados a um arquivo PDF:

1. Chame o [EmbeddedFiles](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) da coleção [delete()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) método.
1. Salve o arquivo atualizado usando o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) do objeto [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método.

O trecho de código a seguir mostra como remover anexos de um documento PDF.

```python

import aspose.pdf as ap

def remove_attachment(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete()
        document.save(outfile)
```

## Remova um anexo específico pelo nome

Se precisar remover apenas um anexo e manter os demais, use o [delete_by_key()](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/delete_by_key/) método e passe o nome do anexo.

Para excluir um anexo específico:

1. Abra o arquivo PDF de origem.
1. Chamar `document.embedded_files.delete_by_key(attachment_name)`.
1. Salve o arquivo PDF atualizado.

O trecho de código a seguir remove um anexo pelo seu nome.

```python

import aspose.pdf as ap

def remove_attachment(infile, attachment_name, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        document.embedded_files.delete_by_key(attachment_name)
        document.save(outfile)
```

## Tópicos Relacionados a Anexos

- [Trabalhar com anexos PDF em Python](/pdf/pt/python-net/attachments/)
- [Adicionar anexos a PDF em Python](/pdf/pt/python-net/add-attachment-to-pdf-document/)
- [Criar e gerenciar portfólios PDF em Python](/pdf/pt/python-net/portfolio/)

