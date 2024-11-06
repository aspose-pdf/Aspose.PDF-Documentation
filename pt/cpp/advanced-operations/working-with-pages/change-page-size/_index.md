---
title: Change PDF Page Size Programmatically 
linktitle: Change PDF Page Size
type: docs
weight: 40
url: pt/cpp/change-page-size/
description: Alterar o tamanho da página do seu arquivo PDF usando a biblioteca C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF é um formato de layout estático e imprimível, por isso se tornou amplamente utilizado na vida empresarial.

No entanto, você pode ter tarefas em que precisa redimensionar seu documento PDF, pois o tamanho da página é maior que o tamanho do papel. Mas como?

Não se preocupe. Nesta página, você encontrará uma maneira de resolver sua tarefa.

Mas primeiro, vamos lembrar que existe a Série de Tamanhos de Página.

Existem duas séries de tamanhos de página amplamente adotadas no mundo. É claro que existem muitos formatos, mas existem aqueles mais comumente usados. O primeiro é o ISO Paper Sizes. Série A4 é usada para Impressão Padrão e Papelaria. O papel tamanho Carta é usado para Pôsteres, Gráficos de Parede, etc. Os Estados Unidos, Canadá e em parte o México adotaram a segunda Série de Tamanho de Página e hoje são as únicas nações industrializadas nas quais os tamanhos de papel padrão ISO ainda não são amplamente utilizados.

Agora vamos ver como o Aspose.PDF solicita que você redimensione a página usando a biblioteca C++.

## Alterar Tamanho da Página PDF

Aspose.PDF para C++ permite que você altere o tamanho da página PDF com linhas simples de código em suas aplicações C++. Este tópico explica como atualizar/alterar as dimensões (tamanho) da página de um arquivo PDF existente.

A classe [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) contém o método SetPageSize(...) que permite definir o tamanho da página. O trecho de código abaixo atualiza as dimensões da página em algumas etapas simples:

1. Carregar o arquivo PDF de origem.
1. Obter as páginas no objeto [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. Obter uma página específica.
1. Chame o método SetPageSize(..) para atualizar suas dimensões. 1. Chame o método Save(..) da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) para gerar o arquivo PDF com as dimensões de página atualizadas.

O trecho de código a seguir mostra como alterar as dimensões da página do PDF para o tamanho A4.

```cpp
void ChangePageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");
    String outputFileName("UpdateDimensions_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Obter página específica
    auto pdfPage = document->get_Pages()->idx_get(1);

    // Definir o tamanho da página como A4 (11.7 x 8.3 pol) e em Aspose.Pdf, 1 polegada = 72 pontos
    // Portanto, as dimensões A4 em pontos serão (842.4, 597.6)
    pdfPage->SetPageSize(597.6, 842.4);
    // Salvar o documento atualizado
    document->Save(_dataDir + outputFileName);
}
```

## Obter Tamanho da Página do PDF

Você pode ler o tamanho da página de um arquivo PDF existente usando Aspose.PDF para C++. O seguinte exemplo de código mostra como ler as dimensões da página PDF usando C++.

```cpp
void GetPDFPageSize() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("UpdateDimensions.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Obter página específica
    auto page = document->get_Pages()->idx_get(1);

    // Obter informações de altura e largura da página
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());
    // Rotacionar página em um ângulo de 90 graus
    page->set_Rotate(Rotation::on90);
    // Obter informações de altura e largura da página
    Console::WriteLine(u"{0} {1}", page->GetPageRect(true)->get_Width(), page->GetPageRect(true)->get_Height());

}
```