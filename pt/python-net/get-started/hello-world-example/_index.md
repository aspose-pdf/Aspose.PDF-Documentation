---
title: Exemplo de Hello World usando Python
linktitle: Exemplo Hello World
type: docs
weight: 20
url: /pt/python-net/hello-world-example/
description: Esta amostra demonstra como criar um documento PDF simples com o texto Hello World usando Aspose.PDF for Python via .NET.
lastmod: "2026-05-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Exemplo Hello World via Python
Abstract: Este artigo fornece um exemplo Hello World usando a biblioteca Aspose.PDF for Python via .NET para criar um documento PDF. O exemplo demonstra as etapas básicas de uso da API Aspose.PDF gerando um PDF com o texto "Hello World!". O processo envolve instanciar um objeto `Document`, adicionar um `Page`, criar um objeto `TextFragment`, definir propriedades de texto como tamanho da fonte e cor, e usar um `TextBuilder` para adicionar o texto à página. O PDF resultante é então salvo como "HelloWorld_out.pdf". O artigo inclui um trecho completo de código Python ilustrando essas etapas, servindo como um guia introdutório para o uso da biblioteca.
---

Um exemplo "Hello World" mostra a sintaxe mais simples e o programa mais simples em qualquer linguagem de programação. Os desenvolvedores são introduzidos à sintaxe básica da linguagem de programação ao aprender como imprimir "Hello World" na tela do dispositivo. Portanto, tradicionalmente iniciaremos nosso contato com a biblioteca a partir dele.

Neste artigo, estamos criando um documento PDF contendo o texto "Hello World!". Após instalar **Aspose.PDF for Python via .NET** em seu ambiente, você pode executar o exemplo de código abaixo para ver como a API Aspose.PDF funciona.

O trecho de código abaixo segue estas etapas:

1. Instanciar um [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) objeto
1. Adicionar um [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) para objeto Document
1. Criar um [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) objeto
1. Definir cores do texto
1. Criar um Text Builder
1. Adicionar [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) para a Página
1. [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) documento PDF resultante

O trecho de código a seguir é um programa "Hello World" que demonstra a funcionalidade do Aspose.PDF for Python via the .NET API.

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
    textFragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    textFragment.text_state.background_color = ap.Color.blue
    textFragment.text_state.foreground_color = ap.Color.yellow

    # Create TextBuilder object
    textBuilder = ap.text.TextBuilder(page)

    # Append the text fragment to the PDF page
    textBuilder.append_text(textFragment)

    document.save(self.data_dir + "HelloWorld_out.pdf")
```
