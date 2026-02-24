---
title: Trabalhando com Portfólio em PDF usando Python
linktitle: Portfólio
type: docs
weight: 20
url: /pt/python-net/portfolio/
description: Como criar um Portfólio PDF com Python. Você deve usar um arquivo Microsoft Excel, um documento Word e um arquivo de imagem para criar um Portfólio PDF.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como trabalhar com Portfólio em PDF com Python
Abstract: Este artigo discute a criação e o gerenciamento de portfólios PDF usando Aspose.PDF para Python via .NET. Um portfólio PDF facilita a consolidação de vários tipos de arquivos — como arquivos de texto, imagens, planilhas e apresentações — em um único documento organizado, garantindo que todo o material relevante seja armazenado coletivamente. O artigo descreve o processo de criação de um portfólio PDF, destacando o uso da classe `Document` e da classe `FileSpecification` para adicionar arquivos a uma coleção de documentos. Um exemplo é fornecido, demonstrando a inclusão de um arquivo Microsoft Excel, um documento Word e um arquivo de imagem em um portfólio PDF. Além disso, o artigo inclui trechos de código tanto para criar um portfólio quanto para remover arquivos dele, ilustrando a simplicidade e a eficiência de gerenciar portfólios PDF com Aspose.PDF para Python.
---

A criação de um portfólio PDF permite consolidar e arquivar diferentes tipos de arquivos em um único documento consistente. Esse documento pode incluir arquivos de texto, imagens, planilhas, apresentações e outros materiais, garantindo que todo o material relevante seja armazenado e organizado em um só lugar.

O portfólio PDF ajudará a apresentar sua apresentação de maneira de alta qualidade, onde quer que você a utilize. Em geral, criar um portfólio PDF é uma tarefa muito atual e moderna.

## Como criar um Portfólio PDF

Aspose.PDF for Python via .NET permite criar documentos de Portfólio PDF usando a classe [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) . Adicione um arquivo ao objeto document.collection depois de obtê-lo com a classe [FileSpecification](https://reference.aspose.com/pdf/python-net/aspose.pdf/filespecification/) . Quando os arquivos forem adicionados, use o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) da classe Document para salvar o documento do portfólio.

O exemplo a seguir usa um arquivo Microsoft Excel, um documento Word e um arquivo de imagem para criar um Portfólio PDF.

O código abaixo gera o portfólio a seguir.

### Um Portfólio PDF criado com Aspose.PDF para Python

![Um Portfólio PDF criado com Aspose.PDF para Python](working-with-pdf-portfolio_1.jpg)

```python

    import aspose.pdf as ap

    # Instantiate Document Object
    document = ap.Document()

    # Instantiate document Collection object
    document.collection = ap.Collection()

    # Get Files to add to Portfolio
    excel = ap.FileSpecification(input_excel)
    word = ap.FileSpecification(input_doc)
    image = ap.FileSpecification(input_jpg)

    # Provide description of the files
    excel.description = "Excel File"
    word.description = "Word File"
    image.description = "Image File"

    # Add files to document collection
    document.collection.append(excel)
    document.collection.append(word)
    document.collection.append(image)

    # Save Portfolio document
    document.save(output_pdf)
```

## Remover arquivos do Portfólio PDF

Para excluir/remover arquivos do portfólio PDF, experimente usar as linhas de código a seguir.

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)
    document.collection.delete()

    # Save updated file
    document.save(output_pdf)
```


