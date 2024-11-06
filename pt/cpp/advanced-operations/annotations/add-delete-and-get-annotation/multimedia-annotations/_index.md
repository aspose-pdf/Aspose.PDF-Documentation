---
title: Anotação Multimídia em PDF usando C++
linktitle: Anotação Multimídia
type: docs
weight: 40
url: pt/cpp/multimedia-annotation/
description: Aspose.PDF para C++ permite adicionar, obter e excluir a anotação multimídia do seu documento PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Adicionar vídeo, áudio e conteúdo interativo transforma PDFs em ferramentas de comunicação multidimensionais que aumentam o interesse e o engajamento com seus documentos. Esse tipo de conteúdo em arquivos no formato PDF é chamado de Anotações Multimídia.

Anotações em um documento PDF estão contidas na coleção de Anotações de um objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). Esta coleção contém todas as anotações apenas para aquela página individual: cada página tem sua própria coleção de Anotações. Para adicionar uma anotação a uma página específica, adicione-a à coleção de Anotações dessa página usando o método Add.

Use a classe [ScreenAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.screen_annotation) no namespace Aspose.PDF.InteractiveFeatures.Annotations para incluir arquivos SWF como anotações em um documento PDF. Uma anotação de tela especifica uma região de uma página na qual clipes de mídia podem ser reproduzidos.

Quando você precisa adicionar um link de vídeo externo em um documento PDF, pode usar [MovieAnnotaiton](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.movie_annotation). Uma Anotação de Filme contém gráficos animados e som para serem apresentados na tela do computador e através dos alto-falantes.

Uma [Sound Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.sound_annotation) deve ser análoga a uma anotação de texto, exceto que em vez de uma nota de texto, contém som gravado do microfone do computador ou importado de um arquivo. Quando a anotação é ativada, o som deve ser reproduzido. A anotação deve se comportar como uma anotação de texto na maioria dos aspectos, com um ícone diferente (por padrão, um alto-falante) para indicar que representa um som.

No entanto, quando há a necessidade de incorporar mídia dentro do documento PDF, você precisa usar [RichMediaAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.rich_media_annotation).
## Adicionar Anotação de Tela

O seguinte trecho de código mostra como adicionar Anotação de Tela a um arquivo PDF:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MultimediaAnnotations::AddScreenAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"input.swf";

    // Criar Anotação de Tela
    auto screenAnnotation = MakeObject<ScreenAnnotation>(page, MakeObject<Rectangle>(170, 190, 470, 380), mediaFile);
    page->get_Annotations()->Add(screenAnnotation);

    document->Save(_dataDir + u"sample_swf.pdf");
}
```

## Adicionar Anotação de Som

O seguinte trecho de código mostra como adicionar Anotação de Som a um arquivo PDF:

```cpp
  void MultimediaAnnotations::AddSoundAnnotation()
{

    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"file_example_WAV_1MG.wav";

    // Criar Anotação de Som
    auto soundAnnotation = MakeObject<SoundAnnotation>(page, new Rectangle(20, 700, 60, 740), mediaFile);
    soundAnnotation->set_Color(Color::get_Blue());
    soundAnnotation->set_Title(u"John Smith");
    soundAnnotation->set_Subject(u"Demo de Anotação de Som");
    soundAnnotation->set_Popup(MakeObject<PopupAnnotation>(document));

    page->get_Annotations()->Add(soundAnnotation);

    document->Save(_dataDir + u"sample_wav.pdf");
}

