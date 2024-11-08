---
title: Qué hay de nuevo
linktitle: Qué hay de nuevo
type: docs
weight: 10
url: /es/java/whatsnew/
description: En esta página se presentan las características nuevas más populares en Aspose.PDF para Java que se han introducido en lanzamientos recientes.
sitemap:
    changefreq: "monthly"
    priority: 0.8
lastmod: "2021-06-05"
---

## Qué hay de nuevo en Aspose.PDF 24.8

Desde 24.8, soporte para el formato PDF/A-4:

```java

    Document document = new Document(inputPdf);
    // Solo los documentos PDF-2.x pueden ser convertidos a PDF/A-4
    document.convert(new ByteArrayOutputStream(), PdfFormat.v_2_0, ConvertErrorAction.Delete);
    boolean converted = document.convert(logFile, PdfFormat.PDF_A_4, ConvertErrorAction.Delete);
    document.save(outputFile);
```

Además, es posible agregar texto alternativo para el Sello de Imagen:

La propiedad AlternativeText ha sido añadida a ImageStamp - si se le asigna un valor, entonces al agregar un ImageStamp a un documento tiene Texto Alternativo.

```java

    String p1_Alt1 = "*** página 1, texto alt 1 ***",
                    p1_Alt2 = "*** página 1, texto alt 2 ***",
                    p2_Alt1 = "--- página 1, texto alt 1 ---",
                    p2_Alt2 = "--- página 1, texto alt 2 ---";

    StructTreeRootElement structTreeRoot = document.getTaggedContent().getStructTreeRootElement();

    ImageStamp imageStamp = new ImageStamp(dataDir + "test.jpg");
    imageStamp.setXIndent(100);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setQuality(100);
    imageStamp.setAlternativeText(p1_Alt1);

    // A la página 1
    document.getPages().get_Item(1).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p1_Alt2);
    document.getPages().get_Item(1).addStamp(imageStamp);

    // A la página 2
    document.getPages().add();
    imageStamp.setXIndent(400);
    imageStamp.setYIndent(700);
    imageStamp.setWidth(50);
    imageStamp.setHeight(50);
    imageStamp.setAlternativeText(p2_Alt1);
    document.getPages().get_Item(2).addStamp(imageStamp);

    imageStamp.setYIndent(500);
    imageStamp.setAlternativeText(p2_Alt2);
    document.getPages().get_Item(2).addStamp(imageStamp);

    // Guardar documento
    document.save(outFile);
```


También, el siguiente código muestra cómo agregar TextoAlternativo en las imágenes existentes en FigureElements.

```java

    String inFile = dataDir + "46040.pdf";
    String outFile = dataDir + "46040_1_out.pdf";

    Document document = new Document(inFile);

    ITaggedContent taggedContent = document.getTaggedContent();
    StructureElement rootElement = taggedContent.getRootElement();

    Iterator tmp0 = (rootElement.getChildElements()).iterator();
    while (tmp0.hasNext())
    {
        com.aspose.pdf.tagged.logicalstructure.elements.Element element = (com.aspose.pdf.tagged.logicalstructure.elements.Element)tmp0.next();
        if (element instanceof com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)
                {
            com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figureElement = (com.aspose.pdf.tagged.logicalstructure.elements.FigureElement)element;

            // Establecer Texto Alternativo
            figureElement.setAlternativeText("Texto alternativo de la figura (técnica 1)");
        }
    }

    // Guardar documento
    document.save(outFile);
```


## Qué hay de nuevo en Aspose.PDF 24.7

Desde la versión 24.7, como parte de la edición de PDF etiquetados, se añadieron métodos en **Aspose.Pdf.LogicalStructure.Element**:

- Tag (agregar etiquetas a operadores específicos como imágenes, texto y enlaces)
- InsertChild
- RemoveChild
- ClearChilds

Estos métodos te permiten editar las etiquetas de archivos PDF, por ejemplo:

