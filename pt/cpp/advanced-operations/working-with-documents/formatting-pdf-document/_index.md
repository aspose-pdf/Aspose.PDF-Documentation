---
title: Formatação de Documento PDF usando C++
linktitle: Formatação de Documento PDF
type: docs
weight: 20
url: pt/cpp/formatting-pdf-document/
description: Crie e formate o Documento PDF com Aspose.PDF para C++. Use o próximo trecho de código para resolver suas tarefas.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Formatação de Documento PDF

### Obter Propriedades da Janela do Documento e Exibição de Página

Este tópico ajuda você a entender como obter propriedades da janela do documento, aplicativo visualizador e como as páginas são exibidas. Para definir essas propriedades, abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Agora você pode definir as propriedades do objeto Document, tais como:

- CenterWindow – Centralizar a janela do documento na tela. Padrão: false.
- Direction – Ordem de leitura. Isso determina como as páginas são dispostas quando exibidas lado a lado. Padrão: da esquerda para a direita.
- DisplayDocTitle – Exibir o título do documento na barra de título da janela do documento. - HideMenuBar – Ocultar ou exibir a barra de menu da janela do documento. Padrão: false (a barra de menu é exibida).
- HideToolBar – Ocultar ou exibir a barra de ferramentas da janela do documento. Padrão: false (a barra de ferramentas é exibida).
- HideWindowUI – Ocultar ou exibir elementos da janela do documento, como barras de rolagem. Padrão: false (elementos da UI são exibidos).
- NonFullScreenPageMode – Como o documento é exibido quando não está em modo de página inteira.
- PageLayout – O layout da página.
- PageMode – Como o documento é exibido quando aberto pela primeira vez. As opções são mostrar miniaturas, tela cheia, mostrar painel de anexos.

O seguinte trecho de código mostra como obter as propriedades usando a classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void GetDocumentWindowAndPageDisplayProperties()
{
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");
    // String para nome do arquivo.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Obter diferentes propriedades do documento
    // Posição da janela do documento - Padrão: false
    Console::WriteLine(u"CenterWindow : {0}", document->get_CenterWindow());

    // Ordem de leitura predominante; determina a posição da página
    // Quando exibido lado a lado - Padrão: L2R
    Console::WriteLine(u"Direction : {0}", document->get_Direction());

    // Se a barra de título da janela deve exibir o título do documento
    // Se false, a barra de título exibe o nome do arquivo PDF - Padrão: false
    Console::WriteLine(u"DisplayDocTitle : {0}", document->get_DisplayDocTitle());

    // Se deve redimensionar a janela do documento para ajustar ao tamanho da
    // Primeira página exibida - Padrão: false
    Console::WriteLine(u"FitWindow : {0}", document->get_FitWindow());

    // Se deve ocultar a barra de menu do aplicativo visualizador - Padrão: false
    Console::WriteLine(u"HideMenuBar : {0}", document->get_HideMenubar());

    // Se deve ocultar a barra de ferramentas do aplicativo visualizador - Padrão: false
    Console::WriteLine(u"HideToolBar : {0}", document->get_HideToolBar());

    // Se deve ocultar elementos da UI como barras de rolagem
    // E deixar apenas o conteúdo da página exibido - Padrão: false
    Console::WriteLine(u"HideWindowUI : {0}", document->get_HideWindowUI());

    // Modo de página do documento. Como exibir o documento ao sair do modo de tela cheia.
    Console::WriteLine(u"NonFullScreenPageMode : {0}", document->get_NonFullScreenPageMode());

    // O layout da página, ou seja, página única, uma coluna
    Console::WriteLine(u"PageLayout : {0}", document->get_PageLayout());

    // Como o documento deve ser exibido quando aberto
    // Ou seja, mostrar miniaturas, tela cheia, mostrar painel de anexos
    Console::WriteLine(u"pageMode : {0}", document->get_PageMode());
}
```
### Definir Propriedades da Janela do Documento e Exibição de Página

Este tópico explica como definir as propriedades da janela do documento, aplicativo visualizador e exibição de página. Para definir essas diferentes propriedades:

1. Abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Defina diferentes propriedades do documento:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

1. [Salve](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/#ac082fe8e67b25685fc51d33e804269fa) o arquivo PDF atualizado usando o método Save.

As propriedades disponíveis são:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

Cada uma é usada e descrita no código abaixo. O seguinte trecho de código mostra como definir as propriedades usando a classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void SetDocumentWindowAndPageDisplayProperties()
{
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");
    // String para nome do arquivo.
    String inputFileName("sample.pdf");
    String outputFileName("sample_page_display_properties.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Definir diferentes propriedades do documento
    // Especificar para posicionar a janela do documento - Padrão: false
    document->set_CenterWindow(true);

    // Ordem de leitura predominante; determina a posição da página
    // Quando exibido lado a lado - Padrão: L2R
    document->set_Direction(Direction::R2L);

    // Especificar se a barra de título da janela deve exibir o título do documento
    // Se falso, a barra de título exibe o nome do arquivo PDF - Padrão: false
    document->set_DisplayDocTitle(true);

    // Especificar se deve redimensionar a janela do documento para ajustar o tamanho da
    // Primeira página exibida - Padrão: false
    document->set_FitWindow(true);

    // Especificar se deve ocultar a barra de menu do aplicativo visualizador - Padrão: false
    document->set_HideMenubar(true);

    // Especificar se deve ocultar a barra de ferramentas do aplicativo visualizador - Padrão: false
    document->set_HideToolBar(true);

    // Especificar se deve ocultar elementos da interface do usuário, como barras de rolagem
    // E deixar apenas o conteúdo da página exibido - Padrão: false
    document->set_HideWindowUI(true);

    // Modo de página do documento. especificar como exibir o documento ao sair do modo de tela cheia.
    document->set_NonFullScreenPageMode(PageMode::UseOC);

    // Especificar o layout da página, ou seja, página única, uma coluna
    document->set_PageLayout(PageLayout::TwoColumnLeft);

    // Especificar como o documento deve ser exibido quando aberto
    // Ou seja, mostrar miniaturas, tela cheia, mostrar painel de anexos
    document->set_PageMode(PageMode::UseThumbs);

    // Salvar arquivo PDF atualizado
    document->Save(_dataDir + outputFileName);
}
```
### Incorporando Fontes em um arquivo PDF existente

