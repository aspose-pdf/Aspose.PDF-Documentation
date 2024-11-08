---
title: Anotación Multimedia en PDF 
linktitle: Anotación Multimedia
type: docs
weight: 40
url: /es/java/multimedia-annotation/
description: Aspose.PDF para Java le permite agregar, obtener y eliminar la anotación multimedia de su documento PDF.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Las anotaciones en un documento PDF están contenidas en la colección de Anotaciones de un objeto [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page). Esta colección contiene todas las anotaciones solo para esa página individual: cada página tiene su propia colección de Anotaciones. Para agregar una anotación a una página en particular, agréguela a la colección de Anotaciones de esa página usando el método Add.

Utilice la clase [ScreenAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/ScreenAnnotation) en el espacio de nombres Aspose.PDF.InteractiveFeatures.Annotations para incluir archivos SWF como anotaciones en un documento PDF en su lugar.
 Una anotación de pantalla especifica una región de una página sobre la cual se pueden reproducir clips multimedia.

Cuando necesitas agregar un enlace de video externo en un documento PDF, puedes usar [MovieAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/MovieAnnotation). Una Anotación de Película contiene gráficos animados y sonido para ser presentados en la pantalla de la computadora y a través de los altavoces.

Una [Sound Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/soundannotation) será análoga a una anotación de texto, excepto que en lugar de una nota de texto, contiene sonido grabado desde el micrófono de la computadora o importado desde un archivo. Cuando se activa la anotación, el sonido se reproducirá. La anotación se comportará como una anotación de texto en la mayoría de los aspectos, con un icono diferente (por defecto, un altavoz) para indicar que representa un sonido.

Sin embargo, cuando hay un requisito para incrustar medios dentro de un documento PDF, necesitas usar [RichMediaAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/RichMediaAnnotation).
Los siguientes métodos/propiedades de la clase RichMediaAnnotation pueden ser utilizados.

- Stream CustomPlayer { set; }: Permite establecer el reproductor utilizado para reproducir video.
- string CustomFlashVariables { set; }: Permite establecer variables que se pasan a la aplicación flash. Esta línea es un conjunto de pares “key=value” que están separados con ‘&'.
- void AddCustomData(string name, Stream data): Añadir datos adicionales para el reproductor. Por ejemplo source=video.mp4&autoPlay=true&scale=100
- ActivationEvent ActivateOn { get; set}: Evento activa el reproductor; los valores posibles son Click, PageOpen, PageVisible
- void SetContent(Stream stream, string name): Establecer datos de video/audio para ser reproducidos.
- void Update(): Crear una estructura de datos de la anotación. Este método debe ser llamado al final
- void SetPoster(Stream): Establecer el póster del video, es decir, la imagen mostrada cuando el reproductor no está activo

## Añadir Anotación de Pantalla

El siguiente fragmento de código muestra cómo añadir una Anotación de Pantalla a un archivo PDF:

```java
package com.aspose.pdf.examples;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;
import com.aspose.pdf.*;

public class ExampleMultimediaAnnotation {

    // La ruta al directorio de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddScreenAnnotation() {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "input.swf";
        // Crear Anotación de Pantalla
        ScreenAnnotation screenAnnotation = new ScreenAnnotation(page, new Rectangle(170, 190, 470, 380), mediaFile);
        page.getAnnotations().add(screenAnnotation);

        document.save(_dataDir + "sample_swf.pdf");
    }
}
```


## Agregar Anotación de Sonido

El siguiente fragmento de código muestra cómo agregar una anotación de sonido a un archivo PDF:

```java
          public static void AddSoundAnnotation() {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        String mediaFile = _dataDir + "file_example_WAV_1MG.wav";

        // Crear Anotación de Sonido
        SoundAnnotation soundAnnotation = new SoundAnnotation(page, new Rectangle(20, 700, 60, 740), mediaFile);
        soundAnnotation.setColor(Color.getBlue());
        soundAnnotation.setTitle("John Smith");
        soundAnnotation.setSubject("Demostración de Anotación de Sonido");
        soundAnnotation.setPopup(new PopupAnnotation(document));

        page.getAnnotations().add(soundAnnotation);

        document.save(_dataDir + "sample_wav.pdf");
    }
```

## Agregar RichMediaAnnotation

El siguiente fragmento de código muestra cómo agregar RichMediaAnnotation a un archivo PDF:

