---
title: Criar documento PDF programaticamente
linktitle: Criar PDF
type: docs
weight: 10
url: /pt/python-net/create-document/
description: Esta página descreve como criar um documento PDF do zero com a biblioteca Aspose.PDF for Python via .NET.
TechArticle: true
AlternativeHeadline: Gerando arquivos PDF com Aspose.PDF for Python
Abstract: Em desenvolvimento de software, gerar arquivos PDF programaticamente é uma necessidade comum, particularmente para a criação de relatórios e outros documentos. Escrever código personalizado para essa tarefa pode ser ineficiente e demorado. Em vez disso, os desenvolvedores podem utilizar **Aspose.PDF for Python via .NET**, uma solução robusta para criar arquivos PDF usando Python. O processo envolve criar um objeto `Document`, adicionar um objeto `Page` à coleção `Pages` do documento, inserir um `TextFragment` na coleção `paragraphs` da página e, em seguida, salvar o documento. Um fragmento de código Python de exemplo demonstra essas etapas, mostrando a facilidade com que arquivos PDF podem ser gerados usando o Aspose.PDF.
---

Para desenvolvedores, existem muitos cenários em que se torna necessário gerar arquivos PDF programaticamente. Você pode precisar gerar relatórios PDF e outros arquivos PDF em seu software. É bastante longo e ineficiente escrever seu próprio código e funções do zero. Para criar um arquivo PDF com Python, há uma solução melhor - **Aspose.PDF for Python via .NET**.

## Como criar um arquivo PDF usando Python

Para criar um arquivo PDF usando Python, os seguintes passos podem ser usados.

1. Crie um objeto da classe [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/)
1. Adicione um objeto [Page](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) à coleção [Pages](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) do objeto Document
1. Adicione [TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) à coleção [paragraphs](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/#properties) da página
1. Salve o documento PDF resultante

```python

    import aspose.pdf as ap

    # Initialize document object
    document = ap.Document()
    # Add page
    page = document.pages.add()
    # Initialize textfragment object
    text_fragment = ap.text.TextFragment("Hello,world!")
    # Add text fragment to new page
    page.paragraphs.add(text_fragment)
    # Save updated PDF
    document.save("output.pdf")
```



