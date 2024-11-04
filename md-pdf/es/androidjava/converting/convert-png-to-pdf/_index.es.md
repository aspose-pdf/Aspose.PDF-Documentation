---
title: Convertir PNG a PDF 
linktitle: Convertir PNG a PDF
type: docs
weight: 200
url: /androidjava/convert-png-to-pdf/
lastmod: "2021-06-05"
description: Este artículo muestra cómo convertir PNG a PDF con la biblioteca Aspose.PDF en tus aplicaciones Android mediante Java. Puedes convertir imágenes PNG a formato PDF usando pasos simples.
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para Android mediante Java** soporta la función de convertir imágenes PNG a formato PDF. Consulta el siguiente fragmento de código para realizar tu tarea.

<abbr title="Portable Network Graphics">PNG</abbr> se refiere a un tipo de formato de archivo de imagen de trama que utiliza compresión sin pérdida, lo que lo hace popular entre sus usuarios.

Puedes convertir imágenes PNG a PDF utilizando los siguientes pasos:

1. Cargar imagen PNG de entrada
1. Leer valores de altura y anchura
1. Crear un nuevo documento y agregar una página
1. Establecer dimensiones de la página
1. Guardar el archivo de salida

Además, el fragmento de código a continuación muestra cómo convertir PNG a PDF en tus aplicaciones Java:

```java
    public void convertPNGtoPDF () {
        // Inicializar el objeto documento
        document = new Document();

        Page page = document.getPages().add();
        Image image = new Image();

        File imgFileName = new File(fileStorage, "Conversion/sample.png");

        try {
            inputStream = new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }
```