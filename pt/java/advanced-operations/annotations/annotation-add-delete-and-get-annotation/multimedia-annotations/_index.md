---
title: Anotação Multimídia em PDF
linktitle: Anotação Multimídia
type: docs
weight: 40
url: /pt/java/multimedia-annotation/
description: Aspose.PDF para Java permite adicionar, obter e excluir a anotação multimídia do seu documento PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Anotações em um documento PDF estão contidas na coleção Annotations de um objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page). Esta coleção contém todas as anotações apenas para aquela página individual: cada página tem sua própria coleção Annotations. Para adicionar uma anotação a uma página específica, adicione-a à coleção Annotations dessa página usando o método Add.

Use a classe [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/ScreenAnnotation) no namespace Aspose.PDF.InteractiveFeatures.Annotations para incluir arquivos SWF como anotações em um documento PDF.
 Uma anotação de tela especifica uma região de uma página na qual clipes de mídia podem ser reproduzidos.

Quando você precisa adicionar um link de vídeo externo em um documento PDF, pode usar [MovieAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/MovieAnnotation). Uma Anotação de Filme contém gráficos animados e som para serem apresentados na tela do computador e através dos alto-falantes.

Uma [Sound Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation) deve ser análoga a uma anotação de texto, exceto que em vez de uma nota de texto, ela contém som gravado do microfone do computador ou importado de um arquivo. Quando a anotação é ativada, o som deve ser reproduzido. A anotação deve se comportar como uma anotação de texto na maioria das maneiras, com um ícone diferente (por padrão, um alto-falante) para indicar que representa um som.

No entanto, quando há a necessidade de incorporar mídia dentro de um documento PDF, você precisa usar [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/RichMediaAnnotation).
Os seguintes métodos/propriedades da classe RichMediaAnnotation podem ser utilizados.

- Stream CustomPlayer { set; }: Permite definir o player usado para reproduzir o vídeo.
- string CustomFlashVariables { set; }: Permite definir variáveis que são passadas para a aplicação flash. Esta linha é um conjunto de pares “key=value” que são separados por ‘&'.
- void AddCustomData(string name, Stream data): Adiciona dados adicionais para o player. Por exemplo source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set; }: Evento ativa o player; valores possíveis são Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Define os dados de vídeo/áudio a serem reproduzidos.
- void Update(): Cria uma estrutura de dados da anotação. Este método deve ser chamado por último.
- void SetPoster(Stream): Define o pôster do vídeo, ou seja, a imagem mostrada quando o player não está ativo.

## Adicionar Anotação de Tela

O trecho de código a seguir mostra como adicionar uma Anotação de Tela a um arquivo PDF:

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;
import com.aspose.pdf.*;

public class ExampleMultimediaAnnotation {

    // O caminho para o diretório dos documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddScreenAnnotation() {
        // Carrega o arquivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "input.swf";
        // Cria Anotação de Tela
        ScreenAnnotation screenAnnotation = new ScreenAnnotation(page, new Rectangle(170, 190, 470, 380), mediaFile);
        page.getAnnotations().add(screenAnnotation);

        document.save(_dataDir + "sample_swf.pdf");
    }
}
```


## Adicionar Anotação de Som

O snippet de código a seguir mostra como adicionar uma Anotação de Som a um arquivo PDF:

```java
          public static void AddSoundAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "file_example_WAV_1MG.wav";

        // Criar Anotação de Som
        SoundAnnotation soundAnnotation = new SoundAnnotation(page, new Rectangle(20, 700, 60, 740), mediaFile);
        soundAnnotation.setColor(Color.getBlue());
        soundAnnotation.setTitle("John Smith");
        soundAnnotation.setSubject("Demonstração de Anotação de Som");
        soundAnnotation.setPopup(new PopupAnnotation(document));

        page.getAnnotations().add(soundAnnotation);

        document.save(_dataDir + "sample_wav.pdf");
    }
