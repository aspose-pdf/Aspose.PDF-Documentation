---
title: Migrando su código a Aspose.PDF para Java 2.5.0
type: docs
weight: 10
url: es/java/migrating-your-code-to-aspose-pdf-for-java-2-5-0/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

En este artículo hemos intentado resaltar algunas de las áreas de un código existente de Aspose.PDF para Java para hacerlo compatible con la última versión publicada.

{{% /alert %}}

## Detalles

Con el lanzamiento de Aspose.PDF para Java 2.5.0, ha habido muchos cambios en la estructura de la API y la construcción de clases. La mayoría de los nombres de los miembros de clase se han actualizado, se han eliminado algunos miembros de clase existentes y también se han agregado algunos métodos y propiedades más a las clases existentes. Solo para darle un resumen de los cambios, vamos a echar un vistazo al siguiente código simple, basado en versiones de Aspose.PDF para Java publicadas antes de la 2.5.0.

En este código simple, agregaremos un hipervínculo y un enlace a la página dentro del mismo documento PDF.

```java
import com.aspose.pdf.elements.*;
com.aspose.pdf.License lic = new com.aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}

//Instanciar un objeto Pdf llamando a su constructor vacío

Pdf pdf1 = new Pdf();

//Crear una sección en el objeto Pdf

Section sec1 = pdf1.getSections().add();

//Crear un párrafo de texto con la referencia de una sección

Text text1 = new Text(sec1);

//Agregar el párrafo de texto en la colección de párrafos de la sección

sec1.getParagraphs().add(text1);

//Agregar un segmento de texto en el párrafo de texto

Segment segment1 = text1.getSegments().add("este es un enlace local");

//Establecer el texto en el segmento de texto para que esté subrayado

segment1.getTextInfo().setUnderLine(true);

//Establecer el tipo de enlace del segmento de texto como Local

//Asignar el id del párrafo deseado como id objetivo para el segmento de texto

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

//Crear un párrafo de texto para ser enlazado con el segmento de texto

Text text3 = new Text(sec1,"información del producto 1 ...");

//Agregar el párrafo de texto a la colección de párrafos de la sección

sec1.getParagraphs().add(text3);

//Establecer este párrafo como el primero para que pueda mostrarse en una página separada

//en el documento

text3.setFirstParagraph(true);

//Establecer el id de este segmento de texto a "product1"

text3.setID("product1"); 

// guardar el archivo PDF

FileOutputStream out = new FileOutputStream(new File("UpdateOfCode_Test.pdf"));

pdf1.save(out);
```


Cuando se utilizan las versiones anteriores a Aspose.PDF para Java 2.5.0, el código se puede ejecutar con éxito y se puede generar un documento PDF resultante que contiene un hipervínculo hacia una página dentro del mismo documento. Pero, cuando el mismo código se compila con 2.5.0, notarás varios errores porque ha habido cambios en los miembros de clase y también algunos de los métodos en las clases han sido eliminados. Ahora, comencemos con la modificación del código para la versión 2.5.0.

Usa `import aspose.pdf.*`; en lugar de `import com.aspose.pdf.elements.*`; para incluir el paquete.

Para la inicialización de la licencia, por favor actualiza tu código existente de

{{% alert color="primary" %}}
**com.aspose.pdf.License lic = new com.aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```

{{% /alert %}}

a

{{% alert color="primary" %}}
**aspose.pdf.License lic = new aspose.pdf.License();**

```java

 try
{
lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));
}

```


{{% /alert %}}

**TextInfo** ya no contiene un método **setUnderLine(...)**. Por favor intenta usar **TextInfo.setIsUnderline(...)** **en su lugar**.**

La clase llamada **HyperLinkToLocalPdf** ha sido eliminada. Así que por favor actualiza cualquier código existente como

{{% alert color="primary" %}}
**//Establecer el tipo de enlace del segmento de texto a Local**

```java

 //Asignar el id del párrafo deseado como un id de destino para el segmento de texto

segment1.setHyperLink(new HyperLinkToLocalPdf("product1"));

```

{{% /alert %}}

a

{{% alert color="primary" %}}
**segment1.getHyperlink().setLinkType(HyperlinkType.Local);**

```java

 segment1.getHyperlink().setTargetID("product1");

```

{{% /alert %}}

El nombre del método **setFirstParagraph** ha sido eliminado de la clase Text.
 Para mostrar el segmento de texto en una nueva página, necesitas crear un nuevo objeto Section y añadir el objeto de texto a la sección recién creada. Como por defecto cada sección se muestra en una nueva página, no es necesario llamar a un método como **sec2.setIsNewPage(true**)**;

## Método de guardado actualizado

El método de guardado en la clase Pdf, que solía tomar un objeto FileOutputStream como argumento, ha sido eliminado. En la nueva versión, puedes utilizar cualquiera de los siguientes métodos sobrecargados de guardado.

- save(BasicStream stream)
- save(java.lang.String pdfFile)
- save(java.lang.String fileName, SaveType saveType, aspose.pdf.HttpResponse response)

Después de realizar todos los cambios especificados anteriormente, al usar Aspose.PDF para Java 2.5.0, el código se compilará y ejecutará sin mostrar ningún mensaje de error. El fragmento de código completamente actualizado se especifica a continuación.

```java
import aspose.pdf.*;
aspose.pdf.License lic = new aspose.pdf.License();

try {

lic.setLicense(new FileInputStream(new File("Aspose.Total.Java.lic")));

    } catch (Exception e)

{

System.out.println(e.getMessage());

}

try {

//Instanciar un objeto Pdf llamando a su constructor vacío

Pdf pdf1 = new Pdf();

//Crear una sección en el objeto Pdf

Section sec1 = pdf1.getSections().add();

//Crear un párrafo de texto con la referencia de una sección

Text text1 = new Text(sec1);

//Añadir el párrafo de texto a la colección de párrafos de la sección

sec1.getParagraphs().add(text1);

//Añadir un segmento de texto en el párrafo de texto

Segment segment1 = text1.getSegments().add("este es un enlace local");

//Configurar el texto en el segmento de texto para que esté subrayado

segment1.getTextInfo().setIsUnderline(true);


//Establecer el tipo de enlace del segmento de texto a Local

//Asignar el id del párrafo deseado como id de destino para el segmento de texto

segment1.getHyperlink().setLinkType(HyperlinkType.Local);

segment1.getHyperlink().setTargetID("product1");

// añadir una nueva sección que contendrá el objeto de texto con ID "Product 1"

Section sec2 = pdf1.getSections().add();

//Crear un párrafo de texto para ser enlazado con el segmento de texto

Text text3 = new Text(sec1,"información del producto 1 ...");

//Añadir el párrafo de texto a la colección de párrafos de la sección

sec2.getParagraphs().add(text3);

//Establecer el id de este segmento de texto a "product1"

text3.setID("product1");


// guardar el archivo PDF

pdf1.save("UpdateOfCode_Test.pdf");


     }catch(Exception e)

{

System.out.println(e.getMessage());

}
```

## Conclusión

En el tema anterior hemos explicado algunas de las clases y métodos que han sido cambiados en la nueva versión. Para una lista completa de todas las clases y sus miembros, por favor visite [Referencia API de Aspose.PDF para Java](http://www.aspose.com/documentation/java-components/aspose.pdf-for-java/aspose.pdf-for-java-api-reference.html)

Para aprender más sobre Aspose y sus productos, por favor haga clic aquí <http://www.aspose.com/>