```java

    Document document = new Document(dataDir + "test.pdf");

    // Recuperar la primera página del documento.
    Page page = document.getPages().get_Item(1);

    // Inicializar variables para almacenar elementos BDC (Begin Dictionary Context) para diferentes propósitos.
    BDC imageBdc = null;
    BDC pBdc = null;
    BDC link1Bdc = null;
    BDC link2Bdc = null;
    BDC helloBdc = null;

    // Iterar a través de los contenidos de la página.
    for (int i = 1; i <= page.getContents().size(); i++)
    {
        // Obtener el operador actual de los contenidos de la página.
        Operator op = page.getContents().get_Item(i);

        // Verificar si el operador es una instancia de BDC.
        if (op instanceof BDC) {
        BDC bdc = (BDC)op; // Convertir el operador al tipo BDC.
        if (bdc != null)
        {
            // Verificar si el MCID (Identificador de Contenido Marcado) del BDC es 0.
            if (bdc.getProperties().getMCID()[0] != null && bdc.getProperties().getMCID()[0] == 0)
            {
                helloBdc = bdc; // Almacenar el BDC para su uso posterior.
            }
        }
    }

    // Verificar si el operador es una instancia de Do (Dibujar Objeto).
    if (op instanceof Do) {
        Do doXobj = (Do)op; // Convertir el operador al tipo Do.
        if (doXobj != null)
        {
            // Crear un nuevo BDC para una imagen e insertarlo en los contenidos de la página.
            imageBdc = new BDC("Figure");
            page.getContents().insert(i - 2, imageBdc); // Insertar antes del operador actual.
            i++; // Incrementar el índice para tener en cuenta el BDC insertado.
            page.getContents().insert(i + 1, new EMC()); // Insertar un EMC (Fin de Contenido Marcado).
            i++; // Incrementar el índice de nuevo.
        }
    }

    // Verificar si el operador es una instancia de TextShowOperator (para mostrar texto).
    if (op instanceof TextShowOperator) {
        TextShowOperator tx = (TextShowOperator)op; // Convertir el operador al tipo TextShowOperator.
        if (tx != null)
        {
            // Verificar el contenido de texto específico e insertar los BDC correspondientes.
            if (tx.getText().contains("efter Ukendt forfatter er licenseret under"))
            {
                pBdc = new BDC("P");
                page.getContents().insert(i - 1, pBdc); // Insertar antes del operador actual.
                i++; // Incrementar el índice.
                page.getContents().insert(i + 1, new EMC()); // Insertar un EMC.
                i++; // Incrementar el índice.
            }
            if (tx.getText().contains("CC"))
            {
                link1Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link1Bdc); // Insertar antes del operador actual.
                i++; // Incrementar el índice.
                page.getContents().insert(i + 1, new EMC()); // Insertar un EMC.
                i++; // Incrementar el índice.
            }
            if (tx.getText().contains("Dette billede"))
            {
                link2Bdc = new BDC("Link");
                page.getContents().insert(i - 1, link2Bdc); // Insertar antes del operador actual.
                i++; // Incrementar el índice.
                page.getContents().insert(i + 1, new EMC()); // Insertar un EMC.
                i++; // Incrementar el índice.
            }
        }
    }
}
 
    // Recuperar el contenido etiquetado del documento.
    ITaggedContent tagged = document.getTaggedContent();

    // Procesar el contenido etiquetado para modificar atributos de estructura.
    // Obtener el primer elemento hijo del elemento raíz en el contenido etiquetado.
    com.aspose.pdf.tagged.logicalstructure.elements.Element p = tagged.getRootElement().getChildElements().get_Item(1);
    p.clearChilds(); // Limpiar elementos hijo existentes.

    // Etiquetar el helloBdc con el elemento de estructura padre.
    MCRElement mcr = p.tag(helloBdc);

    // Crear y establecer atributos de estructura para el elemento etiquetado.
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
            .getAttributes().createAttributes(AttributeOwnerStandard.Layout);
    StructureAttribute attr = new StructureAttribute(AttributeKey.SpaceAfter);
    attr.setNumberValue(30.625); // Establecer atributo de espacio después.
    attrs.setAttribute(attr); // Aplicar el atributo a la estructura.

    // Crear un nuevo FigureElement en el contenido etiquetado.
    com.aspose.pdf.tagged.logicalstructure.elements.FigureElement figure = tagged.createFigureElement();
    tagged.getRootElement().insertChild(figure, 2); // Insertar el elemento figura en la segunda posición.
    figure.setAlternativeText("A fly."); // Establecer texto alternativo para la figura.

    // Etiquetar el imageBdc con el elemento figura.
    MCRElement mcr = figure.tag(imageBdc);

    // Recuperar el elemento de estructura padre del MCR especificado (Referencia de Contenido Marcado)
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Crear un nuevo StructureAttribute para espacio después del elemento
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(3.625); // Establecer el valor de espacio después a 3.625 unidades
    attrs.setAttribute(spaceAfter); // Asignar el atributo de espacio después a los atributos de estructura

    // Crear un nuevo StructureAttribute para el cuadro delimitador (BBox)
    StructureAttribute bbox = new StructureAttribute(AttributeKey.BBox);
    bbox.setArrayNumberValue(new Double[][] { new Double[] { (71.9971) }, new Double[] { (375.839) }, new Double[] { (523.299) }, new Double[] { (714.345) } });
    // Establecer los valores del cuadro delimitador para el atributo de estructura
    attrs.setAttribute(bbox); // Asignar el atributo de cuadro delimitador a los atributos de estructura

    // Crear un nuevo StructureAttribute para la ubicación
    StructureAttribute placement = new StructureAttribute(AttributeKey.Placement);
    placement.setNameValue(AttributeName.Placement_Block); // Establecer el tipo de ubicación a bloque
    attrs.setAttribute(placement); // Asignar el atributo de ubicación a los atributos de estructura

    // Recuperar el cuarto elemento hijo del elemento raíz de la estructura etiquetada
    StructureElement p2 = (StructureElement)tagged.getRootElement().getChildElements().get_Item(3);
    p2.clearChilds(); // Limpiar cualquier elemento hijo existente de p2

    // Crear un nuevo SpanElement para ser agregado a p2
    SpanElement span1 = tagged.createSpanElement();

    // Crear atributos de estructura para el elemento de tramo
    StructureAttributes attrs = span1.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Crear un nuevo StructureAttribute para el tipo de decoración de texto
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Establecer la decoración de texto a subrayado
    attrs.setAttribute(textDecorationType); // Asignar el atributo de tipo de decoración de texto a los atributos de estructura

    // Crear un nuevo StructureAttribute para el grosor de la decoración de texto
    StructureAttribute textDecorationThickness = new StructureAttribute(AttributeKey.TextDecorationThickness);
    textDecorationThickness.setNumberValue(0); // Establecer el grosor de la decoración de texto a 0
    attrs.setAttribute(textDecorationThickness); // Asignar el atributo de grosor de decoración de texto a los atributos de estructura

    // Crear un nuevo StructureAttribute para el color de la decoración de texto
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);
    textDecorationColor.setArrayNumberValue(new Double[][] { new Double[] { (0.0196075) }, new Double[] { (0.384308) }, new Double[] { (0.756866) } });
    // Establecer los valores de color RGB para la decoración de texto
    attrs.setAttribute(textDecorationColor); // Asignar el atributo de color de decoración de texto a los atributos de estructura

    p2.appendChild(span1); // Agregar el elemento span1 a p2


    // Crear un nuevo elemento MCR y etiquetarlo con pBdc
    MCRElement mcr = p2.tag(pBdc);
    // Recuperar el elemento de estructura padre del MCR y crear atributos de diseño
    StructureAttributes attrs = com.aspose.pdf.tagged.logicalstructure.elements.InternalHelper.getParentStructureElement(mcr)
    .getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Crear un nuevo StructureAttribute para la alineación del texto
    StructureAttribute textAlign = new StructureAttribute(AttributeKey.TextAlign);
    textAlign.setNameValue(AttributeName.TextAlign_Center); // Establecer la alineación del texto a centrado
    attrs.setAttribute(textAlign); // Asignar el atributo de alineación de texto a los atributos de estructura

    // Crear un nuevo StructureAttribute para espacio después del elemento
    StructureAttribute spaceAfter = new StructureAttribute(AttributeKey.SpaceAfter);
    spaceAfter.setNumberValue(21.75); // Establecer el valor de espacio después a 21.75 unidades
    attrs.setAttribute(spaceAfter); // Asignar el atributo de espacio después a los atributos de estructura


    // Crear un nuevo SpanElement para ser agregado a p2
    SpanElement span2 = tagged.createSpanElement();

    // Crear atributos de estructura para el elemento de tramo
    StructureAttributes attrs = span2.getAttributes().createAttributes(AttributeOwnerStandard.Layout);

    // Crear un nuevo StructureAttribute para el tipo de decoración de texto
    StructureAttribute textDecorationType = new StructureAttribute(AttributeKey.TextDecorationType);
    textDecorationType.setNameValue(AttributeName.TextDecorationType_Underline); // Establecer la decoración de texto a subrayado
    attrs.setAttribute(textDecorationType); // Asignar el atributo de tipo de decoración de texto a los atributos de estructura

    // Crear un nuevo StructureAttribute para el color de decoración de texto usando la clave especificada.
    StructureAttribute textDecorationColor = new StructureAttribute(AttributeKey.TextDecorationColor);

    // Establecer el valor del número de matriz para el atributo de color de decoración de texto.
    // El color se representa en una matriz de valores RGB, donde cada valor es un Double.
    textDecorationColor.setArrayNumberValue(new Double[][] {
    new Double[] { (0.0196075) }, // Componente Rojo
    new Double[] { (0.384308) },  // Componente Verde
    new Double[] { (0.756866) }   // Componente Azul
    });

    // Establecer el atributo de color de decoración de texto en el objeto attrs.
    attrs.setAttribute(textDecorationColor);

    // Agregar un elemento de tramo hijo al elemento padre p2.
    p2.appendChild(span2);

    // Crear una nueva instancia de LinkElement para el segundo enlace.
    LinkElement link2 = tagged.createLinkElement();

    // Asignar un ID único al elemento de enlace usando un UUID generado aleatoriamente.
    link2.setId(UUID.randomUUID().toString());

    // Agregar el elemento link2 como un hijo de span2.
    span2.appendChild(link2);

    // Etiquetar el elemento link2 con la anotación correspondiente de las anotaciones de la página.
    link2.tag(page.getAnnotations().get_Item(1));

    // Etiquetar el elemento link2 con metadatos adicionales o contexto (link2Bdc).
    link2.tag(link2Bdc);

    // Crear otra instancia de LinkElement para el primer enlace.
    LinkElement link1 = tagged.createLinkElement();

    // Asignar un ID único al elemento link1 usando un UUID generado aleatoriamente.
    link1.setId(UUID.randomUUID().toString());

    // Agregar el elemento link1 como un hijo de span1.
    span1.appendChild(link1);

    // Etiquetar el elemento link1 con la anotación correspondiente de las anotaciones de la página.
    link1.tag(page.getAnnotations().get_Item(2));

    // Etiquetar el elemento link1 con metadatos adicionales o contexto (link1Bdc).
    link1.tag(link1Bdc);

    // Eliminar el primer elemento hijo del elemento raíz del documento etiquetado.
    tagged.getRootElement().removeChild(0);

    // Guardar el documento en el directorio de salida especificado con el nombre de archivo "_out.pdf".
    document.save(dataDir + "_out.pdf");

```