```

## Adicionar RichMediaAnnotation

O snippet de código a seguir mostra como adicionar RichMediaAnnotation a um arquivo PDF:

```java
     public static void AddRichMediaAnnotation() throws FileNotFoundException {
        Document doc = new Document();
        var pathToAdobeApp = "C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";
        Page page = doc.getPages().add();

        // dar nome aos dados de vídeo. Esses dados serão incorporados ao documento com este
        // nome e referenciados a partir das variáveis flash por este nome.
        // videoName não deve conter o caminho para o arquivo; isso é mais um "chave" para acessar
        // os dados dentro do documento PDF

        String videoName = "file_example_MP4_480_1_5MG.mp4";
        String posterName = "file_example_MP4_480_1_5MG_poster.jpg";

        // também usamos skin para o reprodutor de vídeo
        String skinName = "SkinOverAllNoFullNoCaption.swf";

        RichMediaAnnotation rma = new RichMediaAnnotation(page, new Rectangle(100, 500, 300, 600));

        // aqui devemos especificar o stream contendo o código do reprodutor de vídeo
        rma.setCustomPlayer(new FileInputStream(pathToAdobeApp + "Players" + "Videoplayer.swf"));

        // compor a linha de variáveis flash para o reprodutor. por favor, note que reprodutores diferentes
        // podem ter formato diferente para a linha de variáveis flash.
        // Consulte a documentação para o seu reprodutor.
        rma.setCustomFlashVariables("source=" + videoName + "&skin=" + skinName);

        // adicionar o código do skin.
        rma.addCustomData(skinName, new FileInputStream(pathToAdobeApp + "SkinOverAllNoFullNoCaption.swf"));
        // definir poster para o vídeo
        rma.setPoster(new FileInputStream(_dataDir + posterName));

        // definir conteúdo de vídeo
        rma.setContent(videoName, new FileInputStream(_dataDir + videoName));

        // definir tipo do conteúdo (vídeo)
        rma.setType(RichMediaAnnotation.ContentType.Video);

        // ativar reprodutor por clique
        rma.setActivateOn(RichMediaAnnotation.ActivationEvent.Click);

        // atualizar dados da anotação. Este método deve ser chamado após todas
        // atribuições/configuração. Este método inicializa a estrutura de dados da anotação
        // e incorpora os dados necessários.
        rma.update();

        // adicionar anotação na página.
        page.getAnnotations().add(rma);

        doc.save(_dataDir + "RichMediaAnnotation.pdf");
    }
```


## Obter MultimediaAnnotation

Por favor, tente usar o seguinte trecho de código para Obter MultimediaAnnotation de um documento PDF.

```java
public static void GetMultimediaAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();

        for (Annotation ma : mediaAnnotations) {
            System.out.println(ma.getAnnotationType() + " " + ma.getRect());
        }
    }