Os leitores de PDF suportam [um núcleo de 14 fontes](https://en.wikipedia.org/wiki/PDF#Text) para que os documentos possam ser exibidos da mesma forma, independentemente da plataforma em que o documento é exibido. Quando um PDF contém uma fonte que não é uma das 14 fontes principais, incorpore a fonte ao arquivo PDF para evitar a substituição de fontes.

O Aspose.PDF for C++ suporta a incorporação de fontes em arquivos PDF existentes. Você pode incorporar uma fonte completa ou um subconjunto da fonte. Para incorporar a fonte, abra o arquivo PDF usando a classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document). Em seguida, use a classe [Aspose.Pdf.Text.Font](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.font) para incorporar a fonte ao arquivo PDF. Para incorporar a fonte completa, use a propriedade IsEmbeded da classe Font; para usar um subconjunto da fonte, use a propriedade IsSubset.

{{% alert color="primary" %}}

Um subconjunto de fonte incorpora apenas os caracteres que são usados e é útil onde as fontes são usadas para frases curtas ou slogans, por exemplo, onde uma fonte corporativa é usada para um logotipo, mas não para o texto do corpo. Usar um subconjunto reduz o tamanho do arquivo do PDF de saída. No entanto, se uma fonte personalizada for usada para o texto do corpo, incorpore-a em sua totalidade.

{{% /alert %}}

O trecho de código a seguir mostra como incorporar uma fonte em um arquivo PDF.

### Incorporando Fontes Padrão Tipo 1

Existem documentos PDF que usam fontes de um conjunto especial chamado "Fontes Padrão Tipo 1". Este conjunto inclui 14 fontes e incorporar este tipo de fonte requer o uso de flags especiais, ou seja, [Aspose.Pdf.Document.EmbedStandardFonts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a8f1a88eef22e05ee9ee22a79db9cb9f6).

A seguir está o trecho de código que pode ser usado para obter um documento com todas as fontes incorporadas, incluindo Fontes Padrão Tipo 1:

```cpp
void EmbeddingStandardType1Fonts()
{

    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");
    // String para nome do arquivo.
    String inputFileName("sample.pdf");
    String outputFileName("embedded-fonts-updated_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Definir a propriedade EmbedStandardFonts do documento
    document->set_EmbedStandardFonts(true);
    for (auto page : document->get_Pages())
    {
        auto fonts = page->get_Resources()->get_Fonts();
        if (fonts != nullptr)
        {
            for (auto pageFont : fonts)
            {
                // Verificar se a fonte já está incorporada
                if (!pageFont->get_IsEmbedded())
                {
                    pageFont->set_IsEmbedded(true);
                }
            }
        }
    }
    document->Save(_dataDir + outputFileName);
}
```
### Incorporando Fontes ao criar PDF

Se você precisar usar qualquer fonte além das 14 fontes principais suportadas pelo Adobe Reader, deverá incorporar a descrição da fonte ao gerar o arquivo Pdf. Se as informações da fonte não estiverem incorporadas, o Adobe Reader as obterá do Sistema Operacional se estiverem instaladas no sistema, ou construirá uma fonte substituta de acordo com o descritor de fonte no Pdf.