## Qué hay de nuevo en Aspose.PDF 24.6

Desde la versión 24.6, Aspose.PDF para Java permite firmar PDF con java.security.cert.X509Certificate, java.security.PrivateKey:

Este código recupera un certificado y una clave privada del almacén de certificados y luego los usa para aplicar una firma digital a la primera página de un documento PDF.

```java

    KeyStore trustStore = KeyStore.getInstance("Windows");
    trustStore.load(null, null);
    java.security.cert.X509Certificate certificate = (java.security.cert.X509Certificate) trustStore.getCertificate("ProfMoriarty");
    PrivateKey key = (PrivateKey) trustStore.getKey("ProfMoriarty", null);

    PdfFileSignature pdfSign = new PdfFileSignature(getInputPdf());
    Signature signature = new ExternalSignature(certificate, key);
    pdfSign.sign(1, "reasonTest", "contactTest", "locationTest", true, new java.awt.Rectangle(1, 691, 100, 100), signature);

    pdfSign.save("PDFJAVA.pdf");
    pdfSign.close();
```

## Qué hay de nuevo en Aspose.PDF 24.5

Desde la versión 24.5, se implementaron los Plugins del Editor de Formulario.

**Cómo Editar Formularios en PDF usando el Editor de Formularios**

- Establezca sus claves de licencia
- Cree una instancia de la clase FormEditor, que proporciona métodos para manipular formularios PDF
- Cree una instancia de la clase FormEditorAddOptions, que especifica las opciones para agregar campos de formulario a un documento PDF
- Añada una fuente de archivo de entrada y una fuente de archivo de salida al objeto FormEditorAddOptions, utilizando la clase FileDataSource que representa una ruta de archivo o flujo
- Llame al método Process del objeto FormEditor, pasando el objeto FormEditorAddOptions como parámetro
- Acceda al resultado usando ResultContainer.resultCollection

```java

    // Especificar las rutas de entrada y salida para los archivos PDF.
    String inputPath = "sample.pdf";
    String outputPath = "out.pdf";

    // Crear una instancia del complemento FormEditor.
    FormEditor pdfFormPlugin = new FormEditor();

    // Crear opciones para agregar campos de formulario.
    ArrayList<FormFieldCreateOptions> options = new ArrayList<FormFieldCreateOptions>();

    // Crear un campo de formulario de cuadro de texto.
    FormTextBoxFieldCreateOptions tmp1 = new FormTextBoxFieldCreateOptions(1, new Rectangle(10, 600, 90, 610));
    tmp1.setValue("TextBoxField");
    tmp1.setColor(Color.getChocolate());
    tmp1.setPartialName("TexBoxField");
    options.add(tmp1);

    // Crear un campo de formulario de cuadro combinado.
    FormComboBoxFieldCreateOptions tmp2 = new FormComboBoxFieldCreateOptions(1, new Rectangle(310, 800, 350, 815));

    tmp2.setColor(com.aspose.pdf.Color.getRed());
    tmp2.setEditable(new Boolean[]{true});
    tmp2.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    ArrayList<String> list1 = new ArrayList<String>();
    list1.add("p1");
    list1.add("p2");
    list1.add("p3");
    tmp2.setOptions(list1);
    tmp2.setSelected(new Integer[]{2});
    tmp2.setPartialName("ComboBoxField");
    options.add(tmp2);

    // Crear un campo de formulario de casilla de verificación.
    FormCheckBoxFieldCreateOptions tmp3 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(10, 700, 90, 715));
    tmp3.setValue("CheckBoxField 1");
    tmp3.setPartialName("CheckBoxField_1");
    tmp3.setColor(Color.getBlue());
    options.add(tmp3);


    // Crear un campo de formulario de casilla de verificación.
    FormCheckBoxFieldCreateOptions tmp4 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(100, 700, 190, 715));
    tmp4.setChecked(new Boolean[]{true});
    tmp4.setValue("CheckBoxField 2");
    tmp4.setDefaultAppearance(new DefaultAppearance("Arial Bold", 12, java.awt.Color.GREEN));
    tmp4.setStyle(new Integer[]{BoxStyle.Cross});
    options.add(tmp4);


    // Crear un campo de formulario de casilla de verificación.
    FormCheckBoxFieldCreateOptions tmp5 = new FormCheckBoxFieldCreateOptions(1, new Rectangle(200, 700, 390, 715));
    tmp5.setPartialName("CheckBoxField_3");
    tmp5.setValue("CheckBoxField 3");
    tmp5.setStyle(new Integer[]{BoxStyle.Star});
    tmp5.setChecked(new Boolean[]{true});
    tmp5.setTextHorizontalAlignment(new HorizontalAlignment[]{HorizontalAlignment.Center});
    options.add(tmp5);

    FormEditorAddOptions opt = new FormEditorAddOptions(options);

    // Añadir archivos de entrada y salida a las opciones.
    opt.addInput(new FileDataSource(inputPath));
    opt.addOutput(new FileDataSource(outputPath));

    // Procesar los campos del formulario usando el complemento.
    ResultContainer results = pdfFormPlugin.process(opt);
```


Esta versión nos permite trabajar con capas de PDF. Por ejemplo:

- bloquear una capa de PDF
- extraer elementos de la capa de PDF
- aplanar un PDF con capas
- fusionar todas las capas dentro del PDF en una sola

**Bloquear una capa de PDF**

Desde la versión 24.5, puedes abrir un PDF, bloquear una capa específica en la primera página y guardar el documento con los cambios. Se añadieron dos métodos nuevos y una propiedad:

Layer.Lock(); - Bloquea la capa.
Layer.Unlock(); - Desbloquea la capa.
Layer.Locked; - Propiedad que indica el estado de bloqueo de la capa.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    Layer layer = page.getLayers().get(0);

    layer.lock();

    document.save(output);
```

**Extraer elementos de la capa de PDF**

La biblioteca Aspose.PDF para Java permite la extracción de cada capa de la primera página y guarda cada capa en un archivo separado.

Para crear un nuevo PDF a partir de una capa, se puede usar el siguiente fragmento de código:

```java

    Document document = new Document(inputPath);
    java.util.List<Layer> layers = document.getPages().get_Item(1).getLayers();

    for (Layer layer : layers)
    {
        layer.save(outputPath);
    }
```


**Aplanar un PDF por capas**

La biblioteca Aspose.PDF para Java abre un PDF, itera a través de cada capa en la primera página y aplana cada capa, haciéndola permanente en la página.

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);

    for (Layer layer : page.getLayers())
    {
        layer.flatten(true);
    }
    document.save(output);
```

El método Layer.flatten(boolean cleanupContentStream) acepta el parámetro booleano que especifica si se deben eliminar los marcadores del grupo de contenido opcional del flujo de contenido.
Establecer el parámetro cleanupContentStream en false acelera el proceso de aplanado.

**Combinar todas las capas dentro del PDF en una sola**

La biblioteca Aspose.PDF para Java permite combinar todas las capas de PDF o una capa específica en la primera página en una nueva capa y guarda el documento actualizado.

Se añadieron dos métodos para combinar todas las capas en la página:

- void mergeLayers(String newLayerName);

- void mergeLayers(String newLayerName, String newOptionalContentGroupId);

El segundo parámetro permite renombrar el marcador del grupo de contenido opcional. El valor predeterminado es "oc1" (/OC /oc1 BDC).

