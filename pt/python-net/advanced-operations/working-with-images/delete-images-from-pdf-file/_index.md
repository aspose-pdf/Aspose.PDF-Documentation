---
title: Excluir Imagens de Arquivo PDF usando Python
linktitle: Excluir Imagens
type: docs
weight: 20
url: /pt/python-net/delete-images-from-pdf-file/
description: Aprenda como excluir imagens específicas ou todas as imagens de arquivos PDF em Python.
lastmod: "2026-05-20"
TechArticle: true
AlternativeHeadline: Excluir imagens de arquivos PDF com Python
Abstract: Este artigo mostra como excluir imagens de documentos PDF com Aspose.PDF for Python via .NET. Ele aborda a remoção de um recurso de imagem específico e a exclusão de todas as imagens de uma página selecionada.
---

Use esta página quando precisar remover gráficos desnecessários, reduzir o tamanho do PDF ou limpar conteúdo visual sensível de um documento.

## Excluir Imagens de Arquivo PDF

Use os seguintes passos para excluir uma imagem de uma página:

1. Carregue o PDF de origem com `ap.Document(infile)`.
1. Selecione a página e o índice do recurso de imagem.
1. Excluir a imagem com `resources.images.delete(index)`.
1. Salve o PDF atualizado.

```python
import aspose.pdf as ap


def delete_image(infile, outfile):
    document = ap.Document(infile)
    document.pages[1].resources.images.delete(1)
    document.save(outfile)
```

## Excluir Todas as Imagens de uma Página

Use este exemplo para remover todas as imagens de uma página específica.

```python
import aspose.pdf as ap


def delete_all_images_from_page(infile, outfile, page_number):
    document = ap.Document(infile)
    page = document.pages[page_number]

    while len(page.resources.images) != 0:
        page.resources.images.delete(1)

    document.save(outfile)
```

## Tópicos Relacionados à Imagem

- [Trabalhar com imagens em PDF usando Python](/pdf/pt/python-net/working-with-images/)
- [Substituir imagens em arquivos PDF existentes](/pdf/pt/python-net/replace-image-in-existing-pdf-file/)
- [Extrair imagens de arquivos PDF](/pdf/pt/python-net/extract-images-from-pdf-file/)
- [Adicionar imagens a arquivos PDF existentes](/pdf/pt/python-net/add-image-to-existing-pdf-file/)