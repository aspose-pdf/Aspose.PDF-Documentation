title: Convertir PDF a PNG
linktitle: Convertir PDF a PNG
type: docs
weight: 20
url: es/androidjava/convert-pdf-to-png/
lastmod: "2021-06-05"
description: Esta página describe cómo convertir páginas PDF a imágenes PNG, convertir todas y páginas individuales a imágenes PNG con Aspose.PDF para Android a través de Java.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Utilice la biblioteca **Aspose.PDF para Android a través de Java** para convertir páginas PDF a Imágenes <abbr title="Portable Network Graphics">PNG</abbr> de una manera accesible y conveniente.

La clase PngDevice le permite convertir páginas PDF a imágenes PNG. Esta clase proporciona un método llamado Process que le permite convertir una página particular del archivo PDF al formato de imagen PNG.

## Convertir páginas PDF a imágenes PNG 

Para convertir todas las páginas de un archivo PDF a archivos PNG, recorra las páginas individuales y convierta cada una al formato PNG. El siguiente fragmento de código muestra cómo recorrer todas las páginas de un archivo PDF y convertir cada una a una imagen PNG.

{{% alert color="primary" %}} 

Inténtalo en línea. Puedes comprobar la calidad de la conversión de Aspose.PDF y ver los resultados en línea en este enlace [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## Convertir una sola página PDF a imagen PNG

Pasa el índice de la página como un argumento al método Process(..). El siguiente fragmento de código muestra los pasos para convertir la primera página de PDF al formato PNG.

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Crear objeto de flujo para guardar la imagen de salida
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Crear objeto Resolution
            Resolution resolution = new Resolution(300);

            // Crear objeto PngDevice con una resolución particular
            PngDevice PngDevice = new PngDevice(resolution);

            // Convertir una página particular y guardar la imagen en el flujo
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Cerrar el flujo
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## Convertir todas las páginas de PDF a imagen PNG

Aspose.PDF para Android a través de Java te muestra cómo convertir todas las páginas en un archivo PDF a imágenes:

1. Recorre todas las páginas en el archivo.
1. Convierte cada página individualmente:
    1. Crea un objeto de la clase Document para cargar el documento PDF.
    1. Obtén la página que deseas convertir.
    1. Llama al método Process para convertir la página a Png.

El siguiente fragmento de código te muestra cómo convertir todas las páginas de PDF a imágenes PNG.

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Recorre todas las páginas del archivo PDF
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Crea un objeto de flujo para guardar la imagen de salida
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Crea un objeto Resolution
            Resolution resolution = new Resolution(300);
            // Crea un objeto JpegDevice con una resolución particular
            PngDevice JpegDevice = new PngDevice(resolution);

            // Convierte una página particular y guarda la imagen en el flujo
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Cierra el flujo
            try {
                imageStream.close();
            } catch (Exception e) {
                resultMessage.setText(e.getMessage());
                return;
            }
        }
        resultMessage.setText(R.string.success_message);
    }
```


## Convertir una página particular de PDF a una imagen PNG

Aspose.PDF para Android vía Java te muestra cómo convertir una página particular al formato PNG:

```java
public void convertPDFtoPNG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Obtener el rectángulo de una región particular de la página
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // establecer el valor de CropBox según el rectángulo de la región deseada de la página
        document.getPages().get_Item(1).setCropBox(pageRect);
        // guardar el documento recortado en un flujo
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // abrir el documento PDF recortado desde el flujo y convertirlo en imagen
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Crear objeto de resolución
        Resolution resolution = new Resolution(300);
        // Crear dispositivo Png con atributos especificados
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Convertir una página particular y guardar la imagen en el flujo
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```