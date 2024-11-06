---
title: PDF Multimedia Annotation using C++
linktitle: Multimedia Annotation
type: docs
weight: 40
url: es/cpp/multimedia-annotation/
description: Aspose.PDF for C++ le permite agregar, obtener y eliminar la anotación multimedia de su documento PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Agregar video, audio y contenido interactivo convierte los PDFs en herramientas de comunicación multidimensionales que aumentan el interés y la participación con sus documentos. Dicho contenido en archivos en formato PDF se llama Anotaciones Multimedia.

Las anotaciones en un documento PDF están contenidas en la colección de Anotaciones de un objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page). Esta colección contiene todas las anotaciones solo para esa página individual: cada página tiene su propia colección de Anotaciones. Para agregar una anotación a una página en particular, agréguela a la colección de Anotaciones de esa página usando el método Add.

Use la clase [ScreenAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.screen_annotation) en el espacio de nombres Aspose.PDF.InteractiveFeatures.Annotations para incluir archivos SWF como anotaciones en un documento PDF en su lugar. Una anotación de pantalla especifica una región de una página en la que se pueden reproducir clips de medios.

Cuando necesitas agregar un enlace de video externo en un documento PDF, puedes usar [MovieAnnotaiton](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.movie_annotation). Una Anotación de Película contiene gráficos animados y sonido para ser presentados en la pantalla de la computadora y a través de los altavoces.

Una [Sound Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.sound_annotation) deberá ser análoga a una anotación de texto excepto que, en lugar de una nota de texto, contiene sonido grabado desde el micrófono de la computadora o importado desde un archivo. Cuando la anotación se activa, el sonido se reproducirá. La anotación deberá comportarse como una anotación de texto en la mayoría de los aspectos, con un icono diferente (por defecto, un altavoz) para indicar que representa un sonido.

Sin embargo, cuando hay un requisito para incrustar medios dentro de un documento PDF, necesitas usar [RichMediaAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.rich_media_annotation).
## Añadir Anotación de Pantalla

El siguiente fragmento de código muestra cómo agregar una Anotación de Pantalla a un archivo PDF:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MultimediaAnnotations::AddScreenAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"input.swf";

    // Crear Anotación de Pantalla
    auto screenAnnotation = MakeObject<ScreenAnnotation>(page, MakeObject<Rectangle>(170, 190, 470, 380), mediaFile);
    page->get_Annotations()->Add(screenAnnotation);

    document->Save(_dataDir + u"sample_swf.pdf");
}
```

## Añadir Anotación de Sonido

El siguiente fragmento de código muestra cómo agregar una Anotación de Sonido a un archivo PDF:

```cpp
  void MultimediaAnnotations::AddSoundAnnotation()
{

    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    String mediaFile = _dataDir + u"file_example_WAV_1MG.wav";

    // Crear Anotación de Sonido
    auto soundAnnotation = MakeObject<SoundAnnotation>(page, new Rectangle(20, 700, 60, 740), mediaFile);
    soundAnnotation->set_Color(Color::get_Blue());
    soundAnnotation->set_Title(u"John Smith");
    soundAnnotation->set_Subject(u"Demostración de Anotación de Sonido");
    soundAnnotation->set_Popup(MakeObject<PopupAnnotation>(document));

    page->get_Annotations()->Add(soundAnnotation);

    document->Save(_dataDir + u"sample_wav.pdf");
}