```java

    Document document = new Document(input);
    Page page = document.getPages().get_Item(1);
    page.mergeLayers("NewLayerName");

    // O page.mergeLayers("NewLayerName", "OC1");

    document.save(output);
```

## Novedades en Aspose.PDF 24.4

Esta versión introdujo plugins Java para PDF:

- Plugin Form Flattener

```java

    FormFlattener pdfFormPlugin = new FormFlattener();

    FormFlattenAllFieldsOptions opt = new FormFlattenAllFieldsOptions();

    opt.addInput(new FileDataSource("sample.pdf"));
    opt.addOutput(new FileDataSource("sample-flat.pdf"));

    ResultContainer result = pdfFormPlugin.process(opt);

    // Comprobar resultado.
    java.util.List < IOperationResult > resultCollectionInternal = result.getResultCollection();
```

- Exportador de Formularios

```java

    Rectangle rect = new com.aspose.pdf.Rectangle(0, 220, 600, 330);

    // Uso del plugin.
    FormExporter pdfFormPlugin = new FormExporter();
    SelectField selectField = new SelectField() {
      public boolean invoke(Field field) {
        return field instanceof TextBoxField && field.getPageIndex() == 2 && rect.isInclude(field.getRect(), 0);
      }
    };
    FormExporterValuesToCsvOptions opt = new FormExporterValuesToCsvOptions(selectField, ';');

    opt.addInput(new FileDataSource(inputFileNameWithFields));
    opt.addInput(new FileDataSource(getInputPath("document-1.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-2.pdf")));
    opt.addInput(new FileDataSource(getInputPath("document-3.pdf")));
    opt.addOutput(new FileDataSource(getOutputPath("out.csv")));
    ResultContainer result = pdfFormPlugin.process(opt);

    // Comprobar resultado.
    System.out.println(result.getResultCollectionInternal().size() > 0);
    System.out.println(result.getResultCollectionInternal().get_Item(0).isFile());
    System.out.println(result.getResultCollectionInternal().get_Item(0).getData().toString());
```


- Plugin de Fusión

```java

    String input1 = "sample.pdf";
    String input2 = "sample.pdf";

    String output = "TestMergeFileAndStream_ResultAsFile.pdf";

    Merger merger = new Merger();

    MergeOptions opt = new MergeOptions();
    opt.addInput(new FileDataSource(input1));
    opt.addInput(new StreamDataSource(new FileInputStream(input2)));

    opt.addOutput(new FileDataSource(output));

    ResultContainer results = merger.process(opt);

    System.out.println(results.getResultCollection().size());
    System.out.println(results.getResultCollection().get(0).isFile());
```

- Plugin de Optimizador

¿Cómo reducir el tamaño de los Documentos PDF?

```java

    String input = "Test.pdf";
    String output = "Optimized.pdf";

    Optimizer optimizer = new Optimizer();

    OptimizeOptions opt = new OptimizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    optimizer.process(opt);
```

¿Cómo cambiar el tamaño de los Documentos PDF?

```java

    String input = "sample.pdf";
    String output = "ResizeMain.pdf";

    Optimizer organizer = new Optimizer();

    ResizeOptions opt = new ResizeOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));

    opt.setPageSize(PageSize.getA1());

    organizer.process(opt);
```


Cómo rotar documentos PDF?

```java

    String input = "sample.pdf";
    String output = "OptimizerRotateMain.pdf";

    Optimizer optimizer = new Optimizer();

    RotateOptions opt = new RotateOptions();
    opt.addInput(new FileDataSource(input));
    opt.addOutput(new FileDataSource(output));
    opt.setRotation(Rotation.on90);

    ResultContainer results = optimizer.process(opt);
```

## Qué hay de nuevo en Aspose.PDF 24.3

Desde la versión 24.3 se implementa una búsqueda a través de una lista de frases en un TextFragmentAbsorber.

```java

    String[] expressions = new String[] {
      // detectar número de teléfono
      "\\b\\d{3}-\\d{3}-\\d{4}\\b",
      // detectar número de tarjeta
      "\\b(?:\\d[ -]*?){13,16}\\b"
    };
    Document document = new Document(input);

    TextFragmentCollection newTextFragmentCollection = new TextFragmentCollection();

    Pattern[] regexes = new Pattern[6];
    for (int i = 0; i < expressions.length; i++) {
      regexes[i] = Pattern.compile(expressions[i], Pattern.CASE_INSENSITIVE);
    }
    TextFragmentAbsorber newAbsorber = new TextFragmentAbsorber(regexes, new TextSearchOptions(true));
    document.getPages().accept(newAbsorber);
    HashMap < Pattern, TextFragmentCollection > map = newAbsorber.getRegexResults();
```


La siguiente característica es agregar la capacidad de convertir tablas para el convertidor de PDF a Markdown

```java

    Document doc = new Document(dataDir + "56201.pdf");
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    doc.save(dataDir + "56201.md", saveOptions);
```

## Qué hay de nuevo en Aspose.PDF 24.2

Desde la versión 24.2 es posible agregar la Marca de Agua en PDF con AcroForms. TextStamp es adecuado para usar con archivos AcroForm. Si utiliza TextStamp para archivos XFA, el texto se dibuja en la página como en un archivo PDF habitual (se puede ver en aquellos visores PDF que no pueden leer archivos XFA, por ejemplo, en un navegador Chrome). Para agregar texto al archivo XFA, debe cambiarse en el XML interno del archivo XFA.

```java

    String sourceName = dataDir + "551.3xfa.pdf";
    String targetName = dataDir + "output_2_" + BuildVersionInfo.AssemblyVersion + ".pdf";

    Document pdfDocument = new Document(sourceName);
    XFA xfa = pdfDocument.getForm().getXFA();

    String watermark =
    "<subform>" +
    "<draw rotate=\"90\" x=\"100px\" y=\"100px\">" +
    "<value>" +
    "<text>Sello de Muestra</text>\n" +
    "</value>" +
    "<font typeface=\"Arial\" size=\"14px\" weight=\"bold\" posture=\"italic\">" +
    "<fill>" +
    "<color value=\"0,128,0\"/>" +
    "</fill>" +
    "</font>" +
    "</draw>" +
    "</subform>";

    xfa.appendToTemplate("//tpl:pageArea", watermark);

    pdfDocument.save(targetName);
    pdfDocument.close();
```


Set StateModel para Anotación
Podemos usar setReviewState y setMarkedState de la clase MarkupAnnotation para establecer el estado necesario.
Todas las anotaciones de marcado tienen una opción de Establecer Estado disponible.

```java

    // Abrir el documento PDF de origen
    Document pdfDocument = new Document();
    pdfDocument.getPages().add();
    // Crear anotación
    TextAnnotation textAnnotation = new TextAnnotation(pdfDocument.getPages().get_Item(1), new Rectangle(200,
            400, 400, 600));

    //Establecer el título de la anotación
    textAnnotation.setTitle("Título de Anotación de Ejemplo");

    //Establecer el asunto de la anotación
    textAnnotation.setSubject("Asunto de Ejemplo");
    //Especificar el contenido de la anotación
    textAnnotation.setContents("Contenido de ejemplo para la anotación");
    textAnnotation.setOpen(true);
    textAnnotation.setIcon(TextIcon.Key);
    com.aspose.pdf.Border border = new com.aspose.pdf.Border(textAnnotation);
    border.setWidth(5);
    border.setDash(new Dash(1, 1));
    textAnnotation.setBorder(border);
    String userName1 = "Aspose1";
    textAnnotation.setReviewState(AnnotationState.Rejected, userName1);
    textAnnotation.setRect(new Rectangle(200, 400, 400, 600));

    //Agregar la anotación en la colección de anotaciones de la página
    pdfDocument.getPages().get_Item(1).getAnnotations().add(textAnnotation);
    pdfDocument.processParagraphs();

    //Guardar el archivo de salida
    pdfDocument.save(dataDir + "output_24_2_Rejected.pdf");

    pdfDocument = new Document(dataDir + "output" + version + "3.pdf");
    TextAnnotation textAnnotation2 = (TextAnnotation) pdfDocument.getPages().get_Item(1).getAnnotations().get_Item(1);

    String userName2 = "Aspose2";
    textAnnotation2.setReviewState(AnnotationState.Accepted, userName2);
    pdfDocument.save(dataDir + "output_24_2_Rejected_and_Accepted.pdf");
```


