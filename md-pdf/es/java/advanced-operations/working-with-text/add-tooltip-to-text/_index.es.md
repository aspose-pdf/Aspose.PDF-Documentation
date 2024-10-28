---
title: Usando Tooltip 
linktitle: PDF Tooltip
type: docs
weight: 20
url: /java/pdf-tooltip/
description: Aprende cómo añadir un tooltip al fragmento de texto en PDF usando Java y Aspose.PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Añadir Tooltip al Texto Buscado agregando un Botón Invisible

A menudo se requiere añadir algunos detalles para una frase o palabra específica como un tooltip en el documento PDF para que pueda aparecer cuando el usuario pase el cursor del ratón sobre el texto. Aspose.PDF para Java proporciona esta característica para crear tooltips añadiendo un botón invisible sobre el texto buscado. El siguiente fragmento de código te mostrará la forma de lograr esta funcionalidad:

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.ButtonField;
import com.aspose.pdf.Document;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.TextFragmentAbsorber;
import com.aspose.pdf.TextFragmentCollection;

public class ExampleToolTip {

    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddToolTip() {
        String outputFile = _dataDir + "Tooltip_out.pdf";

        // Crear documento de muestra con texto
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("Mueve el cursor del ratón aquí para mostrar un tooltip"));
        doc.getPages().get_Item(1).getParagraphs().add(new TextFragment("Mueve el cursor del ratón aquí para mostrar un tooltip muy largo"));
        doc.save(outputFile);

        // Abrir documento con texto
        Document document = new Document(outputFile);
        // Crear objeto TextAbsorber para encontrar todas las frases que coinciden con la expresión regular
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("Mueve el cursor del ratón aquí para mostrar un tooltip");
        // Aceptar el absorber para las páginas del documento
        document.getPages().accept(absorber);
        // Obtener los fragmentos de texto extraídos
        TextFragmentCollection textFragments = absorber.getTextFragments();

        // Recorrer los fragmentos
        for(TextFragment fragment : textFragments)
        {
            // Crear botón invisible en la posición del fragmento de texto
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // El valor de AlternateName se mostrará como tooltip por una aplicación de visualización
            field.setAlternateName ("Tooltip para texto.");
            // Añadir campo de botón al documento
            document.getForm().add(field);
        }

        // A continuación será un ejemplo de tooltip muy largo
        absorber = new TextFragmentAbsorber("Mueve el cursor del ratón aquí para mostrar un tooltip muy largo");
        document.getPages().accept(absorber);
        textFragments = absorber.getTextFragments();

        for(TextFragment fragment : textFragments)
        {
            ButtonField field = new ButtonField(fragment.getPage(), fragment.getRectangle());
            // Establecer texto muy largo
            field.setAlternateName ("Lorem ipsum dolor sit amet, consectetur adipiscing elit," +
                                    " sed do eiusmod tempor incididunt ut labore et dolore magna" +
                                    " aliqua. Ut enim ad minim veniam, quis nostrud exercitation" +
                                    " ullamco laboris nisi ut aliquip ex ea commodo consequat." +
                                    " Duis aute irure dolor in reprehenderit in voluptate velit" +
                                    " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint" +
                                    " occaecat cupidatat non proident, sunt in culpa qui officia" +
                                    " deserunt mollit anim id est laborum.");
            document.getForm().add(field);
        }

