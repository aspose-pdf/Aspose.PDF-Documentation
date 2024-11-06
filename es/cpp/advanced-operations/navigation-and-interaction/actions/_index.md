---
title: Trabajando con Acciones en PDF
linktitle: Acciones
type: docs
weight: 20
url: es/cpp/actions/
description: Esta sección explica cómo agregar acciones al documento y campos de formulario programáticamente con C++.
lastmod: "2022-01-25"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Agregar Hipervínculo en un Archivo PDF

Los documentos PDF son una excelente manera de compartir información. Son fáciles de leer, editar y distribuir. Sin embargo, crear enlaces en un documento PDF puede ser un desafío. Vamos a mostrarte cómo.

Es posible agregar hipervínculos a archivos PDF, ya sea para permitir que los lectores naveguen a otra parte del PDF o a contenido externo.

Por ejemplo, es posible que desees agregar un índice interactivo a tus libros electrónicos, citar recursos externos para tu artículo o navegar rápidamente al lector a una página diferente en el sitio web para obtener más información sobre un tema.

Para crear hipervínculos con unos pocos clics, sigue estos sencillos pasos:

1. Crea un objeto de clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).  
1. Obtén la clase [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) a la que deseas añadir el enlace.  
1. Crea un objeto [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) usando los objetos Page y [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/). El objeto rectangle se utiliza para especificar la ubicación en la página donde se debe añadir el enlace.  
1. Establece la propiedad Action en el objeto [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) que especifica la ubicación del URI remoto.  
1. Para mostrar un texto de hipervínculo, añade una cadena de texto en una ubicación similar a donde se coloca el objeto [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation).  
1. Para añadir un texto libre:

- Instancia un objeto [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation). It also accepts Page and Rectangle objects as argument, so it is possible to provide same values as specified against the LinkAnnotation constructor.
- Usando la propiedad Contents del objeto [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation), especifique la cadena que debe mostrarse en el PDF de salida.
- Opcionalmente, establezca el ancho del borde de ambos objetos [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) y FreeTextAnnotation a 0 para que no aparezcan en el documento PDF.
- Una vez que se han definido los objetos [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) y [FreeTextAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.free_text_annotation), agregue estos enlaces a la colección Annotations del objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).

- Finalmente, guarde el PDF actualizado usando el método Save del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
El siguiente fragmento de código te muestra cómo agregar un hipervínculo a un archivo PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddHyperlinkInPDFFile() {

String _dataDir("C:\\Samples\\");

// Abrir documento

auto document = MakeObject<Document>(_dataDir + u"AddHyperlink.pdf");

// Crear enlace

auto page = document->get_Pages()->idx_get(1);

// Crear objeto de anotación de enlace

auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 100, 300, 300));

// Crear objeto de borde para LinkAnnotation

auto border = MakeObject<Aspose::Pdf::Annotations::Border>(link);

// Establecer el valor del ancho del borde como 0

border->set_Width(0);

// Establecer el borde para LinkAnnotation

link->set_Border(border);

// Especificar el tipo de enlace como URI remoto

link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

// Agregar anotación de enlace a la colección de anotaciones de la primera página del archivo PDF

page->get_Annotations()->Add(link);


// Crear anotación de texto libre

auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::FreeTextAnnotation>(


page,


MakeObject<Rectangle>(100, 100, 300, 300),


MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(



FontRepository::FindFont(u"TimesNewRoman"), 10, Color::get_Blue()));


// Cadena a ser añadida como texto libre

textAnnotation->set_Contents(u"Link to Aspose website");

// Establecer el borde para la anotación de texto libre

textAnnotation->set_Border(border);

// Agregar anotación de texto libre a la colección de anotaciones de la primera página del documento

page->get_Annotations()->Add(textAnnotation);


// Guardar documento actualizado

