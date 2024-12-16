---
title:  Extrair dados de AcroForm 
linktitle:  Extrair dados de AcroForm
type: docs
weight: 50
url: /pt/cpp/extract-data-from-acroform/
description: Aspose.PDF facilita a extração de dados de campos de formulário de arquivos PDF. Aprenda a extrair dados de AcroForms e salvá-los em formato XML ou FDF.
lastmod: "2021-12-13"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Extrair campos de formulário de documento PDF

Aspose.PDF para C++ permite não apenas criar campos de formulário e preencher campos de formulário, mas também facilita a extração de dados de campos de formulário ou informações de campos de formulário de arquivos PDF.

No exemplo de código abaixo, demonstramos como iterar sobre cada página em PDF para extrair informações sobre todos os AcroForms em PDF, bem como os valores dos campos de formulário. Este exemplo de código assume que você não conhece os nomes dos campos do formulário antecipadamente.

```cpp
void ExtractFormFields() {
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para nome do arquivo
    String infilename("StudentInfoFormElectronic.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Obter valores de todos os campos
    for (auto formField : document->get_Form()->get_Fields()) {
        std::cout << "Nome do Campo :" << formField->get_PartialName() << std::endl;
        std::cout << "Valor : " << formField->get_Value() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Extrair Dados para XML de um Arquivo PDF

A classe [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) permite exportar dados para um arquivo XML a partir do arquivo PDF usando o método ExportXml. Para exportar dados para XML, você precisa criar um objeto da classe Form e então chamar o método ExportXml usando o objeto FileStream. Em seguida, você deve fechar o objeto FileStream e desfazer o objeto Form.

O trecho de código a seguir mostra como exportar dados para um arquivo XML.

```cpp
void ExtractFormFieldsToXML() {
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para nome do arquivo
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String xmlFileName(_dataDir + u"StudentInfoFormElectronic.xml");

    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);
    auto fdfOutputStream = System::IO::File::OpenWrite(xmlFileName);

    // Exportar dados
    form->ExportXml(fdfOutputStream);

    // Fechar fluxo de arquivo
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Exportar Dados para FDF a partir de um Arquivo PDF

A classe [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) permite que você exporte dados para um arquivo FDF a partir de um arquivo PDF usando o método ExportFdf. Para exportar dados para FDF, você precisa criar um objeto da classe Form e então chamar o método ExportFdf usando o objeto FileStream. Depois, você pode salvar o arquivo PDF usando o método Save da classe Form.

O seguinte trecho de código mostra como exportar dados para um arquivo FDF.

```cpp
void ExtractFormExportFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // String para o nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para o nome do arquivo
    String infilename(_dataDir + u"StudentInfoFormElectronic.pdf");
    String fdfFileName(_dataDir+ u"StudentInfoFormElectronic.fdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // Exportar dados
    form->ExportFdf(fdfOutputStream);

    // Fechar fluxo de arquivo
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Exportar Dados para XFDF de um Arquivo PDF

Aspose PDF para C++ com a classe [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.form) permite que você exporte dados para um arquivo XFDF a partir do arquivo PDF usando o método ExportXfdf. Para exportar dados para XFDF, você precisa criar um objeto da classe Form e então chamar o método ExportXfdf usando o objeto FileStream.

No final, você pode salvar o arquivo PDF usando o método Save da classe Form.

O trecho de código a seguir mostra como exportar dados para um arquivo XFDF.

```cpp
void ExtractFormExportXFDF() {
    std::clog << __func__ << ": Start" << std::endl;
    // String para nome do caminho
    String _dataDir("C:\\Samples\\Parsing\\");

    // String para nome do arquivo
    String infilename("StudentInfoFormElectronic.pdf");
    String fdfFileName("StudentInfoFormElectronic.xfdf");

    //String fdfFileName = Paths.get(_dataDir, "student.xfdf").toString();
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + infilename);

    auto fdfOutputStream = System::IO::File::OpenWrite(fdfFileName);

    // Exportar dados
    form->ExportXfdf(fdfOutputStream);

    // Fechar fluxo de arquivo
    fdfOutputStream->Close();
    std::clog << __func__ << ": Finish" << std::endl;
}
```