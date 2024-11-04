---

title: Crear AcroForms - Crear PDF Rellenables en PHP  
linktitle: Crear AcroForms  
type: docs  
weight: 10  
url: /php-java/create-forms/  
description: Esta sección explica cómo crear AcroForms desde cero en tus documentos PDF con Aspose.PDF para PHP a través de Java.  
lastmod: "2024-06-05"  
sitemap:  
    changefreq: "weekly"  
    priority: 0.7  
---

## Añadir un Campo de Formulario en un Documento PDF

La clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) proporciona una colección llamada Form que ayuda a gestionar los campos de formulario en un documento PDF.

Para añadir un campo de formulario:

1. Crea el campo de formulario que quieres añadir.
2. Llama al método add de la colección [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form).

Este ejemplo muestra cómo añadir un TextBoxField. Puedes añadir cualquier campo de formulario usando el mismo enfoque:

1. Primero, crea un objeto de campo y establece sus propiedades.
2. Luego, añade el campo a la colección Form.

### Añadiendo TextBoxField

Un campo de texto es un elemento de formulario que permite a un destinatario ingresar texto en tu formulario.
 Esto se usaría cada vez que desees permitir al usuario la libertad de escribir lo que quiera.

Los siguientes fragmentos de código muestran cómo agregar un TextBoxField a un documento PDF.

```php

    // Abrir documento
    $colors = new Color();
    $document = new Document($inputFile);
    $page = $document->getPages()->get_Item(1);

    // Crear un campo
    $textBoxField = new TextBoxField($page, new Rectangle(110, 300, 310, 320));
    $textBoxField->setPartialName("textbox1");
    $textBoxField->setValue("Algún valor en el cuadro de texto");

    $border = new Border($textBoxField);
    $border->setWidth(5);
    $border->setDash(new Dash(1, 1));
    $textBoxField->setBorder($border);
    $textBoxField->setColor($colors->getGreen());

    // Agregar campo al documento
    $document->getForm()->add($textBoxField, 1);

    // Guardar PDF modificado
    $document->save($outputFile);
    $document->close();
```

## Agregar RadioButtonField

Un botón de opción se utiliza más comúnmente para preguntas de opción múltiple, en el escenario donde solo se puede seleccionar una respuesta.
Los siguientes fragmentos de código muestran cómo agregar [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) en un documento PDF.

```php

    // Abrir documento            
    $document = new Document($inputFile);

    // agregar una página al archivo PDF
    $page = $document->getPages()->get_Item(1);

    // instanciar objeto RadioButtonField con el número de página como argumento
    $radio = new RadioButtonField($page);

    // agregar la primera opción de botón de radio y también especificar su origen 
    // usando el objeto Rectangle

    $radio->addOption("Test1", new Rectangle(20, 720, 40, 740));

    // agregar la segunda opción de botón de radio
    $radio->addOption("Test2", new Rectangle(120, 720, 140, 740));

    // agregar el botón de radio al objeto formulario del objeto Document
    $document->getForm()->add($radio);

    // guardar el archivo PDF
    $document->save($outputFile);
    $document->close();
```

El siguiente fragmento de código muestra los pasos para agregar [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) con tres opciones y colocarlos dentro de celdas de tabla.

```php

    $colors = new Color();
    $document = new Document();
    $page = $document->getPages()->add();

    $table = new Table();
    $table->setColumnWidths("120 120 120");
    $page->getParagraphs()->add($table);
    $r1 = $table->getRows()->add();
    $c1 = $r1->getCells()->add();
    $c2 = $r1->getCells()->add();
    $c3 = $r1->getCells()->add();

    $rf = new RadioButtonField($page);
    $rf->setPartialName("radio1");
    $document->getForm()->add($rf, 1);

    $opt1 = new RadioButtonOptionField();
    $opt2 = new RadioButtonOptionField();
    $opt3 = new RadioButtonOptionField();

    $opt1->setOptionName("Item1");
    $opt2->setOptionName("Item2");
    $opt3->setOptionName("Item3");

    $opt1->setWidth(15.0);
    $opt1->setHeight(15.0);
    $opt2->setWidth(15.0);
    $opt2->setHeight(15.0);
    $opt3->setWidth(15.0);
    $opt3->setHeight(15.0);

    $rf->add($opt1);
    $rf->add($opt2);
    $rf->add($opt3);

    $border1 = new Border($opt1);
    $opt1->setBorder($border1);
    $opt1->getBorder()->setWidth(1.0);
    $opt1->getBorder()->setStyle(BorderStyle::$Solid);
    $opt1->getCharacteristics()->setBorder($colors->getBlack());
    $opt1->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt1->setCaption(new TextFragment("Elemento1"));

    $border2 = new Border($opt2);
    $opt3->setBorder($border2);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt2->getCharacteristics()->setBorder($colors->getBlack());
    $opt2->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt2->setCaption(new TextFragment("Elemento2"));

    $border3 = new Border($opt3);
    $opt3->setBorder($border3);
    $opt3->getBorder()->setWidth(1.0);
    $opt3->getBorder()->setStyle(BorderStyle::$Solid);
    $opt3->getCharacteristics()->setBorder($colors->getBlack());
    $opt3->getDefaultAppearance()->setTextColor($colors->getRed()->toRgb());
    $opt3->setCaption(new TextFragment("Elemento3"));

    $c1->getParagraphs()->add($opt1);
    $c2->getParagraphs()->add($opt2);
    $c3->getParagraphs()->add($opt3);

    $document->save($outputFile);
    $document->close();
```


## Añadiendo campo ComboBox

Un Combo Box es un campo de formulario que añadirá un menú desplegable a su documento.

Los siguientes fragmentos de código muestran cómo agregar un campo [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) en un documento PDF.

```php

        $document = new Document($inputFile);

        // instanciar objeto de campo ComboBox
        $page = $document->getPages()->get_Item(1);
        $combo = new ComboBoxField($page, new Rectangle(100, 600, 150, 616));

        // añadir opción al ComboBox
        $combo->addOption("Red");
        $combo->addOption("Yellow");
        $combo->addOption("Green");
        $combo->addOption("Blue");

        // añadir objeto combo box a la colección de campos de formulario del objeto documento
        $document->getForm()->add($combo);

        // guardar el documento PDF
        $document->save($outputFile);
        $document->close();
```

## Añadir Descripción Emergente al Formulario

La clase Document proporciona una colección llamada Form que gestiona los campos de formulario en un documento PDF.
 Para agregar una descripción emergente a un campo de formulario, use la clase Field AlternateName. Adobe Acrobat utiliza el ‘nombre alternativo’ como una descripción emergente del campo.

Los fragmentos de código que siguen muestran cómo agregar una descripción emergente a un campo de formulario con PHP.

```php

    $document = new Document($inputFile);
    $textBoxField = $document->getForm()->get("textbox1");

    // Establecer la descripción emergente para el campo de texto
    $textBoxField->setAlternateName("Descripción emergente de la caja de texto");

    // guardar el documento PDF
    $document->save($outputFile);
    $document->close();
```