Desde 24.2 implementar la conversión de OFD a PDF:

```java

    Document document = new Document(inputPath, new OfdLoadOptions());
    document.save(outputPath);
```

## Qué hay de nuevo en Aspose.PDF 24.1

Desde el lanzamiento 24.1 implementar la conversión de PDF a Markdown:

```java

    final Document doc = new Document(inputPdfPath);
    MarkdownSaveOptions saveOptions = new MarkdownSaveOptions();
    saveOptions.setHeadingRecognitionStrategy(HeadingRecognitionStrategy.Outlines);
    doc.save(markdownOutputFilePath, saveOptions);
```

Además, en 24.1 se ha implementado la interrupción del hilo usando el InterruptMonitor.

```java

    final InterruptMonitor monitor = new InterruptMonitor();

    new Thread(new Runnable() {

      public void run() {

        InterruptMonitor.setThreadLocalInstance(monitor);
        Document document = new Document();

        try {
          Page page = document.getPages().insert(1);
          PageInfo pageInfo = page.getPageInfo();
          pageInfo.setLandscape(true);
          Table topicTable = new Table();
          topicTable.setBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setDefaultCellBorder(new BorderInfo(BorderSide.All, 0.5 f, Color.getBlack()));
          topicTable.setColumnWidths("5% 10% 5% 60% 10% 10%");
          topicTable.setRepeatingRowsCount(1);

          Row topicRow = topicTable.getRows().add();

          topicRow.getCells().add("texto");
          topicRow.getCells().add("texto");
          topicRow.getCells().add("texto");
          topicRow.getCells().add("texto");
          topicRow.getCells().add("texto");
          topicRow.getCells().add("texto");

          // conversión de foreach a while statements
          Iterator tmp0 = (topicRow.getCells()).iterator();
          while (tmp0.hasNext()) {
            Cell cell = (Cell) tmp0.next();
            cell.setVerticalAlignment(VerticalAlignment.Center);
            cell.setAlignment(HorizontalAlignment.Center);
          }

          Row row2 = topicTable.getRows().add();
          row2.getCells().add("texto");
          row2.getCells().add("texto");
          row2.getCells().add("texto");
          String LongText = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus.";
          row2.getCells().add(LongText);
          row2.getCells().add("texto");
          row2.getCells().add("texto");
          page.getParagraphs().add(topicTable);
          document.save(dataDir + "out" + version + ".pdf");

        } catch (com.aspose.pdf.exceptions.OperationCanceledException ex) {
          System.out.println("Interrumpiendo el hilo de guardado en " + System.currentTimeMillis());
        } finally {
          if (document != null) {
            document.close();
          }
        }

      }

    }).start();

    System.out.println("El proceso ha comenzado el hilo en " + System.currentTimeMillis());

    // El tiempo de espera debe ser menor que el tiempo necesario para guardar el documento completo (sin interrupción).
    Thread.sleep(500);

    // Interrumpir el proceso
    monitor.interrupt();

    System.out.println("Interrumpido el hilo de guardado en " + System.currentTimeMillis());
```


## Qué hay de nuevo en Aspose.PDF 23.12

El formulario se puede encontrar y el texto se puede reemplazar utilizando el siguiente fragmento de código:

```java

    Document document = new Document(input);
    String expectedText = "Este es un texto añadido mientras se crea un nuevo PDF en Kofx Power PDF Standard.";

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
      XForm form = (XForm) tmp0.next();
      if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        absorber.visit(form);

        Iterator tmp1 = (absorber.getTextFragments()).iterator();
        while (tmp1.hasNext()) {
          TextFragment fragment = (TextFragment) tmp1.next();
          fragment.setText("");
        }
      }
    }

    document.save(output);
```            

O el formulario se puede eliminar completamente:

```java

    Document document = new Document(input);
    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    // Conversión de sentencias foreach a while
    Iterator tmp0 = (forms).iterator();
    while (tmp0.hasNext()) {
        XForm form = (XForm) tmp0.next();
        if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
            String name = forms.getFormName(form);
            forms.delete(name);
        }
    }

    document.save(output);
```            


Otra variante de eliminar el formulario:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    for (int i = 1; i <= forms.size(); i++) {
        if ("Typewriter".equals(forms.get_Item(i).getIT()) && "Form".equals(forms.get_Item(i).getSubtype())) {
            forms.delete(forms.get_Item(i).getName());
        }
    }

    document.save(output);
``` 

- Todos los formularios se pueden eliminar usando el siguiente fragmento de código:

```java

    Document document = new Document(input);

    XFormCollection forms = document.getPages().get_Item(1).getResources().getForms();

    forms.clear();

    document.save(output);
```

## Qué hay de nuevo en Aspose.PDF 23.11

A partir de esta versión es posible eliminar texto oculto del archivo PDF:

```java

    Document document = new Document(inputFile);

    TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber();
    textAbsorber.setTextReplaceOptions(new TextReplaceOptions(TextReplaceOptions.ReplaceAdjustment.None));
    document.getPages().accept(textAbsorber);

    msStringBuilder result = new msStringBuilder();

    // Conversión de declaraciones foreach a while
    Iterator tmp0 = (textAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext()) {
            TextFragment fragment = (TextFragment) tmp0.next();
            if (fragment.getTextState().isInvisible()) {
                result.append(fragment.getText());
                fragment.setText("");
            }
        }

    document.save(outputFile);
```


## Novedades en Aspose.PDF 23.10

La actualización actual presenta tres versiones de eliminación de etiquetas de PDFs etiquetados.

- Eliminar algún elemento nodo de un documentElement (elemento raíz del árbol):

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element documentElement = structure.getChildren().get_Item(0);
    Element structElement = (documentElement.getChildren().getCount() > 1) ?  documentElement.getChildren().get_Item(1) : null;
    documentElement.getChildren().remove(structElement);
    // También puede eliminar el structElement en sí
                //if (structElement != null)
                //{
                //    structElement.remove();
                //}
    document.save(outputPath);
```

- Eliminar todas las etiquetas de elementos marcados del documento, pero mantener los elementos de estructura:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root= structure.getChildren().get_Item(0);
    Queue<Element> queue = new ArrayDeque<Element>();
    queue.add(root);
    for (Element element : structure.getChildren() ) {
        queue.add(element);
        for (Element child : element.getChildren())
        {
            queue.add(child);
        }
    }
    for (Element element:queue ) {
        if (element instanceof TextElement  || element instanceof FigureElement)
            element.remove();
    }
    document.save(outputPath);
```


- Eliminar todas las etiquetas:

```java

    Document document = new Document(inputPath);
    RootElement structure = document.getLogicalStructure();
    Element root = structure.getChildren().get_Item(0);
    root.remove();
    document.save(outputPath);
```

Hemos implementado una nueva función para medir la altura de un carácter. Usa el siguiente código para medir la altura de un carácter:

```java

    Document doc = new Document("input.pdf");
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    absorber.visit(doc.getPages().get_Item(1));
    double height = absorber.getTextFragments().get_Item(1).getTextState().measureHeight('h')