```java
     public static void AddRichMediaAnnotation() throws FileNotFoundException {
        Document doc = new Document();
        var pathToAdobeApp = "C:\\Program Files (x86)\\Adobe\\Acrobat 2017\\Acrobat\\Multimedia Skins";
        Page page = doc.getPages().add();

        // dar nombre a los datos del video. Estos datos se incrustarán en el documento con este
        // nombre y se referenciarán desde variables flash por este nombre.
        // videoName no debe contener la ruta al archivo; esto es más bien una "clave" para acceder
        // a los datos dentro del documento PDF

        String videoName = "file_example_MP4_480_1_5MG.mp4";
        String posterName = "file_example_MP4_480_1_5MG_poster.jpg";

        // también usamos skin para el reproductor de video
        String skinName = "SkinOverAllNoFullNoCaption.swf";

        RichMediaAnnotation rma = new RichMediaAnnotation(page, new Rectangle(100, 500, 300, 600));

        // aquí deberíamos especificar el flujo que contiene el código del reproductor de video
        rma.setCustomPlayer(new FileInputStream(pathToAdobeApp + "Players" + "Videoplayer.swf"));

        // componer línea de variables flash para el reproductor. tenga en cuenta que diferentes reproductores
        // pueden tener diferente formato de la línea de variables flash.
        // Consulte la documentación para su reproductor.
        rma.setCustomFlashVariables("source=" + videoName + "&skin=" + skinName);

        // agregar código de skin.
        rma.addCustomData(skinName, new FileInputStream(pathToAdobeApp + "SkinOverAllNoFullNoCaption.swf"));
        // establecer póster para el video
        rma.setPoster(new FileInputStream(_dataDir + posterName));

        // establecer contenido del video
        rma.setContent(videoName, new FileInputStream(_dataDir + videoName));

        // establecer tipo de contenido (video)
        rma.setType(RichMediaAnnotation.ContentType.Video);

        // activar reproductor por clic
        rma.setActivateOn(RichMediaAnnotation.ActivationEvent.Click);

        // actualizar datos de la anotación. Este método debe ser llamado después de todas
        // las asignaciones/configuraciones. Este método inicializa la estructura de datos de la anotación
        // e incrusta los datos necesarios.
        rma.update();

        // agregar anotación en la página.
        page.getAnnotations().add(rma);

        doc.save(_dataDir + "RichMediaAnnotation.pdf");
    }
```


## Obtener MultimediaAnnotation

Por favor intente usar el siguiente fragmento de código para obtener MultimediaAnnotation del documento PDF.

