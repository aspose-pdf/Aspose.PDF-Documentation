---
title: Trabajando con Operadores
linktitle: Trabajando con Operadores
type: docs
weight: 170
url: /java/operators/
description: Este tema explica cómo usar operadores con Aspose.PDF. Las clases de operadores proporcionan grandes características para la manipulación de PDF.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Introducción a los Operadores PDF y su Uso

Un operador es una palabra clave de PDF que especifica alguna acción que debe realizarse, como pintar una forma gráfica en la página. Una palabra clave de operador se distingue de un objeto nombrado por la ausencia de un carácter solidus inicial (2Fh). Los operadores solo tienen sentido dentro del flujo de contenido.

Un flujo de contenido es un objeto de flujo PDF cuyos datos consisten en instrucciones que describen los elementos gráficos que se pintarán en una página. Se pueden encontrar más detalles sobre los operadores PDF en la [especificación PDF](https://www.adobe.com/devnet/pdf/pdf_reference.html).

### Detalles de Implementación

Este tema explica cómo usar operadores con Aspose.PDF.
 El ejemplo seleccionado añade una imagen en un archivo PDF para ilustrar el concepto. Para añadir una imagen en un archivo PDF, se necesitan diferentes operadores. Este ejemplo utiliza [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do), y [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).

- El operador [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) guarda el estado gráfico actual del PDF.
- Este tema explica cómo usar operadores con Aspose.PDF. El ejemplo seleccionado agrega una imagen en un archivo PDF para ilustrar el concepto. Para agregar una imagen en un archivo PDF, se necesitan diferentes operadores. Este ejemplo utiliza [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave), [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix), [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do), y [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore).
El operador (concatenate matrix) se utiliza para definir cómo debe colocarse una imagen en la página del PDF.
- El operador [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) dibuja la imagen en la página.
- El operador [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) restaura el estado gráfico.

Para agregar una imagen en un archivo PDF:

1. Cree un objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) y abra el documento PDF de entrada.
1. Obtén la página particular a la que se va a añadir la imagen.
1. Añade la imagen a la colección de Recursos de la página.
1. Usa los operadores para colocar la imagen en la página:
   - Primero, utiliza el operador [GSave](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GSave) para guardar el estado gráfico actual.
   - Luego usa el operador [ConcatenateMatrix](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/ConcatenateMatrix) para especificar dónde se colocará la imagen.
   - Usa el operador [Do](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/Do) para dibujar la imagen en la página.
