---
title: Excluir Imagens de Arquivo PDF usando Python
linktitle: Excluir Imagens
type: docs
weight: 20
url: /pt/python-net/delete-images-from-pdf-file/
description: Esta seção explica como excluir imagens de arquivos PDF usando Aspose.PDF para Python via .NET.
lastmod: "2025-09-27"
TechArticle: true
AlternativeHeadline: Como remover imagens de PDF usando Python
Abstract: O artigo discute as várias razões para remover imagens de arquivos PDF, como proteger a privacidade, impedir o acesso não autorizado a informações sensíveis, reduzir o tamanho do arquivo para facilitar o compartilhamento e armazenamento, e preparar o documento para compressão ou extração de texto. Ele apresenta **Aspose.PDF for Python via .NET** como uma ferramenta para realizar essa tarefa. O artigo fornece instruções passo a passo e trechos de código para excluir imagens específicas ou todas as imagens de um arquivo PDF usando Aspose.PDF. O processo envolve abrir um documento PDF existente, excluir imagens individualmente ou em massa e salvar o arquivo atualizado. O código Python fornecido demonstra como remover imagens acessando os recursos do documento e modificando as páginas desejadas.
---

Existem muitas razões para remover todas ou imagens específicas de PDFs.
Às vezes, um arquivo PDF pode conter imagens importantes que precisam ser removidas para proteger a privacidade ou impedir o acesso não autorizado a determinadas informações.

Remover imagens indesejadas ou redundantes pode ajudar a reduzir o tamanho do arquivo, facilitando o compartilhamento ou armazenamento de PDFs.
Se necessário, você pode reduzir o número de páginas removendo todas as imagens do documento.
Além disso, excluir imagens do documento ajudará a preparar o PDF para compressão ou extração de informações de texto.

**Aspose.PDF for Python via .NET** ajudará você com esta tarefa.

## Excluir Imagens de Arquivo PDF

Para excluir uma imagem de um arquivo PDF:

1. Abra o documento PDF existente.
1. Exclua uma imagem específica.
1. Salve o arquivo PDF atualizado.

O trecho de código a seguir mostra como excluir uma imagem de um arquivo PDF.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, outfile)

    document = ap.Document(path_infile)
    document.pages[1].resources.images.delete(1)
    document.save(path_outfile)
```