document->Save(_dataDir + u"AddHyperlink_out.pdf");

}
```

## Crear Hipervínculo a páginas en el mismo PDF

Aspose.PDF para C++ proporciona una gran característica para la creación de PDF así como su manipulación. También ofrece la función de agregar enlaces a páginas PDF y un enlace puede dirigir a páginas en otro archivo PDF, una URL web, un enlace para lanzar una Aplicación o incluso un enlace a páginas en el mismo archivo PDF. Para agregar hipervínculos locales (enlaces a páginas en el mismo archivo PDF), se ha añadido una clase llamada [LocalHyperlink](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.local_hyperlink) al espacio de nombres Aspose.PDF y esta clase tiene una propiedad llamada TargetPageNumber, que se utiliza para especificar la página de destino para el hipervínculo.

Para agregar el hipervínculo local, necesitamos crear un TextFragment para que el enlace pueda asociarse con el TextFragment. La clase [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment) tiene una propiedad llamada Hyperlink que se utiliza para asociar una instancia de LocalHyperlink. El siguiente fragmento de código muestra los pasos para cumplir con este requisito.

```cpp
void CreateHyperlinkToPagesInSamePDF() {

String _dataDir("C:\\Samples\\");


// Crear una instancia de Document

auto document = MakeObject<Document>();


// Agregar página a la colección de páginas del archivo PDF

auto page = document->get_Pages()->Add();


// Crear una instancia de Text Fragment

auto text = MakeObject<TextFragment>(u"vincular número de página a la página 2");


// Crear una instancia de hipervínculo local

auto link = MakeObject<LocalHyperlink>();


// Establecer la página de destino para la instancia de enlace

link->set_TargetPageNumber(2);


// Establecer el hipervínculo de TextFragment

text->set_Hyperlink(link);


// Agregar texto a la colección de párrafos de la página

page->get_Paragraphs()->Add(text);


// Crear una nueva instancia de TextFragment

text = new TextFragment(u"vincular número de página a la página 1");


// TextFragment debería agregarse en una nueva página

text->set_IsInNewPage(true);


// Crear otra instancia de hipervínculo local

link = new LocalHyperlink();


// Establecer la página de destino para el segundo hipervínculo

link->set_TargetPageNumber(1);


// Establecer el enlace para el segundo TextFragment

text->set_Hyperlink(link);


// Agregar texto a la colección de párrafos del objeto página

page->get_Paragraphs()->Add(text);


// Guardar el documento actualizado

document->Save(_dataDir + u"CreateLocalHyperlink_out.pdf");
}
```
## Obtener el Destino del Hipervínculo en PDF (URL)

Los enlaces se representan como anotaciones en un archivo PDF y se pueden agregar, actualizar o eliminar. Aspose.PDF para C++ también admite obtener el destino (URL) del hipervínculo en un archivo PDF.

Para obtener la URL de un enlace:

1. Crear un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Obtener la [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) de la que desea extraer los enlaces.
1. Usar la clase [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) para extraer todos los objetos [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) de la página especificada.
1. Pasar el objeto [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) al método Accept del objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).
1. Obtén todas las anotaciones de enlace seleccionadas en un objeto IList usando la propiedad Selected del objeto [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/).
1. Finalmente, extrae la Acción de LinkAnnotation como GoToURIAction.

El siguiente fragmento de código muestra cómo obtener destinos de hipervínculo (URL) de un archivo PDF.

```cpp
void GetPDFHyperlinkDestination() {

String _dataDir("C:\\Samples\\");


auto document = new Document(_dataDir + u"Aspose-app-list.pdf");

// Extraer acciones

auto page = document->get_Pages()->idx_get(1);


auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(


MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));

page->Accept(selector);


auto list = selector->get_Selected();

// Iterar a través de cada elemento individual dentro de la lista

if (list->get_Count() == 0)


Console::WriteLine(u"No se encontraron hipervínculos...");