```

## Adicionar RichMediaAnnotation

O trecho de código a seguir mostra como adicionar RichMediaAnnotation a um arquivo PDF:

```cpp
       void MultimediaAnnotations::AddRichMediaAnnotation()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();

    String pathToAdobeApp (u"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins");
    auto page = document->get_Pages()->Add();

    // dê um nome aos dados do vídeo. Esses dados serão incorporados ao documento com este
    // nome e referenciados a partir das variáveis flash por este nome.
    // videoName não deve conter o caminho para o arquivo; este é mais um "key" para acessar
    // dados dentro do documento PDF

    String videoName (u"file_example_MP4_480_1_5MG.mp4");
    String posterName (u"file_example_MP4_480_1_5MG_poster.jpg");

    // também usamos uma skin para o player de vídeo
    String skinName (u"SkinOverAllNoFullNoCaption.swf");

    auto rma = MakeObject<RichMediaAnnotation>(page, MakeObject<Rectangle>(100, 500, 300, 600));

    // aqui devemos especificar o stream contendo o código do player de vídeo
    rma->set_CustomPlayer(System::IO::File::OpenRead(pathToAdobeApp + u"Players\\" + u"Videoplayer.swf"));

    // compor linha de variáveis flash para o player. por favor, note que players diferentes
    // podem ter formatos diferentes para a linha de variáveis flash.
    // Consulte a documentação para o seu player.
    rma->set_CustomFlashVariables(u"source=" + videoName + u"&skin=" + skinName);

    // adicionar código da skin.
    rma->AddCustomData(skinName, System::IO::File::OpenRead(pathToAdobeApp + u"SkinOverAllNoFullNoCaption.swf"));
    // definir poster para o vídeo
    rma->SetPoster(System::IO::File::OpenRead(_dataDir + posterName));

    // definir conteúdo do vídeo
    rma->SetContent(videoName, System::IO::File::OpenRead(_dataDir + videoName));

    // definir tipo de conteúdo (vídeo)
    rma->set_Type(RichMediaAnnotation::ContentType::Video);

    // ativar player ao clicar
    rma->set_ActivateOn(RichMediaAnnotation::ActivationEvent::Click);

    // atualizar dados da anotação. Este método deve ser chamado após todas as
    // atribuições/configurações. Este método inicializa a estrutura de dados da anotação
    // e incorpora os dados necessários.
    rma->Update();

    // adicionar anotação na página.
    page->get_Annotations()->Add(rma);

    document->Save(_dataDir + u"RichMediaAnnotation.pdf");
}
```

### Obter MultimediaAnnotation

Por favor, tente usar o seguinte trecho de código para obter MultimediaAnnotation do documento PDF.

```cpp
void MultimediaAnnotations::GetMultimediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        Console::WriteLine(u"{0} {1}", ma->get_AnnotationType(), ma->get_Rect());
    }
}
```

### Excluir MultimediaAnnotation

O seguinte trecho de código mostra como excluir MultimediaAnnotation do arquivo PDF.

```cpp
void MultimediaAnnotations::DeleteRichMediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"RichMediaAnnotation.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<RichMediaAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto mediaAnnotations = annotationSelector->get_Selected();

    for (auto ma : mediaAnnotations) {
        page->get_Annotations()->Delete(ma);
    }
    document->Save(_dataDir + u"RichMediaAnnotation_del.pdf");
}
```

## Adicionar Anotação 3D

Hoje em dia, arquivos PDF podem conter uma variedade de conteúdos além de texto e gráficos simples, incluindo estruturas lógicas, elementos interativos como anotações e campos de formulário, camadas, multimídia (incluindo conteúdo de vídeo) e objetos 3D.

Esse conteúdo 3D pode ser visualizado em um arquivo PDF usando anotações 3D.

Esta seção mostra os passos básicos para criar uma anotação 3D em um documento PDF usando a biblioteca C++ do Aspose.PDF.

A anotação 3D é adicionada usando um modelo criado no formato U3D.

1. Crie um novo [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/)
1. Carregue os dados do modelo 3D desejado (neste caso "Ring.u3d") para criar [PDF3DContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_content/)
1. Crie um objeto [3dArtWork](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_artwork/) e vincule-o ao documento e ao 3DContent
1. Ajuste o objeto pdf3dArtWork:

```cpp
void MultimediaAnnotation::Add3DAnnottaion()
{
    public static void Add3dAnnotation()
    {
        // Carregar o arquivo PDF
        Document document = new Document();
        PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
        PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
        pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        var topMatrix = new Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Topo")); //1
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Esquerda")); //2

        var page = document.getPages().add();

        var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
        pdf3dAnnotation.setDefaultViewIndex(1);
        pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
        pdf3dAnnotation.setName("Ring.u3d");
        //definir imagem de pré-visualização, se necessário
        //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
        document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

        document.save(_dataDir + "sample_3d.pdf");
    }
}
```

Este exemplo de código nos mostrou tal modelo:

![Demonstração de Anotação 3D](3d_demo.png)


## Adicionar Anotação de Widget

Uma Anotação de Widget representa a aparência dos campos de formulário em um formulário PDF interativo.

Desde o PDF v 1.2 podemos usar Anotações de Widget. Estes são elementos de formulário interativos que podemos adicionar ao PDF para facilitar a entrada, envio de informações ou realizar alguma outra ação com o usuário. Embora widgets sejam um tipo especial de anotação, não podemos criá-los como anotações diretamente, porque anotações de widget são uma representação gráfica de um campo de formulário em páginas específicas.

Cada campo de formulário para cada local no documento representa um Widget de Anotação. Dados de anotação específicos de local para o widget são adicionados a uma página específica. Cada campo de formulário possui várias opções. Um botão pode ser um alternador, uma caixa de seleção ou um botão. O widget de seleção pode ser uma caixa de lista ou uma caixa de combinação.

Aspose.PDF para C++ permite que você adicione essa anotação usando a classe [Widget Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.widget_annotation/).

Para adicionar um botão à página, precisamos usar o próximo trecho de código:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;

void ExampleWidgetAnnotation::AddButton() {

    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto rect = MakeObject<Rectangle>(72, 748, 164, 768);

    auto printButton = MakeObject<ButtonField>(page, rect);
    printButton->set_AlternateName(u"Imprimir documento atual");
    printButton->set_Color(Color::get_Black());
    printButton->set_PartialName(u"printBtn1");
    printButton->set_NormalCaption(u"Imprimir Documento");

    auto border = MakeObject<Border>(printButton);
    border->set_Style(BorderStyle::Solid);
    border->set_Width(2);

    printButton->set_Border(border);
    printButton->get_Characteristics()->set_Border(System::Drawing::Color::FromArgb(255, 0, 0, 255));
    printButton->get_Characteristics()->set_Background(System::Drawing::Color::FromArgb(255, 0, 191, 255));
    auto wa = System::DynamicCast<Field>(printButton);
    document->get_Form()->Add(wa);

    document->Save(_dataDir + u"sample_widgetannot.pdf");
}
```

