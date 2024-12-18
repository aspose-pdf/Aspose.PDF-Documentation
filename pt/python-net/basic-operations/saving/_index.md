---
title: Salvar documento PDF programaticamente
linktitle: Salvar PDF
type: docs
weight: 30
url: /pt/python-net/save-pdf-document/
description: Aprenda como salvar arquivo PDF em Python Aspose.PDF para biblioteca Python via .NET. Salvar documento PDF no sistema de arquivos, no fluxo e em aplicações Web.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Salvar documento PDF no sistema de arquivos

Você pode salvar o documento PDF criado ou manipulado no sistema de arquivos usando o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # fazer alguma manipulação, por exemplo, adicionar uma nova página vazia
    document.pages.add()
    document.save(output_pdf)
```

## Salvar documento PDF em fluxo

Você também pode salvar o documento PDF criado ou manipulado em fluxo usando sobrecargas dos métodos `Save`.

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    # fazer alguma manipulação, por exemplo, adicionar uma nova página vazia
    document.pages.add()
    document.save(io.FileIO(output_pdf, 'w'))
```


## Salvar formato PDF/A ou PDF/X

PDF/A é uma versão do Portable Document Format (PDF) padronizada pela ISO para uso em arquivamento e preservação a longo prazo de documentos eletrônicos. O PDF/A difere do PDF porque proíbe recursos que não são adequados para arquivamento a longo prazo, como vinculação de fontes (em oposição à incorporação de fontes) e criptografia. Os requisitos da ISO para visualizadores de PDF/A incluem diretrizes de gerenciamento de cores, suporte a fontes incorporadas e uma interface de usuário para leitura de anotações incorporadas.

PDF/X é um subconjunto do padrão ISO PDF. O propósito do PDF/X é facilitar a troca de gráficos e, portanto, possui uma série de requisitos relacionados à impressão que não se aplicam a arquivos PDF padrão.

Em ambos os casos, o método [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) é usado para armazenar os documentos, enquanto os documentos devem ser preparados usando o método [convert](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    document = ap.Document(input_pdf)
    document.pages.add()
    document.convert(output_log, ap.PdfFormat.PDF_X_3, ap.ConvertErrorAction.DELETE)
    document.save(output_pdf)
```