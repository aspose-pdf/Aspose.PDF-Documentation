---
title: Extrair Links do Arquivo PDF 
linktitle: Extrair Links
type: docs
weight: 30
url: /cpp/extract-links/
description: Extrair links de PDF com C#. Este tópico explica como extrair links usando a classe AnnotationSelector.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Links do Arquivo PDF

Os links são representados como anotações em um arquivo PDF, então para extrair links, extraia todos os objetos [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).

1. Crie um objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Obtenha a [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) da qual você deseja extrair links.
1. Use a classe [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) para extrair todos os objetos [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) da página especificada.

1. Passe o objeto [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) para o método Accept do objeto Page.
2. Obtenha todas as anotações de link selecionadas em um objeto IList usando a propriedade Selected do objeto [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/).

O trecho de código a seguir mostra como extrair links de um arquivo PDF.

```cpp
void ExtractLinksFromThePDFFile() {
   
    // Carregar o arquivo PDF
    String _dataDir("C:\\Samples\\");

    // Criar instância do Documento
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Adicionar página à coleção de páginas do arquivo PDF
    auto page = document->get_Pages()->idx_get(1);

    auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(selector);
    auto list = selector->get_Selected();
    for (auto annot : list)
    {
        Console::WriteLine(u"Anotação localizada: {0}", annot->get_Rect());
    }
}
```