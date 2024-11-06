---
title: Manipular Documento PDF
linktitle: Manipular Documento PDF
type: docs
weight: 30
url: pt/cpp/manipulate-pdf-document/
lastmod: "2021-11-11"
description: Esta seção explica sobre a validação de Documento PDF para o Padrão PDF A, como trabalhar com TOC, como definir a data de expiração do PDF e como determinar o Progresso da geração do arquivo PDF.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Validar Documento PDF para o Padrão PDF A (A 1A e A 1B)

Para validar um documento PDF para compatibilidade com PDF/A-1a ou PDF/A-1b, use o método [Validate](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#aa1ac4565b320807c718c44eeee7cda8c) da classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Este método permite que você especifique o nome do arquivo no qual o resultado deve ser salvo e o tipo de validação necessário [PdfFormat](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ac83739fd7c818167c2fdc4dd554de763) enumeração: PDF_A_1A ou PDF_A_1B.


{{% alert color="primary" %}}

O formato XML de saída é um formato Aspose personalizado. O XML contém uma coleção de tags com o nome Problem; cada tag contém os detalhes de um problema específico. O atributo ObjectID da tag Problem representa o ID do objeto específico ao qual este problema está relacionado. O atributo Clause representa uma regra correspondente na especificação PDF.

{{% /alert %}}

O trecho de código a seguir mostra como validar um documento PDF para PDF/A-1A.

```cpp
void ExampleValidate01() {
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1A.xml");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Validar PDF para PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1A);
}
```

O trecho de código a seguir mostra como validar um documento PDF para PDF/A-1B.

```cpp
void ExampleValidate02() {
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo.
    String inputFileName("ValidatePDFAStandard.pdf");
    String outputFileName("Validation-result-A1B.xml");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Validar PDF para PDF/A-1a
    document->Validate(_dataDir + outputFileName, PdfFormat::PDF_A_1B);
}
```

## Trabalhando com TOC

### Adicionar TOC a um PDF Existente

A API Aspose.PDF permite que você adicione um índice, seja ao criar um PDF ou a um arquivo existente.

Para adicionar um índice a um arquivo PDF existente, use a classe [Heading](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.heading) no namespace Aspose.Pdf. O namespace Aspose.Pdf permite que você crie novos arquivos PDF e manipule arquivos PDF existentes. Para adicionar um índice a um PDF existente, use o namespace Aspose.Pdf.

O trecho de código a seguir mostra como criar um índice dentro de um arquivo PDF existente.

```cpp
void ExampleToc01() {
    // String para nomes de caminho.
    String _dataDir("C:\\Samples\\");

    // String para nomes de arquivo
    String inputFileName("AddTOC.pdf");
    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Obter acesso à primeira página do arquivo PDF
    auto tocPage = document->get_Pages()->Insert(1);

    // Criar objeto para representar a informação do índice
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Definir o título para o índice
    tocInfo->set_Title(title);
    tocPage->set_TocInfo(tocInfo);

    // Criar objetos de string que serão usados como elementos do índice
    auto titles = MakeArray<String>(4);
    titles->SetValue(u"Primeira página", 0);
    titles->SetValue(u"Segunda página", 1);
    titles->SetValue(u"Terceira página", 2);
    titles->SetValue(u"Quarta página", 3);

    for (int i = 0; i < 2; i++)
    {
        // Criar objeto Heading
        auto heading2 = MakeObject<Heading>(1);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);

        // Especificar a página de destino para o objeto heading

        heading2->set_DestinationPage(document->get_Pages()->idx_get(i + 2));

        // Página de destino
        heading2->set_Top(document->get_Pages()->idx_get(i + 2)->get_Rect()->get_Height());

        // Coordenada de destino
        segment2->set_Text(titles[i]);

        // Adicionar heading à página contendo o índice
        tocPage->get_Paragraphs()->Add(heading2);
    }

    // Salvar o documento atualizado
    document->Save(_dataDir + outputFileName);
}
```

### Definir diferentes TabLeaderType para diferentes Níveis de TOC

Aspose.PDF para C++ também permite definir diferentes TabLeaderType para diferentes níveis de TOC. Você precisa definir a propriedade LineDash de FormatArray com o valor apropriado de TabLeaderType. Em seguida, você pode adicionar a seção de lista à coleção de seções do documento Pdf. Depois, crie uma seção no documento Pdf e salve o arquivo PDF.

```cpp
void ExampleToc02() {
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto tocPage = document->get_Pages()->Add();
    auto tocInfo = MakeObject<TocInfo>();

    //definir LeaderType
    tocInfo->set_LineDash(TabLeaderType::Solid);

    // Criar objeto para representar informações de TOC
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Definir o título para TOC
    tocInfo->set_Title(title);

    //Adicionar a seção de lista à coleção de seções do documento Pdf
    tocPage->set_TocInfo(tocInfo);

    //Definir o formato da lista de quatro níveis definindo as margens esquerdas
    //e
    //configurações de formato de texto de cada nível

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Left(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(0)->set_LineDash(TabLeaderType::Dot);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(10);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(1)->set_LineDash(TabLeaderType::None);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Left(20);
    tocInfo->get_FormatArray()->idx_get(2)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->set_LineDash(TabLeaderType::Solid);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_Margin()->set_Right(30);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    //Criar uma seção no documento Pdf
    auto page = document->get_Pages()->Add();

    //Adicionar quatro títulos na seção
    for (int Level = 1; Level <= 4; Level++)
    {
    auto heading2 = MakeObject<Heading>(Level);
    auto segment2 = MakeObject<TextSegment>();

    heading2->get_Segments()->Add(segment2);
    heading2->set_IsAutoSequence(true);
    heading2->set_TocPage(tocPage);
    segment2->set_Text(u"Sample Heading" + Level);
    heading2->get_TextState()->set_Font(FontRepository::FindFont(u"Arial Unicode MS"));

    //Adicionar o título no Table Of Contents.
    heading2->set_IsInList(true);
    page->get_Paragraphs()->Add(heading2);
    }

    // salvar o Pdf
    document->Save(_dataDir + outputFileName);
}
```

### Ocultar Números de Página no TOC

Se você deseja ocultar números de página junto com os títulos em um índice, pode usar a propriedade [IsShowPageNumbers](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info#ada10e841699bba062dcd0b440c26b832) da Classe [TOCInfo](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.toc_info) como falso.

Por favor, verifique o seguinte trecho de código para ocultar números de página no índice:

```cpp
void ExampleToc03() {
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto tocPage = document->get_Pages()->Add();

    // Criar objeto para representar informações do TOC
    auto tocInfo = MakeObject<TocInfo>();
    auto title = MakeObject<TextFragment>("Table Of Contents");
    title->get_TextState()->set_FontSize(20);
    title->get_TextState()->set_FontStyle(FontStyles::Bold);

    // Definir o título para TOC
    tocInfo->set_Title(title);

    // Adicionar a seção de lista à coleção de seções do documento Pdf  
    tocPage->set_TocInfo(tocInfo);

    tocInfo->set_IsShowPageNumbers(false);

    // Definir o formato dos quatro níveis de lista configurando as margens esquerdas e
    // configurações de formato de texto de cada nível

    tocInfo->set_FormatArrayLength(4);
    tocInfo->get_FormatArray()->idx_get(0)->get_Margin()->set_Right(0);
    tocInfo->get_FormatArray()->idx_get(0)->get_TextState()->set_FontStyle(FontStyles::Bold | FontStyles::Italic);
    tocInfo->get_FormatArray()->idx_get(1)->get_Margin()->set_Left(30);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_Underline(true);
    tocInfo->get_FormatArray()->idx_get(1)->get_TextState()->set_FontSize(10);
    tocInfo->get_FormatArray()->idx_get(2)->get_TextState()->set_FontStyle(FontStyles::Bold);
    tocInfo->get_FormatArray()->idx_get(3)->get_TextState()->set_FontStyle(FontStyles::Bold);

    auto page = document->get_Pages()->Add();
    // Adicionar quatro cabeçalhos na seção
    for (int Level = 1; Level != 5; Level++)
    {
        auto heading2 = MakeObject<Heading>(Level);
        auto segment2 = MakeObject<TextSegment>();
        heading2->set_TocPage(tocPage);
        heading2->get_Segments()->Add(segment2);
        heading2->set_IsAutoSequence(true);
        segment2->set_Text(u"este é o cabeçalho do nível " + Level);
        heading2->set_IsInList(true);
        page->get_Paragraphs()->Add(heading2);
    }
    // salvar o Pdf
    document->Save(_dataDir + outputFileName);
}
```

## Como definir a data de expiração do PDF

Aplicamos privilégios de acesso em arquivos PDF para que um determinado grupo de usuários possa acessar recursos/objetos específicos de documentos PDF. Para restringir o acesso ao arquivo PDF, geralmente aplicamos criptografia e podemos ter a necessidade de definir a expiração do arquivo PDF, para que o usuário que acessa/visualiza o documento receba um aviso válido sobre a expiração do arquivo PDF.

Para cumprir o requisito acima mencionado, podemos usar o objeto [JavascriptAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.javascript_action/). Por favor, verifique o seguinte trecho de código.

```cpp
void SetPDFexpiryDate() {

    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo. 
    String outputFileName("SetExpiryDate_out.pdf");

    // Instanciar objeto Documento
    auto document = MakeObject<Document>();

    // Adicionar página à coleção de páginas do arquivo PDF
    document->get_Pages()->Add();

    // Adicionar fragmento de texto à coleção de parágrafos do objeto página
    document->get_Pages()->idx_get(1)->get_Paragraphs()->Add(new TextFragment(u"Hello World..."));

    String javascriptCode(u"var year=2017;");
    javascriptCode += u"var month=5;";
    javascriptCode += u"today = new Date(); today = new Date(today.getFullYear(), today.getMonth());";
    javascriptCode += u"expiry = new Date(year, month);";
    javascriptCode += u"if (today.getTime() > expiry.getTime())";
    javascriptCode += u"app.alert('The file is expired. You need a new one.');";

    // Criar objeto JavaScript para definir a data de expiração do PDF
    auto javaScript = MakeObject<Aspose::Pdf::Annotations::JavascriptAction>(javascriptCode);

    // Definir JavaScript como ação de abertura do PDF
    document->set_OpenAction(javaScript);

    // Salvar Documento PDF
    document->Save(_dataDir + outputFileName);
}
```

## Determinar o Progresso da Geração de Arquivo PDF

Um cliente nos pediu para adicionar um recurso que permite aos desenvolvedores determinar o progresso da geração de arquivos PDF. Aqui está a resposta para essa solicitação.

O campo [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb) da classe [DocSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options) permite que você determine como está indo a geração do PDF.

Os trechos de código abaixo mostram como usar o [CustomerProgressHandler](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.doc_save_options#a712bcc865fa8f75bbdc2a3b55e4581fb).

```cpp
using ProgressHandler = System::MulticastDelegate<void(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo>)>;
void ConversionProgressCallback(SharedPtr<UnifiedSaveOptions::ProgressEventHandlerInfo> eventInfo)
{
    String eventType;
    switch (eventInfo->EventType)
    {
    case ProgressEventType::ResultPageCreated:
        eventType = u"ResultPageCreated";
        break;
    case ProgressEventType::ResultPageSaved:
        eventType = u"ResultPageSaved";
        break;
    case ProgressEventType::SourcePageAnalysed:
        eventType = u"SourcePageAnalysed";
        break;
    case ProgressEventType::TotalProgress:
        eventType = u"TotalProgress";
        break;
    }
    Console::WriteLine(String::Format(u"Event type: {0}, Value: {1}, MaxValue: {2}", 
        eventType, eventInfo->Value, eventInfo->MaxValue));
}
```

```cpp
void DetermineProgressOfPDFfileGeneration() {
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo.
    String inputFileName("AddTOC.pdf");

    String outputFileName("TOC_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    // Abrir documento
    auto saveOptions = MakeObject<DocSaveOptions>();

    saveOptions->CustomProgressHandler = ProgressHandler(ConversionProgressCallback);

    document->Save(_dataDir + outputFileName, saveOptions);
}
```

## Achatar PDF Preenchível em C++

Documentos PDF frequentemente incluem formulários com widgets interativos preenchíveis, como botões de rádio, caixas de seleção, caixas de texto, listas, etc. Para torná-lo não editável para vários fins de aplicação, precisamos achatar o arquivo PDF. O Aspose.PDF para C++ fornece a função para achatar seu PDF em C++ com apenas algumas linhas de código:

```cpp
void FlattenFillablePDF() {
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");
    // String para nome do arquivo.
    String inputFileName("sample-form.pdf");
    String outputFileName("FlattenForms_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Achatar PDF Preenchível
    if (document->get_Form()->get_Fields()->get_Count() > 0)
    {
        for (auto item : document->get_Form()->get_Fields())
        item->Flatten();
    }

    // Salvar o documento atualizado
    document->Save(_dataDir + outputFileName);
}
```