---
title: Trabalhando com Portfólio em PDF
linktitle: Portfólio
type: docs
weight: 40
url: /cpp/portfolio/
description: Crie um Portfólio em PDF com Aspose.PDF para C++. Você deve usar um arquivo do Microsoft Excel, um documento do Word e um arquivo de imagem para criar um Portfólio em PDF.
lastmod: "2022-02-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Como Criar um Portfólio em PDF

O Aspose.PDF permite criar documentos de Portfólio em PDF usando a classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Adicione um arquivo em um objeto Document.Collection após obtê-lo com a classe [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification). Quando os arquivos tiverem sido adicionados, use o método Save da classe Document para salvar o documento do portfólio.

O exemplo a seguir usa um arquivo do Microsoft Excel, um documento do Word e um arquivo de imagem para criar um Portfólio em PDF.

O código abaixo resulta no seguinte portfólio.

### Um Portfólio em PDF criado com Aspose.PDF

![Um Portfólio em PDF criado com Aspose.PDF para C++](working-with-pdf-portfolio_1.jpg)

```cpp
void WorkingWithAttachments::CreatePortfolio()
{
    String _dataDir("C:\\Samples\\");

    // Instanciar objeto Document
    auto pdfDocument = MakeObject<Document>();

    // Instanciar objeto de coleção de documentos
    pdfDocument->set_Collection(MakeObject<Collection>());

    // Obter arquivos para adicionar ao portfólio
    auto excel = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.xlsx");
    auto word = MakeObject<FileSpecification>(_dataDir + u"HelloWorld.docx");
    auto image = MakeObject<FileSpecification>(_dataDir + u"sample.jpg");

    // Fornecer descrição dos arquivos
    excel->set_Description(u"Arquivo Excel");
    word->set_Description(u"Arquivo Word");
    image->set_Description(u"Arquivo de Imagem");

    // Adicionar arquivos à coleção de documentos
    pdfDocument->get_Collection()->Add(excel);
    pdfDocument->get_Collection()->Add(word);
    pdfDocument->get_Collection()->Add(image);

    // Salvar documento do portfólio
    pdfDocument->Save(_dataDir + u"PDFPortfolio.pdf");
}
```

## Extrair arquivos do portfólio PDF

PDF Portfolios permitem que você reúna conteúdo de uma variedade de fontes (por exemplo, arquivos PDF, Word, Excel, JPEG) em um único contêiner unificado. Os arquivos originais mantêm suas identidades individuais, mas são montados em um arquivo de Portfólio PDF. Os usuários podem abrir, ler, editar e formatar cada arquivo componente de forma independente dos outros arquivos componentes.

Aspose.PDF permite a criação de documentos de Portfólio PDF usando a classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Ele também oferece a capacidade de extrair arquivos de um portfólio PDF.

O snippet de código a seguir mostra as etapas para extrair arquivos de um portfólio PDF.

```cpp
void WorkingWithAttachments::ExtractPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // Abra um documento
    auto pdfDocument = MakeObject <Document>(_dataDir + u"PDFPortfolio.pdf");
    // Obter coleção de arquivos incorporados
    auto embeddedFiles = pdfDocument->get_EmbeddedFiles();

    // Iterar através de arquivos individuais do Portfólio
    for (auto fileSpecification : embeddedFiles) {
    auto initialStream = fileSpecification->get_Contents();
    auto fileContent = MakeArray<uint8_t>(fileSpecification->get_Contents()->get_Length());
    fileSpecification->get_Contents()->Read(fileContent, 0, fileContent->get_Length());
    auto filename = System::IO::Path::GetFileName(fileSpecification->get_Name());
    // Salvar o arquivo extraído em algum local
    auto fileStream = System::IO::File::OpenWrite(_dataDir + u"_out_" + filename);
    fileStream->Write(fileContent, 0, fileContent->get_Length());
    // Fechar o objeto stream
    fileStream->Close();
    }
}
```

![Extrair arquivos de um Portfólio PDF](working-with-pdf-portfolio_2.jpg)

## Remover Arquivos do Portfólio PDF

Para excluir/remover arquivos de um portfólio PDF, tente usar as seguintes linhas de código.

```cpp
void WorkingWithAttachments::RemoveFilesFromPDFPortfolio()
{
    String _dataDir("C:\\Samples\\");
    // Carregar Portfólio PDF de origem
    auto pdfDocument = MakeObject<Document>(_dataDir + u"PDFPortfolio.pdf");
    pdfDocument->get_Collection()->Delete();
    pdfDocument->Save(_dataDir + u"No_PortFolio_out.pdf");
}
```