```

Nota que la medición se basa en la fuente incrustada en el documento. Si falta alguna información para una dimensión, este método devuelve 0.

## Qué hay de nuevo en Aspose.PDF 23.9

A partir de la versión 23.9 se admite la eliminación de una anotación hija de un campo rellenable.

ejemplo 1:

```java

    String input = "55343_1.pdf";
    Document doc = new Document(input);
    final String fieldName = "1 Vehicle Identification Number";
    Field field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
    Rectangle rect = field.getRect();
    doc.getForm().addFieldAppearance(field, 2, rect);
    System.out.println(2 == field.size());

    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(2 == field.size());
    doc.getForm().removeFieldAppearance(field, 1);

    System.out.println(0 == field.size());
    field = (Field) doc.getForm().get_Item(fieldName);
    System.out.println(0 == field.size());
```


example 2:

```java

    {
    String option1 = "opción 1";
    String option2 = "opción 2";
    String outputPdf = "salida.pdf";

    final Document document = new Document();
    try /*JAVA: se estaba usando*/ {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 50, 70, 70));

        // Establecer el valor de la primera opción del grupo de casillas de verificación
        checkbox.setExportValue(option1);
        checkbox.addOption(option2);
        document.getForm().add(checkbox);
        java.util.List < String > tmp0 = new ArrayList < String > ();
        tmp0.add("Off");
        tmp0.add(option1);
        tmp0.add(option2);
        System.out.println(collectionAssert_AreEqual(tmp0, checkbox.getAllowedStates()));
        checkbox.setValue(option2);

        WidgetAnnotation f = document.getForm().get_Item(1);
        document.getForm().removeFieldAppearance((Field) f, 2);

        checkbox = (CheckboxField) document.getForm().get_Item(1);
        java.util.List < String > tmp1 = new java.util.ArrayList < String > ();
        tmp1.add("Off");
        tmp1.add(option1);
        System.out.println(collectionAssert_AreEqual(tmp1, checkbox.getAllowedStates()));

        document.save(outputPdf);
    } finally {
        if (document != null)(document).close();
    }
    }
    public static boolean collectionAssert_AreEqual(java.util.List < String > value1,
    java.util.List < String > value2) {
    if (value1.size() == value2.size()) {
        for (int i = 0; i < value1.size(); i++) {
        if (!value1.get(i).equals(value2.get(i)))
            return false;
        }
    } else {
        return false;
    }
    return true;
    }
```


Agregar imagen con ImageFilterType.Flate no preserva la transparencia.

```java

    Document document = new Document();
    Page page = document.getPages().add();

    FileInputStream stream = new FileInputStream(("55037_1.png"));

    page.getResources().getImages().addWithImageFilterType(stream, ImageFilterType.Flate);
    page.getContents().add(new GSave());
    Rectangle rectangle = new Rectangle(413, 428, 548, 564);
    Matrix matrix = new Matrix(
      new double[] {
        rectangle.getURX() - rectangle.getLLX(), 0, 0, rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY()
      });

    page.getContents().add(new ConcatenateMatrix(matrix));
    XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
    page.getContents().add(new Do(ximage.getName()));
    page.getContents().add(new GRestore());
    document.save(getOutputPath("55157.pdf"));
    stream.close();
```

## Qué hay de nuevo en Aspose.PDF 23.8

La función para detectar Actualizaciones Incrementales en un documento PDF se ha añadido en la versión 23.8. Esta función devuelve 'true' cuando el documento se guardó con actualizaciones incrementales, de lo contrario, devuelve 'false'.

```java

    Document doc = new Document(dataDir+"PDF_Support_Tech_Note.pdf");
    boolean not_updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(not_updatedIncrementally);

    doc.getPages().add();
    doc.saveIncrementally(dataDir+"PDF_updatedIncrementally.pdf");

    doc = new Document(dataDir+"PDF_updatedIncrementally.pdf");
    boolean updatedIncrementally = doc.hasIncrementalUpdate();
    System.out.println(updatedIncrementally);
    doc.close();
```

Otra característica más es Copiar OutputIntents del PDF de entrada al PDF de destino.

Añadimos una nueva propiedad pública Document.getOutputIntents() para permitir el acceso a las intenciones de salida en un documento.
Por el momento, solo se admite el uso de intenciones de salida ya existentes en algunos documentos, el usuario no puede crear OutputIntent desde cero.

```java

    Document document1 = new Document(dataDir+"pdfa.pdf");
    Document resultDocument = new Document();
    resultDocument.getPages().add(document1.getPages());

    for (OutputIntent intent : document1.getOutputIntents())
    {
        resultDocument.getOutputIntents().addItem(intent);
    }

    resultDocument.save(dataDir+"resultpath.pdf");
```  


Desde Aspose.PDF 23.8 soporte para agregar la extracción de formas:

```java

{
    String input1 = getInputPdf("46298_1");
    String input2 = getInputPdf("46298_2");

    Document source = new Document(input1);
    Document dest = new Document(input2);

    Page destPage = dest.getPages().get_Item(1);

    TextFragmentAbsorber tfAbsorber = new TextFragmentAbsorber();
    tfAbsorber.visit(source.getPages().get_Item(1));

    // Conversión de foreach a while
    Iterator tmp0 = ( tfAbsorber.getTextFragments()).iterator();
        while (tmp0.hasNext())
        {
            TextFragment textFragment = (TextFragment)tmp0.next();
            System.out.println(textFragment.getText());
            addTextImproved(destPage, textFragment);
        }

    ImagePlacementAbsorber imageAbsorber = new ImagePlacementAbsorber();
    imageAbsorber.visit(source);

    Iterator tmp1 = ( imageAbsorber.getImagePlacements()).iterator();
        while (tmp1.hasNext())
        {
            ImagePlacement image = (ImagePlacement)tmp1.next();
            destPage.addImage(image.getImage().toStream(), image.getRectangle());
        }

    GraphicsAbsorber vectorAbsorber = new GraphicsAbsorber();
    vectorAbsorber.visit(source.getPages().get_Item(1));
    Rectangle area = new Rectangle(90, 250, 300, 400);
    dest.getPages().get_Item(1).addGraphics(vectorAbsorber.getElements(), area);
    dest.save(getOutputPath("46298-out.pdf"));
    }

    private static void addTextImproved(Page page, TextFragment textFragment)
    {
        TextFragment local = new TextFragment();
        local.setPosition(textFragment.getPosition());

        // Recalcular una nueva posición ya que el tamaño de la página difiere del PDF original
        local.getPosition().setXIndent(textFragment.getPosition().getXIndent());//2.5 * 72;
        double newPageHeight = page.getPageRect(true).getHeight();
        double oldPageHeight = textFragment.getPage().getPageRect(true).getHeight();
        local.getPosition().setYIndent(textFragment.getPosition().getYIndent());

        local.setText(textFragment.getText());
        local.getTextState().setFont(textFragment.getTextState().getFont());
        local.getTextState().setFontSize(textFragment.getTextState().getFontSize());

        local.getTextState().setFormattingOptions(textFragment.getTextState().getFormattingOptions());
        local.getTextState().setForegroundColor(textFragment.getTextState().getForegroundColor());

        TextBuilder textBuilder = new TextBuilder(page);
        textBuilder.appendText(local);
    }
