---
title: Adicionar Selos de Texto ao PDF em Python
linktitle: Selos de texto em arquivo PDF
type: docs
weight: 20
url: /pt/python-net/text-stamps-in-the-pdf-file/
description: Aprenda como adicionar selos de texto a documentos PDF em Python.
lastmod: "2026-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar selos de Texto em PDF usando Python
Abstract: Este artigo fornece um guia abrangente sobre como adicionar selos de texto a arquivos PDF usando a biblioteca Aspose.PDF para Python. Ele descreve o uso da classe `TextStamp` para criar selos de texto personalizáveis com propriedades como tamanho da fonte, estilo, cor e alinhamento. O artigo inclui trechos de código que demonstram como adicionar um selo de texto simples, configurar o alinhamento do texto e aplicar modos avançados de renderização, como texto preenchido contornado. A primeira seção explica a criação de um objeto `Document` e `TextStamp`, a definição das propriedades de texto e a adição do selo a uma página específica. A segunda seção apresenta a propriedade `text_alignment` para alinhar o texto horizontal e verticalmente, fornecendo um exemplo de código que centraliza o texto em uma página PDF. A seção final discute os modos de renderização, demonstrando como adicionar texto preenchido contornado usando um objeto `TextState` para definir a cor do contorno e o modo de renderização antes de vinculá-lo a um selo. Cada seção é acompanhada de exemplos práticos para facilitar a compreensão e a implementação.
---

## Adicionando selo de Texto com Python

Você pode usar [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) classe para adicionar um carimbo de texto em um arquivo PDF. [TextStamp](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstamp/) A classe fornece propriedades necessárias para criar um carimbo baseado em texto, como tamanho da fonte, estilo da fonte e cor da fonte etc. Para adicionar um carimbo de texto, você precisa criar um objeto Document e um objeto TextStamp usando as propriedades requeridas. Depois disso, você pode chamar [add_stamp()](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#methods) método da Page para adicionar o carimbo no PDF. O trecho de código a seguir mostra como adicionar um carimbo de texto no arquivo PDF. Isso é útil para adicionar anotações, marcas d'água ou rótulos às páginas PDF.

1. Abra o documento PDF.
1. Crie um objeto TextStamp.
1. Defina o comportamento de fundo do stamp.
1. Posicione o stamp na página.
1. Gire o stamp se necessário.
1. Defina as propriedades do texto.
1. Adicione o carimbo a uma página.
1. Salve o documento PDF modificado.

```python
import sys
import aspose.pdf as ap
from os import path

def add_text_stamp(input_file_name, output_file_name):
    document = ap.Document(input_file_name)

    # Create text stamp
    text_stamp = ap.TextStamp("Sample Stamp")
    # Set whether stamp is background
    text_stamp.background = True
    # Set origin
    text_stamp.x_indent = 100
    text_stamp.y_indent = 100
    # Rotate stamp
    text_stamp.rotate = ap.Rotation.ON90
    # Set text properties
    text_stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_stamp.text_state.font_size = 14.0
    text_stamp.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_stamp.text_state.foreground_color = ap.Color.dark_green
    # Add stamp to particular page
    document.pages[1].add_stamp(text_stamp)

    document.save(output_file_name)
```

## Tópicos Relacionados ao Carimbo

- [Carimbar páginas PDF em Python](/pdf/pt/python-net/stamping/)
- [Adicionar carimbos de página ao PDF em Python](/pdf/pt/python-net/page-stamps-in-the-pdf-file/)
- [Adicionar carimbos de imagem ao PDF em Python](/pdf/pt/python-net/image-stamps-in-pdf-page/)
- [Adicionar números de página ao PDF em Python](/pdf/pt/python-net/add-page-number/)