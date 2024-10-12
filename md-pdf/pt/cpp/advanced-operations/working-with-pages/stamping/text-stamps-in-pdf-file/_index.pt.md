---
title: Adicionar Carimbos de Texto em Arquivo PDF
linktitle: Carimbos de Texto em Arquivo PDF
type: docs
weight: 20
url: /cpp/text-stamps-in-the-pdf-file/
description: Adicione um carimbo de texto a um arquivo PDF usando a classe TextStamp com C++.
lastmod: "2021-12-95"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Carimbo de Texto com C++

Você pode usar a classe [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) para adicionar um carimbo de texto em um arquivo PDF. A classe TextStamp fornece as propriedades necessárias para criar um carimbo baseado em texto, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar um carimbo de texto, você precisa criar um objeto Document e um objeto TextStamp usando as propriedades necessárias. Depois disso, você pode chamar o método AddStamp da Page para adicionar o carimbo no PDF. O trecho de código a seguir mostra como adicionar um carimbo de texto no arquivo PDF.

```cpp
void AddTextStampToPDFFile() {
   
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    
    // Criar carimbo de texto
    auto textStamp =MakeObject<TextStamp>(u"Sample Stamp");

    // Definir se o carimbo é de fundo
    textStamp->set_Background(true);
    // Definir origem
    textStamp->set_XIndent(100);
    textStamp->set_YIndent(100);
    // Rotacionar carimbo
    textStamp->set_Rotate(Rotation::on90);

    // Definir propriedades do texto
    textStamp->get_TextState()->set_Font(FontRepository::FindFont(u"Arial"));
    textStamp->get_TextState()->set_FontSize(14.0F);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Bold);
    textStamp->get_TextState()->set_FontStyle(FontStyles::Italic);
    textStamp->get_TextState()->set_ForegroundColor(Color::get_Green());
    // Adicionar carimbo a uma página específica
    document->get_Pages()->idx_get(1)->AddStamp(textStamp);

    // Salvar documento de saída
    document->Save(_dataDir + outputFileName);
}
```

## Definir alinhamento para o objeto TextStamp

Adicionar marcas d'água a documentos PDF é um dos recursos frequentemente demandados e o Aspose.PDF para C++ é totalmente capaz de adicionar marcas d'água de imagem, bem como de texto. Temos uma classe chamada [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) que fornece o recurso de adicionar marcas de texto sobre o arquivo PDF. Recentemente, houve a necessidade de suportar o recurso de especificar o alinhamento do texto ao usar o objeto TextStamp. Portanto, para atender a esse requisito, introduzimos a propriedade TextAlignment na classe TextStamp. Usando esta propriedade, podemos especificar o alinhamento horizontal do texto.

Os seguintes trechos de código mostram um exemplo de como carregar um documento PDF existente e adicionar um TextStamp sobre ele.

```cpp
void DefineAlignmentTextStamp() {

    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);
    
    // instanciar objeto FormattedText com string de exemplo
    auto text = MakeObject<Aspose::Pdf::Facades::FormattedText>("This");

    // adicionar nova linha de texto ao FormattedText
    text->AddNewLineText(u"is sample");
    text->AddNewLineText(u"Center Aligned");
    text->AddNewLineText(u"TextStamp");
    text->AddNewLineText(u"Object");

    // criar objeto TextStamp usando FormattedText
    auto stamp = MakeObject<TextStamp>(text);
    // especificar o alinhamento horizontal da marca de texto como centralizado
    stamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    // especificar o alinhamento vertical da marca de texto como centralizado
    stamp->set_VerticalAlignment(VerticalAlignment::Center);
    // especificar o alinhamento horizontal do texto do TextStamp como centralizado
    stamp->set_TextAlignment(HorizontalAlignment::Center);
    // definir margem superior para o objeto de marca
    stamp->set_TopMargin(20);
    // adicionar marca a todas as páginas do arquivo PDF
    document->get_Pages()->idx_get(1)->AddStamp(stamp);

    // salvar documento de saída
    document->Save(_dataDir + outputFileName);
}
```

## Preencher Texto de Contorno como Carimbo em Arquivo PDF

Implementamos a configuração do modo de renderização para cenários de adição e edição de texto. Para renderizar texto de contorno, crie um objeto TextState e defina RenderingMode para TextRenderingMode.StrokeText e também selecione a cor para a propriedade StrokingColor. Depois, vincule o TextState ao carimbo usando o método BindTextState().

O seguinte trecho de código demonstra a adição de Texto de Contorno de Preenchimento:

```cpp
void FillStrokeTextAsStampInPDFFile() {

    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String inputFileName("AddTextStamp.pdf");
    String outputFileName("AddTextStamp_out.pdf");

    // Criar objeto TextState para transferir propriedades avançadas
    auto ts = MakeObject<TextState>();

    // Definir cor para o contorno
    ts->set_StrokingColor(Color::get_Gray());

    // Definir modo de renderização de texto
    ts->set_RenderingMode(TextRenderingMode::StrokeText);

    // Carregar um documento PDF de entrada
    auto fileStamp = MakeObject<Aspose::Pdf::Facades::PdfFileStamp>(MakeObject<Document>(_dataDir + inputFileName));

    auto stamp = MakeObject<Aspose::Pdf::Facades::Stamp>();

    auto formattedText = MakeObject<Aspose::Pdf::Facades::FormattedText>(u"PAID IN FULL", Color::get_Gray(), Aspose::Pdf::Facades::EncodingType::Winansi, true, 78);
    stamp->BindLogo(formattedText);

    // Vincular TextState
    stamp->BindTextState(ts);

    // Definir origem X,Y
    stamp->SetOrigin(100, 100);
    stamp->set_Opacity(5);
    stamp->set_BlendingSpace(Aspose::Pdf::Facades::BlendingColorSpace::DeviceRGB);
    stamp->set_Rotation(45.0F);
    stamp->set_IsBackground(false);

    // Adicionar Carimbo
    fileStamp->AddStamp(stamp);
    fileStamp->Save(_dataDir + outputFileName);
    fileStamp->Close();
}
```