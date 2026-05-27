---
title: Criar Portfólios PDF em Python
linktitle: Portfólio
type: docs
weight: 20
url: /pt/python-net/portfolio/
description: Saiba como criar e gerenciar portfólios PDF em Python com Aspose.PDF for Python via .NET.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crie e edite portfólios PDF com arquivos incorporados em Python
Abstract: Este artigo explica como criar e gerenciar portfólios PDF usando Aspose.PDF for Python via .NET. Saiba como agrupar múltiplos tipos de arquivo em um único portfólio PDF, adicionar arquivos a uma coleção de documentos e remover itens do portfólio programaticamente com Python.
---

Criar um portfólio PDF permite consolidar e arquivar diferentes tipos de arquivos em um único documento consistente. Esse documento pode incluir arquivos de texto, imagens, planilhas, apresentações e outros materiais, garantindo que todo o material relevante seja armazenado e organizado em um só lugar.

O portfólio PDF ajudará a exibir sua apresentação de forma de alta qualidade, onde quer que você a use. Em geral, criar um portfólio PDF é uma tarefa muito atual e moderna.

Use um portfólio PDF quando quiser distribuir um conjunto de arquivos relacionados juntos, mantendo cada arquivo em seu formato original dentro de um único contêiner PDF.

## Como criar um portfólio PDF

Aspose.PDF for Python via .NET permite criar documentos de PDF Portfolio usando o [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) class. Adicione um arquivo em um document.collection object após obtê‑lo com o [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) classe. Quando os arquivos foram adicionados, use a\u00A0Document\u00A0class\u0027 [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) método para salvar o documento de portfólio.

O exemplo a seguir usa um arquivo Microsoft Excel, um documento Word e um arquivo de imagem para criar um Portfólio PDF.

O código abaixo resulta no seguinte portfólio.

### Um PDF Portfolio criado com Aspose.PDF para Python

![Um PDF Portfolio criado com Aspose.PDF para Python](working-with-pdf-portfolio_1.jpg)

```python
import aspose.pdf as ap

def create_pdf_portfolio(input_files, outfile):
    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_files[0])
    word = ap.FileSpecification(input_files[1])
    image = ap.FileSpecification(input_files[2])

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(outfile)
```

## Remover arquivos do PDF Portfolio

Para excluir/remover arquivos do PDF portfolio, tente usar as linhas de código a seguir.

```python
import aspose.pdf as ap

def remove_files_from_pdf_portfolio(infile, outfile):
    # Open document
    document = ap.Document(infile)
    document.collection.delete()

    # Save updated file
    document.save(outfile)
```

## Tópicos Relacionados ao Anexo

- [Trabalhar com anexos PDF em Python](/pdf/pt/python-net/attachments/)
- [Adicionar anexos ao PDF em Python](/pdf/pt/python-net/add-attachment-to-pdf-document/)
- [Remover anexos do PDF em Python](/pdf/pt/python-net/removing-attachment-from-an-existing-pdf/)

