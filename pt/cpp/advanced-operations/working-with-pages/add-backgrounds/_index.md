---
title: Adicionar fundo ao PDF com C++
linktitle: Adicionar fundos
type: docs
weight: 110
url: pt/cpp/add-backgrounds/
descriptions: Adicione imagem de fundo ao seu arquivo PDF com C++. Use o objeto BackgroundArtifact.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Adicionar um fundo aos arquivos PDF ajuda a melhorar a legibilidade geral do documento. O conteúdo no PDF se torna mais envolvente e os leitores vão perceber se você tem uma boa aparência do documento. O fundo também pode ser usado para destacar os destaques do PDF.

Imagens de fundo podem ser usadas para adicionar uma marca d'água, ou outro design sutil, aos documentos. No Aspose.PDF para C++, cada documento PDF é uma coleção de páginas e cada página contém uma coleção de artefatos. A classe [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) pode ser usada para adicionar uma imagem de fundo a um objeto de página.

O seguinte trecho de código mostra como adicionar uma imagem de fundo às páginas de um PDF usando o objeto BackgroundArtifact com C++.

```cpp
void WorkingWithPages::AddBackgrounds()
{
    String _dataDir("C:\\Samples\\");

    // Cria um novo objeto Document
    auto document = MakeObject<Document>();

    // Adiciona uma nova página ao objeto documento
    auto page = document->get_Pages()->Add();

    // Cria objeto Artifact de Fundo
    auto background = MakeObject<BackgroundArtifact>();

    // Especifica a imagem para o objeto backgroundartifact
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // Adiciona backgroundartifact à coleção de artefatos da página
    page->get_Artifacts()->Add(background);

    // Salva o documento
    document->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```