>Observe que a fonte incorporada deve estar instalada na máquina host, ou seja, no caso do seguinte código, a fonte 'Univers Condensed' está instalada no sistema.

Usamos a propriedade IsEmbedded da classe Font para incorporar as informações da fonte no arquivo Pdf. Definir o valor dessa propriedade como 'True' incorporará o arquivo completo da fonte no Pdf, sabendo que isso aumentará o tamanho do arquivo Pdf. A seguir, está o trecho de código que pode ser usado para incorporar as informações da fonte no Pdf.

```cpp
void EmbeddingFontsWhileCreatingPDF()
{
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");
    // String para nome do arquivo.
    String inputFileName("sample.pdf");
    String outputFileName("EmbedFontWhileDocCreation_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Crie uma seção no objeto Pdf
    auto page = document->get_Pages()->Add();

    auto fragment = MakeObject<TextFragment>("");
    auto segment = MakeObject <TextSegment>(u"Este é um texto de exemplo usando fonte personalizada.");

    auto ts = MakeObject<TextState>();

    ts->set_Font(FontRepository::FindFont(u"Arial"));
    ts->get_Font()->set_IsEmbedded(true);
    segment->set_TextState(ts);
    fragment->get_Segments()->Add(segment);
    page->get_Paragraphs()->Add(fragment);

    // Salvar Documento PDF
    document->Save(_dataDir);
}
```

### Definir Nome de Fonte Padrão ao Salvar PDF

Quando um documento PDF contém fontes que não estão disponíveis no próprio documento e no dispositivo, a API substitui essas fontes pela fonte padrão. Quando a fonte está disponível (está instalada no dispositivo ou está incorporada no documento), o PDF de saída deve ter a mesma fonte (não deve ser substituída pela fonte padrão). O valor da fonte padrão deve conter o nome da fonte (não o caminho para os arquivos de fonte). Apose.PDF para C++ implementou um recurso para definir o nome da fonte padrão ao salvar um documento como PDF. O seguinte trecho de código pode ser usado para definir a fonte padrão:

```cpp
void SetDefaultFontNameWhileSavingPDF()
{
    // String para o nome do caminho.
    String _dataDir("C:\\Samples\\");
    // String para o nome do arquivo.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);

    auto pdfSaveOptions = MakeObject<PdfSaveOptions>();

    // Especificar Nome da Fonte Padrão
    pdfSaveOptions->set_DefaultFontName(newName);
    document->Save(_dataDir + outputFileName, pdfSaveOptions);
}
```

### Obter Todas as Fontes do Documento PDF

