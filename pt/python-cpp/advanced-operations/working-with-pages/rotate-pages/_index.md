---
title: Rotate PDF Pages Using Python via C++
linktitle: Rotate PDF Pages
type: docs
weight: 20
url: /pt/python-cpp/rotate-pages/
description: Este tópico descreve como rotacionar a orientação da página em um arquivo PDF existente programaticamente com Python via C++.
lastmod: "2024-04-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Às vezes, as páginas de PDF podem ter orientação incorreta devido a problemas de digitalização ou criação. Rotacionar as páginas garante que elas sejam exibidas na orientação correta para facilitar a leitura e visualização.
Rotacionar páginas de PDF ajuda a manter uma experiência de visualização consistente em diferentes dispositivos e plataformas.

Rotacionar páginas de PDF pode facilitar tarefas de edição, como adicionar anotações, comentários ou assinaturas. Ao rotacionar as páginas para a orientação desejada, você pode tornar os processos de edição e revisão mais eficientes.

Além disso, ao imprimir documentos PDF, é importante garantir que as páginas estejam orientadas corretamente para evitar problemas de desalinhamento ou corte.
 Rotacionar páginas conforme necessário antes de imprimir ajuda a otimizar a saída de impressão e garante que o conteúdo seja exibido conforme o pretendido.  
Rotacionar páginas PDF é um recurso útil que ajuda a melhorar a legibilidade, consistência e apresentação de documentos em vários contextos e propósitos.

Este tópico descreve como atualizar ou alterar a orientação da página de páginas em um arquivo PDF existente programaticamente com Python.

## Alterar Orientação da Página

Aspose.PDF para Python via C++ suporta ótimos recursos como alterar a orientação da página.

1. Crie um objeto de documento a partir do arquivo de entrada
1. Obtenha a coleção de páginas do documento usando 'apCore.document_get_pages'
1. Obtenha a primeira página da coleção de páginas com 'apCore.page_collection_get_page'
1. Rotacione a página em 90 graus no sentido horário usando 'apCore.page_set_rotate'
1. Salve o documento modificado no arquivo de saída com o método 'document.save'

```python

    import AsposePDFPython as apCore
    import os
    import os.path

    # Criando um caminho para o diretório contendo os arquivos de exemplo
    dataDir = os.path.join(os.getcwd(), "samples")

    # Criando caminhos para os arquivos de entrada e saída
    input_file = os.path.join(dataDir, "sample0.pdf")
    output_file = os.path.join(dataDir, "results", "rotated_document.pdf")

    # Criando um objeto de documento carregando o arquivo de entrada
    doc = apCore.document_create_from_file(inputFile)

    # Obtendo a coleção de páginas no documento
    pages = apCore.document_get_pages(doc)

    # Obtendo a primeira página da coleção
    page = apCore.page_collection_get_page(pages, 1)

    # Rotacionando a página em 90 graus no sentido horário
    apCore.page_set_rotate(page, apCore.Rotation(apCore.on90))

    # Salvando o documento modificado no arquivo de saída
    apCore.document_save(doc, output_file)

    # Fechando o handle do documento para liberar recursos
    apCore.close_handle(doc)
```