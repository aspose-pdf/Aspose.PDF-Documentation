---
title: Salvar documento PDF programaticamente
linktitle: Salvar PDF
type: docs
weight: 30
url: /pt/python-net/save-pdf-document/
description: Aprenda como salvar arquivos PDF em Python usando a biblioteca Aspose.PDF for Python via .NET. Salve documentos PDF no sistema de arquivos, em streams e em aplicações Web.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Salvando documentos PDF usando a biblioteca Aspose.PDF em Python
Abstract: O artigo fornece orientações sobre como salvar documentos PDF usando a biblioteca Aspose.PDF em Python. Ele descreve três métodos principais para salvar PDFs – no sistema de arquivos, em um stream e em formatos específicos como PDF/A ou PDF/X. O método `save()` da classe `Document` é central para essas operações. Para salvar um PDF no sistema de arquivos, um documento pode ser criado ou manipulado, como adicionar uma nova página, e então salvo diretamente em um caminho. Para salvar em um stream, as sobrecargas do método `Save` permitem escrever um documento em um objeto stream. Além disso, o artigo explica como salvar documentos nos formatos PDF/A ou PDF/X, que são padrões para arquivamento de longo prazo e intercâmbio de gráficos, respectivamente. Esse processo requer preparar o documento com o método `convert` antes de salvá‑lo. Os trechos de código Python fornecidos demonstram cada abordagem, ilustrando a aplicação prática desses métodos.
---

## Salvar documento PDF no sistema de arquivos

Você pode salvar o documento PDF criado ou manipulado no sistema de arquivos usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(output_pdf)
```

## Salvar documento PDF em stream

Você também pode salvar o documento PDF criado ou manipulado em um stream usando as sobrecargas dos métodos `Save`.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # make some manipation, i.g add new empty page
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```

## Salvar formato PDF/A ou PDF/X

PDF/A é uma versão padronizada pela ISO do Portable Document Format (PDF) para uso em arquivamento e preservação de longo prazo de documentos eletrônicos.
PDF/A difere do PDF por proibir recursos não adequados para arquivamento de longo prazo, como link de fontes (em vez de incorporação de fontes) e criptografia. Os requisitos ISO para visualizadores de PDF/A incluem diretrizes de gerenciamento de cores, suporte a fontes incorporadas e uma interface de usuário para leitura de anotações incorporadas.

PDF/X é um subconjunto do padrão ISO PDF. O objetivo do PDF/X é facilitar o intercâmbio de gráficos, e por isso possui uma série de requisitos relacionados à impressão que não se aplicam a arquivos PDF padrão.

Em ambos os casos, o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) é usado para armazenar os documentos, enquanto os documentos devem ser preparados usando o método [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```