```

## Añadir RichMediaAnnotation

El siguiente fragmento de código muestra cómo agregar RichMediaAnnotation a un archivo PDF:

```cpp
       void MultimediaAnnotations::AddRichMediaAnnotation()
{
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>();

    String pathToAdobeApp (u"C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins");
    auto page = document->get_Pages()->Add();

    // dar nombre a los datos de video. Estos datos se incrustarán en el documento con este
    // nombre y se referenciarán desde variables flash con este nombre.
    // videoName no debe contener la ruta al archivo; esto es más bien una "clave" para acceder
    // a los datos dentro del documento PDF

    String videoName (u"file_example_MP4_480_1_5MG.mp4");
    String posterName (u"file_example_MP4_480_1_5MG_poster.jpg");

    // también usamos una piel para el reproductor de video
    String skinName (u"SkinOverAllNoFullNoCaption.swf");

    auto rma = MakeObject<RichMediaAnnotation>(page, MakeObject<Rectangle>(100, 500, 300, 600));

    // aquí deberíamos especificar el flujo que contiene el código del reproductor de video
    rma->set_CustomPlayer(System::IO::File::OpenRead(pathToAdobeApp + u"Players\\" + u"Videoplayer.swf"));

    // componer la línea de variables flash para el reproductor. tenga en cuenta que diferentes reproductores
    // pueden tener diferentes formatos de la línea de variables flash.
    // Consulte la documentación para su reproductor.
    rma->set_CustomFlashVariables(u"source=" + videoName + u"&skin=" + skinName);

    // agregar el código de la piel.
    rma->AddCustomData(skinName, System::IO::File::OpenRead(pathToAdobeApp + u"SkinOverAllNoFullNoCaption.swf"));
    // establecer el póster para el video
    rma->SetPoster(System::IO::File::OpenRead(_dataDir + posterName));

    // establecer el contenido del video
    rma->SetContent(videoName, System::IO::File::OpenRead(_dataDir + videoName));

    // establecer el tipo de contenido (video)
    rma->set_Type(RichMediaAnnotation::ContentType::Video);

    // activar el reproductor al hacer clic
    rma->set_ActivateOn(RichMediaAnnotation::ActivationEvent::Click);

    // actualizar los datos de la anotación. Este método debe llamarse después de todas
    // las asignaciones/configuraciones. Este método inicializa la estructura de datos de la anotación
    // y incrusta los datos requeridos.
    rma->Update();

    // agregar la anotación en la página.
    page->get_Annotations()->Add(rma);

    document->Save(_dataDir + u"RichMediaAnnotation.pdf");
}
```

### Obtener MultimediaAnnotation

Por favor, intente usar el siguiente fragmento de código para Obtener MultimediaAnnotation del documento PDF.

```cpp
void MultimediaAnnotations::GetMultimediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Cargar el archivo PDF
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

### Eliminar MultimediaAnnotation

El siguiente fragmento de código muestra cómo Eliminar MultimediaAnnotation del archivo PDF.

