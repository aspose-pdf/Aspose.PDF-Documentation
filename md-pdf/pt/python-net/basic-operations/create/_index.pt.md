---
title: Criar documento PDF programaticamente
linktitle: Criar PDF
type: docs
weight: 10
url: /python-net/create-document/
description: Esta página descreve como criar um documento PDF do zero com Aspose.PDF para Python via .NET library.
---

Para desenvolvedores, há muitos cenários onde se torna necessário gerar arquivos PDF programaticamente. Você pode precisar gerar relatórios PDF e outros arquivos PDF programaticamente em seu software. É bastante longo e ineficiente escrever seu próprio código e funções do zero. Para criar um arquivo PDF com Python, há uma solução melhor - **Aspose.PDF para Python via .NET**.

## Como Criar Arquivo PDF usando Python

Para criar um arquivo PDF usando Python, os seguintes passos podem ser usados.

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)

1. Adicione um objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à coleção [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) do objeto Document
1. Adicione [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) à coleção [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) da página
1. Salve o documento PDF resultante

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