        // Guardar documento
        document.save(outputFile);
    }
}
```


{{% alert color="primary" %}}

Con respecto a la longitud del tooltip, el texto del tooltip está contenido en el documento PDF como un tipo de cadena PDF, fuera del flujo de contenido. No hay una restricción efectiva sobre tales cadenas en archivos PDF (Ver PDF Reference Appendix C.). Sin embargo, un lector conforme (por ejemplo, Adobe Acrobat) que se ejecuta en un procesador particular y en un entorno operativo particular sí tiene tal límite. Por favor, consulte la documentación de su aplicación de lector PDF.

{{% /alert %}}

## Crear un Bloque de Texto Oculto y Mostrarlo al Pasar el Ratón

En Aspose.PDF, se implementa una función para ocultar acciones mediante la cual es posible mostrar/ocultar el campo de cuadro de texto (o cualquier otro tipo de anotación) al entrar/salir del ratón sobre algún botón invisible. Para este propósito, se utiliza la Clase Aspose.Pdf.Annotations.HideAction para asignar la acción de ocultar/mostrar al bloque de texto. Por favor, utilice el siguiente fragmento de código para Mostrar/Ocultar un Bloque de Texto al Entrar/Salir el Ratón.

Por favor, tenga en cuenta también que las acciones PDF en los documentos funcionan bien en los lectores conformes (por ejemplo,
 Adobe Reader) pero no hay garantías para otros lectores de PDF (por ejemplo, complementos de navegadores web). Hemos realizado una breve investigación y encontramos:

- Todas las implementaciones de la acción de ocultar en documentos PDF funcionan bien en Internet Explorer v.11.0.
- Todas las implementaciones de la acción de ocultar también funcionan en Opera v.12.14, pero notamos algún retraso en la respuesta al abrir el documento por primera vez.
- Solo la implementación que utiliza el constructor HideAction que acepta el nombre del campo funciona si Google Chrome v.61.0 navega por el documento; Utilice los constructores correspondientes si navegar en Google Chrome es significativo:

>buttonField.Actions.OnEnter = new HideAction(floatingField.FullName, false);
>buttonField.Actions.OnExit = new HideAction(floatingField.FullName);

```java
    public static void name() {
        String outputFile = _dataDir + "TextBlock_HideShow_MouseOverOut_out.pdf";

        // Crear documento de muestra con texto
        Document doc = new Document();
        doc.getPages().add().getParagraphs().add(new TextFragment("Mueve el cursor del mouse aquí para mostrar texto flotante"));
        doc.save(outputFile);

        // Abrir documento con texto
        Document document = new Document(outputFile);
        // Crear objeto TextAbsorber para encontrar todas las frases que coincidan con la expresión regular
        TextFragmentAbsorber absorber = new TextFragmentAbsorber("Mueve el cursor del mouse aquí para mostrar texto flotante");
        // Aceptar el absorber para las páginas del documento
        document.getPages().accept(absorber);
        // Obtener el primer fragmento de texto extraído
        TextFragmentCollection textFragments = absorber.getTextFragments();
        TextFragment fragment = textFragments.get_Item(1);

        // Crear campo de texto oculto para texto flotante en el rectángulo especificado de la página
        TextBoxField floatingField = new TextBoxField(fragment.getPage(), new Rectangle(100, 700, 220, 740));
        // Establecer texto para mostrar como valor del campo
        floatingField.setValue ("Este es el \"campo de texto flotante\".");
        // Recomendamos hacer el campo 'solo lectura' para este escenario
        floatingField.setReadOnly(true);

        // Establecer bandera 'oculto' para hacer que el campo sea invisible al abrir el documento
        floatingField.setFlags( floatingField.getFlags() | AnnotationFlags.Hidden);

        // No es necesario establecer un nombre de campo único, pero está permitido
        floatingField.setPartialName ("FloatingField_1");

        // No es necesario establecer características de apariencia del campo, pero lo mejora
        DefaultAppearance da = new DefaultAppearance("Helvetica", 16, java.awt.Color.RED);
        floatingField.setDefaultAppearance(da);
        //new DefaultAppearance("Helv", 10, Color.getBlue()
        floatingField.getCharacteristics().setBackground(Color.getLightBlue());
        floatingField.getCharacteristics().setBorder(Color.getDarkBlue());;
        floatingField.setBorder(new Border(floatingField));
        floatingField.getBorder().setWidth(1);
        floatingField.setMultiline(true);

        // Agregar campo de texto al documento
        document.getForm().add(floatingField);

        // Crear botón invisible en la posición del fragmento de texto
        Field buttonField = new ButtonField(fragment.getPage(), fragment.getRectangle());
        // Crear nueva acción de ocultar para el campo especificado (anotación) y bandera de invisibilidad.
        // (También puede referirse al campo flotante por el nombre si lo especificó arriba.)
        // Agregar acciones al entrar/salir del ratón en el campo de botón invisible
        buttonField.getActions().setOnEnter(new HideAction(floatingField, false));
        buttonField.getActions().setOnExit (new HideAction(floatingField));

        // Agregar campo de botón al documento
        document.getForm().add(buttonField);

        // Guardar documento
        document.save(outputFile);
    }
```