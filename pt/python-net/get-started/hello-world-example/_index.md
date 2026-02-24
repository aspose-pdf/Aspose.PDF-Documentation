---
title: Exemplo de Hello World usando Python
linktitle: Exemplo de Hello World
type: docs
weight: 20
url: /pt/python-net/hello-world-example/
description: Este exemplo demonstra como criar um documento PDF simples com o texto Hello World usando Aspose.PDF para Python via .NET.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exemplo de Hello World via Python
Abstract: Este artigo fornece um exemplo Hello World usando a biblioteca Aspose.PDF para Python via .NET para criar um documento PDF. O exemplo demonstra as etapas básicas de uso da API Aspose.PDF gerando um PDF com o texto "Hello World!". O processo envolve instanciar um objeto `Document`, adicionar uma `Page`, criar um objeto `TextFragment`, definir propriedades de texto como tamanho da fonte e cor, e usar um `TextBuilder` para adicionar o texto à página. O PDF resultante é então salvo como "HelloWorld_out.pdf". O artigo inclui um trecho completo de código Python ilustrando estas etapas, servindo como um guia introdutório ao uso da biblioteca.
---

Um exemplo "Hello World" mostra a sintaxe mais simples e o programa mais simples em qualquer linguagem de programação. Os desenvolvedores são introduzidos à sintaxe básica da linguagem aprendendo a imprimir "Hello World" na tela do dispositivo. Portanto, tradicionalmente começaremos nosso conhecimento da biblioteca a partir dele.

Neste artigo, estamos criando um documento PDF contendo o texto "Hello World!". Após instalar **Aspose.PDF para Python via .NET** em seu ambiente, você pode executar o exemplo de código abaixo para ver como a API Aspose.PDF funciona.

O trecho de código abaixo segue estas etapas:

1. Instanciar um objeto [Documento](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) 
1. Adicionar uma [Página](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) ao objeto documento
1. Criar um objeto [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)
1. Definir cores do texto
1. Criar um Construtor de Texto
1. Adicionar [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) à Página
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) documento PDF resultante

O trecho de código a seguir é um programa "Hello World" que demonstra a funcionalidade do Aspose.PDF para Python via API .NET.

```python

from datetime import timedelta
import aspose.pdf as ap

def run_simple(self):
    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Add text to new page
    textFragment = ap.text.TextFragment("Hello, world!")
    textFragment.position = ap.text.Position(100, 600)

    textFragment.text_state.font_size = 12
    textFragment.text_state.font = ap.text.FontRepository.find_font(
        "TimesNewRoman"
    )
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
