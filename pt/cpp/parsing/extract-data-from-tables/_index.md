---
title: Extrair Dados de Tabela em PDF 
linktitle: Extrair Dados de Tabela
type: docs
weight: 40
url: pt/cpp/extract-data-from-table-in-pdf/
description: Aprenda a extrair tabelas de PDF usando Aspose.PDF para C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair Tabelas de PDF programaticamente

Como o PDF é o formato mais comum para troca de documentos, vamos considerar um documento com vários conjuntos de dados que precisam de análise. Neste artigo, descreveremos a extração de tabelas de PDF.

**Aspose.PDF para C++** fornece aos desenvolvedores as ferramentas necessárias para extrair dados de tabelas em documentos PDF.

Este exemplo demonstra o uso da Classe [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) para recuperar dados tabulares de tabelas em um arquivo PDF.

O exemplo a seguir mostra a extração de tabelas de todas as páginas:

```cpp
void ExtractTable() {
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para nome do arquivo
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    // Escanear páginas
    for (auto page : document->get_Pages()) {
        absorber->Visit(page);
        for (auto table : absorber->get_TableList()) {
        std::cout << "Table" << std::endl;
        // Iterar através da lista de linhas
        for (auto row : table->get_RowList()) {
            // Iterar através da lista de células
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extrair tabela em área específica da página PDF

Cada tabela absorvida tem a propriedade [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/) que descreve a posição da tabela na página.

Portanto, se você precisar extrair tabelas localizadas em uma região específica, terá que trabalhar com coordenadas específicas.

O exemplo a seguir mostra como extrair tabela marcada com Anotação Quadrada:

```cpp
void ExtractMarkedTable()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para nome do arquivo
    String infilename("sample-table.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    auto page = document->get_Pages()->idx_get(1);
    auto sqa = MakeObject<Aspose::Pdf::Annotations::SquareAnnotation>(page, Rectangle::get_Trivial());
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(sqa);

    auto list = annotationSelector->get_Selected();
    if (list->get_Count() == 0) {
        std::cerr << "Tabelas marcadas não encontradas.." << std::endl;
        return;
    }

    auto squareAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::SquareAnnotation>(list->idx_get(1));

    absorber->Visit(page);

    for (auto table : absorber->get_TableList())
    {
        auto isInRegion =
        (squareAnnotation->get_Rect()->get_LLX() < table->get_Rectangle()->get_LLX()) &&
        (squareAnnotation->get_Rect()->get_LLY() < table->get_Rectangle()->get_LLY()) &&
        (squareAnnotation->get_Rect()->get_URX() > table->get_Rectangle()->get_URX()) &&
        (squareAnnotation->get_Rect()->get_URY() > table->get_Rectangle()->get_URY());

        if (isInRegion)
        {
        for (auto row : table->get_RowList()) {
            // Iterar através da lista de células
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extrair Dados da Tabela do PDF e armazená-los em arquivo CSV

O exemplo a seguir mostra como extrair uma tabela e armazená-la como arquivo CSV. Para ver como converter PDF em Planilha Excel, consulte o artigo [Converter PDF para Excel](/pdf/cpp/convert-pdf-to-excel/).

```cpp
void ExtractTableSaveCSV()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para nome do arquivo
    String infilename("sample-table.pdf");
    String outfilename("PDFToXLS_out.csv");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto ExcelSave Option
    auto excelSave = MakeObject<ExcelSaveOptions>();
    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::CSV);

    // Salvar a saída no formato XLS
    document->Save(_dataDir + outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```