### Usando ações de navegação de documentos

Este exemplo mostra como criar 4 botões:

```cpp
void ExampleWidgetAnnotation::AddDocumentNavigationActions() {

    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"JSON Fundamenals.pdf");

    auto buttons = MakeArray<System::SmartPtr<ButtonField>>(4);
    auto alternateNames = MakeArray<String>({ u"Ir para a primeira página", u"Ir para a página anterior", u"Ir para a próxima página", u"Ir para a última página" });
    auto normalCaptions = MakeArray<String>({ u"Primeira", u"Anterior", u"Próxima", u"Última" });
    PredefinedAction actions[] = { PredefinedAction::FirstPage, PredefinedAction::PrevPage,
                                    PredefinedAction::NextPage, PredefinedAction::LastPage };
    auto clrBorder = System::Drawing::Color::FromArgb(255, 0, 255, 0);
    auto clrBackGround = System::Drawing::Color::Color::FromArgb(255, 0, 96, 70);

// Devemos criar os botões sem anexá-los à página.

    for (int i = 0; i < 4; i++) {
        buttons[i] = MakeObject<ButtonField>(document, MakeObject<Rectangle>(32 + i * 80, 28, 104 + i * 80, 68));
        buttons[i]->set_AlternateName(alternateNames[i]);
        buttons[i]->set_Color(Color::get_White());
        buttons[i]->set_NormalCaption(normalCaptions[i]);
        buttons[i]->set_OnActivated(new NamedAction(actions[i]));
        auto border = MakeObject<Border>(buttons[i]);
        border->set_Style(BorderStyle::Solid);
        border->set_Width(2);
        buttons[i]->set_Border(border);
        buttons[i]->get_Characteristics()->set_Border(clrBorder);
        buttons[i]->get_Characteristics()->set_Background(clrBackGround);
    }

// Devemos duplicar este array de botões em cada página do documento.

    for (int pageIndex = 1; pageIndex <= 4; pageIndex++)
        for (int i = 0; i < 4; i++)
            document->get_Form()->Add(buttons[i], String::Format(u"btn{0}_{1}", pageIndex,(i + 1)), pageIndex);

    document->get_Form()->idx_get(u"btn1_1")->set_ReadOnly(true);
    document->get_Form()->idx_get(u"btn1_2")->set_ReadOnly(true);

    document->get_Form()->idx_get(String::Format(u"btn{0}_3", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->get_Form()->idx_get(String::Format(u"btn{0}_4", document->get_Pages()->get_Count()))->set_ReadOnly(true);
    document->Save(_dataDir + u"sample_widgetannot_2.pdf");
}
```

### Excluir Anotação de Widget

```cpp
void ExampleWidgetAnnotation::DeleteWidgetAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Carregar o arquivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_widgetannot.pdf");
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(MakeObject<ButtonField>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto buttonFields = annotationSelector->get_Selected();

    // excluir anotações
    for (auto wa : buttonFields) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_widgetannot_del.pdf");
}
```