---
title: Atualizar Links em PDF 
linktitle: Atualizar Links
type: docs
weight: 20
url: /cpp/update-links/
description: Atualize links em PDF programaticamente com Aspose.PDF para C++. Este guia é sobre como atualizar links em um arquivo PDF. 
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Atualizar Links em um Arquivo PDF

Conforme discutido em Adicionar Hiperlink em um Arquivo PDF, a classe [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) possibilita adicionar links em um arquivo PDF. Existe também uma classe similar usada para obter links existentes de dentro de arquivos PDF. Use esta se você precisar atualizar um link existente. Para atualizar um link existente:

1. Carregue um arquivo PDF.
1. Vá para uma página específica no arquivo PDF.
1. Especifique o destino do link usando a propriedade Destination do objeto [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action).
1. A página de destino é especificada usando o construtor [XYZExplicitDestination](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.x_y_z_explicit_destination).

### Definir o Alvo do Link para uma Página no Mesmo Documento

O trecho de código a seguir mostra como atualizar um link em um arquivo PDF e definir seu alvo para a segunda página do documento.

```cpp
void SetLinkTargetToAPageInTheSameDocument()
{
    String _dataDir("C:\\Samples\\");
    // Criar instância do Documento
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Modificação do link: alterar destino do link
    auto goToAction = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(link->get_Action());

    // Especificar o destino para o objeto link
    // Representa destino explícito que exibe a página com as coordenadas (esquerda, topo) posicionadas no canto superior esquerdo da 
    // janela e os conteúdos da página ampliados pelo fator de zoom.
    // O 1º parâmetro é o número da página de destino.
    // O 2º é a coordenada esquerda
    // O 3º é a coordenada superior
    // O 4º argumento é o fator de zoom ao exibir a respectiva página. Usar 2 significa que a página será exibida com zoom de 200%
    goToAction->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 1, 2, 2));

    // Salvar o documento com o link atualizado
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```
### Definir Destino do Link para um Endereço da Web

Para atualizar o hyperlink para que ele aponte para um endereço da web, instancie o objeto [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) e passe-o para a propriedade Action do LinkAnnotation. O trecho de código a seguir mostra como atualizar um link em um arquivo PDF e definir seu destino para um endereço da web.

```cpp
void SetLinkDestinationToWebAddress() 
{
    // Carregar o arquivo PDF
    String _dataDir("C:\\Samples\\");
    // Criar instância do Documento
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Modificar link: alterar ação do link e definir destino como endereço da web
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

    // Salvar o documento com o link atualizado
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### Definir o Alvo do Link para Outro Arquivo PDF

O trecho de código a seguir mostra como atualizar um link em um arquivo PDF e definir seu alvo para outro arquivo PDF.

```cpp
void SetLinkTargetToAnotherPDFFile()
{
    // Carregar o arquivo PDF
    String _dataDir("C:\\Samples\\");
    // Criar instância do Documento
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->idx_get(1);
    auto linkAnnot = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Modificação do link: alterar ação do link e definir alvo como endereço web
    auto goToR = System::DynamicCast<Aspose::Pdf::Annotations::GoToRemoteAction>(linkAnnot->get_Action());
    // Próxima linha atualiza o destino, não atualiza o arquivo
    goToR->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(2, 0, 0, 1.5));
    // Próxima linha atualiza o arquivo
    goToR->set_File(MakeObject<FileSpecification>(_dataDir + u"input.pdf"));

    // Salvar o documento com o link atualizado
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### Atualizar Cor do Texto da Anotação de Link

A anotação de link não contém texto. Em vez disso, o texto é colocado no conteúdo da página sob a anotação. Portanto, para mudar a cor do texto, substitua a cor do texto da página em vez de tentar mudar a cor da anotação. O seguinte trecho de código mostra como atualizar a cor da anotação de link em um arquivo PDF.

```cpp
void UpdateLinkAnnotationTextColor() 
{
    // Carregar o arquivo PDF
    String _dataDir("C:\\Samples\\");

    // Criar instância do Documento
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->idx_get(1);

    for (auto annotation : page->get_Annotations())
    {
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Link)
        {
            // Pesquisar o texto sob a anotação
            auto ta = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>();
            auto rect = annotation->get_Rect();
            rect->set_LLX(rect->get_LLX() - 10);
            rect->set_LLY(rect->get_LLY() - 10);
            rect->set_URX(rect->get_URX() + 10);
            rect->set_URY(rect->get_URY() + 10);

            ta->set_TextSearchOptions(MakeObject<Aspose::Pdf::Text::TextSearchOptions>(rect));
            ta->Visit(page);
            // Mudar cor do texto.
            for (auto tf : ta->get_TextFragments())
            {
                tf->get_TextState()->set_ForegroundColor(Color::get_Red());
            }
        }

    }
    // Salvar o documento com o link atualizado
    document->Save(_dataDir + u"UpdateLinkTextColor_out.pdf");
}
```