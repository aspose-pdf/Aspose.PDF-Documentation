---
title: Salvar Documento PDF usando C++
linktitle: Salvar
type: docs
weight: 30
url: /cpp/save-pdf-document/
description: Aprenda como salvar arquivo PDF com a biblioteca Aspose.PDF para C++.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Salvar documento PDF no sistema de arquivos

Você pode salvar o documento PDF criado ou manipulado no sistema de arquivos usando o método Save da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void SaveDocument()
{
    // String para nome do caminho
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);
    // fazer alguma manipulação, por exemplo, adicionar nova página vazia
    document->get_Pages()->Add();
    document->Save(_dataDir + modifiedFileName);
}
```

## Salvar documento PDF em fluxo

Você também pode salvar o documento PDF criado ou manipulado em fluxo usando sobrecargas dos métodos Save.

```cpp
void SaveDocumentStream()
{
    // String para nome do caminho
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);

    // fazer alguma manipulação, por exemplo, adicionar nova página vazia
    document->get_Pages()->Add();

    auto fileStream = System::IO::File::OpenWrite(_dataDir + modifiedFileName);
    document->Save(fileStream);
}
```

## Salvar no formato PDF/A ou PDF/X

PDF/A é uma versão do Formato de Documento Portátil (PDF) padronizada pela ISO para uso em arquivamento e preservação a longo prazo de documentos eletrônicos. O PDF/A difere do PDF na medida em que proíbe recursos não adequados para arquivamento a longo prazo, como vinculação de fontes (em oposição à incorporação de fontes) e criptografia. Os requisitos ISO para visualizadores de PDF/A incluem diretrizes de gerenciamento de cores, suporte a fontes incorporadas e uma interface de usuário para leitura de anotações incorporadas.

PDF/X é um subconjunto do padrão ISO PDF. O objetivo do PDF/X é facilitar a troca de gráficos e, portanto, possui uma série de requisitos relacionados à impressão que não se aplicam aos arquivos PDF padrão.

Em ambos os casos, o método Save é usado para armazenar os documentos, enquanto os documentos devem ser preparados usando o [PdfFormatConversionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_format_conversion_options).

```cpp
void SaveDocumentAsPDFx()
{
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo
    String infilename("SimpleResume.pdf");
    String outfilename("SimpleResume_A3U.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    auto options = new PdfFormatConversionOptions(Aspose::Pdf::PdfFormat::PDF_A_3U);
    try
    {
        document->Convert(options);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what();
    }

    document->Save(_dataDir + outfilename);
}
```