---
title: Otimizar, Comprimir ou Reduzir Tamanho de PDF em Python
linktitle: Otimizar PDF
type: docs
weight: 30
url: pt/python-cpp/optimize-pdf/
keywords: "otimizar pdf Python"
description: Otimizar arquivo PDF, reduzir todas as imagens, diminuir tamanho do PDF, Desincorporar fontes, Remover objetos não utilizados com Python.
lastmod: "2023-12-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Um documento PDF pode, às vezes, conter dados adicionais. Reduzir o tamanho de um arquivo PDF ajudará a otimizar a transferência de rede e o armazenamento. Isso é especialmente útil para publicação em páginas da web, compartilhamento em redes sociais, envio por e-mail ou arquivamento em armazenamento. Podemos usar várias técnicas para otimizar PDF:

- Otimizar o conteúdo da página para navegação online
- Reduzir ou comprimir todas as imagens
- Permitir reutilização de conteúdo de página
- Mesclar fluxos duplicados
- Desincorporar fontes
- Remover objetos não utilizados
- Remover campos de formulário achatados
- Remover ou achatar anotações

{{% alert color="primary" %}}

Explicação detalhada dos métodos de otimização pode ser encontrada na página de Visão Geral dos Métodos de Otimização.

{{% /alert %}}

## Otimizar Documento PDF para a Web

Otimização, ou linearização para a Web, refere-se ao processo de tornar um arquivo PDF adequado para navegação online usando um navegador web. Para otimizar um arquivo para exibição na web:

O trecho de código a seguir mostra como otimizar um documento PDF para a web.

```python

    import AsposePDFPythonWrappers as ap

    # O caminho para o diretório de documentos.
    dataDir = "..."

    # Abrir documento
    document = ap.Document(dataDir + "OptimizeDocument.pdf")

    # Otimizar para a web
    document.optimize()

    dataDir = dataDir + "OptimizeDocument_out.pdf"

    # Salvar documento de saída
    document.Save(dataDir)
```