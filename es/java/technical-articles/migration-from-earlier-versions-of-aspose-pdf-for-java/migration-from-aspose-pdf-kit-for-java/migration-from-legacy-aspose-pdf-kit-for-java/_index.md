---
title: Migración desde Aspose.Pdf.Kit para Java heredado
type: docs
weight: 10
url: /es/java/migration-from-legacy-aspose-pdf-kit-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

El componente actual Aspose.PDF.Kit para Java proporcionaba las funciones para manipular archivos PDF existentes. Sin embargo, a veces en el futuro, este componente se descontinuará como producto separado porque hemos portado todas sus clases y enumeraciones bajo el paquete **com.aspose.pdf.facades** de la nueva versión autopublicada de Aspose.PDF para Java (4.x.x). Ahora esta única versión autopublicada ofrece las capacidades para crear y manipular archivos PDF existentes.

{{% /alert %}}

## Soporte para código heredado

Durante toda la actividad de migración, definitivamente hemos considerado el impacto de esta actividad sobre los clientes existentes y hemos hecho nuestro mejor esfuerzo para minimizar este impacto tanto como sea posible.
 Además, también nos hemos centrado en hacer que la nueva versión autoportada sea compatible hacia atrás para que la base de código de los clientes existentes requiera cambios mínimos. Aunque la nueva versión autoportada proporciona el Modelo de Objeto de Documento (DOM) bajo el paquete com.aspose.pdf para crear y manipular archivos PDF existentes, si aún desea continuar usando su código heredado desarrollado con Aspose.PDF.Kit para Java, solo necesita importar el paquete **com.aspose.pdf.facades** y su código debería funcionar (*excepto para actualizar referencias explícitas de clases*).

El siguiente fragmento de código le muestra cómo ejecutar su código existente de Aspose.PDF.Kit para Java con el nuevo Aspose.PDF autoportado para Java.

```java

 import com.aspose.pdf.facades.*;

public class template {

    public static void main(String[] args) {

        try{

            // cargar archivo PDF existente

            com.aspose.pdf.facades.PdfFileInfo fileInfo = new com.aspose.pdf.facades.PdfFileInfo("input.pdf");

            System.out.println("TITLE: " + fileInfo.getTitle());

            System.out.println("AUTHOR:" + fileInfo.getAuthor());

            System.out.println("CREATIONDATE:" + fileInfo.getCreationDate());

            System.out.println("CREATOR:" + fileInfo.getCreator());

            System.out.println("KeyWORDS:" + fileInfo.getKeywords());

            System.out.println("MODDATE:" + fileInfo.getModDate());

           }


catch(Exception ex)


{System.out.println(ex);}


}

}
```

## Usando la clase ReplaceTextStrategy

Para migrar el código de la clase ReplaceTextStrategy, el método **setScope(..)** se ha actualizado a **setReplaceScope(..)**. Por favor, revise el siguiente fragmento de código.

```java

 // instanciar objeto PdfContentEditor

com.aspose.pdf.facades.PdfContentEditor editor = new com.aspose.pdf.facades.PdfContentEditor();

// vincular archivo PDF de origen

editor.bindPdf("input.pdf");

// crear estrategia de reemplazo de texto

com.aspose.pdf.facades.ReplaceTextStrategy strategy = new com.aspose.pdf.facades.ReplaceTextStrategy();

// establecer la alineación para el reemplazo de texto

strategy.setAlignment(com.aspose.pdf.facades.AlignmentType.Left);

// ámbito para el reemplazo de texto

strategy.setReplaceScope(com.aspose.pdf.facades.ReplaceTextStrategy.Scope.REPLACE_ALL);

// establecer la estrategia de reemplazo

editor.setReplaceTextStrategy(strategy);

editor.replaceText("test","replaced");

// guardar archivo actualizado

editor.save("TxtReplaceTest.pdf");
```