```


También admite la capacidad de detectar desbordamiento al agregar texto:

```java

    Document doc = new Document();
    String paragraphContent = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras nisl tortor, efficitur sed cursus in, lobortis vitae nulla. Quisque rhoncus, felis sed dictum semper, est tellus finibus augue, ut feugiat enim risus eget tortor. Nulla finibus velit nec ante gravida sollicitudin. Morbi sollicitudin vehicula facilisis. Vestibulum ac convallis erat. Ut eget varius sem. Nam varius pharetra lorem, id ullamcorper justo auctor ac. Integer quis erat vitae lacus mollis volutpat eget et eros. Donec a efficitur dolor. Maecenas non dapibus nisi, ut pellentesque elit. Sed pellentesque rhoncus ante, a consectetur ligula viverra vel. Integer eget bibendum ante. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur elementum, sem a auctor vulputate, ante libero iaculis dolor, vitae facilisis dolor lorem at orci. Sed laoreet dui id nisi accumsan, id posuere diam accumsan.";
    Rectangle rectangle = new Rectangle(100, 600, 500, 700, false);
    TextParagraph paragraph = new TextParagraph();
    TextFragment fragment = new TextFragment(paragraphContent);
    paragraph.setVerticalAlignment(VerticalAlignment.Top);
    paragraph.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);
    paragraph.setRectangle(rectangle);
    boolean isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    while (!isFitRectangle)
    {
        fragment.getTextState().setFontSize(fragment.getTextState().getFontSize() - 0.5f);
        isFitRectangle = fragment.getTextState().isFitRectangle(paragraphContent, rectangle);
    }
    paragraph.appendLine(fragment);
    TextBuilder builder = new TextBuilder(doc.getPages().add());
    builder.appendParagraph(paragraph);
    doc.save(output);
```


## Novedades en Aspose.PDF 23.7

Desde la versión 23.7 se admite la escala de página de los preajustes del cuadro de diálogo de impresión:

```java

    Document document = new Document();
    document.getPages().add();
    document.setPrintScaling(PrintScaling.None);//PrintScaling.Default
    document.save(outputPdf);

    Document documentOutput = new Document(outputPdf);
    int printScaling = documentOutput.getPrintScaling();
    System.out.println("PrintScaling: " + printScaling);
```

## Novedades en Aspose.PDF 23.6

Desde la versión 23.6 se admite la capacidad de establecer el título de la página HTML, Epub.

código para HTML:

```java

    HtmlSaveOptions options = new HtmlSaveOptions();
    options.setFixedLayout(true);
    options.setRasterImagesSavingMode(HtmlSaveOptions.RasterImagesSavingModes.AsEmbeddedPartsOfPngPageBackground);
    options.setPartsEmbeddingMode(HtmlSaveOptions.PartsEmbeddingModes.EmbedAllIntoHtml);
    options.setTitle("</title>NEW PAGE & TITILE</head>");

    Document document = new Document(inputPath);
    document.save(outPath, options);
```


código para EPUB:

```java

    EpubSaveOptions epubSaveOptions = new EpubSaveOptions();
    epubSaveOptions.setTitle("</title>NUEVA PÁGINA & TÍTULO</head>");
    epubSaveOptions.setContentRecognitionMode(EpubSaveOptions.RecognitionMode.PdfFlow);

    Document document = new Document(inputPath);
    document.save(outPath, epubSaveOptions);
```

Desde 23.6 soporte para proporcionar una API para posicionar gráficos vectoriales:

```java

    Document document = new Document(input);
    VectorGraphicsAbsorber vectorAbsorber = new VectorGraphicsAbsorber();
    vectorAbsorber.visit(document.getPages().get_Item(1));

    SubPath subPath1 = vectorAbsorber.getSubPaths().get_Item(2);
    SubPath subPath2 = vectorAbsorber.getSubPaths().get_Item(3);
    SubPath subPath3 = vectorAbsorber.getSubPaths().get_Item(4);

    Point point1 = new Point(subPath1.getPosition().getX() + 200, subPath1.getPosition().getY() - 100);
    Point point2 = new Point(subPath2.getPosition().getX() + 200, subPath2.getPosition().getY() - 100);
    Point point3 = new Point(subPath3.getPosition().getX() + 200, subPath3.getPosition().getY() - 100);

    subPath1.setPosition(point1);
    subPath2.setPosition(point2);
    subPath3.setPosition(point3);

    document.save(output);
```

## Qué hay de nuevo en Aspose.PDF 23.1

Desde la versión 23.1, soporte para crear anotaciones PrinterMark. Se añadió una de las variantes de anotación: ColorBarAnnotation.

```java

    Document doc = new Document();
    Page page = doc.getPages().add();
    page.setTrimBox(new com.aspose.pdf.Rectangle(20, 20, 580, 820));
    Rectangle rectBlack = new com.aspose.pdf.Rectangle(100, 300, 300, 320);
    Rectangle rectCyan = new com.aspose.pdf.Rectangle(200, 600, 260, 690);
    Rectangle rectMagenta = new com.aspose.pdf.Rectangle(10, 650, 140, 670);

    ColorBarAnnotation colorBarBlack = new ColorBarAnnotation(page, rectBlack);
    ColorBarAnnotation colorBarCyan = new ColorBarAnnotation(page, rectCyan, ColorsOfCMYK.Cyan);
    ColorBarAnnotation colorBaMagenta = new ColorBarAnnotation(page, rectMagenta);
    colorBaMagenta.setColorOfCMYK(ColorsOfCMYK.Magenta);
    ColorBarAnnotation colorBarYellow = new ColorBarAnnotation(page, new com.aspose.pdf.Rectangle(400, 250, 450, 700), ColorsOfCMYK.Yellow);

    page.getAnnotations().add(colorBarBlack);
    page.getAnnotations().add(colorBarCyan);
    page.getAnnotations().add(colorBaMagenta);
    page.getAnnotations().add(colorBarYellow);
    doc.save("outFile.pdf");
```


## Qué hay de nuevo en Aspose.PDF 22.12

Desde esta versión, soporte para convertir PDF a imagen DICOM:

```java

    DicomDevice device = new DicomDevice(PageSize.getA4());
    Document doc = new Document("Input.pdf");
    ByteArrayOutputStream stream = new ByteArrayOutputStream();
    device.process(doc.getPages().get_Item(1), stream);
```

## Qué hay de nuevo en Aspose.PDF 22.9

Desde 22.09, soporte para agregar propiedad para modificar el orden de las rúbricas del sujeto (E=, CN=, O=, OU=, ) en la firma.

```java

    String inputPdf = getInputPath("input.pdf");
    String inputPfx = getInputPath("input.pfx");
    String outputPdf = getOutputPath("out.pdf");

    final PdfFileSignature fileSign = new PdfFileSignature();
    try 
    {
        fileSign.bindPdf(inputPdf);
        java.awt.Rectangle rect = new java.awt.Rectangle(100, 100, 400, 100);
        PKCS7Detached signature = new PKCS7Detached(inputPfx, "123456789");
        signature.setDate(new Date());
        signature.setCustomAppearance( new SignatureCustomAppearance());
        signature.getCustomAppearance().setUseDigitalSubjectFormat(true);
        signature.getCustomAppearance().setDigitalSubjectFormat(new /*SubjectNameElements*/int[] { SubjectNameElements.CN, SubjectNameElements.O });

        fileSign.sign(1, true, rect, signature);
        fileSign.save(outputPdf);
    }
    finally { 
        if (fileSign != null) 
            fileSign.close(); 
    }
```

## Qué hay de nuevo en Aspose.PDF 22.8

Desde Aspose.PDF 23.8 soporte para agregar método para reconstruir la tabla xref:

```java

    PdfFileSanitization sanitizer = new PdfFileSanitization();
    try {
        sanitizer.bindPdf(dataDir + "50528_1.pdf");
        sanitizer.rebuildXrefAndTrailer();
        sanitizer.save(dataDir + "50528_1" + version + ".pdf");
    } finally {
        if (sanitizer != null) ( sanitizer).close();
    }
