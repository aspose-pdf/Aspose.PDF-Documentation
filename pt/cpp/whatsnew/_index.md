---
title: O que há de novo no C++
linktitle: O que há de novo
type: docs
weight: 10
url: /pt/cpp/whatsnew/
description: Nesta página são apresentadas as novas funcionalidades mais populares no Aspose.PDF para C++ que foram introduzidas em lançamentos recentes.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-12-22"
---

## O que há de novo no Aspose.PDF 24.8

Capacidade de adicionar imagens SVG a uma página.

## O que há de novo no Aspose.PDF 24.4

Corrigido um problema com o carregamento de imagens SVG.

## O que há de novo no Aspose.PDF 24.3

Corrigidos vazamentos de memória ao converter documentos PDF para outros formatos.

## O que há de novo no Aspose.PDF 24.2

Desde a versão 24.2 foi implementado:

- O desempenho do JPXDecoder foi melhorado.

- Corrigida a leitura de documentos com estrutura quebrada.

## O que há de novo no Aspose.PDF 23.7

- A possibilidade de salvar documentos PDF no formato EPUB foi introduzida:

```cpp

    void ConvertPDFtoEPUB()
    {
        std::clog << __func__ << ": Start" << std::endl;
        // String para nome do caminho
        String _dataDir("C:\\Samples\\Conversion\\");

        // String para nome do arquivo de entrada
        String infilename("sample.pdf");
        // String para nome do arquivo de saída
        String outfilename("PDFToEPUB_out.epub");

        // Abrir documento
        auto document = MakeObject<Document>(_dataDir + infilename);

        // Salvar arquivo PDF no formato EPUB
        document->Save(_dataDir + outfilename, SaveFormat::Epub);
        std::clog << __func__ << ": Finish" << std::endl;
    }
```

- O carregamento de arquivos no formato PCL foi implementado:

```cpp

    int main(int argc, char** argv)
    {
        try
        {
            auto options = System::MakeObject<PclLoadOptions>();
            options->ConversionEngine = Aspose::Pdf::PclLoadOptions::ConversionEngines::NewEngine;
            options->SupressErrors = false;

            auto doc = System::MakeObject<Document>(u"c:/aspose.pcl", options);
            doc->Save(u"e:/37432.pdf");
        }
        catch (const System::Exception& error)
        {
            Console::WriteLine(u"Erro: {0}", error->get_Message());
            return 1;
        }
        catch (const std::exception& error)
        {
            std::cerr << "Erro: " << error.what() << std::endl;
            return 1;
        }

        return 0;
    }
```

## O que há de novo no Aspose.PDF 23.1

A partir de 23.1, o suporte para imagens no formato Dicom foi adicionado:

```cpp

    int main()
    {
        auto document = MakeObject<Document>();
        auto page = document->get_Pages()->Add();
        auto image = MakeObject<Image>();
        image->set_FileType(ImageFileType::Dicom);
        image->set_ImageStream(MakeObject<FileStream>(u"c:/aspose.pdf/Aspose.dcm", FileMode::Open, FileAccess::Read));
        page->get_Paragraphs()->Add(image);
        document->Save(u"e:/document.pdf");
    }
```

## O que há de novo no Aspose.PDF 22.11

A partir do 22.11 foi anunciado o primeiro Lançamento Público do **Aspose.PDF para C++ macOS**.

Temos o prazer de anunciar o primeiro lançamento público do Aspose.PDF para C++ macOS. O Aspose.PDF para C++ macOS é uma biblioteca C++ proprietária que permite aos desenvolvedores criar e manipular documentos PDF sem usar o Adobe Acrobat. O Aspose.PDF para C++ macOS permite que os desenvolvedores criem formulários, adicionem/editem texto, manipulem páginas PDF, adicionem anotações, processem fontes personalizadas e muito mais.

## O que há de novo no Aspose.PDF 22.5

Foi implementado o suporte a formulários XFA em documentos PDF.

## O que há de novo no Aspose.PDF 22.4

A nova versão do Aspose.PDF para C++ tem uma base de código do Aspose.PDF para .Net 22.4 e Aspose.Imaging 22.4.

- o método System::Drawing::GetThumbnailImage() foi implementado;
- o construtor RegionDataNodeRect foi otimizado;
- o carregamento de imagem em preto e branco de 1 bit por pixel foi corrigido.

## O que há de novo no Aspose.PDF 22.3

As sobrecargas de métodos foram adicionadas a várias classes. Estes parâmetros suportam ArrayView onde apenas ArrayPtr foi suportado anteriormente.

## O que há de novo no Aspose.PDF 22.1

A nova versão do Aspose.PDF para C++ possui uma base de código do Aspose.PDF para .Net 22.1:

- foi fornecida a nova implementação para System::Xml. Anteriormente, tínhamos uma implementação personalizada que era baseada nas bibliotecas libxml2 e libxslt. A nova versão é baseada no código CoreFX portado

- a biblioteca double-conversion foi atualizada para a versão 3.1.7

- os arquivos DLL são assinados com o certificado Aspose

## O que há de novo no Aspose.PDF 21.10

### Aspose.PDF para C++ suporta recurso para converter SVG para formato PDF

O snippet de código a seguir mostra o processo de conversão de um arquivo SVG em formato PDF com Aspose.PDF para C++.

```cpp

    void ConvertSVGtoPDF()
    {
        std::clog << "SVG to PDF convert: Start" << std::endl;

        String _dataDir("C:\\Samples\\Conversion\\");
        String infilename("sample.svg");
        String outfilename("ImageToPDF-SVG.pdf");

        auto options = MakeObject<SvgLoadOptions>();
        try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
        }
        catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
        }
        std::clog << "SVG to PDF convert: Finish" << std::endl;
    }
```
Сonsiderar um exemplo com recursos avançados:

```cpp

    void ConvertSVGtoPDF_Advanced()
    {
        std::clog << "SVG para PDF converter: Iniciar" << std::endl;

        String _dataDir("C:\\Samples\\Conversion\\");
        String infilename("Aspose.svg");
        String outfilename("ImageToPDF-SVG.pdf");

        auto options = MakeObject<SvgLoadOptions>();
        options->set_AdjustPageSize(true);
        options->ConversionEngine = SvgLoadOptions::ConversionEngines::NewEngine;

        try {
        auto document = MakeObject<Document>(_dataDir + infilename, options);
        document->Save(_dataDir + outfilename);
        }
        catch (System::Exception ex) {
        std::cerr << ex->get_Message() << std::endl;
        }

        std::clog << "SVG para PDF converter: Terminar" << std::endl;
    }
```

## O que há de novo no Aspose.PDF 21.4

### Salvamento de documentos PDF no formato HTML foi implementado

Aspose.PDF para C++ suporta os recursos para converter um arquivo PDF em HTML.

```cpp

    int main()
    {
        auto doc = MakeObject<Document>(u"e:\\sample.pdf");
        doc->Save(u"e:\\sample.html", SaveFormat::Html);
    }
```