else {


// Recorre todos los marcadores


for (auto annot : list) {



auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);



if (la != nullptr) {




auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());




// Imprimir la URL de destino




Console::WriteLine(u"Destino: " + action->get_URI());



}


}

} // fin del else
}
```
## Obtener Texto de Hipervínculo

Un hipervínculo tiene dos partes: el texto que se muestra en el documento y la URL de destino. En algunos casos, es el texto en lugar de la URL lo que necesitamos.

El texto y las anotaciones/acciones en un archivo PDF están representados por diferentes entidades. El texto en una página es solo un conjunto de palabras y caracteres, mientras que las anotaciones aportan cierta interactividad, como la inherente a un hipervínculo.

Para encontrar el contenido de la URL, necesitas trabajar con ambas, la anotación y el texto. El objeto [Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) no tiene el texto en sí, pero se encuentra bajo el texto en la página. Así que para obtener el texto, la Anotación proporciona los límites de la URL, mientras que el objeto de Texto proporciona los contenidos de la URL. Por favor, vea el siguiente fragmento de código.

```cpp
  void GetHyperlinkText() {

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"aspose-app-list.pdf");

// Extract actions

auto page = document->get_Pages()->idx_get(1);


for (auto annot : page->get_Annotations()) {


auto la = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(annot);


if (la != nullptr) {



// Print the URL of each Link Annotation



auto action = System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(la->get_Action());



Console::WriteLine(u"URI: " + action->get_URI());




auto absorber = MakeObject<TextAbsorber>();



absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);



absorber->get_TextSearchOptions()->set_Rectangle(annot->get_Rect());



page->Accept(absorber);



String extractedText = absorber->get_Text();



// Print the text associated with hyperlink



Console::WriteLine(extractedText);


}

}
}
```

## Eliminar la Acción de Apertura de Documento de un Archivo PDF

[Cómo Especificar la Página PDF al Ver el Documento](#how-to-specify-pdf-page-when-viewing-document) explicó cómo indicar a un documento que se abra en una página diferente a la primera. Al concatenar varios documentos, y uno o más tiene una acción GoTo establecida, probablemente querrás eliminarlos. Por ejemplo, si combinas dos documentos y el segundo tiene una acción GoTo que te lleva a la segunda página, el documento resultante se abrirá en la segunda página del segundo documento en lugar de la primera página del documento combinado. Para evitar este comportamiento, elimina el comando de acción de apertura.

Para eliminar una acción de apertura:

1. Establece la propiedad [OpenAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#a24b876bb6bee957feac48ac8031dc28e) del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) en null.
1. Guarda el PDF actualizado utilizando el método Save del objeto Document.

El siguiente fragmento de código muestra cómo eliminar una acción de apertura de documento del archivo PDF.

```cpp
void RemoveDocumentOpenActionFromPDFFile()
{

String _dataDir("C:\\Samples\\");

// Abrir documento

auto document = new Document(_dataDir + u"RemoveOpenAction.pdf");

// Quitar acción de apertura del documento

document->set_OpenAction(nullptr);


// Guardar documento actualizado

document->Save(_dataDir + u"RemoveOpenAction_out.pdf");
}
```

## Cómo Especificar la Página PDF al Ver el Documento {#how-to-specify-pdf-page-when-viewing-document}

Al ver archivos PDF en un visor de PDF como Adobe Reader, los archivos generalmente se abren en la primera página. Sin embargo, es posible configurar el archivo para que se abra en una página diferente.

La clase 'XYZExplicitDestination' te permite especificar una página en un archivo PDF que deseas abrir. Al pasar el valor del objeto GoToAction a la propiedad OpenAction de la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), el documento se abre en la página especificada contra el objeto XYZExplicitDestination. El siguiente fragmento de código muestra cómo especificar una página como la acción de apertura del documento.

```cpp
void HowToSpecifyPDFPageWhenViewingDocument()
{

String _dataDir("C:\\Samples\\");

// Cargar el archivo PDF

auto document = new Document(_dataDir + u"SpecifyPageWhenViewing.pdf");

// Obtener la instancia de la segunda página del documento

auto page2 = document->get_Pages()->idx_get(2);

// Crear la variable para establecer el factor de zoom de la página de destino

double zoom = 1;

// Crear instancia de GoToAction

auto action = MakeObject<Aspose::Pdf::Annotations::GoToAction>(page2);

// Ir a la página 2

action->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(page2, 0, page2->get_Rect()->get_Height(), zoom));

// Establecer la acción de apertura del documento

document->set_OpenAction(action);

// Guardar documento actualizado

document->Save(_dataDir + u"goto2page_out.pdf");
}
```