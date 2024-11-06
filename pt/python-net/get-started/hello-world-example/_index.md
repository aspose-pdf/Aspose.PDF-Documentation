---
title: Exemplo de Hello World usando Python
linktitle: Exemplo de Hello World
type: docs
weight: 20
url: pt/python-net/hello-world-example/
description: Este exemplo demonstra como criar um documento PDF simples com o texto Hello World usando Aspose.PDF para Python via .NET.
lastmod: "2022-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Um exemplo "Hello World" mostra a sintaxe mais simples e o programa mais simples em qualquer linguagem de programação. Os desenvolvedores são introduzidos à sintaxe básica da linguagem de programação aprendendo como imprimir "Hello World" na tela do dispositivo. Portanto, começaremos tradicionalmente nosso conhecimento com nossa biblioteca a partir dele.

Neste artigo, estamos criando um documento PDF contendo o texto "Hello World!". Após instalar **Aspose.PDF for Python via .NET** em seu ambiente, você pode executar o exemplo de código abaixo para ver como a API Aspose.PDF funciona.

O trecho de código abaixo segue estas etapas:

1. Instanciar um objeto [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Adicionar um [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ao objeto de documento
1. Criar um objeto [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)
1. Adicionar TextFragment à coleção de [parágrafos](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) da página
1. [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) o documento PDF resultante

O trecho de código a seguir é um programa "Hello World" para demonstrar o funcionamento do Aspose.PDF para Python via API .NET.

```python

    import aspose.pdf as ap

    # Inicializar objeto de documento
    document = ap.Document()
    # Adicionar página
    page = document.pages.add()
    # Inicializar objeto textfragment
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Adicionar fragmento de texto à nova página
    page.paragraphs.add(text_fragment)
    # Salvar PDF atualizado
    document.save("output.pdf")
```