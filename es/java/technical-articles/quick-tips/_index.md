---
title: Consejos Rápidos
type: docs
weight: 50
url: es/java/quick-tips/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Esta página contiene algunos consejos rápidos relacionados con Aspose.PDF para API de Java

{{% /alert %}}

## Añadir JavaScript al PDF

El siguiente fragmento de código se puede utilizar para establecer/agregar JavaScript al archivo PDF.

```java

String path = "D:\\";
String fileOut = path + "JavaScript.pdf";
IDocument document = null;
try
{

    document = new Document();
    document.getPages().add();
    document.getPages().add();

    //Agregando JavaScript a nivel del documento
    //Instanciar JavascriptAction con la declaración de JavaScript deseada
    JavascriptAction javaScript = new JavascriptAction("this.print({bUI:true,bSilent:false,bShrinkToFit:true});");

    //Asignar el objeto JavascriptAction a la acción deseada del Documento
    document.setOpenAction(javaScript);
    document.setOpenAction(new JavascriptAction("app.alert('Hello PDF')"));

    //Agregando JavaScript a nivel de página
    document.getActions().setBeforeClosing(new JavascriptAction("app.alert('document is closing')"));

    document.getPages().get_Item(1).getActions().setOnOpen(new JavascriptAction("app.alert('page 1 is opened')"));

    document.getPages().get_Item(2).getActions().setOnOpen(new JavascriptAction("app.alert('page 2 is opened')"));

    document.getPages().get_Item(2).getActions().setOnClose(new JavascriptAction("app.alert('page 2 is closed')"));

    document.save(fileOut);

}
finally { if (document != null) document.dispose(); document = null; }

```


**Algunos más ejemplos**

```java

// después de imprimir
document.getActions().setAfterPrinting(new JavascriptAction("app.alert('El archivo fue impreso')"));

// después de guardar
document.getActions().setAfterSaving(new JavascriptAction("app.alert('El archivo fue guardado')"));

```

## Liberar memoria utilizada

Si has completado el trabajo con Aspose.PDF para Java y deseas liberar la memoria de diferentes instancias estáticas,
para maximizar la memoria para otros procesos, debes ejecutar la siguiente línea de código:

```java

 com.aspose.pdf.MemoryCleaner.clear();

```

## Cargar PDF desde ByteArrayInputStream

El siguiente fragmento de código muestra los pasos para cargar un archivo PDF en un ByteArray y luego instanciar un objeto Document con ByteArrayInputStream.

```java

 // archivo PDF de origen

java.io.File file = new java.io.File("c:/pdftest/result.pdf");

java.io.FileInputStream fis = new java.io.FileInputStream(file);

//System.out.println(file.exists() + "!!");

//InputStream in = resource.openStream();

java.io.ByteArrayOutputStream bos = new java.io.ByteArrayOutputStream();

byte[] buf = new byte[1024];

try {

    for (int readNum; (readNum = fis.read(buf)) != -1;) {

        bos.write(buf, 0, readNum); //sin duda aquí es 0

        //Escribe len bytes desde el arreglo de bytes especificado comenzando en el desplazamiento off a este flujo de salida de arreglo de bytes.

        System.out.println("leídos " + readNum + " bytes,");

    }

} catch (java.io.IOException ex) {


}

byte[] bytes = bos.toByteArray();

// instanciar objeto Document con ByteArrayInputStream pasando el arreglo de bytes como argumento

com.aspose.pdf.Document doc = new 
com.aspose.pdf.Document(new java.io.ByteArrayInputStream(bytes));

// obtener el número de páginas del archivo PDF

 System.out.println(doc.getPages().size());

```


## Guardar PDF en ByteArrayOutputStream

El siguiente fragmento de código muestra los pasos para guardar el archivo PDF resultante en ByteArrayOutputStream.

```java

 com.aspose.pdf.Document pdfDocument = new 
com.aspose.pdf.Document("source.pdf");

java.io.InputStream is = null;

java.io.ByteArrayOutputStream os = new java.io.ByteArrayOutputStream();

try{

pdfDocument.save(os,com.aspose.pdf.SaveFormat.Doc);

System.out.println(os.size());

is = new java.io.ByteArrayInputStream(os.toByteArray());

            os.close();

            os.flush();

pdfDocument.close();

}catch (Throwable e) {}

```