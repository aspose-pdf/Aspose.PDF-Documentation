---
title: Trabalhando com Artefatos em C++
linktitle: Trabalhando com Artefatos
type: docs
weight: 110
url: /cpp/artifacts/
description: Esta página descreve como trabalhar com a classe Artifact usando Aspose.PDF para C++. Trechos de código mostram como adicionar uma imagem de fundo às páginas do PDF e como obter cada marca d'água na primeira página de um arquivo PDF.
lastmod: "2021-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Como obter Marca d'Água em PDF?

**O que é um artefato em PDF?**

De acordo com a referência PDF / UA ISO, o conteúdo que não é importante ou não aparece no fundo não carrega informações relevantes, deve ser marcado como um artefato para que tecnologias assistivas possam ignorá-lo.
Se os artefatos não puderem ser identificados no programa para criar, isso deve ser feito manualmente usando Aspose.PDF para C++.

A classe [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) contém as seguintes propriedades:

- **Artifact.Type** – obtém o tipo de artefato (suporta valores da enumeração Artifact.ArtifactType onde os valores incluem Background, Layout, Page, Pagination e Undefined).
- **Artifact.Subtype** – obtém o subtipo do artefato (suporta os valores da enumeração Artifact.ArtifactSubtype, onde os valores incluem Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Por favor, note que marcas d'água criadas com Adobe Acrobat têm o tipo Pagination e subtipo Watermark.

{{% /alert %}}

- **Artifact.Contents** – Obtém uma coleção de operadores internos do artefato. Seu tipo suportado é System.Collections.ICollection.
- **Artifact.Form** – Obtém o XForm de um artefato (se XForm for usado). Marcas d'água, artefatos de cabeçalho e rodapé contêm XForm que mostra todo o conteúdo do artefato.
- **Artifact.Image** – Obtém a imagem de um artefato (se uma imagem estiver presente, caso contrário, nulo).
- **Artifact.Text** – Obtém o texto de um artefato.
- **Artifact.Rectangle** – Obtém a posição de um artefato na página.
- **Artifact.Rotation** – Obtém a rotação de um artefato (em graus, valor positivo indica rotação no sentido anti-horário).
- **Artifact.Opacity** – Obtém a opacidade de um artefato. Valores possíveis estão na faixa de 0...1, onde 1 é completamente opaco.

Para um exemplo de trabalho com artefatos em um arquivo PDF, vamos pegar uma marca d'água.

Uma marca d'água criada com suporte para o Adobe Acrobat é referida como um artefato (conforme descrito em 14.8.2.2 Present Content and PDF Specification Artifacts). Para trabalhar com artefatos, Aspose.PDF contém 2 classes:
[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) e [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

Para obter todos os artefatos em uma página específica, a classe [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) possui a propriedade Artifacts. Este tópico mostra como trabalhar com o artefato de Marca d'água em arquivos PDF.

O trecho de código a seguir mostra como obter cada marca d'água na primeira página de um arquivo PDF com C++:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
void Artifacts::SetWatermark() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto artifact = MakeObject<WatermarkArtifact>();
    String text(u"WATERMARK");    
    artifact->set_Text(text);
    artifact->get_TextState()->set_ForegroundColor(Color::get_Blue());
    artifact->get_TextState()->set_FontSize(72);
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment(VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(_dataDir + u"watermark.pdf");
}
```
Imagens de fundo podem ser usadas para adicionar marcas d'água ou designs exclusivos a documentos PDF. O Aspose.PDF para C++ usa a classe [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) para adicionar uma imagem de fundo ao objeto da página.

O próximo trecho de código mostra como adicionar uma imagem de fundo às páginas do PDF com o objeto BackgroundArtifact:

```cpp
void Artifacts::SetBackground() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto pdfDocument = MakeObject<Document>();

    // Adicionar um MakeObject<page ao objeto do documento
    auto page = pdfDocument->get_Pages()->Add();

    // Criar objeto Background Artifact
    auto background = MakeObject<BackgroundArtifact>();

    // Especificar a imagem para o objeto backgroundartifact
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // Adicionar BackgroundArtifact à coleção de artefatos da página
    page->get_Artifacts()->Add(background);

    // Salvar PDF modificado
    pdfDocument->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```

### Exemplos de Programação: Obtendo Marcas d'Água

O trecho de código a seguir mostra como obter cada marca d'água na primeira página de um arquivo PDF.

```cpp
void Artifacts::GettingWatermarks() {
    
    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    // Iterar e obter subtipo, texto e localização do artefato
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        Console::WriteLine(u"{0} {1} {2}", artifact->get_Subtype(), 
            artifact->get_Text(), artifact->get_Rectangle());
    }

}
```

### Exemplos de Programação: Contando Artefatos de um Tipo Particular

Para calcular o total de artefatos de um tipo específico (por exemplo, o número total de marcas d'água), use o seguinte código:

```cpp
void Artifacts::CountingArtifacts() {

    String _dataDir("C:\\Samples\\");

    // Abrir documento
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    int count = 0;
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        // Se o tipo do artefato é marca d'água, aumentar o contador
        if (artifact->get_Subtype() == Artifact::ArtifactSubtype::Watermark) count++;
    }
    Console::WriteLine(u"A página contém {0} marcas d'água", count);
}
```