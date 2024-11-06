---
title: Adicionar marca d'água ao PDF usando C++
linktitle: Adicionar marca d'água
type: docs
weight: 90
url: pt/cpp/add-watermarks/
description: Este artigo explica os recursos de trabalhar com artefatos e obter marcas d'água em PDFs programaticamente usando o C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Uma marca d'água é uma imagem translúcida que geralmente contém um logotipo ou selo para identificar quem criou o documento ou imagem.

**Aspose.PDF for C++** permite adicionar marcas d'água ao seu documento PDF usando a classe Artifact. Por favor, verifique este artigo para resolver sua tarefa.

Uma marca d'água criada com o Adobe Acrobat é chamada de artefato (conforme descrito em 14.8.2.2 Conteúdo Real e Artefatos da especificação PDF). Para trabalhar com artefatos, o Aspose.PDF possui duas classes: [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) e [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

Para obter todos os artefatos em uma página específica, a classe [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) possui a propriedade Artifacts. Este tópico explica como trabalhar com artefatos em arquivos PDF.

## Trabalhando com Artefatos

A classe [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) contém as seguintes propriedades:

**Artifact.Type** – obtém o tipo de artefato (suporta valores da enumeração Artifact.ArtifactType onde os valores incluem Background, Layout, Page, Pagination e Undefined).
**Artifact.Subtype** – obtém o subtipo de artefato (suporta os valores da enumeração Artifact.ArtifactSubtype onde os valores incluem Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Por favor, note que marcas d'água criadas com Adobe Acrobat têm o tipo Pagination e subtipo Watermark.

{{% /alert %}}

**Artifact.Contents** – Obtém uma coleção de operadores internos de artefato. Seu tipo suportado é System.Collections.ICollection.
**Artifact.Form** – Obtém o XForm de um artefato (se XForm é usado). Artefatos de marcas d'água, cabeçalho e rodapé contêm XForm que mostra todos os conteúdos do artefato.

**Artifact.Image** – Obtém a imagem de um artefato (se uma imagem estiver presente, caso contrário, nulo).**Artifact.Text** – Obtém o texto de um artefato.  
**Artifact.Rectangle** – Obtém a posição de um artefato na página.  
**Artifact.Rotation** – Obtém a rotação de um artefato (em graus, valor positivo indica rotação no sentido anti-horário).  
**Artifact.Opacity** – Obtém a opacidade de um artefato. Os valores possíveis estão na faixa de 0…1, onde 1 é completamente opaco.

## Exemplos de Programação: Como Adicionar Marca D'Água em Arquivos PDF

O trecho de código a seguir mostra como obter cada marca d'água na primeira página de um arquivo PDF com C++.

```cpp
void GettingWatermarks() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("watermark.pdf");
    String outputFileName("watermark_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto artifact = MakeObject<WatermarkArtifact>();
    auto textState = MakeObject<TextState>();
    textState->set_FontSize(72);
    textState->set_ForegroundColor(Color::get_Blue());
    textState->set_Font(FontRepository::FindFont(u"Courier"));
    artifact->SetTextAndState(u"WATERMARK", textState);
    artifact->set_ArtifactHorizontalAlignment (HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment (VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);

    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);

    document->Save(_dataDir + outputFileName);
}
```