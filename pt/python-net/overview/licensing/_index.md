---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 50
url: /pt/python-net/licensing/
description: Aspose. PDF para Python convida seus clientes a obter uma licença Clássica. Assim como usar uma licença limitada para explorar melhor o produto.
lastmod: "2022-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Limitação de uma versão de avaliação

Queremos que nossos clientes testem nossos componentes minuciosamente antes de comprar, então a versão de avaliação permite que você a use normalmente.

- **PDF criado com uma marca d'água de avaliação.** A versão de avaliação do Aspose.PDF para Python fornece funcionalidade completa do produto, mas todas as páginas dos documentos PDF gerados são marcadas com a marca d'água "Somente Avaliação. Criado com Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" no topo.

>Se você deseja testar o Aspose.PDF sem as limitações da versão de avaliação, você também pode solicitar uma Licença Temporária de 30 dias.
 Por favor, consulte [Como obter uma Licença Temporária?](https://purchase.aspose.com/temporary-license)

## Licença clássica

A licença pode ser carregada a partir de um arquivo ou objeto de fluxo. A maneira mais fácil de definir uma licença é colocar o arquivo de licença na mesma pasta que o arquivo Aspose.PDF.dll e especificar o nome do arquivo sem um caminho, como mostrado no exemplo abaixo.

Se você usar qualquer outro componente Aspose para Python junto com o Aspose.PDF para Python, especifique o namespace para License como [classe Aspose.Pdf.License]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```