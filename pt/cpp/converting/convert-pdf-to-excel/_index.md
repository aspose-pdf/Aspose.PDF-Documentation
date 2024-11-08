---
title: Converter PDF para Excel em C++
linktitle: Converter PDF para Excel
type: docs
weight: 20
url: /pt/cpp/convert-pdf-to-excel/
lastmod: "2021-11-19"
description: Aspose.PDF para C++ permite converter PDF para o formato Excel usando C++. Durante isso, as páginas individuais do arquivo PDF são convertidas em planilhas do Excel.
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Visão Geral

Este artigo explica como **converter PDF para formatos Excel usando C++**. Ele abrange os seguintes tópicos.

_Formato_: **XLS**
- [C++ PDF para XLS](#cpp-pdf-to-xls)
- [C++ Converter PDF para XLS](#cpp-pdf-to-xls)
- [C++ Como converter arquivo PDF para XLS](#cpp-pdf-to-xls)

_Formato_: **XLSX**
- [C++ PDF para XLSX](#cpp-pdf-to-xlsx)
- [C++ Converter PDF para XLSX](#cpp-pdf-to-xlsx)
- [C++ Como converter arquivo PDF para XLSX](#cpp-pdf-to-xlsx)

_Formato_: **Formato Microsoft Excel XLS**
- [C++ PDF para Excel](#cpp-pdf-to-excel-xls)
- [C++ Converter PDF para Excel](#cpp-pdf-to-excel-xls)
- [C++ Como converter arquivo PDF para Excel](#cpp-pdf-to-excel-xls)

_Formato_: **Formato Microsoft Excel XLSX**
- [C++ PDF para Excel](#cpp-pdf-to-excel-xlsx)
- [C++ Converter PDF para Excel](#cpp-pdf-to-excel-xlsx)
- [C++ Como converter arquivo PDF para Excel](#cpp-pdf-to-excel-xlsx)

Outros tópicos abordados por este artigo
- [Veja Também](#see-also)

## Conversões de PDF para Excel em C++

**Aspose.PDF para C++** suporta o recurso de conversão de arquivos PDF para formatos Excel.

Aspose.PDF para C++ é um componente de manipulação de PDF, introduzimos um recurso que renderiza arquivo PDF para planilha Excel (arquivos XLS). Durante esta conversão, as páginas individuais do arquivo PDF são convertidas em planilhas Excel.

Para converter arquivos PDF para formato <abbr title="Planilha do Microsoft Excel">XLS</abbr>, Aspose.PDF possui uma classe chamada ExcelSaveOptions. Um objeto da classe ExcelSaveOptions é passado como segundo argumento para o construtor Document.Save(..).

O trecho de código a seguir mostra o processo de conversão de arquivo PDF para formato XLS com Aspose.PDF para C++.

<a name="cpp-pdf-to-xls" id="cpp-pdf-to-xls"><strong>Passos: Converter PDF para XLS em C++</strong></a> | <a name="cpp-pdf-to-excel-xls" id="cpp-pdf-to-excel-xls"><strong>Passos: Converter PDF para formato Excel XLS em C++</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) com o documento PDF de origem.
2. Salve-o no formato _XLS_ chamando o método **Document->Save()**.

```cpp
void ConvertPDFtoExcel()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Salve a saída no formato XLS
    document->Save(_dataDir + outfilename, SaveFormat::Excel);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message();
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Converter PDF para XLS com Controle de Coluna

Ao converter um PDF para o formato XLS, uma coluna em branco é adicionada ao arquivo de saída como primeira coluna. A opção InsertBlankColumnAtFirst da classe in ExcelSaveOptions é usada para controlar esta coluna. Seu valor padrão é verdadeiro.

```cpp
void ConvertPDFtoExcel_Advanced_InsertBlankColumnAtFirst()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para o nome do arquivo
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto ExcelSave Option
    auto excelSave = MakeObject<ExcelSaveOptions>();

    // A opção InsertBlankColumnAtFirst da classe in ExcelSaveOptions é usada para controlar esta coluna. Seu valor padrão é verdadeiro.
    excelSave->set_InsertBlankColumnAtFirst(false);

    // Salvar a saída no formato XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Converter PDF para uma única planilha Excel

Ao exportar um arquivo PDF com muitas páginas para XLS, cada página é exportada para uma folha diferente no arquivo Excel. Isso ocorre porque a propriedade MinimizeTheNumberOfWorksheets é configurada como false por padrão. Para garantir que todas as páginas sejam exportadas para uma única planilha no arquivo Excel de saída, configure a propriedade MinimizeTheNumberOfWorksheets como true.

```cpp
void ConvertPDFtoExcel_Advanced_MinimizeTheNumberOfWorksheets()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de opção de salvamento Excel
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_MinimizeTheNumberOfWorksheets(true);

    // Salvar a saída no formato XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Converter para o formato XLSX

Por padrão, o Aspose.PDF usa XML Spreadsheet 2003 para armazenar dados. Para converter arquivos PDF para o formato XLSX, Aspose.PDF possui uma classe chamada [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) com 'Format'. Um objeto da classe [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options) é passado como segundo argumento para o método [Save](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa).

O seguinte trecho de código mostra o processo de conversão de arquivo PDF para o formato XLSX.

<a name="cpp-pdf-to-xlsx" id="cpp-pdf-to-xlsx"><strong>Passos: Converter PDF para XLSX em C++</strong></a> | <a name="cpp-pdf-to-excel-xlsx" id="cpp-pdf-to-excel-xlsx"><strong>Passos: Converter PDF para formato Excel XLSX em C++</strong></a>

1. Crie uma instância do objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) com o documento PDF de origem.
2. Crie uma instância de [ExcelSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.excel_save_options).
3. Defina o formato como _ExcelSaveOptions::ExcelFormat::XLSX_.
4. Salve no formato _XLSX_ chamando o método **Document->Save()** e passando a ele a instância de _ExcelSaveOptions_.

```cpp
void ConvertPDFtoExcel_Advanced_SaveXLSX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nome do arquivo
    String infilename("sample.pdf");
    String outfilename("PDFToExcel.xls");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto ExcelSave Option
    auto excelSave = MakeObject<ExcelSaveOptions>();

    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::XLSX);

    // Salvar a saída no formato XLS
    document->Save(outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}

**Tente converter PDF para Excel online**
Aspose.PDF for C++ apresenta a você o aplicativo online gratuito ["PDF to XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), onde você pode experimentar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Convertion PDF to Excel with Free App](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}

## Veja Também

Este artigo também abrange estes tópicos. Os códigos são os mesmos que acima.

_Format_: **Formato Microsoft Excel XLS**
- [C++ PDF para Excel XLS Código](#cpp-pdf-to-excel-xls)
- [C++ PDF para Excel XLS Programaticamente](#cpp-pdf-to-excel-xls)
- [C++ PDF para Excel XLS Biblioteca](#cpp-pdf-to-excel-xls)
- [C++ Salvar PDF como Excel XLS](#cpp-pdf-to-excel-xls)
- [C++ Gerar Excel XLS de PDF](#cpp-pdf-to-excel-xls)
- [C++ Criar Excel XLS de PDF](#cpp-pdf-to-excel-xls)
- [C++ PDF para Excel XLS Conversor](#cpp-pdf-to-excel-xls)

_Format_: **Formato Microsoft Excel XLSX**
- [C++ PDF para Excel XLSX Código](#cpp-pdf-to-excel-xlsx)

- [C++ PDF para Excel XLSX Programaticamente](#cpp-pdf-to-excel-xlsx)
- [Biblioteca de C++ PDF para Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ Salvar PDF como Excel XLSX](#cpp-pdf-to-excel-xlsx)
- [C++ Gerar Excel XLSX a partir de PDF](#cpp-pdf-to-excel-xlsx)
- [C++ Criar Excel XLSX a partir de PDF](#cpp-pdf-to-excel-xlsx)
- [Conversor de C++ PDF para Excel XLSX](#cpp-pdf-to-excel-xlsx)

_Formato_: **XLS**
- [Código C++ PDF para XLS](#cpp-pdf-to-xls)
- [C++ PDF para XLS Programaticamente](#cpp-pdf-to-xls)
- [Biblioteca de C++ PDF para XLS](#cpp-pdf-to-xls)
- [C++ Salvar PDF como XLS](#cpp-pdf-to-xls)
- [C++ Gerar XLS a partir de PDF](#cpp-pdf-to-xls)
- [C++ Criar XLS a partir de PDF](#cpp-pdf-to-xls)
- [Conversor de C++ PDF para XLS](#cpp-pdf-to-xls)

_Formato_: **XLSX**
- [Código C++ PDF para XLSX](#cpp-pdf-to-xlsx)
- [C++ PDF para XLSX Programaticamente](#cpp-pdf-to-xlsx)
- [Biblioteca de C++ PDF para XLSX](#cpp-pdf-to-xlsx)
- [C++ Salvar PDF como XLSX](#cpp-pdf-to-xlsx)
- [C++ Gerar XLSX a partir de PDF](#cpp-pdf-to-xlsx)
- [C++ Criar XLSX a partir de PDF](#cpp-pdf-to-xlsx)
- [Conversor de C++ PDF para XLSX](#cpp-pdf-to-xlsx)