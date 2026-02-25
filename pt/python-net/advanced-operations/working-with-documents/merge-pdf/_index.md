---
title: Como Mesclar PDF usando Python
linktitle: Mesclar arquivos PDF
type: docs
weight: 50
url: /pt/python-net/merge-pdf-documents/
description: Esta página explica como mesclar documentos PDF em um único arquivo PDF com Python.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Combine páginas de PDF usando Python
Abstract: Este artigo aborda a necessidade comum de mesclar vários arquivos PDF em um único documento, um processo valioso para organizar e otimizar o armazenamento e o compartilhamento de conteúdo PDF. Ele explora o uso do Aspose.PDF para Python via .NET para combinar eficientemente arquivos PDF, reconhecendo que mesclar PDFs em Python pode ser desafiador sem bibliotecas de terceiros. O artigo fornece um guia passo a passo para concatenar arquivos PDF – criando um novo documento, mesclando os arquivos e salvando o documento mesclado. Um trecho de código demonstra a implementação usando Aspose.PDF, destacando a capacidade da biblioteca de simplificar o processo de mesclagem. Além disso, apresenta o Aspose.PDF Merger, uma ferramenta online para mesclar PDFs, permitindo que os usuários explorem a funcionalidade em um ambiente baseado na web.
---

## Mesclar ou combinar vários PDF em um único PDF em Python

Combinar arquivos PDF é uma consulta muito popular entre os usuários. Isso pode ser útil quando você tem vários arquivos PDF que deseja compartilhar ou armazenar juntos como um único documento.

Mesclar arquivos PDF pode ajudá-lo a organizar seus documentos, liberar espaço de armazenamento no seu PC e compartilhar vários arquivos PDF com outras pessoas ao combiná-los em um único documento.

Mesclar PDF em Python via .NET não é uma tarefa simples sem usar uma biblioteca de terceiros.
Este artigo mostra como mesclar vários arquivos PDF em um único documento PDF usando Aspose.PDF para Python via .NET.

## Mesclar arquivos PDF usando Python e DOM

Para concatenar dois arquivos PDF:

1. Crie um novo documento.
1. Mescle os arquivos PDF
1. Salve o documento mesclado

Combinando vários documentos PDF em um único arquivo:

```python

    import aspose.pdf as apdf
    import aspose.pydrawing as asdrw
    from io import FileIO
    from os import path

    path_infile1 = path.join(self.dataDir, infile1)
    path_infile2 = path.join(self.dataDir, infile2)
    path_outfile = path.join(self.dataDir, outfile)

    document = apdf.Document()
    document.merge(files=[path_infile1, path_infile2])
    document.save(path_outfile)
```

## Exemplo ao vivo

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) é um aplicativo web gratuito que permite investigar como funciona a funcionalidade de mesclagem de apresentações.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)


