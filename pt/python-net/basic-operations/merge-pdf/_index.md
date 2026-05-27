---
title: Mesclar arquivos PDF em Python
linktitle: Mesclar arquivos PDF
type: docs
weight: 50
url: /pt/python-net/merge-pdf/
description: Aprenda como mesclar vários arquivos PDF em um único documento em Python.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combinar páginas PDF usando Python
Abstract: Este artigo aborda a necessidade comum de mesclar vários arquivos PDF em um único documento, um processo valioso para organizar e otimizar o armazenamento e o compartilhamento de conteúdo PDF. Ele explora o uso do Aspose.PDF for Python via .NET para combinar arquivos PDF de forma eficiente, reconhecendo que mesclar PDFs em Python pode ser desafiador sem bibliotecas de terceiros. O artigo fornece um guia passo a passo para concatenar arquivos PDF – criando um novo Document, mesclando os arquivos e salvando o Document mesclado. Um trecho de código demonstra a implementação usando Aspose.PDF, destacando a capacidade da biblioteca de simplificar o processo de mesclagem. Além disso, ele apresenta o Aspose.PDF Merger, uma ferramenta online para mesclar PDFs, permitindo que os usuários explorem a funcionalidade em um ambiente baseado na web.
---

## Mesclar arquivos PDF usando Python e DOM

Para concatenar dois arquivos PDF:

1. Crie um Novo Documento.
1. Mescle os Arquivos PDF
1. Salve o Documento Mesclado

Combinando vários documentos PDF em um único arquivo:

```python
import sys
import aspose.pdf as ap
from os import path

def merge_two_documents(infile1, infile2, outfile):
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)
    document1.pages.add(document2.pages)
    document1.save(outfile)
```

## Exemplo ao Vivo

[Aspose.PDF Mesclador](https://products.aspose.app/pdf/merger) é uma aplicação web gratuita online que permite investigar como a funcionalidade de mesclagem de apresentações funciona.

[![Aspose.PDF Mesclador](merger.png)](https://products.aspose.app/pdf/merger)