```

## Deletar MultimediaAnnotation

O seguinte trecho de código mostra como Deletar MultimediaAnnotation de um arquivo PDF.

```java
    public static void DeletePolyAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "RichMediaAnnotation.pdf");

        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(
                new RichMediaAnnotation(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> mediaAnnotations = annotationSelector.getSelected();
        for (Annotation ma : mediaAnnotations) {
            page.getAnnotations().delete(ma);
        }
        document.save(_dataDir + "RichMediaAnnotation_del.pdf");
    }
```


## Adicionar Anotações de Widget

Formulários interativos utilizam [Anotações de Widget](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/WidgetAnnotation) para representar a aparência dos campos e gerenciar interações do usuário. Usamos esses elementos de formulário que adicionamos a um PDF para facilitar a entrada, envio de informações ou realizar algumas outras interações do usuário.

As Anotações de Widget são uma representação gráfica de um campo de formulário em páginas específicas, portanto, não podemos criá-las diretamente como uma anotação.

Cada Anotação de Widget terá gráficos apropriados (aparência) dependendo de seu tipo. Após a criação, certos aspectos visuais podem ser alterados, como estilo de borda e cor de fundo. Outras propriedades, como cor do texto e fonte, podem ser alteradas através do campo, uma vez anexadas a um.

Em alguns casos, você pode querer que um campo apareça em mais de uma página, repetindo o mesmo valor.
 No caso, campos que normalmente têm apenas um widget podem ter múltiplos widgets anexados: um TextField, ListBox, ComboBox e CheckBox geralmente têm exatamente um, enquanto o RadioGroup tem múltiplos widgets, um para cada botão de rádio. Alguém preenchendo o formulário pode usar qualquer um desses widgets para atualizar o valor do campo, e isso é refletido em todos os outros widgets também.

Cada campo de formulário para cada lugar no documento representa uma Anotação de Widget. Os dados específicos de localização da Anotação de Widget são adicionados à página em particular. Cada campo de formulário tem várias variações. Um botão pode ser um botão de rádio, um checkbox ou um botão de pressão. Um widget de escolha pode ser uma caixa de lista ou uma caixa de combinação.

Neste exemplo, aprenderemos como adicionar botões de pressão para navegação no documento.

## Adicionar Botão ao Documento

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWidgetAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddButton()
    {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        Rectangle rect = new Rectangle(72, 748, 164, 768);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Imprimir documento atual");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setNormalCaption("Imprimir Documento");

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);

        printButton.setBorder(border);
        printButton.getCharacteristics().setBorder(Color.fromArgb(255, 0, 0, 255));
        printButton.getCharacteristics().setBackground(Color.fromArgb(255, 0, 191, 255));
        document.getForm().add(printButton);

        document.save(_dataDir + "sample_textannot.pdf");
    }
}
```

Este botão possui borda e define um fundo. Também definimos um nome de botão (Name), uma dica de ferramenta (AlternateName), uma legenda (NormalCaption) e uma cor para o texto da legenda (Color).

## Usando ações de navegação no documento

Existe um exemplo mais complexo do uso de Anotações de Widget - navegação de documento em documento PDF. Isso pode ser necessário para preparar uma apresentação de documento PDF.

Este exemplo mostra como criar 4 botões:

```java
public static void AddDocumentNavigationActions() {
// Carregar o arquivo PDF
Document document = new Document(_dataDir + "JSON Fundamenals.pdf");

ButtonField[] buttons = new ButtonField[4];
String[] alternateNames = { "Ir para a primeira página", "Ir para a página anterior", "Ir para a próxima página", "Ir para a última página" };
String[] normalCaptions = { "Primeira", "Anterior", "Próxima", "Última" };
int[] actions = { PredefinedAction.FirstPage, PredefinedAction.PrevPage, PredefinedAction.NextPage,
PredefinedAction.LastPage };
Color clrBorder = Color.fromArgb(255, 0, 255, 0);
Color clrBackGround = Color.fromArgb(255, 0, 96, 70);

for (int i = 0; i < 4; i++) {
buttons[i] = new ButtonField(document, new Rectangle(32 + i * 80, 28, 104 + i * 80, 68));
buttons[i].setAlternateName(alternateNames[i]);
buttons[i].setColor(Color.getWhite());
buttons[i].setNormalCaption(normalCaptions[i]);
buttons[i].setOnActivated(new NamedAction(actions[i]));
Border border = new Border(buttons[i]);
border.setStyle(BorderStyle.Solid);
border.setWidth(2);
buttons[i].setBorder(border);
buttons[i].getCharacteristics().setBorder(clrBorder);
buttons[i].getCharacteristics().setBackground(clrBackGround);
}

for (int pageIndex = 1; pageIndex <= 1; pageIndex++)
for (int i = 0; i < 4; i++)
document.getForm().add(buttons[i], "btn" + pageIndex + "_" + (i + 1), pageIndex);

document.getForm().get("btn1_1").setReadOnly(true);
document.getForm().get("btn1_2").setReadOnly(true);

document.getForm().get("btn" + document.getPages().size() + "_3").setReadOnly(true);
document.getForm().get("btn" + document.getPages().size() + "_4").setReadOnly(true);
document.save(_dataDir + "sample_widgetannot_2.pdf");
}
```


## Como deletar Anotação de Widget

Aspose.PDF para Java tem regras para remover anotações do seu arquivo:

```java
public static void DeleteWidgetAnnotation() {
        // Carregar o arquivo PDF
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // Filtrar anotações usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(new ButtonField(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> buttonFields = annotationSelector.getSelected();

        // deletar anotações
        for (Annotation wa : buttonFields) {
            page.getAnnotations().delete(wa);
        }
        document.save(_dataDir + "sample_widgetannot_del.pdf");
    }
```

Nos documentos PDF, você pode visualizar e gerenciar conteúdo 3D de alta qualidade criado com software de CAD 3D ou modelagem 3D e incorporado no documento PDF.
 Pode girar elementos 3D em todas as direções como se estivesse segurando-os em suas mãos.

Por que você precisa de uma exibição 3D de imagens?

Nos últimos anos, a tecnologia fez grandes avanços em todas as áreas graças à impressão 3D. As tecnologias de impressão 3D podem ser aplicadas para ensinar habilidades tecnológicas em construção, engenharia mecânica, design como a ferramenta principal. Essas tecnologias, graças ao surgimento de dispositivos de impressão pessoal, podem contribuir para a introdução de novas formas de organização do processo educacional, aumentar a motivação e a formação das competências necessárias de graduados e professores.

A principal tarefa do modelamento 3D é a ideia de um objeto futuro ou objeto porque, para liberar um objeto, é necessário entender suas características de design em todos os detalhes para a regeneração sucessiva em design industrial ou arquitetura.

## Adicionar Anotação 3D

A anotação 3D é adicionada usando um modelo criado no formato U3D com Aspose.PDF para Java
1. Crie um novo [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Carregue os dados do modelo 3D desejado (no nosso caso "Ring.u3d") para criar [PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PDF3DContent)
1. Crie um objeto [3dArtWork](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DArtwork) e vincule-o ao documento e ao 3DContent
1. Ajuste o objeto pdf3dArtWork:

    - 3DLightingScheme - (nós definiremos `CAD` no exemplo)
    - 3DRenderMode - (nós definiremos `Solid` no exemplo)
    - Preencha `ViewArray`, crie pelo menos uma [3D View](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DView) e adicione-a ao array.

1. Defina 3 parâmetros básicos na anotação:
    - a `page` na qual a anotação será colocada,
    - o `rectangle`, dentro do qual a anotação,
    - e o objeto `3dArtWork`.
1. Para uma melhor apresentação do objeto 3D, defina a moldura da borda
1. Defina a vista padrão (por exemplo - TOP)

1. Adicione alguns parâmetros adicionais: nome, pôster de visualização etc.
1. Adicione Anotação à [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)
1. Salve o resultado

## Exemplo

Por favor, verifique o seguinte trecho de código para adicionar Anotação 3D.

```java
    public class Example3DAnnotation
    {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";
    public static void Add3dAnnotation()
    {
    // Carregar o arquivo PDF
    Document document = new Document();
    PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
    PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
    pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
    pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

    var topMatrix = new Matrix3D(1,0,0,0,-1,0,0,0,-1,0.10271,0.08184,0.273836);
    var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
    pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

    var page = document.getPages().add();

    var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
    pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
    pdf3dAnnotation.setDefaultViewIndex(1);
    pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
    pdf3dAnnotation.setName("Ring.u3d");
    //definir imagem de visualização se necessário
    //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
    document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

    document.save(_dataDir+"sample_3d.pdf");
    }
}
```


This code example mostrou-nos tal modelo:

![3D Annotation demo](3d_demo.png)