1. Finalmente, utiliza el operador [GRestore](https://reference.aspose.com/pdf/java/com.aspose.pdf.operators/GRestore) para guardar el estado gráfico actualizado.

El siguiente fragmento de código muestra cómo usar los operadores de PDF.

```java
public class WorkingWithOperators {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Operators/";

    public static void AddImageUsingOpeartors() {

        // Crea un nuevo documento PDF
        Document pdfDocument = new Document(_dataDir + "PDFOperators.pdf");

        // Obtén la página donde se necesita añadir la imagen
        Page page = pdfDocument.getPages().get_Item(1);

        // Establece las coordenadas
        int lowerLeftX = 100;
        int lowerLeftY = 100;
        int upperRightX = 200;
        int upperRightY = 200;

        // Carga la imagen en el flujo
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(_dataDir + "PDFOperators.jpg");
        } catch (FileNotFoundException e) {
            // TODO Bloque catch auto-generado
            e.printStackTrace();
        }

        // Añadir imagen a la colección de Imágenes de los Recursos de la Página
        page.getResources().getImages().add(imageStream);

        // Usando el operador GSave: este operador guarda el estado gráfico actual
        page.getContents().add(new GSave());
        // Crear objetos Rectángulo y Matriz
        Rectangle rectangle = new Rectangle(lowerLeftX, lowerLeftY, upperRightX, upperRightY);
        Matrix matrix = new Matrix(new double[] { rectangle.getURX() - rectangle.getLLX(), 0, 0,
                rectangle.getURY() - rectangle.getLLY(), rectangle.getLLX(), rectangle.getLLY() });

        // Usando el operador ConcatenateMatrix (concatenar matriz): define cómo debe
        // colocarse la imagen
        page.getContents().add(new ConcatenateMatrix(matrix));

        XImage ximage = page.getResources().getImages().get_Item(page.getResources().getImages().size());
        // Usando el operador Do: este operador dibuja la imagen
        page.getContents().add(new Do(ximage.getName()));
        // Usando el operador GRestore: este operador restaura el estado gráfico
        page.getContents().add(new GRestore());

        // Guarda el documento actualizado
        pdfDocument.save(_dataDir + "PDFOperators_out.pdf");
    }
```


## Dibujar XForm en la Página usando Operadores

Este tema demuestra cómo usar los operadores GSave/GRestore, el operador ConcatenateMatrix para posicionar un xForm y el operador Do para dibujar un xForm en una página.

El código a continuación envuelve los contenidos existentes de un archivo PDF con el par de operadores GSave/GRestore. Este enfoque ayuda a obtener el estado gráfico inicial al final de los contenidos existentes. Sin este enfoque, podrían quedar transformaciones indeseables al final de la cadena de operadores existente.

```java
    public static void DrawXFormUsingOpeartors() {
        String imageFile = _dataDir + "aspose-logo.jpg";
        String inFile = _dataDir + "DrawXFormOnPage.pdf";
        String outFile = _dataDir + "blank-sample2_out.pdf";

        Document pdfDocument = new Document(inFile);
        OperatorCollection pageContents = pdfDocument.getPages().get_Item(1).getContents();

        // El ejemplo demuestra
        // uso de operadores GSave/GRestore
        // uso del operador ConcatenateMatrix para posicionar xForm
        // uso del operador Do para dibujar xForm en la página

        // Envolver los contenidos existentes con el par de operadores GSave/GRestore
        // esto es para obtener el estado gráfico inicial al final de los contenidos existentes
        // de lo contrario, podrían quedar algunas transformaciones indeseables al final de
        // la cadena de operadores existente
        pageContents.insert(1, new GSave());
        pageContents.add(new GRestore());

        // Agregar operador de estado gráfico de guardado para limpiar adecuadamente el estado gráfico después de
        // nuevos comandos
        pageContents.add(new GSave());

        // Crear xForm
        XForm form = XForm.createNewForm(pdfDocument.getPages().get_Item(1), pdfDocument);
        pdfDocument.getPages().get_Item(1).getResources().getForms().add(form);
        form.getContents().add(new GSave());

        // Definir ancho y alto de imagen
        form.getContents().add(new ConcatenateMatrix(200, 0, 0, 200, 0, 0));

        // Cargar imagen en flujo
        FileInputStream imageStream = null;
        try {
            imageStream = new FileInputStream(imageFile);
        } catch (FileNotFoundException e) {
            // TODO Bloque catch generado automáticamente
            e.printStackTrace();
        }

        // Agregar imagen a la colección de Imágenes de los Recursos de XForm
        form.getResources().getImages().add(imageStream);
        XImage ximage = form.getResources().getImages().get_Item(form.getResources().getImages().size());
        // Usando el operador Do: este operador dibuja la imagen
        form.getContents().add(new Do(ximage.getName()));
        form.getContents().add(new GRestore());

        pageContents.add(new GSave());
        // Colocar formulario en las coordenadas x=100 y=500
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 500));
        // Dibujar formulario con el operador Do
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        pageContents.add(new GSave());

        // Colocar formulario en las coordenadas x=100 y=300
        pageContents.add(new ConcatenateMatrix(1, 0, 0, 1, 100, 300));

        // Dibujar formulario con el operador Do
        pageContents.add(new Do(form.getName()));
        pageContents.add(new GRestore());

        // Restaurar el estado gráfico con GRestore después del GSave
        pageContents.add(new GRestore());
        pdfDocument.save(outFile);
    }
```


## Eliminar objetos gráficos usando clases de operador

Las clases de operador proporcionan grandes características para la manipulación de PDF. Cuando un archivo PDF contiene gráficos que no se pueden eliminar utilizando el método [DeleteImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor#deleteImage--) de la clase [PdfContentEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfContentEditor), se pueden usar las clases de operador para eliminarlos en su lugar.

El siguiente fragmento de código muestra cómo eliminar gráficos. Tenga en cuenta que si el archivo PDF contiene etiquetas de texto para los gráficos, podrían persistir en el archivo PDF utilizando este enfoque. Por lo tanto, busque los operadores gráficos para un método alternativo para eliminar dichas imágenes.

```java
    public static void RemoveGraphicsOpeartors() {
        Document pdfDocument  = new Document(_dataDir+ "RemoveGraphicsObjects.pdf");
        Page page = pdfDocument.getPages().get_Item(2);
        OperatorCollection oc = page.getContents();

        // Operadores de pintura de ruta utilizados
        Operator[] operators = new Operator[] {
                new Stroke(),
                new ClosePathStroke(),
                new Fill()
        };

        oc.delete(operators);
        pdfDocument.save(_dataDir+ "No_Graphics_out.pdf");
    }
```


## Cambio del Espacio de Color de un Documento PDF

{{% alert color="primary" %}}

Aspose.PDF para Java 9.0.0 soporta cambiar el espacio de color de un documento PDF. Es posible cambiar el color RGB a CMYK y viceversa.

{{% /alert %}}

Los siguientes métodos han sido implementados en la clase [Operator](https://reference.aspose.com/java/pdf/com.aspose.pdf/Operator) para permitirte cambiar el espacio de color. Úsalo para cambiar algunos colores RGB/CMYK específicos al espacio de color CMYK/RGB, manteniendo el resto del documento PDF tal como está.

{{% alert color="primary" %}}
**Cambios en la API Pública**
Los siguientes métodos están implementados:

- com.aspose.pdf.Operator.SetRGBColorStroke.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetRGBColor.getCMYKColor(new double[3], new double[4])
- com.aspose.pdf.Operator.SetCMYKColorStroke.getRGBColor(new double[4], new double[3])
- com.aspose.pdf.Operator.SetCMYKColor.getRGBColor(new double[4], new double[3])

{{% /alert %}}

El siguiente fragmento de código demuestra cómo cambiar el espacio de color utilizando Aspose.PDF para Java.

```java
Document doc = new Document("input_color.pdf");
OperatorCollection contents = doc.getPages().get_Item(1).getContents();
System.out.println("Valores de los operadores de color RGB en el documento pdf");
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetRGBColor || oper instanceof Operator.SetRGBColorStroke)
        try {
            // Convirtiendo color RGB a CMYK
            System.out.println(oper.toString());

            double[] rgbFloatArray = new double[] { Double.valueOf(oper.getParameters().get(0).toString()), Double.valueOf(oper.getParameters().get(1).toString()), Double.valueOf(oper.getParameters().get(2).toString()), };
            double[] cmyk = new double[4];
            if (oper instanceof Operator.SetRGBColor) {
                ((Operator.SetRGBColor) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColor(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else if (oper instanceof Operator.SetRGBColorStroke) {
                ((Operator.SetRGBColorStroke) oper).getCMYKColor(rgbFloatArray, cmyk);
                contents.set_Item(j, new Operator.SetCMYKColorStroke(cmyk[0], cmyk[1], cmyk[2], cmyk[3]));
            } else
                throw new java.lang.Throwable("Comando no soportado");

        } catch (Throwable e) {
            e.printStackTrace();
        }
}
doc.save("input_colorout.pdf");

// Probando el resultado
System.out.println("Valores de los operadores de color CMYK convertidos en el documento pdf resultado");
doc = new Document("input_colorout.pdf");
contents = doc.getPages().get_Item(1).getContents();
for (int j = 1; j <= contents.size(); j++) {
    Operator oper = contents.get_Item(j);
    if (oper instanceof Operator.SetCMYKColor || oper instanceof Operator.SetCMYKColorStroke) {
        System.out.println(oper.toString());
    }
}
```