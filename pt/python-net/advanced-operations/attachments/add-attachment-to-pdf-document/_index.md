---
title: Adicionar Anexo a um documento PDF usando Python
linktitle: Adicionar Anexo a um documento PDF
type: docs
weight: 10
url: /pt/python-net/add-attachment-to-pdf-document/
description: Esta página descreve como adicionar um anexo a um arquivo PDF com a biblioteca Aspose.PDF para Python via .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar Anexos a um PDF com Python
Abstract: Este artigo fornece um guia passo a passo sobre como adicionar anexos a um arquivo PDF usando Python e a biblioteca Aspose.PDF. Ele detalha o processo de configuração de um novo projeto Python, importação do pacote Aspose.PDF necessário e criação de um objeto `Document`. O artigo explica como criar um objeto `FileSpecification` com o arquivo desejado e sua descrição, e como adicionar este objeto à `EmbeddedFileCollection` do documento PDF usando o método `add`. A `EmbeddedFileCollection` contém todos os anexos dentro do PDF. Um trecho de código está incluído para demonstrar o processo de abertura de um documento, configuração de um arquivo para anexar, acrescentá‑lo à coleção de anexos do documento e salvar o PDF atualizado.
---

Os anexos podem conter uma grande variedade de informações e podem ser de diversos tipos de arquivo. Este artigo explica como adicionar um anexo a um arquivo PDF.

1. Crie um novo projeto Python.
1. Importe o pacote Aspose.PDF
1. Crie um [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto.
1. Crie um [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) objeto com o arquivo que está adicionando e a descrição do arquivo.
1. Adicione o objeto [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) ao objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) da [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) coleção, usando o método [add](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/#methods) da coleção.

A coleção [EmbeddedFileCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/embeddedfilecollection/) contém todos os anexos no arquivo PDF. O trecho de código a seguir mostra como adicionar um anexo em um documento PDF.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Setup new file to be added as attachment
    fileSpecification = ap.FileSpecification(attachment_file, "Sample text file")

    # Add attachment to document's attachment collection
    document.embedded_files.append(fileSpecification)

    # Save new output
    document.save(output_pdf)
```