```cpp
void MultimediaAnnotations::DeleteRichMediaAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Cargar el archivo PDF
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

## Añadir Anotación 3D

Hoy en día, los archivos PDF pueden contener una variedad de contenido además de texto y gráficos simples, incluyendo estructuras lógicas, elementos interactivos como anotaciones y campos de formulario, capas, multimedia (incluyendo contenido de video) y objetos 3D.

Dicho contenido 3D puede ser visto en un archivo PDF utilizando anotaciones 3D.

Esta sección muestra los pasos básicos para crear una anotación 3D en un documento PDF utilizando la biblioteca C++ de Aspose.PDF.

La anotación 3D se añade usando un modelo creado en el formato U3D.

1. Crear un nuevo [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document/)
1. Cargar los datos del modelo 3D deseado (en nuestro caso "Ring.u3d") para crear [PDF3DContent](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_content/)
1. Crear un objeto [3dArtWork](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.p_d_f3_d_artwork/) y enlazarlo al documento y al 3DContent
1. Ajustar el objeto pdf3dArtWork:

```cpp
void MultimediaAnnotation::Add3DAnnottaion()
{
    public static void Add3dAnnotation()
    {
        // Cargar el archivo PDF
        Document document = new Document();
        PDF3DContent pdf3DContent = new PDF3DContent(_dataDir + "Ring.u3d");
        PDF3DArtwork pdf3dArtWork = new PDF3DArtwork(document, pdf3DContent);
        pdf3dArtWork.setLightingScheme(new PDF3DLightingScheme(LightingSchemeType.CAD));
        pdf3dArtWork.setRenderMode(new PDF3DRenderMode(RenderModeType.Solid));

        var topMatrix = new Matrix3D(1, 0, 0, 0, -1, 0, 0, 0, -1, 0.10271, 0.08184, 0.273836);
        var frontMatrix = new Matrix3D(0, -1, 0, 0, 0, 1, -1, 0, 0, 0.332652, 0.08184, 0.085273);
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, topMatrix, 0.188563, "Top")); //1
        pdf3dArtWork.getViewArray().add(new PDF3DView(document, frontMatrix, 0.188563, "Left")); //2

        var page = document.getPages().add();

        var pdf3dAnnotation = new PDF3DAnnotation(page, new Rectangle(100, 500, 300, 700), pdf3dArtWork);
        pdf3dAnnotation.setBorder(new Border(pdf3dAnnotation));
        pdf3dAnnotation.setDefaultViewIndex(1);
        pdf3dAnnotation.setFlags(com.aspose.pdf.AnnotationFlags.NoZoom);
        pdf3dAnnotation.setName("Ring.u3d");
        //establecer imagen de vista previa si es necesario
        //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
        document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

        document.save(_dataDir + "sample_3d.pdf");
    }
}
```

Este ejemplo de código nos mostró tal modelo:

![3D Annotation demo](3d_demo.png)


## Añadir Anotación de Widget

Una Anotación de Widget representa la apariencia de los campos de formulario en un formulario PDF interactivo.

Desde PDF v 1.2 podemos usar Anotaciones de Widget. Estos son elementos de formulario interactivos que podemos añadir al PDF para facilitar la entrada, envío de información, o realizar alguna otra acción con el usuario. Aunque los widgets son un tipo especial de anotación, no podemos crearlos como anotaciones directamente, porque las anotaciones de widget son una representación gráfica de un campo de formulario en páginas específicas.

Cada campo de formulario para cada ubicación en el documento representa un Widget de Anotación. Los datos de anotación específicos de la ubicación para el widget se añaden a una página específica. Cada campo de formulario tiene varias opciones. Un botón puede ser un interruptor, casilla de verificación, o botón. El widget de selección puede ser un cuadro de lista o un cuadro combinado.

Aspose.PDF para C++ te permite añadir esta anotación utilizando la clase [Widget Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.widget_annotation/).

Para añadir un botón a la página necesitamos usar el siguiente fragmento de código:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;
using namespace Aspose::Pdf::Annotations;

void ExampleWidgetAnnotation::AddButton() {

    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto rect = MakeObject<Rectangle>(72, 748, 164, 768);

    auto printButton = MakeObject<ButtonField>(page, rect);
    printButton->set_AlternateName(u"Imprimir documento actual");
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

### Usando acciones de navegación de documentos

Este ejemplo muestra cómo crear 4 botones:

```cpp
void ExampleWidgetAnnotation::AddDocumentNavigationActions() {

    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"JSON Fundamenals.pdf");

    auto buttons = MakeArray<System::SmartPtr<ButtonField>>(4);
    auto alternateNames = MakeArray<String>({ u"Ir a la primera página", u"Ir a la página anterior", u"Ir a la siguiente página", u"Ir a la última página" });
    auto normalCaptions = MakeArray<String>({ u"Primera", u"Anterior", u"Siguiente", u"Última" });
    PredefinedAction actions[] = { PredefinedAction::FirstPage, PredefinedAction::PrevPage,
                                    PredefinedAction::NextPage, PredefinedAction::LastPage };
    auto clrBorder = System::Drawing::Color::FromArgb(255, 0, 255, 0);
    auto clrBackGround = System::Drawing::Color::Color::FromArgb(255, 0, 96, 70);

// Debemos crear los botones sin adjuntarlos a la página.

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

// Debemos duplicar este array de botones en cada página del documento.

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

### Eliminar Anotación de Widget

```cpp
void ExampleWidgetAnnotation::DeleteWidgetAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Cargar el archivo PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_widgetannot.pdf");
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(MakeObject<ButtonField>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto buttonFields = annotationSelector->get_Selected();

    // eliminar anotaciones
    for (auto wa : buttonFields) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_widgetannot_del.pdf");
}
```