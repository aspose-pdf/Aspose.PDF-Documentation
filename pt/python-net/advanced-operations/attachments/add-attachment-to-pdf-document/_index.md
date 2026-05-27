---
title: Adicionar anexos ao PDF em Python
linktitle: Adicionando anexo a um documento PDF
type: docs
weight: 10
url: /pt/python-net/add-attachment-to-pdf-document/
description: Aprenda como adicionar anexos de arquivos a documentos PDF em Python usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar anexos ao PDF com Python
Abstract: Este artigo fornece um guia passo a passo sobre como adicionar anexos a um arquivo PDF usando Python e a biblioteca Aspose.PDF. Ele detalha o processo de configuração de um novo projeto Python, importação do pacote Aspose.PDF necessário e criação de um objeto `Document`. O artigo explica como criar um objeto `FileSpecification` com o arquivo e a descrição desejados, e como adicionar esse objeto à `EmbeddedFileCollection` do documento PDF usando o método `add`. A `EmbeddedFileCollection` contém todos os anexos dentro do PDF. Um trecho de código está incluído para demonstrar o processo de abertura de um documento, configuração de um arquivo para anexar, adicioná‑lo à coleção de anexos do documento e salvar o PDF atualizado.
---

Os anexos podem conter uma grande variedade de informações e podem ser de diversos tipos de arquivo. Este artigo explica como adicionar um anexo a um arquivo PDF.

Use anexos PDF incorporados quando precisar empacotar arquivos-fonte de suporte, planilhas, imagens ou documentos relacionados junto com o PDF principal.

1. Crie um novo projeto Python.
1. Importe o pacote Aspose.PDF
1. Crie um [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) object.
1. Crie um [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) objeto com o arquivo que você está adicionando e a descrição do arquivo.
1. Adicionar o [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) objeto ao [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) do objeto [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) coleção, com a coleção’s [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) método.

O [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) A coleção contém todos os anexos no arquivo PDF. O trecho de código a seguir mostra como adicionar um anexo em um documento PDF.

```python
from os import path
import aspose.pdf as ap

def add_attachments(infile, attachment_path, outfile):
    with ap.Document(infile) as document:
        file_spec = ap.FileSpecification(attachment_path, "Sample text file")
        document.embedded_files.add(path.basename(attachment_path), file_spec)
        document.save(outfile)
```

## Tópicos Relacionados a Anexos

- [Trabalhar com anexos PDF em Python](/pdf/pt/python-net/attachments/)
- [Remover anexos de PDF em Python](/pdf/pt/python-net/removing-attachment-from-an-existing-pdf/)
- [Criar e gerenciar portfólios PDF em Python](/pdf/pt/python-net/portfolio/)