```

## Qué hay de nuevo en Aspose.PDF 22.6

PDF a PDF_A_1A - implementar opción para eliminar el color de transparencia para evitar un tamaño de archivo de salida grande.

Desde la versión 22.5 el cliente es capaz de controlar la calidad de la transparencia convertida, y el tamaño del archivo de salida como resultado:

```java
    opts.setTransparencyResolution(300);
```

## Qué hay de nuevo en Aspose.PDF 22.5

Durante la conversión a PDF/A se elimina el contenido transparente y se reemplaza con una imagen. Hemos implementado una nueva característica, y ahora el cliente puede controlar la calidad de la imagen con el parámetro TransparencyResolution:

```java

    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document("input.pdf");
    PdfFormatConversionOptions options = new PdfFormatConversionOptions("log.xml", PdfFormat.PDF_A_1A, ConvertErrorAction.Delete);
    options.setTransparencyResolution(300);
    pdfDocument.convert(options);
    pdfDocument.save("finalOutput.pdf");
```


## Qué hay de nuevo en Aspose.PDF 22.4

Esta versión incluye información para Aspose.PDF para Java:

- PDF a ODS: Reconocer texto en subíndice y superíndice;

**ejemplo**

```java

    Document pdfDocument = new Document("Superscript-Subscript.pdf");
    ExcelSaveOptions options = new ExcelSaveOptions();
    options.Format = ExcelSaveOptions.ExcelFormat.ODS;
    pdfDocument.Save("output.ods"), options);
```

- PDF a XMLSpreadSheet2003: Reconocer texto en subíndice y superíndice;

- PDF a Excel: Reconocer texto en subíndice y superíndice;

## Qué hay de nuevo en Aspose.PDF 22.3

PDF a ODS: Soporte para RTL está disponible en la versión 22.3

```java

    ExcelSaveOptions options = new ExcelSaveOptions();
    options.setFormat(ExcelSaveOptions.ExcelFormat.ODS);
    pdfDocument.save("output.ods", options);
```

## Qué hay de nuevo en Aspose.PDF 22.2

Esta versión incluye PDF a XSLX: Soporte para RTL (Hebreo, Árabe).

## Qué hay de nuevo en Aspose.PDF 22.1

Aspose.PDF para Java permite cargar documentos en formato de documento portátil (PDF) versión 2.0.

## ¿Qué hay de nuevo en Aspose.PDF 21.10?

### ¿Cómo detectar texto oculto?

Por favor, use el siguiente código:

```java

Document pdf = new Document(inFile);
        Page page = pdf.getPages().get_Item(1);
        TextFragmentAbsorber textFragmentAbsorber = new com.aspose.pdf.TextFragmentAbsorber();
        page.accept(textFragmentAbsorber);
        TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

        int fragmentsCount = textFragmentAbsorber.getTextFragments().size();
        int invisibleCount = 0;

        Iterator tmp0 = ( textFragmentCollection).iterator();
            while (tmp0.hasNext())
            {
                com.aspose.pdf.TextFragment fragment = (com.aspose.pdf.TextFragment)tmp0.next();
                System.out.println(fragment.getText());
                System.out.println(fragment.getTextState().isInvisible());
                if (fragment.getTextState().isInvisible())
                    invisibleCount++;
            }
```


## Qué hay de nuevo en Aspose.PDF 21.8

### ¿Cómo cambiar el color del texto en la Firma Digital?

En la versión 21.8, setForegroundColor permite cambiar el color del texto en la Firma Digital:

```java
Por favor, use el siguiente código:

                    PdfFileSignature pdfSign = new PdfFileSignature();                
                    pdfSign.bindPdf(inFile);
                    //crear un rectángulo para la ubicación de la firma
                    java.awt.Rectangle rect = new java.awt.Rectangle(310, 45, 200, 50);
                    PKCS7 pkcs = new PKCS7(inPfxFile, "");

                    pkcs.setCustomAppearance(new SignatureCustomAppearance());
//establecer color del texto
                    pkcs.getCustomAppearance().setForegroundColor(Color.getGreen());

                    // firmar el archivo PDF
                    pdfSign.sign(1, true, rect, pkcs);
                    //guardar el archivo PDF de salida
                    pdfSign.save(outFile);
```

## Qué hay de nuevo en Aspose.PDF 21.6

### Ocultando imagen usando ImagePlacementAbsorber del documento

Con Aspose.PDF para Java puedes ocultar imágenes usando ImagePlacementAbsorber del documento:

```java
      Document doc = new Document("input.pdf");

        for (Page page : doc.getPages()) {
            ImagePlacementAbsorber ipa = new ImagePlacementAbsorber();
            ipa.visit(page);
            for (ImagePlacement ip : ipa.getImagePlacements()) {
                ip.hide();
            }
        }

        doc.save("out.pdf");
```

## Qué hay de nuevo en Aspose.PDF 21.5

### Añadir API para fusionar imágenes

Aspose.PDF 21.4 te permite combinar Imágenes. Fusiona una lista de flujos de imágenes como un solo flujo de imagen. Se admiten formatos de salida Png/jpg/tiff; en caso de usar un formato no soportado, el flujo de salida se codifica como Jpeg por defecto.
Sigue el siguiente fragmento de código:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile300dpi = new FileInputStream("image1.jpg");
        try  {
            inputImagesStreams.add(inputFile300dpi);
            InputStream inputFile600dpi = new FileInputStream("image2.jpg");
            try {
                inputImagesStreams.add(inputFile600dpi);
                inputStream = PdfConverter.mergeImages(
                        inputImagesStreams,
                        com.aspose.pdf.ImageFormat.Jpeg,
                        ImageMergeMode.Vertical,
                        new Integer(1),
                        new Integer(1)
                );
            } finally {
                if (inputFile600dpi != null) (inputFile600dpi).close();
            }
        } finally {
            if (inputFile300dpi != null) (inputFile300dpi).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out.pdf");
        inputStream.close();
```


También puede combinar sus imágenes en formato Tiff:

```java
InputStream inputStream;

        ArrayList<InputStream> inputImagesStreams = new ArrayList<InputStream>();
        InputStream inputFile1 = new FileInputStream("1.tif");
        try  {
            inputImagesStreams.add(inputFile1);
            InputStream inputFile2 = new FileInputStream("2.tif");
            try {
                inputImagesStreams.add(inputFile2);
                inputStream = PdfConverter.mergeImagesAsTiff(inputImagesStreams);
            } finally {
                if (inputFile2 != null) (inputFile2).close();
            }
        } finally {
            if (inputFile1 != null) (inputFile1).close();
        }

        Document doc = new Document();
        Page p = doc.getPages().add();
        Image image = new Image();
        image.setImageStream(inputStream);
        p.getParagraphs().add(image);
        doc.save("out2.pdf");
        inputStream.close();
```

## Qué hay de nuevo en Aspose.PDF 21.02

Aspose.PDF v21.02 Firmar PDF con Firmas PAdES LTV

```java
final Document document = new Document(inputPdf);
    try 
    {
        PdfFileSignature signature = new PdfFileSignature(document);
        PKCS7 pkcs7 = new PKCS7(getInputPath("cert.pfx"), "password");
        //Firmar PDF con Firmas PAdES LTV
        pkcs7.setUseLtv(true);

        signature.sign(1, true, new Rectangle(100, 100, 300, 300), pkcs7);
        signature.save(outputPdf);
    }
    finally { if (document != null) (document).dispose(); }
```