```java
public static void GetMultimediaAnnotation() {
        // Cargar el archivo PDF
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

## Eliminar MultimediaAnnotation

El siguiente fragmento de código muestra cómo eliminar MultimediaAnnotation del archivo PDF.

```java
    public static void DeletePolyAnnotation() {
        // Cargar el archivo PDF
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


## Añadir Anotaciones de Widget

Los formularios interactivos utilizan [Anotaciones de Widget](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/WidgetAnnotation) para representar la apariencia de los campos y gestionar las interacciones del usuario. Usamos estos elementos de formulario que se añaden a un PDF para facilitar la entrada, el envío de información o realizar algunas otras interacciones del usuario.

Las Anotaciones de Widget son una representación gráfica de un campo de formulario en páginas específicas, por lo que no podemos crearlas directamente como una anotación.

Cada Anotación de Widget tendrá gráficos apropiados (apariencia) dependiendo de su tipo. Después de la creación, ciertos aspectos visuales pueden cambiarse, como el estilo del borde y el color de fondo. Otras propiedades como el color del texto y la fuente pueden cambiarse a través del campo, una vez que esté adherido a uno.

En algunos casos, puede que desee que un campo aparezca en más de una página, repitiendo el mismo valor.
 En ese caso, los campos que normalmente tienen solo un widget pueden tener varios widgets adjuntos: un TextField, ListBox, ComboBox y CheckBox generalmente tienen exactamente uno, mientras que el RadioGroup tiene múltiples widgets, uno para cada botón de radio. 
Alguien que complete el formulario puede usar cualquiera de esos widgets para actualizar el valor del campo, y esto se refleja en todos los demás widgets también.

Cada campo de formulario para cada lugar en el documento representa una Anotación de Widget. Los datos específicos de ubicación de la Anotación de Widget se agregan a la página particular. Cada campo de formulario tiene varias variaciones. Un botón puede ser un botón de radio, un checkbox o un botón de empuje. Un widget de elección puede ser un cuadro de lista o un cuadro combinado.

En este ejemplo, aprenderemos cómo agregar los botones de empuje para la navegación en el documento.

## Agregar Botón al Documento

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import java.util.*;

public class ExampleWidgetAnnotation {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddButton()
    {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample.pdf");
        Page page = document.getPages().get_Item(1);

        Rectangle rect = new Rectangle(72, 748, 164, 768);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Imprimir documento actual");
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

Este botón tiene un borde y establece un fondo. También establecemos un nombre para el botón (Name), una descripción emergente (AlternateName), una etiqueta (NormalCaption) y un color para el texto de la etiqueta (Color).

## Uso de acciones de navegación de documentos

Existe un ejemplo más complejo del uso de las anotaciones de widgets: la navegación de documentos en un documento PDF. Esto puede ser necesario para preparar una presentación de documento PDF.

Este ejemplo muestra cómo crear 4 botones:

```java
public static void AddDocumentNavigationActions() {
// Cargar el archivo PDF
Document document = new Document(_dataDir + "JSON Fundamenals.pdf");

ButtonField[] buttons = new ButtonField[4];
String[] alternateNames = { "Ir a la primera página", "Ir a la página anterior", "Ir a la página siguiente", "Ir a la última página" };
String[] normalCaptions = { "Primera", "Anterior", "Siguiente", "Última" };
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


## Cómo eliminar la anotación de widget

Aspose.PDF para Java tiene reglas para eliminar anotaciones de su archivo:

```java
public static void DeleteWidgetAnnotation() {
        // Cargar el archivo PDF
        Document document = new Document(_dataDir + "sample_textannot.pdf");

        // Filtrar anotaciones usando AnnotationSelector
        Page page = document.getPages().get_Item(1);
        AnnotationSelector annotationSelector = new AnnotationSelector(new ButtonField(page, Rectangle.getTrivial()));
        page.accept(annotationSelector);
        List<Annotation> buttonFields = annotationSelector.getSelected();

        // eliminar anotaciones
        for (Annotation wa : buttonFields) {
            page.getAnnotations().delete(wa);
        }
        document.save(_dataDir + "sample_widgetannot_del.pdf");
    }
```

En los documentos PDF, puede ver y gestionar contenido 3D de alta calidad creado con software CAD 3D o de modelado 3D e incrustado en el documento PDF.
 Puede rotar elementos 3D en todas las direcciones como si los estuviera sosteniendo en sus manos.

¿Por qué necesita una visualización 3D de imágenes en absoluto?

En los últimos años, la tecnología ha logrado grandes avances en todas las áreas gracias a la impresión 3D. Las tecnologías de impresión 3D se pueden aplicar para enseñar habilidades tecnológicas en construcción, ingeniería mecánica, diseño como herramienta principal. Estas tecnologías, gracias a la aparición de dispositivos de impresión personal, pueden contribuir a la introducción de nuevas formas de organización del proceso educativo, aumentar la motivación y la formación de las competencias necesarias de los graduados y profesores.

La tarea principal del modelado 3D es la idea de un objeto o elemento futuro porque, para liberar un objeto, se necesita comprender sus características de diseño en todo detalle para su regeneración sucesiva en diseño industrial o arquitectura.

## Añadir Anotación 3D

Se añade anotación 3D utilizando un modelo creado en el formato U3D con Aspose.PDF para Java
1. Crear un nuevo [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document)
1. Cargar los datos del modelo 3D deseado (en nuestro caso "Ring.u3d") para crear [PDF3DContent](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/PDF3DContent)
1. Crear un objeto [3dArtWork](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DArtwork) y enlazarlo al documento y 3DContent
1. Configurar el objeto pdf3dArtWork:

    - 3DLightingScheme - (en el ejemplo estableceremos `CAD`)
    - 3DRenderMode - (en el ejemplo estableceremos `Solid`)
    - Llenar `ViewArray`, crear al menos una [3D View](https://reference.aspose.com/pdf/java/com.aspose.pdf/PDF3DView) y añadirla al array.

1. Establecer 3 parámetros básicos en la anotación:
    - la `page` en la cual se colocará la anotación,
    - el `rectangle`, dentro del cual la anotación,
    - y el objeto `3dArtWork`.
1. Para una mejor presentación del objeto 3D, establecer el marco de Bordes.
1. Establecer la vista predeterminada (por ejemplo - TOP)

1. Agregar algunos parámetros adicionales: nombre, cartel de vista previa, etc.
2. Agregar anotación a la [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)
3. Guardar el resultado

## Ejemplo

Por favor, revise el siguiente fragmento de código para agregar una Anotación 3D.

```java
    public class Example3DAnnotation
    {
    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";
    public static void Add3dAnnotation()
    {
    // Cargar el archivo PDF
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
    //establecer imagen de vista previa si es necesario
    //pdf3dAnnotation.setImagePreview(_dataDir + "sample_3d.png");
    document.getPages().get_Item(1).getAnnotations().add(pdf3dAnnotation);

    document.save(_dataDir+"sample_3d.pdf");
    }
}
```


Este ejemplo de código nos mostró un modelo así:

![Demostración de anotación 3D](3d_demo.png)