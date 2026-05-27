---
title: Licença Aspose PDF
linktitle: Licenciamento e limitações
type: docs
weight: 50
url: /pt/python-net/licensing/
description: Aspose.PDF for Python convida seus clientes a obter uma licença Classic. Também pode usar uma licença limitada para explorar melhor o produto.
lastmod: "2026-05-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licenciamento do Aspose.PDF for Python
Abstract: O artigo discute as limitações e opções de licenciamento para Aspose.PDF for Python. Destaca que a versão de avaliação permite testar todas as funcionalidades, mas adiciona uma marca d'água aos PDFs gerados, indicando "Evaluation Only" juntamente com informações de direitos autorais. Para usuários que desejam testar sem essas limitações, uma Licença Temporária de 30 dias está disponível. O artigo também explica como implementar uma licença Classic carregando-a a partir de um arquivo ou stream, recomendando colocar o arquivo de licença no mesmo diretório do arquivo Aspose.PDF.dll e definir a licença usando a classe `Aspose.Pdf.License`. Trechos de código são fornecidos para ilustrar o processo de licenciamento.
---

## Limitação de uma versão de avaliação

Queremos que nossos clientes testem nossos componentes de forma completa antes de comprar, então a versão de avaliação permite que você a use como normalmente faria.

- **PDF criado com marca d'água de avaliação.** A versão de avaliação do Aspose.PDF for Python oferece funcionalidade completa do produto, mas todas as páginas nos documentos PDF gerados recebem a marca d'água "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" no topo.

Se você quiser testar o Aspose.PDF sem as limitações da versão de avaliação, também pode solicitar uma Licença Temporária de 30 dias. Por favor, consulte [Como obter uma Licença Temporária?](https://purchase.aspose.com/temporary-license)

## Licença clássica

A licença pode ser carregada a partir de um arquivo ou objeto de fluxo. A maneira mais fácil de definir uma licença é colocar o arquivo de licença na mesma pasta que o arquivo Aspose.PDF.dll e especificar o nome do arquivo sem caminho, como mostrado no exemplo abaixo.

Se você usar qualquer outro componente Aspose para Python juntamente com o Aspose.PDF for Python, por favor, especifique o namespace para License assim [classe Aspose.Pdf.License]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```