Caso você queira obter todas as fontes de um documento PDF, você pode usar o método [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a2e22a508e8baef176dfc34734cf0def9).GetAllFonts() fornecido na classe [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

Por favor, verifique o trecho de código a seguir para obter todas as fontes de um documento PDF existente:

```cpp
void GetAllFontsFromPDFdocument()
{
    // String para o nome do caminho.
    String _dataDir("C:\\Samples\\");
    // String para o nome do arquivo.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");
    String newName("Arial");

    auto document = MakeObject<Document>(inputFileName);
    auto fonts = document->get_FontUtilities()->GetAllFonts();
    for (auto font : fonts)
    {
        std::cerr << font->get_FontName() << std::endl;
    }
}
```

### Obter Avisos para Substituição de Fontes

Aspose.PDF para C++ fornece métodos para obter notificações sobre substituição de fontes para lidar com casos de substituição de fontes. Os trechos de código abaixo mostram como usar a funcionalidade correspondente.

```cpp
void GetWarningsForFontSubstitution()
{
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo.
    String inputFileName("sample.pdf");
    String outputFileName("output_out.pdf");

    auto document = MakeObject<Document>(inputFileName);

    document->FontSubstitution = Aspose::Pdf::Document::FontSubstitutionHandler(OnFontSubstitution);
}
```

O método [OnFontSubstitution](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac776d8736d430532bdaa530a36eb51a0) é listado abaixo.

```cpp
void OnFontSubstitution(Aspose::Pdf::Text::Font &font, Aspose::Pdf::Text::Font& newFont) {
    std::cout << "Aviso: Fonte " << font.get_FontName() 
            << " foi substituída por outra fonte -> " 
            << newFont.get_FontName() << std::endl;
}
```

### Melhorar a Incorporação de Fontes usando FontSubsetStrategy

O recurso para incorporar as fontes como um subconjunto pode ser realizado usando a propriedade IsSubset, mas às vezes você deseja reduzir um conjunto de fontes totalmente incorporado para apenas subconjuntos que são usados no documento. [Aspose.Pdf.Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) tem a propriedade [FontUtilities](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document.i_document_font_utilities/) que inclui o método SubsetFonts(FontSubsetStrategy subsetStrategy). No método SubsetFonts(), o parâmetro subsetStrategy ajuda a ajustar a estratégia de subconjunto. FontSubsetStrategy suporta duas variantes de subagrupamento de fontes.

- SubsetAllFonts - Isso irá subagrupar todas as fontes usadas em um documento.
- SubsetEmbeddedFontsOnly - Isso irá subagrupar apenas aquelas fontes que estão totalmente incorporadas ao documento.

O seguinte trecho de código mostra como definir FontSubsetStrategy:

```cpp
void ImproveFontsEmbeddingUsingFontSubsetStrategy()
{
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo.
    String inputFileName("sample.pdf");
    // String para nome do arquivo.
    String outputFileName("sample_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    // Todas as fontes serão incorporadas como subconjunto no documento no caso de SubsetAllFonts.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetAllFonts);
    // O subconjunto de fontes será incorporado para fontes totalmente incorporadas, mas fontes que não estão incorporadas no documento não serão afetadas.
    document->get_FontUtilities()->SubsetFonts(FontSubsetStrategy::SubsetEmbeddedFontsOnly);
    document->Save(_dataDir + outputFileName);
}
```
### Obter-Definir Fator de Zoom do Arquivo PDF

Às vezes, você quer definir o fator de zoom de um documento PDF. Com o Aspose.PDF para C++, você pode definir o valor do fator de zoom pelo método [set_OpenAction(…)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#abb5c84979077034d06a673409b666e21) da classe Document.

A propriedade Destination da classe [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action/) permite que você obtenha o valor de zoom associado a um arquivo PDF. Da mesma forma, ela pode ser usada para definir o fator de zoom de um arquivo.

#### Definir Fator de Zoom

O seguinte trecho de código mostra como definir o fator de zoom de um arquivo PDF.

```cpp
void SetZoomFactor() {
    // String para o nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo.
    String inputFileName("sample.pdf");
    // String para o nome do arquivo.
    String outputFileName("Zoomed_pdf_out.pdf");

    auto document = MakeObject<Document>(inputFileName);
    auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 0, 0, .5));

    document->set_OpenAction(action);
    // Salvar o documento
    document->Save(_dataDir + outputFileName);
}
```

#### Obter Fator de Zoom

Obtenha o fator de zoom no seu arquivo PDF usando Aspose.PDF para C++.

O trecho de código a seguir mostra como obter o fator de zoom de um arquivo PDF:

```cpp
void GetZoomFactor() 
{
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo.
    String inputFileName("sample.pdf");

    auto document = MakeObject<Document>(inputFileName);

    // Criar objeto GoToAction
    auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(document->get_OpenAction());

    // Obter o fator de Zoom do arquivo PDF
    auto zoom = System::DynamicCast<Aspose::Pdf::Annotations::XYZExplicitDestination>(action->get_Destination());
    Console::WriteLine(zoom->get_Zoom()); // Valor de zoom do documento;
}
```

### Configurando Propriedades de Predefinição de Diálogo de Impressão

Aspose.PDF para C++ permite configurar as propriedades de Predefinição de Diálogo de Impressão de um documento PDF. Permite que você altere a propriedade DuplexMode de um documento PDF, que é configurada para simplex por padrão. Isso pode ser alcançado usando duas metodologias diferentes, como mostrado abaixo.

```cpp
void SettingPrintDialogPresetProperties()
{
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");
    // String para nome do arquivo.
    String outputFileName("SettingPrintDialogPresetProperties.pdf");

    auto document = MakeObject<Document>();
    document->get_Pages()->Add();
    document->set_Duplex(PrintDuplex::DuplexFlipLongEdge);
    document->Save(_dataDir + outputFileName);
}
```

### Configurando Propriedades Predefinidas do Diálogo de Impressão usando o Editor de Conteúdo PDF

```cpp
void SettingPrintDialogPresetPropertiesUsingContentEditor() {
    // String para nome do caminho.
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo.
    String inputFileName("sample.pdf");
    String outputFileName("SetPrintDlgPropertiesUsingPdfContentEditor_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto contentEditor = MakeObject<Aspose::Pdf::Facades::PdfContentEditor>();

    contentEditor->BindPdf(outputFileName);
    if ((contentEditor->GetViewerPreference() & Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge) > 0)
    {
    std::cout << "O arquivo tem duplex flip short edge" << std::endl;
    }

    contentEditor->ChangeViewerPreference(Aspose::Pdf::Facades::ViewerPreference::DuplexFlipShortEdge);
    contentEditor->Save(_dataDir + outputFileName);
}
```